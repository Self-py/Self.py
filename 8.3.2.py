my_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}
user_number = int(input("Please enter a number between 1 and 7: "))
if user_number == 1:
	print(my_dict["last_name"])
if user_number == 2:
    print(mariah["birth_date"][3:5])
if user_number == 3:
	print(len(my_dict["hobbies"]))
if user_number == 4:
	print(my_dict["hobbies"][-1])
if user_number == 5:
	my_dict["hobbies"].append("Cooking")
if user_number == 6:
	my_dict["birth_date"] = (int(my_dict["birth_date"][:2]), int(my_dict["birth_date"][3:5]), int(my_dict["birth_date"][6:]))
	print(my_dict["birth_date"])
if user_number == 7:
    day = int(my_dict["birth_date"][:2])
    month = int(my_dict["birth_date"][3:5])
    year = int(my_dict["birth_date"][6:])
    from datetime import date
 
    def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    my_dict["age"] = age(date(year, month, day))
    print(my_dict["age"])