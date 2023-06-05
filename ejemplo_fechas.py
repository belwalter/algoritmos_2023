
from datetime import datetime, date, time, timedelta


current_date = datetime.today()
print(current_date)
print(current_date.date())
print(current_date.day, current_date.month, current_date.year)
print(current_date.time())
print(current_date.hour, current_date.minute, current_date.second)

other_date = datetime.fromisoformat('2023-06-05 20:25:56')

print(current_date > other_date)
print(current_date + timedelta(days=7, hours=7))
print(current_date - timedelta(days=7))

print(current_date.strftime("%A %a %w %d %-d %b %m %-m %y %Y %H %-H %I %-I %p %z %U %j"))
print(current_date.strftime("%c %x %X"))


cantidad = 20
primera_clase = [0] * 5
turista = [0] * 15

print(primera_clase)
print(turista)


