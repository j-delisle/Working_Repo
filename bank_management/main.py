from methods import BankAcct
from functions import assignPin, formatAddress, formatDisplayAcct
import csv

# Init bank data dict
bank = {}
# bank_data = {
#     '2222': BankAcct('Jay', 'Delisle', '3 Earl St Lincoln, RI 02865', '2222')
# }

# pull data into bank dict - CSV format below:
# 0 = ID
# 1 = First Name
# 2 = Last Name
# 3 = Street Address
# 4 = City
# 5 = State
# 6 = Zip Code
# 7 = Pin #

with open('raw_data.csv', 'r') as mock_data:
    csv_data = csv.reader(mock_data)

    next(csv_data)

    for line in csv_data:
        # print(line)
        key = line[7]
        info = [line[1], line[2], line[3], line[4], line[5], line[6]]
        bank.update({key: info})

usedPins = set(bank.keys())

for key, value in bank.items():
    address = [value[2], value[3], value[4], value[5]]
    user_acct = BankAcct(value[0], value[1], formatAddress(address), key)
    print(formatDisplayAcct(user_acct.display_acct()))


customer_input = input(
    'If you are an existing account holder please enter your pin. To creat an account type 0: \n')
if customer_input == '0':
    fname = input('Please enter your first name: ')
    lname = input('Please enter your last name: ')
    pin = assignPin(usedPins)
    if pin == -1:
        pin = assignPin(usedPins)
    else:
        aList = [None] * 4
        aList[0] = input(
            'Please enter your street address (name and number): ')
        aList[1] = input('Please enter your city: ')
        aList[2] = input('Please enter your state: ')
        aList[3] = input('Please enter your zipcode: ')
        address = formatAddress(aList)

    acct_user = BankAcct(fname, lname, address, pin)
    print(acct_user.display_acct())

else:
    pin = customer_input
    if pin in usedPins:
        acct_user = bank[pin]
        acct_user.deposit(1200)
        print(acct_user.display_acct())
    else:
        print('Pin not found - please create an account')
