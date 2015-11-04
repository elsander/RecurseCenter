## A calculator app, written in 1.5 hours for
## technical interview prep

import re
import ipdb
print "Welcome to PyCalc!"
while True:
    var = raw_input("> ")
    if var == 'quit':
        print "Bye!"
        break

    ## only accept alphanumeric input and +-*/
    valid = re.match(r'[a-zA-Z0-9\s\+\*/-]', var)

    if valid is not None:
        var = var.split()
        flag = True
        for i, item in enumerate(var):
            ipdb.set_trace()
            if i % 2 == 0:
                try:
                    var[i] = float(item)
                except ValueError:
                    flag = False
                    break
                if i == 0:
                    tot = item
                else:
                    ## bad practice, avoid using if at all possible
                    tot = eval(str(tot) + var[i-1] + item)
            else:
                if item in ['+', '-', '*', '/']:
                    pass
                else:
                    flag = False
                    break
        if flag:
            print tot
        else:
            print ':('
