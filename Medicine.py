class Medicine:
	medicine_name = []
	medicine_dose = []
	medicines = {

	}

	def medicine_list(self):
		print('Enter medicine info: ')
		print('Enter q for exit')
		while True:
			medicine_input = input("Medicines:")
			dosage_input = input("dosages :")
			if medicine_input == 'q':
				break
			else:
				self.medicine_name.append(medicine_input)
				self.medicine_dose.append(dosage_input)





medicine = Medicine()
medicine.medicine_list()
