#! /usr/bin/python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pycapacity',
    version='1.1.0',
    author='Antun Skuric',
    author_email='antun.skuric@inria.fr',
    description='A real-time task space capacity calculation module for robotic manipulators and human musculoskeletal models',
    long_description=long_description, #'A Real-time capable robot capacity calculation module', 
    long_description_content_type="text/markdown",
    url='https://gitlab.inria.fr/auctus-team/people/antunskuric/pycapacity',
    license='MIT',
    package_dir = {'pycapacity': 'pycapacity'}, 
    packages = setuptools.find_packages(),
    py_modules=['pycapacity.robot','pycapacity.human'],
    install_requires=['numpy','scipy','cvxopt']
)