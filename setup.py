from setuptools import find_packages
from setuptools import setup

from owslogger import __version__


setup(
    name='owslogger',
    version=__version__,
    url='https://github.com/theorchard/python-owslogger/',
    author='The Orchard',
    author_email='webdev@theorchard.com',
    description=(
        'Logging library.'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests-futures'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],)
