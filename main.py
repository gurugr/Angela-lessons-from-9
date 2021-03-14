
def leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    year = False
def days_in_month(month,year):
  month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
  if leap_year(year) and month == 2:
    days = month_days[month-1] + 1
    return 29
  else:
    days = month_days[month-1]
    return days

    
    
while True:
  year =  int(input("Enter the year : "))

  month =  int(input("Enter the month : "))
  if month > 0 and month < 13:
    days = days_in_month(month,year)
    print(f"{year},days of {month} are {days}")
  else:
    print(f"{month} is a invalied input ")
  