import calendar
from datetime import datetime

def calendar_days(payload: dict):
    '''
    All days, weekend, weekday for each month
    Need algo to check whether the days for that month are alldays, weekend, or weekday
    '''
    numbers: list = payload["numbers"]
    year = int(numbers[0])
    days_in_month = [calendar.monthrange(year, month)[1] for month in range(1, 13)]
    new_month_day = [1 for i in range(12)] # which day corresponds to a new month: 1st day of jan is 1, etc
    for i in range(1, 12):
        new_month_day[i] = new_month_day[i-1] + days_in_month[i-1]
    # Next, how to check all days/weekend/weekday?
    # for each month, can already determine the numbers required for weekend/weekday/alldays
    # Use array (for the months) of arrays (for weekend/weekday/alldays)
    if calendar.isleap(year):
        days_given = [0 for _ in range(366)]
    else:
        days_given = [0 for _ in range(365)]
    for i in numbers[1:]:
        if 0 < int(i) <= len(days_given):
            days_given[i-1] = 1
    output_by_month = []
    for i in range(len(new_month_day)):
        start_day = new_month_day[i] - 1
        if i != 11:
            end_day = new_month_day[i+1] - 1
        else:
            end_day = len(days_given)
        output_by_month.append(get_days(days_given[start_day:end_day], year, i+1))
    part1 = ",".join(output_by_month)
    part1 = part1 + ","

    whitespace_index = part1.find(" ")
    new_year = 2001 + whitespace_index
    days_in_month = [calendar.monthrange(new_year, month)[1] for month in range(1, 13)]
    new_month_day = [1 for i in range(12)] # which day corresponds to a new month: 1st day of jan is 1, etc
    for i in range(1, 12):
        new_month_day[i] = new_month_day[i-1] + days_in_month[i-1]
    # Use output_by_month
    # Go through each section in output_by_month
    # if is alldays, get the days from datetime
    days = []
    for i in range(len(output_by_month)):
        if output_by_month[i] == "alldays":
            days.extend([j for j in range(new_month_day[i], new_month_day[i]+7)])
        elif output_by_month[i] == "weekday":
            days.extend(get_weekday(new_year, i+1, new_month_day[i]))
        elif output_by_month[i] == "weekend":
            days.extend(get_weekend(new_year, i+1, new_month_day[i]))
        else:
            days.extend(get_somedays(new_year, i+1, new_month_day[i], output_by_month[i]))
    part2 = [new_year] + days
    return {"part1": part1, "part2": part2}

    
def get_days(given_days: list, year: int, month: int) -> str:
    # print(given_days)
    # print(year, month, calendar.monthrange(year, month))
    days_of_week = [False for _ in range(7)]
    days = "mtwtfss"
    no_days = calendar.monthrange(year, month)[1]
    day_of_week = datetime(year, month, 1).weekday() + 1
    assert no_days == len(given_days), "number of days should equal given days"
    for i in range(len(given_days)):
        if given_days[i] == 1:
            # print(days_of_week, day_of_week)
            days_of_week[(day_of_week - 1) % 7] = True
        day_of_week += 1
    if all(days_of_week):
        return "alldays"
    elif all(days_of_week[:5]) and not any(days_of_week[5:]):
        return "weekday"
    elif  all(days_of_week[5:]) and not any(days_of_week[:5]):
        return "weekend"
    else:
        toReturn = ""
        for i in range(len(days_of_week)):
            if days_of_week[i] == True:
                toReturn += days[i]
            else:
                toReturn += " "
        # print(toReturn)
        return toReturn

def get_weekday(year: int, month: int, starting_day: int):
    weekdays = []
    for i in range(7):
        if datetime(year, month, i+1).isoweekday() < 6:
            weekdays.append(i+starting_day)
    assert len(weekdays) == 5, "need 5 weekdays"
    return weekdays

def get_weekend(year: int, month: int, starting_day: int):
    weekend = []
    for i in range(7):
        if datetime(year, month, i+1).isoweekday() >= 6:
            weekend.append(i+starting_day)
    assert len(weekend) == 2, "need 2 weekends"
    return weekend

def get_somedays(year: int, month: int, starting_day: int, req_days: str):
    return_days = []
    req_days_ind = [i for i in range(len(req_days)) if req_days[i] != " "]
    for i in range(7):
        if datetime(year, month, i+1).weekday() in req_days_ind:
            return_days.append(i+starting_day)
    assert len(req_days) - req_days.count(' ') == len(return_days), "need same number of days to be returned"
    return return_days