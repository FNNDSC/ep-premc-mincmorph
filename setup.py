from setuptools import setup

setup(
    name             = 'premc-mincmorph',
    version          = '0.1.1',
    description      = 'Smoothen a mask in preparation for marching cubes.',
    author           = 'Jennings Zhang',
    author_email     = 'Jennings.Zhang@childrens.harvard.edu',
    url              = 'https://github.com/FNNDSC/ep-premc-mincmorph',
    py_modules       = ['premc_mincmorph'],
    install_requires = ['chris_plugin', 'pycivet', 'loguru'],
    license          = 'MIT',
    python_requires  = '>=3.10.2',
    entry_points     = {
        'console_scripts': [
            'premc_mincmorph = premc_mincmorph:main'
            ]
        },
    classifiers      = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ]
)
