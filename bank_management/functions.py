from random import randint


def assignPin(usedPins):
    p = randint(999, 9999)
    if p in usedPins:
        return -1
    else:
        return p


def formatAddress(aList):
    return '{} {}, {} {}'.format(aList[0], aList[1], aList[2], aList[3])


def formatDisplayAcct(acct):
    return f'Name: {acct[0]} \nAddress: {acct[1]} \nAccount Balance: {acct[2]}'
