import Authentication

db = Authentication.Database()

class Datatable:

    def get_data(self):
        name = input("Doctor please enter your name again: ")
        print('this is data')
        patient_name = input("please enter patient name: ")
        print(db.get_patient_data(name,patient_name))



data = Datatable()
data.get_data()
