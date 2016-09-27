"""
daho
-------------

dahi

Links
`````

* `development version <http://github.com/muatik/dahi/>`

"""
import sys
from setuptools import setup

install_requires = [
]

setup(
    name='bot-dahi',
    version='0.1.12',
    url='https://github.com/muatik/dahi',
    license=open('LICENSE').read(),
    author='Mustafa Atik',
    author_email='muatik@gmail.com',
    description='question answer bot',
    keywords=[
        'bot', 'question answering'
    ],
    long_description=open('README.md').read(),
    packages=['dahi'],
    package_data={
        'dahi': [
            'matchers/*',
            ]
        },
    test_suite="tests.suite",
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
