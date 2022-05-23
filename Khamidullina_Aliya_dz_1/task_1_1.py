SECS_IN_MINUTE = 60
HOURS_IN_DAY = 24


def convert_time(duration):
    if duration < 0 or not isinstance(duration, int):
        print("No numbers below zero!")
        print("The function takes only integers!")
    else:
        floor = duration // SECS_IN_MINUTE
        if floor < 1:
            return f"{duration} сек"
        elif 1 <= floor < SECS_IN_MINUTE:
            return f"{floor} мин {duration % SECS_IN_MINUTE} сек"
        elif SECS_IN_MINUTE <= floor < 1440:
            return f"{floor // SECS_IN_MINUTE} час {floor % SECS_IN_MINUTE} мин {duration % SECS_IN_MINUTE} сек"
        elif 1440 <= floor:
            hours = floor // SECS_IN_MINUTE
            return (f"{hours // HOURS_IN_DAY} дн {hours % HOURS_IN_DAY} час {floor % SECS_IN_MINUTE} мин "
                    f"{duration % SECS_IN_MINUTE} сек")


check_time = [0, 23, 59, 60, 61, 153, 3599, 3600, 3601, 45600, 86399, 86400, 86401, 400153]

for n in check_time:
    print(convert_time(n))
