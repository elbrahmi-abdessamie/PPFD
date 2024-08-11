import datetime, time

x = datetime.datetime.now()
s = time.time()
print(f"Seconds since January 1, 1970: {(s):,.4f} {(s):.2E} in scientific notation")
print(x.strftime("%b"), x.day, x.year)