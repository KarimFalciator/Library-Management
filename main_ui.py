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
        self.create_read_tab()
        self.create_resource_list_tab()
        self.create_settings_tab()
        self.create_help_tab()
        self.add_borrowed_from_db()

    # home tab ---------------------------------------------------------------
    
    def create_home_tab(self):
        home_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(home_tab, text='Home')

        columns = ('ref', 's_id', 'r_id', 'b_date', 'd_date', 'r_date')
        self.current_tree = ttk.Treeview(home_tab, columns=columns, show='headings')

        bg_color = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = self.main._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        self.main.bind("<<TreeviewSelect>>", lambda event: self.main.focus_set())

        self.current_tree.bind("<Button-3>", self.show_context_menu)

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
        scrollbar = ttk.Scrollbar(home_tab, orient='vertical', command=self.current_tree.yview)
        scrollbar.grid(row=0, column=4, sticky='ns')
        self.current_tree.configure(yscrollcommand=scrollbar.set)

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

    def show_context_menu(self, event):
        # Get the selected item
        selected_item = event.widget.selection()
        if selected_item:
            # Create a context menu
            context_menu = tk.Menu(event.widget, tearoff=0)
            context_menu.add_command(label="Return Object", command= self.retun_object)
            context_menu.add_command(label="Extend Due Date", command= self.extend_borrowed)
            context_menu.add_command(label="close", command= self.close_context_menu)
            
            # Show the context menu
            context_menu.post(event.x_root, event.y_root)

             # Bind the focus out event to destroy the context menu
            self.current_tree.bind("<FocusOut>", self.hide_context_menu)

    def hide_context_menu(self, event):
        if hasattr(self, 'context_menu'):
            self.context_menu.unpost()
            del self.context_menu
        else:
            pass
    
    def retun_object(self):
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
            self.refresh_tree()
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
            self.refresh_tree()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")

    def refresh_tree(self):
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
            self.refresh_tree()
        else:
            messagebox.showerror('Error', 'Resource not available or Student does not exist')

    def add_borrowed_from_db(self):
        # Fetch all borrowed records from the database
        borrowed_records = database.get_all_borrowed(self.conn, self.t_id)

        # Insert each borrowed record into the Treeview
        for record in borrowed_records:
            self.current_tree.insert('', 'end', values=record)


    #  read tab -----------------------------------------------------------------
    def create_read_tab(self):
        read_tab = ctk.CTkFrame(self.Notebook, width=500, height=490)
        self.Notebook.add(read_tab, text='Previous Read resources')

        columns = ('Name', 'Genre', 'Borrowed', 'Returned')
        current_tree = ttk.Treeview(read_tab, columns=columns, show='headings')

        # Define headings
        current_tree.heading('Name', text='Name of resource')
        current_tree.heading('Genre', text='Genre')
        current_tree.heading('Borrowed', text='Borrowed')
        current_tree.heading('Returned', text='Returned')

        # Define column widths
        current_tree.column('Name', width=170)
        current_tree.column('Genre', width=110)
        current_tree.column('Borrowed', width=110)
        current_tree.column('Returned', width=110)

        current_tree.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(read_tab, orient='vertical', command=current_tree.yview)
        scrollbar.grid(row=5, column=5, sticky='ns')

        current_tree.configure(yscrollcommand=scrollbar.set)

    # resource list tab --------------------------------------------------------------
    def create_resource_list_tab(self):
        resource_list_tab = ctk.CTkFrame(self.Notebook, width=300, height=490)
        self.Notebook.add(resource_list_tab, text='List of resources')

        columns = ('Name', 'Author', 'Genre')
        self.resource_list_tree = ttk.Treeview(resource_list_tab, columns=columns, show='headings')

        # Define headings
        self.resource_list_tree.heading('Name', text='Name of resource')
        self.resource_list_tree.heading('Author', text='Author')
        self.resource_list_tree.heading('Genre', text='Genre')

        # Define column widths
        self.resource_list_tree.column('Name', width=170)
        self.resource_list_tree.column('Author', width=110)
        self.resource_list_tree.column('Genre', width=110)

        self.resource_list_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(resource_list_tab, orient='vertical', command=self.resource_list_tree.yview)
        scrollbar.grid(row=0, column=4, sticky='ns')

        self.resource_list_tree.configure(yscrollcommand=scrollbar.set)

        # Add Resource Form
        ctk.CTkLabel(resource_list_tab, text="resource Name:").grid(row=1, column=0, padx=5, pady=5)
        self.resource_name = ctk.CTkEntry(resource_list_tab)
        self.resource_name.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(resource_list_tab, text="Author:").grid(row=2, column=0, padx=5, pady=5)
        self.resource_author = ctk.CTkEntry(resource_list_tab)
        self.resource_author.grid(row=2, column=1, padx=5, pady=5)

        ctk.CTkLabel(resource_list_tab, text="Genre:").grid(row=3, column=0, padx=5, pady=5)
        self.resource_genre = ctk.CTkEntry(resource_list_tab)
        self.resource_genre.grid(row=3, column=1, padx=5, pady=5)

        ctk.CTkButton(resource_list_tab, text="Add Resource", command=self.add_resource).grid(row=4, column=0, columnspan=2, pady=10)

    def add_resource(self):
        # Fetch details from entry widgets
        name = self.resource_name.get()
        author = self.resource_author.get()
        genre = self.resource_genre.get()

        # Insert into Treeview
        self.resource_list_tree.insert('', 'end', values=(name, author, genre))

        # Clear the entry fields
        self.resource_name.delete(0, 'end')
        self.resource_author.delete(0, 'end')
        self.resource_genre.delete(0, 'end')


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


# nuova funzione per aggiungere un tutte le borrowed che sono nel database al treeview della home quando si apre il programma
# fare in modo che la fuzione per aggiungere un borrowed al database chiami solo il borrowed non ritornati
# fai in modo che si puo prendere uno solo di ogni oggetto
# aggiungi oggetto nummero che vuole non perforza deve essere uno in piu se ce il oggetto
# aggiungi t_id a risorse, cosi che un insegnante puo dare via solo i suoi oggetti non quelli di altri insegnanti
# aggiungi una window per aggiungere nuovi oggetti se e la prima volta che si usa il programma, usa un text file per confermare se ha fatto log in (YES/NO)
# aggiungi una window per aggiungere nuovi studenti se e la prima volta che si usa il programma, usa un text file per confermare se ha fatto log in (YES/NO)