from setuptools import setup, find_packages

setup(
    packages=find_packages(exclude=['doc', 'examples']),
    entry_points={
        'console_scripts':
        ['mypackuga-raccoon = mypackuga.raccoon:main']},
)
