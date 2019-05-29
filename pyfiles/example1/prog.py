# 2 different syntaxes for importing a module
import util
from util import myvar1, print_variables

util.myvar0 = 100
myvar1 += 100
print(f'in prog.py, util.myvar0 = {util.myvar0}; myvar1 = {myvar1}')
print_variables()

print('in prog.py, __name__ =', __name__)
# __name__ is a special variable always defined.
# its value depends on how the file is called (directly executed or imported)
if __name__ == '__main__':
    print('end of prog.py')
