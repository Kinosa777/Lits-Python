def convert_n_to_m(x, n, m):
    """Converts a number in n-based system into a number in m-based system."""

    def convert_n_to_dec(x):
        """Converts a n-based number into decimal.
        No int(num, base) function for number conversion is used."""
        if n == 10:
            return x
        elif n == 1:
            return len(x)
        else:
            dec = 0
            for i in range(0, len(x)):
                dec += (chars.index(x[i]) * (n ** (len(x) - i - 1)))
            return dec

    def convert_dec_to_m(dec, result=''):
        """Converts a decimal number into a m-based number.
        Recursion is used."""
        dec = int(dec)
        if m == 10:
            return str(dec)
        elif m == 1:
            return '0'*dec
        else:
            if dec < m:
                return str(dec) + result
            else:
                result = str(chars[dec % m]) + result
                return convert_dec_to_m(dec // m, result)

    x = str(x)
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ch in x:
        if ch not in chars[:n]:
            return False
    return convert_dec_to_m(convert_n_to_dec(x))


print(convert_n_to_m([123], 4, 3))
print(convert_n_to_m("0123", 5, 6))
print(convert_n_to_m("123", 3, 5))
print(convert_n_to_m(123, 4, 1))
print(convert_n_to_m(-1230, 11, 16))
print(convert_n_to_m("A1Z", 36, 16))
