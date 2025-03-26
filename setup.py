from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='Fill_DocAgil_App',
    version='0.2.2',
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
