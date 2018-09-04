import datetime

global store_name
store_name = "X-Mart"
global phone_number
phone_number = "630-867-5309"
global city
city = "Istanbul"
global address
address = "619 N. Clark Rd."
global can_resell
can_resell = False


def date_time(exp=None):
    if exp is None:
        dt = datetime.datetime.now()
    else:
        dt = datetime.datetime.now() + datetime.timedelta(days=90)
    month = str(dt.month)
    day = str(dt.day)
    year = str(dt.year)
    hour = str(dt.hour)
    minute = str(dt.minute)
    if len(str(dt.minute)) == 1:
        minute = '0' + minute
    return month + '/' + day + '/' + year + ' ' + hour + ':' + minute
