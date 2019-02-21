# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


LICENSE = 'LICENSE'
README = 'README.md'
INSTALL_REQUIREMENTS = 'requirements/install.txt'
TEST_REQUIREMENTS = 'requirements/test.txt'
DOCUMENTATION_REQUIREMENTS = 'requirements/documentation.txt'


def get_requirements(*files):
    requirements = list()
    for file in files:
        dependencies = read_file(file, split_lines=True)
        for dependency in dependencies:
            requirements.append(dependency)
    return requirements


def read_file(file, split_lines=False):
    with open(file, 'r') as f:
        return f.read().splitlines() if split_lines else f.read()


setup(
    name='q2-api-client',
    version='0.1.0',
    description='Q2 Rest API Client',
    long_description=read_file(README),
    author='Christopher Aranda',
    author_email='christopher.aranda@q2ebanking.com',
    url='https://bitbucket.q2dc.local/projects/IMPS/repos/q2-api-client/browse',
    license=read_file(LICENSE),
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires=">=3.7",
    install_requires=get_requirements(INSTALL_REQUIREMENTS),
    tests_require=get_requirements(TEST_REQUIREMENTS)
)
