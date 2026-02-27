from datetime import date, timedelta

# start = date(2026, 1, 1)
# end = date(2026, 1, 5)

# current = start
# while current <= end:
#     print(current)
#     current += timedelta(days=1)


def month_starts(year):
    for month in range(1, 13):
        yield date(year, month, 1)


for d in month_starts(2026):
    print(d)

month_starts(2007)
