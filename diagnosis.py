import Authentication

db = Authentication.Database()


class Diagnosis:
    diagnosis = []

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
        return self.diagnosis


