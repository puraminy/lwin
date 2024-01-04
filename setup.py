from setuptools import setup, find_packages

setup(
    name='lwin',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'curses==2.2.0'
        'pyperclip'
        'textwrap'
    ],
)

