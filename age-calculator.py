from datetime import time delta
from datetime import date

def bDay_convert(bDay):
  """
  Converts format of date from string to fromisoformat tuple
  """
  return date.fromisoformat(bDay)
  
def todayPOSIX():
  today = date.today()
  return date.fromisoformat(today)

def delta_calc(dStart):
  """
  Distance between birth date and today's POSIX date
  """
  
  
    
  
bDay = str(input("Please give me your birth date in YYYY-MM-DD form.\n")
bDay_convert = delta_calc(bDay)
delta = delta_calc(bDay_convert)

