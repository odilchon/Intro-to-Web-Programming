from datetime import datetime, timedelta
import time

#Lab 1
current_dt = datetime.now()
formatted_dt = current_dt.strftime("%d-%m-%Y %H:%M:%S")
print("Current date/time:", formatted_dt)
print()

#Lab 2
today_dt = datetime.now()
new_year = datetime(today_dt.year, 12, 31)

if today_dt > new_year:
    new_year = datetime(today_dt.year + 1, 12, 31)

difference = new_year - today_dt
print("Days left until New Year:", difference.days)
print()

#Lab 3
def start_timer(sec):
    finish = datetime.now() + timedelta(seconds=sec)

    while True:
        remaining = finish - datetime.now()
        seconds_left = int(remaining.total_seconds())

        if seconds_left <= 0:
            print("\nRemaining: 0 seconds")
            print("Countdown complete")
            break

        print(f"Remaining: {seconds_left} sec", end="\r")
        time.sleep(1)

start_timer(10)

#Lab 4
def print_calendar(y, m):
    first_day = datetime(y, m, 1)
    first_weekday = first_day.weekday()

    if m == 12:
        next_m = datetime(y + 1, 1, 1)
    else:
        next_m = datetime(y, m + 1, 1)

    last_day = next_m - timedelta(days=1)

    print("\nMon Tue Wed Thu Fri Sat Sun")
    print("    " * first_weekday, end="")

    day_cursor = first_day
    while day_cursor <= last_day:
        print(f"{day_cursor.day:3}", end=" ")

        if day_cursor.weekday() == 6:
            print()

        day_cursor += timedelta(days=1)

    print()

print_calendar(2025, 5)