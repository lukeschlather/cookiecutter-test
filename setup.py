import os
from setuptools import setup, find_packages

setup(
    name='{{ package_name }}',
    version={{ starting_version }},
    description='{{ description }}',
    author='{{ author }}',
    maintainer='{{ maintainer }}',
    maintainer_email='{{ maintainer_email }}',
    url='{{ url }}',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
        ],
    },
    install_requires=(
    ),
)
