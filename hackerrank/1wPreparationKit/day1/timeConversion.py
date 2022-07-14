def timeConversion(s):
    time = s[-2:]
    hour = int(s[:2])
    if time == 'AM':
        if hour >= 12:
            hour -= 12
    elif time == 'PM':
        if hour < 12:
            hour += 12
    if len(str(hour)) == 1:
        hour = '0' + str(hour)
    return str(hour) + s[2:-2]


