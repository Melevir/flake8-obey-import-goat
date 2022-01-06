from typing import Optional

from setuptools import setup, find_packages


package_name = 'flake8_obey_import_goat'


def get_version() -> Optional[str]:
    with open('flake8_obey_import_goat/__init__.py', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")
    return None


def get_long_description() -> str:
    with open('README.md') as f:
        return f.read()


version = get_version()
assert version is not None

setup(
    name=package_name,
    description=(
        'An extension for flake8 that forbids some imports statements in some modules.'
    ),
    classifiers=[
        'Environment :: Console',
        'Framework :: Flake8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.9',
    include_package_data=True,
    keywords='flake8',
    version=version,
    author='Ilya Lebedev',
    author_email='melevir@gmail.com',
    install_requires=['setuptools'],
    entry_points={
        'flake8.extension': [
            'OIG = flake8_obey_import_goat.checker:ImportsChecker',
        ],
    },
    url='https://github.com/Melevir/flake8-obey-import-goat',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)
