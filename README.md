# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.


# datehelper
![Event Logger Workflow](https://github.com/software-students-fall2024/3-python-package-now-youre-unemployed/actions/workflows/event-logger.yml/badge.svg)

**A Python utility package for date manipulation**

---

## Overview

`datehelper` is a Python package to help with simple date manipulation tasks.  The functions included can help calculate date differences, check for weekends, and help find the date of the next requested weekday.  This package can streamline date-related logic in Python projects.

---

## Features

- **days_between(date1, date2)**: Returns the number of days between two dates.
- **add_days(date, days)**: Returns a new date given a date and a number of days.
- **is_weekend(date)**: Checks if a given date is a weekend (Saturday or Sunday).
- **next_weekday(date, weekday)**: Returns the date of the next given weekday.

---

## Installation

1. `pip`:

```bash

pip install datehelper

```

2. Import the functions into your code:

```bash

from datehelper import days_between, add_days, is_weekend, next_weekday

```
---

## Usage Examples

1. **`next_weekday(given_date: date, weekday: int) -> date`**  
   Returns the next occurrence of a specified weekday from a given date. Weekdays are represented by integers where Monday is 0 and Sunday is 6.

2. **`days_between(date1: date, date2: date) -> int`**  
   Calculates the absolute number of days between two dates.

3. **`add_days(start_date: date, days: int) -> date`**  
   Returns a new date that is a specified number of days after the given start date.

4. **`is_weekend(check_date: datetime) -> bool`**  
   Checks if a given date falls on a weekend (Saturday or Sunday).

**For a complete example, see [`example_date.py`](./example_date.py).**

---

## Function Details

### days_between(date1, date2)

### add_days(date, days)

### is_weekend(date)

### next_weekday(date, weekday)

---

## Team Members

- Shray Awasti - [Github Profile](https://github.com/shrayawasti)
- Toshi Troyer - [Github Profile](https://github.com/toshiHTroyer)
- Ethan Cheng - [Github Profile](https://github.com/ethanhcheng)
- Joseph Hwang - [Github Profile](https://github.com/josephnyu)
---
