import datetime

planet_dict = [
	'mercury': 88,
	'venus': 225,
	'mars': 687,
	'jupiter': 4333,
	'saturn': 10759,
	'uranus': 30687,
	'neptune': 60190
]

def birthdate_prompt():
	return str(input('What is your birthdate?'))

def name_prompt():
	return str(input('What is your name?'))

def validate_birthday(x):

def run():
	while True:
		name = name_prompt()
		b_day = birthdate_prompt()
		if validate_birthday:
			print(f'Thank you, {name}!')
			break
		else:
			print(f'That is not a valid entry, {name}. Please try again.\n')
