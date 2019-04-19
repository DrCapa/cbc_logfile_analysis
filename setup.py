from setuptools import setup, find_packages

setup(
    name='cbc_logfile_analysis',
    version='1.0',
    url='https://github.com/DrCapa/cbc_logfile_analysis',
    author='Rico Hoffmann',
    author_email='rico.hoffmann@libero.it',
    description='README',
    packages=find_packages(),
    install_requires=['pandas >= 0.23.4',
                      'matplotlib >= 3.0.2',
                      'xlsxwriter >= 1.0.7']
)
