#!/usr/bin/env python


import os


def all_packages(base):
    for path, dirs, files in os.walk(base):
        if '__init__.py' in files:
            yield path


def all_files(base, sub=''):
    for path, dirs, files in os.walk(os.path.join(base, sub)):
        path = path.lstrip(base + os.sep)
        for file in files:
            yield os.path.join(path, file)


from distutils.core import setup
setup(
    name='fn',
    description='fn is a Django web suite',
    author='Benjamin Feng',
    license='3-clause BSD',
    py_modules=['fn_rest'],
    packages=list(all_packages('fn_blog')),
    package_data={'fn_blog': list(all_files('fn_blog', 'templates'))},
)
