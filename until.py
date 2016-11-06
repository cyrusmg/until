#!/usr/bin/env python

import argparse
from datetime import datetime

def parse_datetime(date, time):
    s = "{} {}".format(date, time)
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

parser = argparse.ArgumentParser(description='Calculate days since/until a date')
parser.add_argument('date', help='event date in YYYY-MM-DD format')
parser.add_argument('time', default="00:00", nargs='?', help='event time in HH:MM format')

args = parser.parse_args()
event_datetime = parse_datetime(args.date, args.time)

timedelta = abs(event_datetime - datetime.now())

days = timedelta.days
hours = timedelta.seconds // 3600

if days == 0 and hours == 0:
    print("It's now!")
elif days == 0 and hours != 0:
    print("{} hours".format(hours))
elif days != 0 and hours == 0:
    print("{} days".format(days))
else:
    print("{} days, {} hours".format(days, hours))
