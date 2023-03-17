# setup.py placed at root directory
from setuptools import setup
setup(
    name='dwebdriver',
    version='0.1.6',
    author='Eric Di Re',
    description='Custom Selenium Web Driving',
    url='https://github.com/edire/dwebdriver.git',
    python_requires='>=3.9',
    packages=['dwebdriver'],
    install_requires=['selenium', 'chromedriver-autoinstaller', 'numpy']
)