from tkinter import *

class AddClient(Frame):
    def __init__(self, master, db, onclose):
        super(AddClient, self).__init__(master)
        self.create_widgets()
        self.grid()
        self.db = db
        self.onclose = onclose

    #All widgets pertaining to client information pop up (font set, location set, width of text boxes set)
    #'Label' pertains to the type of information needed as inputs
    #'Entry' is the actual box you enter information to
    def create_widgets(self):
            Label(self, text= "Enter First Name:", font= "Helvetica 18 bold").grid(row=0, column=1, sticky = W)
            self.entry_first_name = Entry(self, width = 12)
            self.entry_first_name.grid(row=0, column = 3, sticky = W)

            Label(self, text = "Enter Last Name:", font = "Helvetica 18 bold").grid(row= 2, column = 1, sticky = W)
            self.entry_last_name = Entry(self, width = 12)
            self.entry_last_name.grid(row = 2, column = 3, sticky = W)

            Label(self, text = "Email:", font = "Helvetica 18 bold").grid(row = 4, column = 1, sticky = W)
            self.entry_email = Entry(self, width = 20)
            self.entry_email.grid(row = 4, column = 3, sticky = W)

            Label(self, text = "Phone Number:", font = "Helvetica 18 bold").grid(row = 6, column = 1, sticky = W)
            self.entry4_phone_number = Entry(self, width = 20)
            self.entry4_phone_number.grid(row = 6, column = 3, sticky = W)

            Button(self, text="Save", command=self.add_to_database).grid(row=10, column=3, sticky=W)

    #Pushes the information to the MySQL Workbench database for the therapist to see
    def add_to_database(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        phone_number = self.entry4_phone_number.get()

        self.db.insert_add_client(first_name, last_name, email, phone_number)

        print("Added client")
        self.onclose()
