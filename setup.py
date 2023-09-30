import os

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Fill_DocAgil_App',
    version='0.2.0',
    url='https://github.com/Tihamer-k/Fill_DocAgil_App',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='Tihamer Aldana',
    install_requires=['openpyxl', 'pandas', 'colorama'],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'launch_it = Fill_DocAgil_App.main:main',
            'lanzalo = Fill_DocAgil_App.main:main',
        ],
    },
)
