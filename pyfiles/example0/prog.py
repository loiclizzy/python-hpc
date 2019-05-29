# 2 different syntaxes for importing a module
import util
from util import myvar1, print_variables

util.myvar0 = 100
myvar1 += 100
print(f'in prog.py, util.myvar0 = {util.myvar0}; myvar1 = {myvar1}')
print_variables()
