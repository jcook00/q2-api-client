# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Q2 Rest API Client',
    version='0.1.0',
    description='Q2 Rest API Client',
    long_description=readme,
    author='Christopher Aranda',
    author_email='christopher.aranda@q2ebanking.com',
    url='https://bitbucket.q2dc.local/projects/IMPS/repos/q2-api-client/browse',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
