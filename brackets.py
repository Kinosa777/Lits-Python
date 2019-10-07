from colorama import init
init()
from colorama import Back
text = 'ff())(e))(d()(sd()3))23)'
n = bal = 0
while bal >= 0 and n < len(text):
    if text[n] == '(':
        bal += 1
    elif text[n] == ')':
        bal -= 1
    n += 1
if bal == 0:
    print('OK')
elif bal < 0:
    print('Error: ' + text[0:n - 1] + Back.RED + text[n - 1] + Back.RESET + text[n:len(text)])
else:
    print('Error: Missing closing bracket')
