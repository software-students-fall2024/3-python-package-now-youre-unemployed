from datetime import date, datetime
from datehelper import next_weekday, days_between, add_days, is_weekend

# Example for next_weekday
print("Next Thursday after November 4, 2024:", next_weekday(date(2024, 11, 4), 3))

# Example for days_between
print("Days between January 1, 2023 and January 10, 2023:", days_between(date(2023, 1, 1), date(2023, 1, 10)))

# Example for add_days
print("10 days after January 1, 2023:", add_days(date(2023, 1, 1), 10))

# Example for is_weekend
print("Is November 3, 2024 a weekend?", is_weekend(datetime(2024, 11, 3)))