from tkinter import *
from Project.Add_Client import AddClient
from Project.Internal_Assessment_First_Screen import ChoosePath
from Project.Add_Appointment import AddAppointment
from Project.therapy_db import TherapyDatabase

class Therapy_Manager (object):

    def __init__(self):
        self.root = Tk()
        self.db = TherapyDatabase()

    def setup_therapy_selector(self):
        self.root.title ("Select your path!")
        self.path_chooser = ChoosePath(self.root, self.onclose_path_selector)

    def onclose_path_selector(self, selected_therapy):

        if selected_therapy == "add client":
            self.path_chooser.destroy()
            self.root.title("Add Client")
            self.addclient_screen = AddClient(self.root, self.db, self.onclose_add_client_appointment)


        elif selected_therapy == "add appointment":
            self.path_chooser.destroy()
            self.root.title("Add Appointment")
            self.addappointment_screen = AddAppointment(self.root, self.db)
            self.onclose_add_client_appointment

    def onclose_add_client_appointment(self):
        self.path_chooser.destroy()
        self.setup_therapy_selector()


def main():
    therapy = Therapy_Manager()
    therapy.setup_therapy_selector()
    therapy.root.mainloop()

main()
