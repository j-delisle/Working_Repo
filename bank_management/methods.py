class BankAcct:

    def __init__(self, fname, lname, address, pin):
        self.balance = 0
        self.fname = fname
        self.lname = lname
        self.address = address
        self.pin = pin

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def deposit(self, amt):
        self.balance += amt
        return self.balance

    def withdraw(self, amt):
        if amt > self.balance:
            raise ValueError('Insufficient Funds')
        else:
            self.balance -= amt
            return self.balance

    def get_balance(self):
        return self.balance

    def display_acct(self):
        return self.fullname(), self.address, self.balance

    def pin_identifier(self, pin):
        return self.fullname(), self.address, self.balance


# bank1 = BankAcct('Jay', 'Delisle', '3 Earl St Lincoln, RI 02865', '2222')
# bank1.deposit(25)
# print(bank1.pin_identifier('2222'))
