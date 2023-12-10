from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'mysqlclient',
]

setup(
    name='flask_lab',
    version='0.0',
    description='Lab work number 4',
    author='Volodymyr Hotsiy',
    author_email='volodymyr',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
