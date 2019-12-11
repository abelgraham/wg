from setuptools import setup

setup(
    name='wg',
    description='website generator',
    author='Abel Graham',
    author_email='abel@abelgraham.xyz',
    packages=['wg'],
    install_requires=['datetime', 'mistune', 'jinja2'],
    entry_points={
        'console_scripts': [ 
            'wg = wg.generate:main' 
        ] 
    },
)
