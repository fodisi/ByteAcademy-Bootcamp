import datetime

def age_to_time(age):
    today = datetime.date.today()
    birthday_date = datetime.date(today.year - age, today.month, today.day)
    delta = today - birthday_date
    days = delta.days
    months = days // 30
    hours = days * 24
    minutes = hours * 60
    print('months : ' + str(months) + ', days : ' + str(days) + ', hours : ' + str(hours) + ' and minutes : ' + str(minutes))

def birthday_to_time(birthday):
    format_str = '%Y-%m-%d' # The format
    birthday_date = datetime.datetime.strptime(birthday, format_str).date()
    delta = datetime.date.today() - birthday_date
    days = delta.days
    months = days // 30
    hours = days * 24
    minutes = hours * 60
    print('months : ' + str(months) + ', days : ' + str(days) + ', hours : ' + str(hours) + ' and minutes : ' + str(minutes))


age_to_time(33)
birthday_to_time("1985-05-06")