#!/usr/bin/env python

"""
nyc_school_attendence
=================
Simple tools to work with the nyc school attendence data set 
"""

from setuptools import setup

setup(
    name='nyc_school_attendance',
    version='0.0.0',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description="Tools to manipulate NYC's school attendance data set",
    url="adamdeprince.wordpress.com",
    long_description=__doc__,
    py_modules=[
        'nyc_school_attendance/__init__'
        ],
    packages=['nyc_school_attendance',],
    zip_safe=True,
    license='MIT',
    include_package_data=False,
    classifiers=[],
    scripts=['scripts/nyc_school_attendance_download'],
    install_requires=[
        'zopfli'
        ]
    )
