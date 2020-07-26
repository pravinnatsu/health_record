import Authentication
import diagnosis
import Patient

auth = Authentication.Authentication()
db = Authentication.Database()
diag = diagnosis.Diagnosis()

patient = Patient.PatientInfo()


class Hrm:
    email = ""
    password = ""

    doctor_details = {
        "doctors_name": " ",
        "doctors_specialization": " ",
        "hospital_name": " ",
    }

    def greet(self):
        print("Hello Doctor!!!!")

    def ask_for_user_choice(self):
        print("Do you want to login or register ?")
        choice = input("Enter: \n 1 : Login \n 2 : Register \n ")
        if int(choice) == 1:
            self.ask_for_user_data()
            self.login_user()
        elif int(choice) == 2:
            self.ask_for_user_data()
            self.register_user()
            self.ask_for_doctors_details()
            self.store_doctor_detail()
            self.greet()

        else:
            print("Please enter a valid input ")

    def ask_for_doctors_details(self):
        self.doctor_details["doctors_name"] = input("Enter Your name : ")
        self.doctor_details["doctors_specialization"] = input("Enter your specialization : ")
        self.doctor_details["hospital_name"] = input("Enter your hospital name : ")

    def ask_for_user_data(self):
        self.email = input("Enter your email : ")
        self.password = input("Enter your password : ")

    def register_user(self):
        auth.create_user_account(self.email, self.password)

    def login_user(self):
        auth.login_user(self.email, self.password)

    def store_doctor_detail(self):
        db.storing_user_details(self.doctor_details)

    #def get_diagnosis_detail(self):
        #diag.ask_for_diagnosis_report()
        #self.add_diagnosis_report()

    #def add_diagnosis_report(self):
        #name = input("enter your name again")
        #db.store_diagnosed_data(name, diag.patient_details)

    @staticmethod
    def add_patient_details():
        patient.ask_mode()
        name = input("Doctor please enter your name again")
        db.store_patient_details(name,patient.patient_detail)


hrm = Hrm()
hrm.ask_for_user_choice()
hrm.add_patient_details()
