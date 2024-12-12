import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import database
from datetime import datetime, timedelta

class main_UI:
#take off none as t_id once testing after login
    def __init__(self, main, t_id):
        self.main = main
        self.t_id = t_id
        self.main.title('Lending Management System')
        self.main.geometry('700x450')
        self.main.resizable(False, False)
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.conn = database.connect_to_db('lending.db')

        # Apply ttk Notebook style to match CustomTkinter appearance
        style = ttk.Style()
        style.theme_use('default')

        # Customizing the notebook tabs to match CustomTkinter
        style.configure('TNotebook', background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1])
        style.configure('TNotebook.Tab', font=('Arial', 12), padding=[10, 5], background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0])
        style.map("TNotebook.Tab", background=[("selected", ctk.ThemeManager.theme["CTkButton"]["fg_color"][1])])

        # Create a ttk Notebook, styled to match CustomTkinter
        self.Notebook = ttk.Notebook(self.main)
        self.Notebook.pack(pady=10, expand=True, fill='both')

        self.create_home_tab()
        self.create_returned_tab()
        self.create_resources_tab()
        self.create_settings_tab()
        self.create_help_tab()
        self.add_borrowed_from_db()
        self.add_previous_from_db()
        self.add_resources_from_db()

    # home tab ---------------------------------------------------------------
    
    def create_home_tab(self):
        home_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(home_tab, text='Home')

        columns_home = ('ref', 's_id', 'r_id', 'b_date', 'd_date', 'r_date')
        self.current_tree = ttk.Treeview(home_tab, columns=columns_home, show='headings')

        bg_color_home = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color_home = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color_home = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color_home, foreground=text_color_home, fieldbackground=bg_color_home, borderwidth=0)
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
        self.current_tree.column('ref', width=80)
        self.current_tree.column('s_id', width=90)
        self.current_tree.column('r_id', width=90)
        self.current_tree.column('b_date', width=105)
        self.current_tree.column('d_date', width=90)
        self.current_tree.column('r_date', width=105)

        self.current_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

        # Add a vertical scrollbar
        scrollbar_home = ttk.Scrollbar(home_tab, orient='vertical', command=self.current_tree.yview)
        scrollbar_home.grid(row=0, column=4, sticky='ns')
        self.current_tree.configure(yscrollcommand=scrollbar_home.set)

        # Add Borrowed ResourceForm
        self.add_borrowed_CTklable = ctk.CTkLabel(home_tab, text="Add a new borrowed:")
        self.add_borrowed_CTklable.grid(row=1, column=0, padx=5, pady=0, sticky='n')

        self.h_s_id_CTklabel = ctk.CTkLabel(home_tab, text="Student ID:")
        self.h_s_id_CTklabel.grid(row=2, column=0, padx=5, pady=5)
        self.h_s_id_entry = ctk.CTkEntry(home_tab)
        self.h_s_id_entry.grid(row=3, column=0, padx=5, pady=5)

        self.h_r_id_CTklabel = ctk.CTkLabel(home_tab, text="Resource ID:")
        self.h_r_id_CTklabel.grid(row=2, column=1, padx=5, pady=5)
        self.h_r_id_entry = ctk.CTkEntry(home_tab)
        self.h_r_id_entry.grid(row=3, column=1, padx=5, pady=5)

        self.h_days_CTklabel = ctk.CTkLabel(home_tab, text="Days borrowed:")
        self.h_days_CTklabel.grid(row=2, column=2, padx=5, pady=5)
        self.h_days_entry = ctk.CTkEntry(home_tab)
        self.h_days_entry.grid(row=3, column=2, padx=5, pady=5)

        self.add_borrowed = ctk.CTkButton(home_tab, text="Add Borrowed resource", command=self.add_borrowed_resource)
        self.add_borrowed.grid(row=4, column=1, columnspan=1, pady=10)

    def show_context_menu_home(self, event):
        # Get the selected item
        selected_item = event.widget.selection()
        if selected_item:
            # Create a context menu
            context_menu_home = tk.Menu(event.widget, tearoff=0)
            context_menu_home.add_command(label="Return Object", command= self.return_object)
            context_menu_home.add_command(label="Extend Due Date", command= self.extend_borrowed)
            context_menu_home.add_command(label="close", command= self.close_context_menu)
            
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

            tk.Label(self.extend_window, text="Enter number of days to extend:").pack(pady=10)
            self.days_entry = tk.Entry(self.extend_window)
            self.days_entry.pack(pady=5)

            tk.Button(self.extend_window, text="Extend", command=self.update_due_date).pack(pady=10)

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
            messagebox.showerror("Invalid input", "Please enter a valid number")

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

        if database.check_resource_quantity(self.conn, h_r_id, self.t_id) and database.check_student(self.conn, h_s_id):
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
            messagebox.showerror('Error', 'Resource not available or Student does not exist')

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
        self.returned_tree = ttk.Treeview(return_tab, columns=columns, show='headings')

        bg_color_returned = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color_returned = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color_returned = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color_returned, foreground=text_color_returned, fieldbackground=bg_color_returned, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color_returned)], foreground=[('selected', selected_color_returned)])
        self.main.bind("<<TreeviewSelect>>", lambda event: self.main.focus_set())

        # self.returned_tree.bind("<Button-3>", self.show_context_menu_returned)

        # Define headings
        self.returned_tree.heading('ref', text='Reference')
        self.returned_tree.heading('s_id', text='Student ID')
        self.returned_tree.heading('r_id', text='Resource ID')
        self.returned_tree.heading('b_date', text='Borrowed Date')
        self.returned_tree.heading('d_date', text='Due Date')
        self.returned_tree.heading('r_date', text='Returned Date')

        # Define column widths
        self.returned_tree.column('ref', width=80)
        self.returned_tree.column('s_id', width=90)
        self.returned_tree.column('r_id', width=90)
        self.returned_tree.column('b_date', width=105)
        self.returned_tree.column('d_date', width=90)
        self.returned_tree.column('r_date', width=105)

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
        self.resources_tree.column('r_id', width=140)
        self.resources_tree.column('r_type', width=140)
        self.resources_tree.column('r_des', width=140)
        self.resources_tree.column('r_qty', width=140)

        self.resources_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

        # Add a vertical scrollbar
        scrollbar_resources = ttk.Scrollbar(resources_tab, orient='vertical', command=self.resources_tree.yview)
        scrollbar_resources.grid(row=0, column=4, sticky='ns')
        self.resources_tree.configure(yscrollcommand=scrollbar_resources.set)

        # Add Borrowed ResourceForm
        self.add_resources_CTklable = ctk.CTkLabel(resources_tab, text="Add a new resource:")
        self.add_resources_CTklable.grid(row=1, column=0, padx=5, pady=0, sticky='n')

        self.r_type_CTklabel = ctk.CTkLabel(resources_tab, text="Object Name:")
        self.r_type_CTklabel.grid(row=2, column=0, padx=5, pady=5)
        self.r_type_entry = ctk.CTkEntry(resources_tab)
        self.r_type_entry.grid(row=3, column=0, padx=5, pady=5)

        self.r_des_CTklabel = ctk.CTkLabel(resources_tab, text="Model/Description:")
        self.r_des_CTklabel.grid(row=2, column=1, padx=5, pady=5)
        self.r_des_entry = ctk.CTkEntry(resources_tab)
        self.r_des_entry.grid(row=3, column=1, padx=5, pady=5)

        self.r_qty_CTklabel = ctk.CTkLabel(resources_tab, text="Number of resources:")
        self.r_qty_CTklabel.grid(row=2, column=2, padx=5, pady=5)
        self.r_qty_entry = ctk.CTkEntry(resources_tab)
        self.r_qty_entry.grid(row=3, column=2, padx=5, pady=5)

        self.add_resources_button = ctk.CTkButton(resources_tab, text="Add New Resources", command=self.add_resources)
        self.add_resources_button.grid(row=4, column=1, columnspan=1, pady=10)

    def show_context_menu_resources(self, event):

        selected_item = event.widget.selection()
        if selected_item:
            
            context_menu_resources = tk.Menu(event.widget, tearoff=0)
            context_menu_resources.add_command(label="Return Object", command= self.return_object)
            context_menu_resources.add_command(label="Extend Due Date", command= self.extend_borrowed)
            context_menu_resources.add_command(label="close", command= self.close_context_menu)

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

            tk.Label(self.extend_window_r, text="Enter number of resources:").pack(pady=10)
            self.qty_entry = tk.Entry(self.extend_window_r)
            self.qty_entry.pack(pady=5)

            tk.Button(self.extend_window_r, text="Update", command=self.update_qty).pack(pady=10)

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


    # settings
    def create_settings_tab(self):
        settings_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(settings_tab, text='Settings')




    # help tab -------------------------------------------------------------------
    def create_help_tab(self):
        help_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(help_tab, text='Help')

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