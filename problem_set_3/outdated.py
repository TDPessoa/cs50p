"""In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as
middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year
comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any
program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636,
but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted
in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits,
and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year
order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the
list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the
user again. Assume that every month has no more than 31 days; no need to validate whether
a month has 28, 29, 30, or 31 days."""


def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    while True:
        date = str(input("Date:")).strip()
        try:
            if '/' in date:
                date = date.split('/')
                if int(date[0]) < 12 and int(date[1]) < 31:
                    break

            else:
                date = date.split(',')
                date = [(date[0].split())[0], (date[0].split())[1], date[1]]
                if date[0].title() in months and date[1] not in months and int(date[1]) < 31:
                    break

        except BaseException:
            pass

    if date[0].title() in months:
        for m in range(len(months)):
            if date[0].title() == months[m]:
                date[0] = str(m + 1)
                break
    date = [date[2], date[0], date[1]]
    date_final = ''
    for c in date:
        if int(c) < 10 and '0' not in c:
            date_final += '-0'
        elif c != date[0]:
            date_final += '-'
        date_final += c
    print(date_final)


main()
