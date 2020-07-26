class Diet:
	user_diet = {
		"breakfast": "",
		"lunch": "",
		"snacks": "",
		"dinner": "",

	}

	def ask_for_diet_time(self):
		time = input("Enter which time you want : \n 1.Breakfast \n 2.lunch \n 3.snacks \n 4.dinner \n ")
		if time == "1":
			self.user_diet["breakfast"] = input("Enter breakfast diet :")
		elif time == "2":
			self.user_diet["lunch"] = input("Enter lunch diet:")
		elif time == "3":
			self.user_diet["snacks"] = input("Enter snacks diet:")
		elif time == "4":
			self.user_diet["dinner"] = input("Enter dinner diet:")
		else:
			print("Enter valid input")


diet = Diet()
diet.ask_for_diet_time()
