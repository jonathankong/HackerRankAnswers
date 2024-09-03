def TimeConversion(regularTime):
    period = regularTime[-2:]
    hours = int(regularTime[0:2])

    if period == "PM":
        if hours != 12:
            hours += 12
            if (hours >= 24):
                hours -= 24
    else:
        if hours == 12:
            hours = 0
    
    print(f"{format(hours, "02")}{regularTime[2:-2]}")

TimeConversion("07:05:45PM")