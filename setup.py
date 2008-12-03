#!/usr/bin/env python


from distutils.core import setup
setup(
    name='fn',
    description='fn is a Django web suite',
    author='Benjamin Feng',
    license='3-clause BSD',
    py_modules=['fn_rest'],
    packages=['fn_blog'],
    package_data={'fn_blog': ['templates/base.html', 'templates/fn_blog/*.html']},
)
