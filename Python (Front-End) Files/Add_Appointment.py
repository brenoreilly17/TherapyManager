#Python's de-facto standard GUI (graphical user interface) package
#This is what allows us to have a pop-up screen for entering information (a.k.a. what the user sees at all times)
from tkinter import *

class AddAppointment(Frame):
    def __init__(self, master, db, onclose):
        super(AddAppointment, self).__init__(master)
        self.db = db
        self.create_widgets()
        self.grid()
        self.onclose = onclose

    def create_widgets(self):

        #"Label" tells you what type of information to give (and in which format)
        #"Entry" is the actual box you type the information in
        #"Sticky" points to the location of the label on the widget
        Label(self, text="Enter appointment date (YYYY/MM/DD):").grid(row=0, column=1, sticky=W)
        self.entry5_ent = Entry(self, width=6)
        self.entry5_ent.grid(row=0, column=3, sticky=W)

        Label(self, text="Enter appointment time:").grid(row=2, column=1, sticky=W)
        self.entry6_ent = Entry(self, width=6)
        self.entry6_ent.grid(row=2, column=3, sticky=W)

        Label(self, text="Enter appointment duration (in minutes):").grid(row=4, column=1, sticky=W)
        self.entry7_ent = Entry(self, width=6)
        self.entry7_ent.grid(row=4, column=3, sticky=W)

        self.client_names = []
        Label(self, text = "Choose Client:").grid(row=6, column =1, sticky=W)

        clients = self.db.get_client_list()
        self.client_id = StringVar()

        r = 7
        for client in clients:
            rb = Radiobutton(self, text = client[0], variable=self.client_id, value = client[1])
            rb.grid(row=r, column=1, sticky=W)
            r += 1

        Button(self, text="Save", command=self.add_to_appointment_table).grid(row=10, column=3, sticky=W)

        Label(self, text = "Choose Therapy Type:").grid(row = 6, column = 2, sticky = W)

        self.therapy_type = StringVar()
        le = Radiobutton(self, text= "Learning Evaluation", variable=self.therapy_type, value=1)
        le.grid(row=7,column = 2, sticky = W)
        dep = Radiobutton(self, text = "Depression", variable = self.therapy_type, value = 2)
        dep.grid(row = 8, column = 2, sticky = W)
        anx = Radiobutton(self, text = "Anxiety", variable = self.therapy_type, value = 3)
        anx.grid(row = 9, column = 2, sticky = W)


    def add_to_appointment_table(self):
        appt_date = self.entry5_ent.get()
        appt_time = self.entry6_ent.get()
        appt_duration = self.entry7_ent.get()

        self.db.insert_add_appointment(appt_date, appt_time, appt_duration)
        self.onclose()
