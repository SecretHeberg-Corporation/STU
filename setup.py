from gettext import install
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Package for utilitis of SecretHeberg'
LONG_DESCRIPTION = 'A package .'

# Setting up
setup(
    name="shtools",
    version=VERSION,
    author="Rosca (Noamane AIT ABDELLAH OUALI)",
    author_email="<noamane.fr@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'sh', 'tools', 'web', 'nodejs', 'info'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)