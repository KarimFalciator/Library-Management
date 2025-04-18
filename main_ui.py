import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import database
from datetime import datetime, timedelta
import json
import os
import json_functions
import re

class main_UI:

    def __init__(self, main, t_id):
        self.t_id = t_id    

        if os.path.exists('saved_settings.json'):
            with open('saved_settings.json', 'r') as file:
                settings = json.load(file)
        else:
            with open('default_settings.json', 'r') as file:
                settings = json.load(file)

        self.font = settings['Font']
        self.font_size = int(settings["Font_size"])
        self.theme = settings["Theme"]
        self.zoom = max(0.5, min(float(settings["Zoom"]), 3))
        
        width = 695*self.zoom
        height = 430*self.zoom

        self.main = main
        self.main.title('Lending Management System')
        self.main.geometry(f'{width}x{height}')
        # self.main.resizable(False, False)

        ctk.set_appearance_mode(self.theme)
        ctk.set_default_color_theme("blue")

        self.conn = database.connect_to_db('lending.db')

        # Apply ttk Notebook style to match CustomTkinter appearance
        style = ttk.Style()
        style.theme_use('default')

        # Customizing the notebook tabs to match CustomTkinter
        style.configure('TNotebook', background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1])
        style.configure('TNotebook.Tab', font=(self.font, self.font_size - 1), padding=[10, 5], background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0])
        style.map("TNotebook.Tab", background=[("selected", ctk.ThemeManager.theme["CTkButton"]["fg_color"][1])])

        # Create a ttk Notebook, styled to match CustomTkinter
        self.Notebook = ttk.Notebook(self.main)
        self.Notebook.pack(pady=10, expand=True, fill='both')

        self.create_home_tab()
        self.create_returned_tab()
        self.create_resources_tab()
        self.create_students_tab()
        self.create_settings_tab()
        self.create_help_tab()
        self.add_borrowed_from_db()
        self.add_previous_from_db()
        self.add_resources_from_db()
        self.add_students_from_db()

    # home tab ---------------------------------------------------------------
    
    def create_home_tab(self):
        home_tab = ctk.CTkFrame(self.Notebook)
        self.Notebook.add(home_tab, text='Home')

        columns_home = ('ref', 's_id', 'r_id', 'b_date', 'd_date', 'r_date')
        self.current_tree = ttk.Treeview(home_tab, columns=columns_home, show='headings')

        bg_color_home = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color_home = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color_home = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", font=(self.font, self.font_size -1), background=bg_color_home, foreground=text_color_home, fieldbackground=bg_color_home, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color_home)], foreground=[('selected', selected_color_home)])
        self.main.bind("<<TreeviewSelect>>", lambda event: self.main.focus_set())

        self.current_tree.bind("<Button-3>", self.show_context_menu_home)

        # Define headings
        self.current_tree.heading('ref', text='Reference')
        self.current_tree.heading('s_id', text='Student ID')
        self.current_tree.heading('r_id', text='Resource ID')
        self.current_tree.heading('b_date', text='Borrowed Date')
        self.current_tree.heading('d_date', text='Due Date')
        self.current_tree.heading('r_date', text='Returned Date')

        # Define column widths
        self.current_tree.column('ref', width=int(80*self.zoom))
        self.current_tree.column('s_id', width=int(90*self.zoom))
        self.current_tree.column('r_id', width=int(90*self.zoom))
        self.current_tree.column('b_date', width=int(105*self.zoom))
        self.current_tree.column('d_date', width=int(105*self.zoom))
        self.current_tree.column('r_date', width=int(105*self.zoom))

        self.current_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

        # Add a vertical scrollbar
        scrollbar_home = ttk.Scrollbar(home_tab, orient='vertical', command=self.current_tree.yview)
        scrollbar_home.grid(row=0, column=4, sticky='ns')
        self.current_tree.configure(yscrollcommand=scrollbar_home.set)

        # Add Borrowed ResourceForm
        self.add_borrowed_CTklable = ctk.CTkLabel(home_tab, text="Add a new borrowed:", font=(self.font, self.font_size))
        self.add_borrowed_CTklable.grid(row=1, column=0, padx=5, pady=0, sticky='n')

        self.h_s_id_CTklabel = ctk.CTkLabel(home_tab, text="Student ID:", font=(self.font, self.font_size))
        self.h_s_id_CTklabel.grid(row=2, column=0, padx=5, pady=5)
        self.h_s_id_entry = ctk.CTkEntry(home_tab, font=(self.font, self.font_size))
        self.h_s_id_entry.grid(row=3, column=0, padx=5, pady=5)

        self.h_r_id_CTklabel = ctk.CTkLabel(home_tab, text="Resource ID:", font=(self.font, self.font_size))
        self.h_r_id_CTklabel.grid(row=2, column=1, padx=5, pady=5)
        self.h_r_id_entry = ctk.CTkEntry(home_tab, font=(self.font, self.font_size))
        self.h_r_id_entry.grid(row=3, column=1, padx=5, pady=5)

        self.h_days_CTklabel = ctk.CTkLabel(home_tab, text="Days borrowed:", font=(self.font, self.font_size))
        self.h_days_CTklabel.grid(row=2, column=2, padx=5, pady=5)
        self.h_days_entry = ctk.CTkEntry(home_tab, font=(self.font, self.font_size))
        self.h_days_entry.grid(row=3, column=2, padx=5, pady=5)

        self.add_borrowed = ctk.CTkButton(home_tab, text="Add Borrowed resource", font=(self.font, self.font_size), command=self.add_borrowed_resource)
        self.add_borrowed.grid(row=4, column=1, columnspan=1, pady=10)

    def show_context_menu_home(self, event):
        # Get the selected item
        selected_item = event.widget.selection()
        if selected_item:
            # Create a context menu
            context_menu_home = tk.Menu(event.widget, tearoff=0)
            context_menu_home.add_command(label="Return Object", font=(self.font, self.font_size), command= self.return_object)
            context_menu_home.add_command(label="Extend Due Date", font=(self.font, self.font_size), command= self.extend_borrowed)
            context_menu_home.add_command(label="close", font=(self.font, self.font_size), command= self.close_context_menu)
            
            # Show the context menu
            context_menu_home.post(event.x_root, event.y_root)

             # Bind the focus out event to destroy the context menu
            self.current_tree.bind("<FocusOut>", self.hide_context_menu_home)

    def hide_context_menu_home(self, event):
        if hasattr(self, 'context_menu'):
            self.context_menu_home.unpost()
            del self.context_menu_home
        else:
            pass
    
    def return_object(self):
        # Get the selected item
        selected_item = self.current_tree.selection()
        # Get the values of the selected item
        values = self.current_tree.item(selected_item, 'values')
        # Get the reference of the selected item
        ref = values[0]
        r_id = values[2]
        # Ask confirmation from the user
        if messagebox.askyesno('Title', 'Do you want to return the onject?'):
            # Update the returned date in the database
            database.return_borrowed(self.conn, ref, r_id, self.t_id)
            # Refresh the Treeview
            self.refresh_current_tree()
            self.refresh_returned_tree()
            self.refresh_resources_tree()
        else:
            None

    def extend_borrowed(self):
        selected_item = self.current_tree.selection()
        if selected_item:
            self.extend_window = tk.Toplevel(self.main)
            self.extend_window.title("Extend Due Date")

            tk.Label(self.extend_window, text="Enter number of days to extend:", font=(self.font, self.font_size),).pack(pady=10)
            self.days_entry = tk.Entry(self.extend_window, font=(self.font, self.font_size))
            self.days_entry.pack(pady=5)

            tk.Button(self.extend_window, text="Extend", font=(self.font, self.font_size), command=self.update_due_date).pack(pady=10)

    def update_due_date(self):
        try:
            days = int(self.days_entry.get())
            selected_item = self.current_tree.selection()
            values = self.current_tree.item(selected_item, 'values')
            ref = values[0]
            # Update the due date in the database
            database.increase_borrowed_d_date(self.conn, ref, days)
            # Close the window
            self.extend_window.destroy()
            # Refresh the Treeview
            self.refresh_current_tree()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number", font=(self.font, self.font_size),)

    def refresh_current_tree(self):
        # Clear the Treeview
        for item in self.current_tree.get_children():
            self.current_tree.delete(item)

        # Fetch all borrowed records from the database
        borrowed_records = database.get_all_borrowed(self.conn, self.t_id)

        # Insert each borrowed record into the Treeview
        for record in borrowed_records:
            self.current_tree.insert('', 'end', values=record)

    def close_context_menu(self):
        if hasattr(self, 'context_menu'):
            self.context_menu.unpost()
            del self.context_menu
        else:
            pass

    def add_borrowed_resource(self):
        # Fetch details from entry widgets
        h_s_id = self.h_s_id_entry.get()
        h_r_id = self.h_r_id_entry.get()
        h_days = int(self.h_days_entry.get())
        borrowed_date = datetime.now().strftime('%Y-%m-%d')
        returned_date = (datetime.now() + timedelta(days=h_days)).strftime('%Y-%m-%d')
        ref = database.get_last_ref(self.conn) + 1

        if database.check_resource_quantity(self.conn, h_r_id, self.t_id) and database.check_student(self.conn, h_s_id) and h_days > 0:
            database.new_borrowed(self.conn, h_s_id, h_r_id, self.t_id, h_days)
            # Insert into Treeview
            self.current_tree.insert('', '0', values=(ref, h_s_id, h_r_id, borrowed_date, returned_date, 'None'))
            # Clear the entry fields
            self.h_s_id_entry.delete(0, 'end')
            self.h_r_id_entry.delete(0, 'end')
            self.h_days_entry.delete(0, 'end')
            self.refresh_current_tree()
            self.refresh_resources_tree()
        else:
            messagebox.showerror('Error', 'Resource not available or Student does not exist or Number of days is invalid')

    def add_borrowed_from_db(self):
        # Fetch all borrowed records from the database
        borrowed_records = database.get_all_borrowed(self.conn, self.t_id)

        # Insert each borrowed record into the Treeview
        for record in borrowed_records:
            self.current_tree.insert('', 'end', values=record)


    #  read tab -----------------------------------------------------------------

    def create_returned_tab(self):
        return_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(return_tab, text='Returned Borrowed')

        columns = ('ref', 's_id', 'r_id', 'b_date', 'd_date', 'r_date')
        self.returned_tree = ttk.Treeview(return_tab, columns=columns, show='headings', height=17)

        bg_color_returned = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color_returned = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color_returned = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color_returned, foreground=text_color_returned, fieldbackground=bg_color_returned, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color_returned)], foreground=[('selected', selected_color_returned)])
        self.main.bind("<<TreeviewSelect>>", lambda event: self.main.focus_set())

        # Define headings
        self.returned_tree.heading('ref', text='Reference')
        self.returned_tree.heading('s_id', text='Student ID')
        self.returned_tree.heading('r_id', text='Resource ID')
        self.returned_tree.heading('b_date', text='Borrowed Date')
        self.returned_tree.heading('d_date', text='Due Date')
        self.returned_tree.heading('r_date', text='Returned Date')

        # Define column widths
        self.returned_tree.column('ref', width=int(80*self.zoom))
        self.returned_tree.column('s_id', width=int(90*self.zoom))
        self.returned_tree.column('r_id', width=int(90*self.zoom))
        self.returned_tree.column('b_date', width=int(105*self.zoom))
        self.returned_tree.column('d_date', width=int(105*self.zoom))
        self.returned_tree.column('r_date', width=int(105*self.zoom))

        self.returned_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

        # Add a vertical scrollbar
        scrollbar_returned = ttk.Scrollbar(return_tab, orient='vertical', command=self.returned_tree.yview)
        scrollbar_returned.grid(row=0, column=4, sticky='ns')
        self.returned_tree.configure(yscrollcommand=scrollbar_returned.set)

    def refresh_returned_tree(self):
        # Clear the Treeview
        for item in self.returned_tree.get_children():
            self.returned_tree.delete(item)

        # Fetch all borrowed records from the database
        returned_records = database.get_returned_borrowed(self.conn, self.t_id)

        # Insert each borrowed record into the Treeview
        for record in returned_records:
            self.returned_tree.insert('', 'end', values=record)


    def add_previous_from_db(self):
        returned_records = database.get_returned_borrowed(self.conn, self.t_id)

        for record in returned_records:
            self.returned_tree.insert('', 'end', values=record)

    # resource list tab --------------------------------------------------------------
    def create_resources_tab(self):
        resources_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(resources_tab, text='Resources List')

        columns_resources = ('r_id', 'r_type', 'r_des', 'r_qty')
        self.resources_tree = ttk.Treeview(resources_tab, columns=columns_resources, show='headings')

        bg_color_resources = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color_resources = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color_resources = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color_resources, foreground=text_color_resources, fieldbackground=bg_color_resources, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color_resources)], foreground=[('selected', selected_color_resources)])
        self.main.bind("<<TreeviewSelect>>", lambda event: self.main.focus_set())

        self.resources_tree.bind("<Button-3>", self.show_context_menu_resources)

        # Define headings
        self.resources_tree.heading('r_id', text='Resource ID')
        self.resources_tree.heading('r_type', text='Object')
        self.resources_tree.heading('r_des', text='Description')
        self.resources_tree.heading('r_qty', text='Number Available')

        # Define column widths
        self.resources_tree.column('r_id', width=int(140*self.zoom))
        self.resources_tree.column('r_type', width=int(140*self.zoom))
        self.resources_tree.column('r_des', width=int(140*self.zoom))
        self.resources_tree.column('r_qty', width=int(140*self.zoom))

        self.resources_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

        # Add a vertical scrollbar
        scrollbar_resources = ttk.Scrollbar(resources_tab, orient='vertical', command=self.resources_tree.yview)
        scrollbar_resources.grid(row=0, column=4, sticky='ns')
        self.resources_tree.configure(yscrollcommand=scrollbar_resources.set)

        # Add Borrowed ResourceForm
        self.add_resources_CTklable = ctk.CTkLabel(resources_tab, text="Add a new resource:", font=(self.font, self.font_size))
        self.add_resources_CTklable.grid(row=1, column=0, padx=5, pady=0, sticky='n')

        self.r_type_CTklabel = ctk.CTkLabel(resources_tab, text="Object Name:", font=(self.font, self.font_size))
        self.r_type_CTklabel.grid(row=2, column=0, padx=5, pady=5)
        self.r_type_entry = ctk.CTkEntry(resources_tab, font=(self.font, self.font_size))
        self.r_type_entry.grid(row=3, column=0, padx=5, pady=5)

        self.r_des_CTklabel = ctk.CTkLabel(resources_tab, text="Model/Description:", font=(self.font, self.font_size))
        self.r_des_CTklabel.grid(row=2, column=1, padx=5, pady=5)
        self.r_des_entry = ctk.CTkEntry(resources_tab, font=(self.font, self.font_size))
        self.r_des_entry.grid(row=3, column=1, padx=5, pady=5)

        self.r_qty_CTklabel = ctk.CTkLabel(resources_tab, text="Number of resources:", font=(self.font, self.font_size))
        self.r_qty_CTklabel.grid(row=2, column=2, padx=5, pady=5)
        self.r_qty_entry = ctk.CTkEntry(resources_tab, font=(self.font, self.font_size))
        self.r_qty_entry.grid(row=3, column=2, padx=5, pady=5)

        self.add_resources_button = ctk.CTkButton(resources_tab, text="Add New Resources", font=(self.font, self.font_size), command=self.add_resources)
        self.add_resources_button.grid(row=4, column=1, columnspan=1, pady=10)

    def show_context_menu_resources(self, event):

        selected_item = event.widget.selection()
        if selected_item:
            
            context_menu_resources = tk.Menu(event.widget, tearoff=0)
            context_menu_resources.add_command(label="Remove Resource", font=(self.font, self.font_size), command= self.remove_resources)
            context_menu_resources.add_command(label="Increase Quantity", font=(self.font, self.font_size), command= self.upd_qty)
            context_menu_resources.add_command(label="close", font=(self.font, self.font_size), command= self.close_context_menu)

            context_menu_resources.post(event.x_root, event.y_root)

             # Bind the focus out event to destroy the context menu
            self.resources_tree.bind("<FocusOut>", self.hide_context_menu_home)

    def hide_context_menu_resources(self, event):
        if hasattr(self, 'context_menu'):
            self.context_menu_resources.unpost()
            del self.context_menu_resources
        else:
            pass
    
    def remove_resources(self):
        selected_item = self.resources_tree.selection()
        values = self.resources_tree.item(selected_item, 'values')
        r_id = values[0]

        if messagebox.askyesno('Title', 'Do you want to set the object as unavailable?'):
            database.set_resource_unavailable(self.conn, r_id, self.t_id)
            self.refresh_resources_tree()
        else:
            None

    def upd_qty(self):
        selected_item = self.resources_tree.selection()
        if selected_item:
            self.extend_window_r = tk.Toplevel(self.main)
            self.extend_window_r.title("Update Quantity")

            tk.Label(self.extend_window_r, text="Enter number of resources:", font=(self.font, self.font_size)).pack(pady=10)
            self.qty_entry = tk.Entry(self.extend_window_r, font=(self.font, self.font_size))
            self.qty_entry.pack(pady=5)

            tk.Button(self.extend_window_r, text="Update", font=(self.font, self.font_size), command=self.update_qty).pack(pady=10)

    def update_qty(self):
        try:
            qty = int(self.qty_entry.get())
            selected_item = self.resources_tree.selection()
            values = self.resources_tree.item(selected_item, 'values')
            r_id = values[0]
            database.update_resource_qty(self.conn, r_id, qty, self.t_id)
            self.extend_window_r.destroy()
            self.refresh_resources_tree()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")

    def refresh_resources_tree(self):
        for item in self.resources_tree.get_children():
            self.resources_tree.delete(item)

        resources = database.get_all_resources(self.conn, self.t_id)

        for record in resources:
            self.resources_tree.insert('', 'end', values=record)

    def close_context_menu(self):
        if hasattr(self, 'context_menu'):
            self.context_menu_resources.unpost()
            del self.context_menu_resources
        else:
            pass

    def add_resources(self):
        # Fetch details from entry widgets
        r_type = self.r_type_entry.get()
        r_des = self.r_des_entry.get()
        r_qty = int(self.r_qty_entry.get())


        if database.new_resource(self.conn, r_type, r_des, r_qty, self.t_id):
            database.new_resource(self.conn, r_type, r_des, r_qty, self.t_id)
            # Insert into Treeview
            self.resources_tree.insert('', '0', values=(r_type, r_des, r_qty))
            # Clear the entry fields
            self.r_type_entry.delete(0, 'end')
            self.r_des_entry.delete(0, 'end')
            self.r_qty_entry.delete(0, 'end')
            self.refresh_resources_tree()
        else:
            messagebox.showerror('Error', 'Resource already exists')

    def add_resources_from_db(self):
        # Fetch all borrowed records from the database
        resources = database.get_all_resources(self.conn, self.t_id)

        # Insert each borrowed record into the Treeview
        for record in resources:
            self.resources_tree.insert('', 'end', values=record)

    # Students list tab --------------------------------------------------------------
    def create_students_tab(self):
        students_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(students_tab, text='Students List')

        columns_students = ('s_id', 's_fname', 's_lname', 's_email', 's_phone')
        self.students_tree = ttk.Treeview(students_tab, columns=columns_students, show='headings')

        bg_color_students = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color_students = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color_students = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color_students, foreground=text_color_students, fieldbackground=bg_color_students, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color_students)], foreground=[('selected', selected_color_students)])
        self.main.bind("<<TreeviewSelect>>", lambda event: self.main.focus_set())

        self.students_tree.bind("<Button-3>", self.show_context_menu_resources)

        # Define headings
        self.students_tree.heading('s_id', text='Student ID')
        self.students_tree.heading('s_fname', text='First Name')
        self.students_tree.heading('s_lname', text='Last Name')
        self.students_tree.heading('s_email', text='Email')
        self.students_tree.heading('s_phone', text='Phone Number')

        # Define column widths
        self.students_tree.column('s_id', width=int(140*self.zoom))
        self.students_tree.column('s_fname', width=int(140*self.zoom))
        self.students_tree.column('s_lname', width=int(140*self.zoom))
        self.students_tree.column('s_email', width=int(140*self.zoom))
        self.students_tree.column('s_phone', width=int(140*self.zoom))

        self.students_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

        # Add a vertical scrollbar
        scrollbar_students = ttk.Scrollbar(students_tab, orient='vertical', command=self.students_tree.yview)
        scrollbar_students.grid(row=0, column=4, sticky='ns')
        self.students_tree.configure(yscrollcommand=scrollbar_students.set)

        # Add Borrowed ResourceForm
        self.add_students_CTklable = ctk.CTkLabel(students_tab, text="Add a new student:", font=(self.font, self.font_size))
        self.add_students_CTklable.grid(row=1, column=0, padx=5, pady=0, sticky='n')

        self.s_fname_CTklabel = ctk.CTkLabel(students_tab, text="First Name:", font=(self.font, self.font_size))
        self.s_fname_CTklabel.grid(row=2, column=0, padx=5, pady=5)
        self.s_fname_entry = ctk.CTkEntry(students_tab, font=(self.font, self.font_size))
        self.s_fname_entry.grid(row=3, column=0, padx=5, pady=5)

        self.s_lname_CTklabel = ctk.CTkLabel(students_tab, text="Last Name:", font=(self.font, self.font_size))
        self.s_lname_CTklabel.grid(row=2, column=1, padx=5, pady=5)
        self.s_lname_entry = ctk.CTkEntry(students_tab, font=(self.font, self.font_size))
        self.s_lname_entry.grid(row=3, column=1, padx=5, pady=5)

        self.s_phone_CTklabel = ctk.CTkLabel(students_tab, text="Student Phone Number:", font=(self.font, self.font_size))
        self.s_phone_CTklabel.grid(row=2, column=2, padx=5, pady=5)
        self.s_phone_entry = ctk.CTkEntry(students_tab, font=(self.font, self.font_size))
        self.s_phone_entry.grid(row=3, column=2, padx=5, pady=5)

        self.s_email_CTklabel = ctk.CTkLabel(students_tab, text="Student Email:", font=(self.font, self.font_size))
        self.s_email_CTklabel.grid(row=2, column=3, padx=5, pady=5)
        self.s_email_entry = ctk.CTkEntry(students_tab, font=(self.font, self.font_size))
        self.s_email_entry.grid(row=3, column=3, padx=5, pady=5)

        self.add_students_button = ctk.CTkButton(students_tab, text="Add New Student", font=(self.font, self.font_size), command=self.add_students)
        self.add_students_button.grid(row=4, column=1, columnspan=1, pady=10)

    def add_students(self):
        # Fetch details from entry widgets
        s_id = database.generate_student_id()
        s_fname = self.r_des_entry.get()
        s_lname = self.r_qty_entry.get()
        s_email = self.r_des_entry.get()
        s_phone = self.r_qty_entry.get()
        
        email_fromat = regex(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]')
        phone_format = regex(r'^\d{10}$')


        if database.new_student(self.conn,s_id, s_fname, s_lname, s_email, s_phone) and email_fromat.match(s_email) and s_phone.match(phone_format):
            # Insert into Treeview
            self.students_tree.insert('', '0', values=(s_id, s_fname, s_lname, s_email, s_phone))
            # Clear the entry fields
            self.s_fname_entry.delete(0, 'end')
            self.s_lname_entry.delete(0, 'end')
            self.s_email_entry.delete(0, 'end')
            self.s_phone_entry.delete(0, 'end')
            self.refresh_students_tree()
        else:
            messagebox.showerror('Error', 'Student already exists or student format or phone format are invalid')

    def add_students_from_db(self):
        # Fetch all borrowed records from the database
        students = database.get_all_students(self.conn)

        # Insert each borrowed record into the Treeview
        for record in students:
            self.students_tree.insert('', 'end', values=record)

    def refresh_students_tree(self):
        for item in self.students_tree.get_children():
            self.students_tree.delete(item)

        students = database.get_all_students(self.conn)

        for record in students:
            self.students_tree.insert('', 'end', values=record)

    # settings
    def create_settings_tab(self):
        settings_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(settings_tab, text='Settings')

		# Font Type
        self.fontLabel = ctk.CTkLabel(settings_tab, text="Font Type", font=(self.font, self.font_size))
        self.fontLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

		# Font Radio Buttons
        self.fontVar = tk.StringVar()

        self.Ariel = ctk.CTkRadioButton(settings_tab, text="Ariel", font=(self.font, self.font_size), variable=self.fontVar, value="Ariel")
        self.Ariel.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        self.CourierNew = ctk.CTkRadioButton(settings_tab, text="Courier New", font=(self.font, self.font_size), variable=self.fontVar, value="Courier New")
        self.CourierNew.grid(row=0, column=2, padx=20, pady=20, sticky="ew")
		
        self.NewRomans = ctk.CTkRadioButton(settings_tab, text="Roman New Times", font=(self.font, self.font_size), variable=self.fontVar, value="Roman New Times")
        self.NewRomans.grid(row=0, column=3, padx=20, pady=20, sticky="ew")
        # Font Size
        self.font_size_label = ctk.CTkLabel(settings_tab, text="Font Size:", font=(self.font, self.font_size))
        self.font_size_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.font_size_entry = ctk.CTkEntry(settings_tab, font=(self.font, self.font_size),  placeholder_text=self.font_size)
        self.font_size_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        # Theme
        self.themeLabel = ctk.CTkLabel(settings_tab, text="Theme Type", font=(self.font, self.font_size))
        self.themeLabel.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.themeVar = tk.StringVar()

        self.Light = ctk.CTkRadioButton(settings_tab, text="Light", font=(self.font, self.font_size), variable=self.themeVar, value="light")
        self.Light.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

        self.Dark = ctk.CTkRadioButton(settings_tab, text="Dark", font=(self.font, self.font_size), variable=self.themeVar, value="dark")
        self.Dark.grid(row=2, column=2, padx=20, pady=20, sticky="ew")
		
        self.System = ctk.CTkRadioButton(settings_tab, text="System", font=(self.font, self.font_size), variable=self.themeVar, value="System")
        self.System.grid(row=2, column=3, padx=20, pady=20, sticky="ew")
        # Zoom
        self.zoom_label = ctk.CTkLabel(settings_tab, text="Zoom:", font=(self.font, self.font_size))
        self.zoom_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.zoom_entry = ctk.CTkEntry(settings_tab, font=(self.font, self.font_size), placeholder_text=self.zoom)
        self.zoom_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Save Button
        self.save_button = ctk.CTkButton(settings_tab, text="Save Settings", font=(self.font, self.font_size), command=self.save_settings)
        self.save_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

        self.reccomendation = ctk.CTkLabel(settings_tab, text="Recommended Zoom: 0.5 - 2. And make sure it works with the font size", font=(self.font, self.font_size))

    def save_settings(self):
        font = self.fontVar.get()
        font_size = self.font_size_entry.get()
        theme = self.themeVar.get()
        zoom = self.zoom_entry.get()

        if font_size:
            if int(font_size) <= 0:
                messagebox.showerror("Invalid Input", "Font size must be a positive integer.")
                return

        if not font:
            font = self.font
        if not font_size:
            font_size = self.font_size
        if not theme:
            theme = self.theme
        if not zoom:
            zoom = self.zoom

        # Save settings
        json_functions.update_settings(font, font_size, theme, zoom)
        messagebox.showinfo("Settings Saved", "Your settings have been saved successfully.")



    # help tab -------------------------------------------------------------------
    def create_help_tab(self):
        help_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(help_tab, text='Help')

        self.help_label = ctk.CTkLabel(help_tab, text="Help and Instructions", font=(self.font, self.font_size))
        self.help_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.help_text = ctk.CTkTextbox(help_tab, font=(self.font, self.font_size), width=int(575*self.zoom), height=int(300*self.zoom))
        self.help_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.help_text.insert('0.0', "This is a lending management system.\n\n"
                                       "1. To borrow a resource, enter the Student ID, Resource ID, and number of days in the 'Home' tab.\n"
                                       "2. To return a resource, right-click on the borrowed item in the 'Home' tab and select 'Return Object'.\n"
                                       "3. To extend the due date, right-click on the borrowed item and select 'Extend Due Date'.\n"
                                       "4. To add new resources, go to the 'Resources List' tab and fill in the details.\n"
                                       "5. To view returned items, go to the 'Returned Borrowed' tab.\n"
                                       "6. For settings, go to the 'Settings' tab to customize your preferences.\n"
                                       "\n\n"
                                       "If you have any questions, please contact the administrator.")
        self.help_text.configure(state='disabled')

if __name__ == "__main__":  # for testing
    login = ctk.CTk()
    t_id = 111111
    log = main_UI(login, t_id)
    login.mainloop()


# fai in modo che si puo prendere uno solo di ogni oggetto
# aggiungi oggetto nummero che vuole non perforza deve essere uno in piu se ce il oggetto
# aggiungi una window per aggiungere nuovi oggetti se e la prima volta che si usa il programma, usa un text file per confermare se ha fatto log in (YES/NO)
# aggiungi una window per aggiungere nuovi studenti se e la prima volta che si usa il programma, usa un text file per confermare se ha fatto log in (YES/NO)
# fai in modo che non si possa prendere in prestito dopo la chiusura di scuola
# fai in modo che alla chiusura a tutti i borrowed una email viene mandata per ricordargli di restituire l'oggetto