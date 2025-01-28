from setuptools import setup, find_packages

name = 'pre_commit_localization_hooks'
version = '1.0.0'
description = 'pre-commit hooks for localization error messages'

# Package dependencies
dependencies = [
    "Babel==2.12.1",
    "pytest==7.3.1",
    "Faker==18.9.0",
]

# Package setup
setup(
    name=name,
    version=version,
    description=description,
    packages=find_packages(),
    install_requires=dependencies
)
