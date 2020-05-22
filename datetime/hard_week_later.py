"""
https://edabit.com/challenge/S4uZaKhcDa7pJ33nu
"""


from datetime import datetime, timedelta


def week_after(date: str) -> str:
    in_week = datetime.strptime(date, '%d/%m/%Y') + timedelta(days=7)
    return in_week.strftime("%d/%m/%Y")


assert week_after("12/03/2020") == "19/03/2020"
assert week_after("21/12/1989") == "28/12/1989"
assert week_after("01/01/2000") == "08/01/2000"
assert week_after("24/09/1924") == "01/10/1924"
assert week_after("21/07/1964") == "28/07/1964"
assert week_after("14/07/2085") == "21/07/2085"
assert week_after("25/04/1953") == "02/05/1953"
assert week_after("02/01/2200") == "09/01/2200"
assert week_after("06/01/2007") == "13/01/2007"

print('Success')