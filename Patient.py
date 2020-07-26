import diagnosis

diag = diagnosis.Diagnosis()


class PatientInfo:
    patient_detail = {

       "personal_info": {
           "name": "",
           "gender": "",
           "age": "",
           "address": "",
           "contact_detail": "",
       },

        "diagnosis": ""
    }

    def ask_mode(self):
        doc_choice = input("Do you want to add or view patient? 1==add \n,0==view \n")
        if int(doc_choice) == 1:
            print("add")
            self.ask_for_patient_detail()
        elif int(doc_choice) == 0:
            print("view")
        else:
            print("Enter your valid choice")

    def ask_for_patient_detail(self):
        self.patient_detail["personal_info"]["name"] = input("your name:")
        self.patient_detail["personal_info"]["age"] = input("your age:")
        self.patient_detail["personal_info"]["address"] = input("your address:")
        self.patient_detail["personal_info"]["contact_detail"] = int(input("your contact_detail:"))
        gender = input("gender \n M=male \n F=female ")
        if gender == "M":
            self.patient_detail["personal_info"]["gender"] = "male"
        else:
            self.patient_detail["personal_info"]["gender"] = "female"

        self.patient_detail["diagnosis"] = diag.ask_for_diagnosis_report()
        print("This is your info")





