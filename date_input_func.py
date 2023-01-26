from data_func import data_check

def date_input():
    date = input()
    date_checked = data_check(date)
    return date_checked