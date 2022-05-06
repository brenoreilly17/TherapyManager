from Project.db import Database


class TherapyDatabase(Database):
    
    def __init__(self):
       super(TherapyDatabase, self).__init__()

    def insert_add_client(self, first_name, last_name, email, phone_number):
        self.execute("insert into client(first_name, last_name, email, phone) values (%s, %s, %s, %s)",
                    [first_name, last_name, email, phone_number])
        
    def insert_add_appointment(self, appt_date, appt_time, appt_duration):
        self.execute("insert into appointment(appt_date, appt_time, appt_duration) values (%s, %s, %s)", [appt_date, appt_time, appt_duration])

    def get_client_list(self):
        q = " select concat(last_name, ', ', first_name) as name, client_id" \
            " from client"\
            " order by name"
        return self.query(q)
    
    def get_therapy_type(self, therapy_desc):
        therapy_query = "select therapy_type_id from therapy_type where therapy_description = %s"
        return self.query_one(therapy_query, [therapy_desc])
