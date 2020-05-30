"""
https://edabit.com/challenge/PMbf4ktWRLTrh4YQA
"""


from datetime import datetime, timedelta


def add_n_days_to_a_date(date: str, n: int) -> str:
    day, month, year = int(date[:2]), int(date[2:4]), int(date[4:])
    end = datetime(year, month, day) + timedelta(days=n)
    return end.strftime('%d%m%Y')


assert add_n_days_to_a_date("26102000", 6038) == "08052017"
assert add_n_days_to_a_date("15041984", 6037) == "25102000"
assert add_n_days_to_a_date("01011900", 1519) =="29021904"
assert add_n_days_to_a_date("03033003", 20) == "23033003"
assert add_n_days_to_a_date("02031872", 12345) == "20121905"

print("Success")