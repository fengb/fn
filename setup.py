#!/usr/bin/env python


from setuptools import setup, find_packages
setup(
    name='fn',
    description='fn is a Django web suite',
    author='Benjamin Feng',
    license='3-clause BSD',
    packages=find_packages(),
    include_package_data=True,
#    zip_safe=False,

    entry_points={
        'setuptools.file_finders': [
            'hg = setuptools_hg:hg_file_finder',
        ],
    },
)
