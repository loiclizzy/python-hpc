import sys

from .raccoon import main


def test_f_toto():
    sys.argv = "mypackuga-raccoon -f toto".split()
    main()
