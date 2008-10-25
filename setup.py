#!/usr/bin/env python


from distutils.core import setup
setup(
    name='fn_blog',
    description='fn_blog is a Django app',
    author='Benjamin Feng',
    license='3-clause BSD',
    packages=['fn_blog'],
    package_data={'fn_blog': ['templates/base.html', 'templates/fn_blog/*.html']},
)
