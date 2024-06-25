from datetime import datetime, timedelta

def days_calc(date1, date2):
    a = datetime.strptime(date1, '%d.%m.%Y')
    b = datetime.strptime(date2, '%d.%m.%Y')
    results = timedelta((b - a).days)
    return str(results.days)

def result_date_calc(date, days1=0, days2=0):
    a = datetime.strptime(date, '%d.%m.%Y')
    result = a + timedelta(days=days1) + timedelta(days=days2)
    return result.strftime('%d.%m.%Y')
