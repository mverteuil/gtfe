#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='gtfe',
    packages=find_packages(),
    version='1.0.6',
    description='Get the number of seconds since the Unix epoch for a given datetime.',
    author='Matthew de Verteuil, Jason Peddle, Liav Koren',
    author_email='onceuponajooks@gmail.com',
    url='https://github.com/mverteuil/gtfe',
    keywords='epoch datetime time timezone',
    license='MIT',
    long_description=open('README.md', 'r').read().strip(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ],
)
