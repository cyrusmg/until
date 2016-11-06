#!/usr/bin/env python

import argparse
from datetime import datetime

def parse_datetime(date, time):
    s = "{} {}".format(date, time)
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M")
    except ValueError:
        msg = "Not a valid date: '{}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def stringify(time, name):
    if time == 0:
        return None
    elif time == 1:
        return "{} {}".format(time, name)
    else:
        return "{} {}s".format(time, name)

parser = argparse.ArgumentParser(description='Calculate days since/until a date')
parser.add_argument('date', help='event date in YYYY-MM-DD format')
parser.add_argument('time', default="00:00", nargs='?', help='event time in HH:MM format')

args = parser.parse_args()
event_datetime = parse_datetime(args.date, args.time)

timedelta = abs(event_datetime - datetime.now())

days = timedelta.days
hours = timedelta.seconds // 3600

days = stringify(days, "day")
hours = stringify(hours, "hour")

if days and hours:
    print("{}, {}".format(days, hours))
elif days:
    print("{}".format(days))
elif hours:
    print("{}".format(hours))
else:
    print("It's now!")
