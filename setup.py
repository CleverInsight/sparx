import os
from setuptools import setup, find_packages

from sparx import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = [
    "pandas",
    "numpy",
    "scipy",
    "scikit-learn"
]

setup(
    name = "sparx",
    version = "0.0.1",
    description = "Sparx is an advanced and simplified data munging, wrangling and preparation library",
    long_description = read('README.rst'),
    url = 'http://cleverinsight.co',
    license = 'BSD',
    author = 'Bastin Robins J',
    author_email = 'robin@cleverinsight.co',
    packages = find_packages(exclude=['tests']),
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Other/Proprietary License',
        'Operating System :: OS Independent',
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ],
    install_requires = requirements,
    tests_require = [],
)
