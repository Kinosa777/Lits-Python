text = 'ff()(e)(d()(sd()323))'

def balance_brckts(brack_txt):
'''
    Checks if the balance and the order of brackets ()
    in a string is correct
    
    Returns: "Error" or "OK"
'''
    bal_br_res = "OK"
    n = bal = 0
    while bal >= 0 and n < len(brack_txt):
        if brack_txt[n] == '(':
            bal += 1
        elif brack_txt[n] == ')':
            bal -= 1
        n += 1
    if bal:
        bal_br_res = "Error"
    print(bal)
    return(bal_br_res)

result = balance_brckts(text)
print(result)
