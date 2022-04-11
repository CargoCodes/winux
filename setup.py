from setuptools import setup

setup(
    name='winux',
    author='Cargo',
    version='1.0.0',
    packages=['winux'],
    install_requires=['click'],
    entry_points={'console_scripts' : ['clear=winux:clear', 'ls=winux:ls',
        'mv=winux:mv', 'cp=winux:cp', 'rm=winux:rm', 'cat=winux:cat', 'pwd=winux:pwd',
        'date=winux:date', 'nano=winux:nano', 'mem=winux:mem', 'du=winux:du', 'kill=winux:kill',
        ]}
)
