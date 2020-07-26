import datetime


class History:

	patient_problems = {
		"symptom_date": "",
		"symptoms": "",
		"disease": "",
		"surgery": "",
	}

	def ask_user_history(self):
		print("Any past disease history ?")
		choice = input(" 1.Yes \n 2.No ")
		if choice == "1":
			self.starting_of_symptoms()
			self.basic_symptoms()
			self.ask_user_for_problems()
			self.ask_for_allergy()
			self.ask_for_surgeries()
			print(self.patient_problems)
		else:
			print("Thankyou for your time")

	def starting_of_symptoms(self):
		print("When did your symptoms start showing ?")
		year = int(input("Enter the year"))
		date = int(input("Enter the date"))
		month = int(input("Enter the month"))
		self.patient_problems["Symptoms_date"] = datetime.datetime(year, date, month)

	def basic_symptoms(self):
		print("What were your basic symptoms ? ")
		self.patient_problems["Symptoms"] = input("Enter you symptoms :")

	def ask_user_for_problems(self):
		print("Do you have any disease ? \n 1.Yes \n 2.No")
		choice = input("Enter the serial no")
		if int(choice) == 1:
			self.patient_problems["disease"]=input("Enter your disease")
		else:
			print("Enter valid serial number")

	def ask_for_allergy(self):
		print("Do you have any allergy ?")
		allergy = input("Enter : \n 1.Yes \n 2.No ")
		if allergy == "1":
			self.patient_problems["allergy"] = input("Enter your allergy :")
		else:
			print("You can proceed further")

	def ask_for_surgeries(self):
		print("Did you have any past surgeries ?")
		surgery = input(" 1.Yes \n 2.No ")
		if surgery == "1":
			self.patient_problems["Surgery"] = input("Enter surgery : ")
		else:
			print("You can proceed further")



history = History()
history.ask_user_history()