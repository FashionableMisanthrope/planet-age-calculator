from datetime import datetime, timedelta
import re

planet_dict = {
	'mercury': 88,
	'venus': 225,
	'mars': 687,
	'jupiter': 4333,
	'saturn': 10759,
	'uranus': 30687,
	'neptune': 60190
}

def birthdate_prompt():
	return str(input('What is your birthdate? Use (mm/dd/yyyy)\n'))

def name_prompt():
	return str(input('What is your name?\n'))

def validate_birthday(x):
	birthdate_regex = re.compile(r'\d\d\/\d\d\/\d\d\d\d')
	return birthdate_regex.search(x)

def get_days_alive_from_time_delta(bdate):
	month = int(bdate.split('/')[0])
	day = int(bdate.split('/')[1])
	year = int(bdate.split('/')[2])
	bdate_obj = datetime(year, month, day)
	today = datetime.now()
	days_alive = today - bdate_obj
	return days_alive.days

def run():
	name = name_prompt()
	while True:
		b_day = birthdate_prompt()
		if validate_birthday(b_day) is None:
			print(f'That is not a valid entry, {name}. Please try again.\n')
		else:
			print(f'Thank you, {name}!')
			break

	days_alive = get_days_alive_from_time_delta(b_day)
