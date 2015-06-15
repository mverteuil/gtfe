#!/usr/bin/python
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='gtfe',
    packages=find_packages(),
    version='1.2.1',
    description='Get the number of seconds since the Unix epoch for a given datetime.',
    author='Matthew de Verteuil, Jason Peddle, Liav Koren, Ben Webber',
    author_email='onceuponajooks@gmail.com',
    url='https://github.com/mverteuil/gtfe',
    keywords='epoch datetime time timezone',
    license='MIT',
    install_requires=['python-dateutil'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    long_description=open('README.rst', 'r').read().strip(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
