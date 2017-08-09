from setuptools import setup

setup(
    name='shapelets-lts',
    version='0.1.0',
    install_requires=[
        'numpy',
        'scipy',
        'sklearn',
        'matplotlib',
    ],
    packages=['shapelets'],
    package_dir={'': 'lib/python3.6/site-packages/shaplets-python'}
)
