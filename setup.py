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
    packages=['shapelets',
              'shapelets.classification',
              'shapelets.network',
              'shapelets.test',
              'shapelets.util'
             ]
    
)
