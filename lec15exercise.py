import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
#https://docs.python.org/3/library/time.html#time.strftime

from datetime import datetime

current_time = datetime.now().time()
timestamp = current_time.strftime('%H:%M:%S')

if current_time < datetime.strptime('11:59:59', '%H:%M:%S').time():
    print("GOOD MORNING SIR")
elif current_time > datetime.strptime('12:00:00', '%H:%M:%S').time():
    print("GOOD AFTERNOON SIR")





