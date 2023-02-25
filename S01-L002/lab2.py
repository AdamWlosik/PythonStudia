days = ["mon", 'tue', 'wed', 'fri', 'sat', 'sun']
workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')
print('days:', days, 'workdays:', workdays)