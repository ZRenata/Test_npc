from datetime import datetime

def data_check(date):
    if date == '':
        date = datetime.now().date()
        date= str(date)
    date = date.replace('-', '_')
    return date