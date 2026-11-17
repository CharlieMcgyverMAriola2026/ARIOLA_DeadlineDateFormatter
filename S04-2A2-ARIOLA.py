from datetime import date

event = input("Event title: ")
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

d = date(year, month, day)

print("Event:", event.upper())
print("Date:", d.strftime("%B %d, %Y"))
print("Year:", d.year)
print("Month:", d.strftime("%B"))
print("Day:", d.day)
print("Weekday:", d.strftime("%A"))