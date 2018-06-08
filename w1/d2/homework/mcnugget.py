
def is_mcnugget_eighties(num):
    minusSix = num - 6
    minusNine = num - 9
    minusTwenty = num - 20

    if minusSix == 0:
        return True #num is 6
    if minusNine == 0:
        return True #num is 9
    if minusTwenty == 0:
        return True #num is 20

    #condition to stop, because the num is less than 6,
    #so cannot be McNugget Number
    if minusSix < 0:
        return False

    return is_mcnugget_eighties(minusSix) or is_mcnugget_eighties(minusNine) or is_mcnugget_eighties(minusTwenty)

def is_mcnugget_today(num):
    minusFour = num - 4
    minusSix = num - 6
    minusTen = num - 9
    
    if minusFour == 0:
        return True #num is 4
    if minusSix == 0:
        return True #num is 6
    if minusTen == 0:
        return True #num is 9

    #condition to stop, because the num is less than 4,
    #so cannot be McNugget Number
    if minusFour < 0:
        return False

    return is_mcnugget_today(minusFour) or is_mcnugget_today(minusSix) or is_mcnugget_today(minusTen)

if __name__ == '__main__':
    print("type a positive number for NOT McNugget number 80s (6, 9, 20):")
    number = int(input())
    not_mcnugget_eighties = []
    for i in range(number):
        if not is_mcnugget_eighties(i):
            not_mcnugget_eighties.append(i)
    print('Not McNugget numbers(80s):\n{0}'.format(not_mcnugget_eighties))

    print("type a positive number for NOT McNugget number TODAY (4, 6, 9, 20):")
    number = int(input())
    not_mcnugget_today = []
    for i in range(number):
        if not is_mcnugget_today(i):
            not_mcnugget_today.append(i)
    print('Not McNugget numbers(today):\n{0}'.format(not_mcnugget_today))
