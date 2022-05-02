# TherapyManager
A local therapist in my neighborhood came to me to assist her with managing her clients. As her practice grows larger, she needs a way to add, remove, and visualize her clients on one platform. I built a user-friendly program that can assist her (or anyone) with entering, deleting, and updating clientele information.

For personal reasons, the therapist who I created the project for has chosen to remain anonymous. Throughout my explanation of the project, I will refer to her as Dr. N. Dr. N works as both a supervisor of special education at a public school and as the owner of her own therapy private practice in New York. Since Dr. N works around the clock, she finds it difficult to organize important information regarding the operation of her practice. For example, as a psychologist, it is important to keep track of each client you treat, the type of therapy being offered, the amount of money each session costs, the days of the
week each client will visit, and many more aspects of the weekly or monthly sessions that are crucial to organize. So, I decided to intervene and help her out.

To create the user-friendly program for the client, I used Python and MySQL. While MySQL Workbench will help to create the fluid database for the client, a python front end is necessary, and it was developed to ensure that Dr. N could access and manipulate her company data accordingly. MySQL Workbench, being a unified visual tool for database creators, has the potential to store all of Dr. N’s client information in a clean, well-formatted relationship entity
diagram. Both Python and MySQL can develop relatively interactive programs, and Dr. N will benefit from having the ability to manipulate data extensively as she sees fit. Moreover, Python and MySQL programs can be accessed on any computer operating system, which is important to take into account. Although the client currently manages her practice on her MacBook Pro, should she switch computers, it is crucial that the database can be transferable, utilized, and accessed across operating systems.

Currently, the program supports:

1. Simple, stress-free navigation
2. The entering of patient details, including first name, last name, email, and phone
number
3. The entering of appointment details, including appointment duration, appointment
time, and appointment date
4. The option to choose which type of therapy pertains to each client

The program also prevents the client from entering invalid information, and the system allows the user to add as many clients and appointments as she wants until she desires to terminate the program.

The python portion is designed so that the user has two possible paths to embark on when operating the front end.

The first scenario involves adding an appointment to the client’s database. On the first GUI, the user will need to press the “Add Appointment” button. After, the client needs to enter five pieces of information into the tkinter GUI. These five pieces of data are the date of the appointment, the time of the appointment, the duration of the appointment, the client associated with the appointment, and the type of therapy that the client will be needing for the appointment. Once the information about the appointment is entered into the text boxes, the user will press “save”, and all of the data will be transferred to their respective tables in the database.

The second scenario involves the user adding a client to the therapy database. Much like the first scenario, the user will first press the “Add Client” button on the user interface. The second GUI presented to the user will prompt the user to enter the client’s first name, last name, email address, and phone number. Once the information is entered, it will be transferred to the database (SQL). Additionally, the name of the client will be accessible to the
user when entering appointment information should the user choose the “Add Client” path at the beginning of the program.

After each time the user presses “Save”, the user will have the opportunity to either terminate the program or continue to add more clients or appointments, as the home screen will appear again. Print statements will appear notifying the user that the information they have entered has
been saved and has been stored in the database. The user will have access to the information inputted into the database via MySQL Workbench, which will assist the client with running her business smoothly and keeping track of all patient information in a neat, organized, clear, and coherent manner.
