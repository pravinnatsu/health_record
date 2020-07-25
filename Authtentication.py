import pyrebase

config = {
    "apiKey": "AIzaSyAym469AYW_bMgx4An4PdRBKWO2qX-sEdY",
    "authDomain": "health-record-management.firebaseapp.com",
    "databaseURL": "https://health-record-management.firebaseio.com",
    "projectId": "health-record-management",
    "storageBucket": "health-record-management.appspot.com",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


class Authentication:

    @staticmethod
    def create_user_account(email, password):
        auth.create_user_with_email_and_password(email, password)
        print("Registration succesfull")

    @staticmethod
    def login_user(email, password):
        auth.sign_in_with_email_and_password(email, password)
        print("You are successfully login")


class Database:
    @staticmethod
    def storing_user_details(doctor_details):
        db.child("users").child(doctor_details["doctors_name"]).child('doctor_details').set(doctor_details)

    def store_diagnosed_data(self, name, diagnosed_data):
        db.child('users').child(name).child('patients').child('patient-details').set(diagnosed_data)
     

    def store_patient_details(self, name, patient_details):
        db.child('users').child(name).child('patients').set(patient_details)
