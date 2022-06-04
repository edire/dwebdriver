# setup.py placed at root directory
from setuptools import setup
setup(
    name='my_webdrivers-edire',
    version='0.0.2',
    author='Eric Di Re',
    description='Custom Selenium Web Driving',
    url='https://github.com/edire/my_webdrivers.git',
    python_requires='>=3.6',
    packages=['my_webdrivers'],
    install_requires=['selenium', 'chromedriver-autoinstaller']
)