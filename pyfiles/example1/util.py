print('begin of util.py')
myvar0 = 0
myvar1 = 1

def print_variables():
    print(f'in function print_variables: myvar0 = {myvar0}; myvar1 = {myvar1}')

print('in util.py, __name__ =', __name__)
# __name__ is a special variable always defined.
# its value depends on how the file is called (directly executed or imported)
if __name__ == '__main__':
    # this code is executed only in the file is directly executed
    print('the module util.py has been directly executed')
    print_variables()
    print('end of util.py')
else:
    print('the module util.py has been imported')
