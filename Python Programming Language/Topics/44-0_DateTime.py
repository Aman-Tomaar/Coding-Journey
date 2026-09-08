import datetime as dt

date = dt.date(2026, 7, 30)  # (year, month, day)
print(f"Entered Date: {date}")
today = dt.date.today()
print(f"Today's Date: {today}\n")

time = dt.time(12, 30, 1)  # (hour, min, sec)
print(f"Entered Time: {time}")
now = dt.datetime.now()
print(f"Date & Time RightNow: {now}\n")
now = now.strftime("%H:%M:%S %d-%m-%Y")  # strf = string format time
print(f"FORMATTED Date & Time RightNow: {now}\n")
