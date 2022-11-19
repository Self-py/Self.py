temperature = input("Insert the temperature you would like to convert: ").upper()
temperature_number = float(temperature.replace(temperature[-1], ""))
if "F" in (temperature):
	print(5 / 9 * (temperature_number - 32), "C")
elif "C" in (temperature):
	print(9 / 5 * (temperature_number) + 32, "F")