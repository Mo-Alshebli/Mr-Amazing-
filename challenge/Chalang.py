from datetime import date
today = date.today()
Dic_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
input_days = int(input("Enter Days : "))
Data = [today.day, today.month, today.year]
day, month, year = today.day, today.month, today.year
while input_days != 0:
    if day == Dic_month[month]:
        month = month + 1
        day = 0
    day = day + 1
    input_days = input_days - 1
    if month > 12:
        year = year + 1
        if year % 4 == 0:
            Dic_month.update({2: 29})
        else:
            Dic_month.update({2: 28})
        month = 1
print("Today date is: ", today)
print("New date is: ", year, "-", month, "-", day)
