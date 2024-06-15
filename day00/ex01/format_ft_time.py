import datetime, time

x = datetime.datetime.now()
s = time.time()
print(f"Seconds since January 1, 1970: {int(s)} {(s):.2E} in scientific notation")
print(x.strftime("%B")[:3], x.day, x.year)