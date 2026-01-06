"""
Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
"""


def clock_angle(time_str: str) -> int:
    h, m = map(int, time_str.split(":"))
    h %= 12

    hour_angle = 30 * h + 0.5 * m
    minute_angle = 6 * m

    angle = abs(hour_angle - minute_angle)
    angle = min(angle, 360 - angle)

    return round(angle)

def overlapping_times():
    times = []

    for h in range(12):
        total_minutes = (60 * h) / 11

        hour = 12 if h == 0 else h
        minutes = int(total_minutes)
        seconds = round((total_minutes - minutes) * 60)

        # normalize overflow
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hour = 1 if hour == 12 else hour + 1

        times.append(f"{hour:02d}:{minutes:02d}:{seconds:02d}")

    return times


print(clock_angle("03:15")) 
print(overlapping_times())
