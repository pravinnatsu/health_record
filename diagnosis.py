import Authtentication

db = Authtentication.Database()


class Diagnosis:
    diagnosis = []
    patient_details = {
    }

    def ask_for_diagnosis_report(self):
        print('Enter daignosis info: ')
        print('Enter q for exit')
        while True:
            diagnosis_input = input("")
            if diagnosis_input == 'q':
                break
            else:
                self.diagnosis.append(diagnosis_input)

        print(self.diagnosis)
        self.patient_details.update({"diagnosis": self.diagnosis})
        print(self.patient_details)


