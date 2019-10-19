def count_holes(line):
    """
    Counts holes in a first integer number:
    found in a string (leading zeros excluded)
    1 hole for 0469
    2 holes for 8
    """
    number = ""
    got_number = 0 # indicates if the number has been found
    for ch in line:
        if ch in '1234567890.': # forms our number
            number += ch
            got_number = 1
        if got_number and ch not in '1234567890.':
            break
    if not got_number or '.' in number: # real number case
        return 'ERROR'
    number = str(int(number)) # getting rid of leading zeroes
    # count = 0
    # for ch in number:
    #     if ch in '0469':
    #         number += ch
    #         count += 1
    #     elif ch == '8':
    #         number += ch
    #         count += 2
    count = number.count('0') + number.count('4') + number.count('6') + number.count('9') + number.count('8') * 2
    return count


print(count_holes('123'))
print(count_holes('906'))
print(count_holes('001'))
print(count_holes('-8'))
print(count_holes('-8.0'))
print(count_holes('0.06 is not 006')) # this one reveals a bug: should return 1 instead of ERROR (((
print(count_holes('No numbers'))
print(count_holes('Agent 007 is the best'))

