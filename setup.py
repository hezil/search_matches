from setuptools import setup

setup(
    name='search_matches',
    version='0.1',
    py_modules=['search_matches'],
    include_package_data=True,
    install_requires=[
        'click',
        #'os',
        #'re',
        #'shlex',
        #'subprocess',
        'pathlib',

    ],
    entry_points='''
        [console_scripts]
        search_matches=search_matches:cli
    ''',
)
