"""
Setup script for Fill_DocAgil_App.

This script uses setuptools to package the Fill_DocAgil_App project. It reads the long description
from the README.md file and the list of dependencies from the requirements.txt file. The script
also defines entry points for console scripts to run the project.

Attributes:
    long_description (str): The long description read from README.md.
    install_requires (list): The list of dependencies read from requirements.txt.
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='Fill_DocAgil_App',
    version='0.2.5',
    url='https://github.com/Tihamer-k/Fill_DocAgil_App',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Tihamer Aldana',
    install_requires=install_requires,
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'launch_it = main:run_project',
            'lanzalo = main:run_project',
        ],
    },
)
