from setuptools import setup

requires = [
    'bcrypt',
    'psycopg2',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_tm',
    'sqlalchemy',
    'waitress',
    'zope.sqlalchemy',
]

dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',
]

setup(
    name='kenwinauth',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = auth:main'
        ],
        'console_scripts': [
            'initialize_kenwinauth_db = auth.initialize_db:main'
        ],
    },
)
