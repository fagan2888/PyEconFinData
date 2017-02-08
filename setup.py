from setuptools import setup, find_packages

setup_requires = [
    ]

install_requires = [
    ]

dependency_links = [
    ]

setup(
    name='PyEconFinData',
    version='0.1',
    description='Economic and Financial data ',
    author='Syono',
    author_email='syonoki@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    scripts=['manage.py'],
    entry_points={

        },
    )