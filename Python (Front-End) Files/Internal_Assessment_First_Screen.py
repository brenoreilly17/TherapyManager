#Python's de-facto standard GUI (graphical user interface) package
#This is what allows us to have a pop-up screen for entering information (a.k.a. what the user sees at all times)
from tkinter import *

class ChoosePath(Frame):
    def __init__(self, master, onclose):
        super(ChoosePath, self).__init__(master)
        self.create_widgets()
        self.grid()
        self.onclose = onclose


    def create_widgets(self):
        Label(self, text = "Therapy Database Organizer", font = "Helvetica 24 bold", fg = "Blue").grid(row = 0, column = 3, sticky = W)
        self.addclient = Button(self, text = "Add Client", command = self.addclient_clicked, font = "Helvetica 18", fg = "Red")
        self.addclient.grid(row = 5, column = 3)
        self.addappointment = Button(self, text = "Add Appointment", command = self.addappointment_clicked, font = "Helvetica 18", fg = "Red")
        self.addappointment.grid(row = 7, column = 3)

    def addclient_clicked(self):
        self.onclose("add client")

    def addappointment_clicked(self):
        self.onclose("add appointment")
