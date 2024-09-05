# setup.py placed at root directory
from setuptools import setup
setup(
    name='dwebdriver',
    version='1.0.3',
    author='Eric Di Re',
    description='Custom Selenium Web Driving',
    url='https://github.com/edire/dwebdriver.git',
    python_requires='>=3.9',
    packages=['dwebdriver'],
    install_requires=['selenium', 'webdriver-manager>=4.0.2', 'numpy']
)