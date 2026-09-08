import datetime as dt

target_dt = dt.datetime(2020, 1, 1, 12, 0, 1)
current_dt = dt.datetime.now()

if target_dt < current_dt:
    print("Target Date has Passes")
else:
    print("Target Date has NOT Passes")
