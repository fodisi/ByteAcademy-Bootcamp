def get_currency_record(amount):
    if amount >= 100:
        return ('$100', divmod(amount, 100))
    if amount >= 50:
        return ('$50', divmod(amount, 50))
    if amount >= 20:
        return ('$20', divmod(amount, 20))
    if amount >= 10:
        return ('$10', divmod(amount, 10))
    if amount >= 5:
        return ('$5', divmod(amount, 5))
    if amount >= 1:
        return ('$1', divmod(amount, 1))
    if amount >= 0.25:
        return ('quarter', divmod(amount, 0.25))
    if amount >= 0.1:
        return ('dime', divmod(amount, 0.1))
    if amount >= 0.05:
        return ('nickel', divmod(amount, 0.05))
    if amount >= 0.01:
        return ('penny', divmod(amount, 0.01))

def get_printable_set(bill_set):
    
    str_result = []
    if '$100' in bill_set:
        str_result.append(str(bill_set['$100']) + ' $100 bill')
    if '$50' in bill_set:
        str_result.append(str(bill_set['$50']) + ' $50 bill')
    if '$20' in bill_set:
        str_result.append(str(bill_set['$20']) + ' $20 bill')
    if '$10' in bill_set:
        str_result.append(str(bill_set['$10']) + ' $10 bill')
    if '$5' in bill_set:
        str_result.append(str(bill_set['$5']) + ' $5 bill')
    if '$1' in bill_set:
        str_result.append(str(bill_set['$1']) + ' $1 bill')
    if 'quarter' in bill_set:
        str_result.append(str(bill_set['quarter']) + ' quarter')
    if 'dime' in bill_set:
        str_result.append(str(bill_set['dime']) + ' dime')
    if 'nickel' in bill_set:
        str_result.append(str(bill_set['nickel']) + ' nickel')
    if 'penny' in bill_set:
        str_result.append(str(bill_set['penny']) + ' penny')

    return ', '.join(str_result)

def currency_converter(amount):
    bill_set = {}
    while (amount > 0):
        #entry == (key, (value, remainder))
        #entry[0] = dictionary key
        #entry[1][0] = dictionary value
        #entry[1][1] = remainder amount
        entry = get_currency_record(amount)
        if (entry[0] in bill_set):
            bill_set[entry[0]] += entry[1][0]
        else: 
            bill_set[entry[0]] = entry[1][0]
        amount = round(entry[1][1], 2)
    #why on linux this always returns different order of values?
    # why float // do not return an integer value when 0.03 // 0.01?
    #return bill_set
    return get_printable_set(bill_set)

print("type a value with 2 decimal places only. use '.' as decimal separator")
value = round(float(input()), 2)
print(currency_converter(value))
