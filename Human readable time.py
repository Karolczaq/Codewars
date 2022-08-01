###https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    minutes = 0
    hours = 0
    while seconds > 59:
        seconds -= 60
        minutes += 1
        while seconds > 3599:
            seconds -= 3600
            hours += 1
    if minutes == 60:
        minutes -= 60
        hours += 1
    if hours < 10 and minutes < 10 and seconds < 10:
        return("0{}:0{}:0{}".format(hours,minutes,seconds))
    if hours < 10 and minutes < 10:
        return("0{}:0{}:{}".format(hours,minutes,seconds))
    if hours < 10 and seconds < 10:
        return("0{}:{}:0{}".format(hours,minutes,seconds))
    if minutes < 10 and seconds < 10:
        return("{}:0{}:0{}".format(hours,minutes,seconds))
    if hours < 10:
        return("0{}:{}:{}".format(hours,minutes,seconds))
    if minutes < 10:
        return("{}:0{}:{}".format(hours,minutes,seconds))
    if seconds < 10:
        return("{}:{}:0{}".format(hours,minutes,seconds))
    else:
        return("{}:{}:{}".format(hours,minutes,seconds))