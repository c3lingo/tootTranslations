from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tootTranslations',
    version='0.0.1',
    description='Announce which talk will be translated in which language at Chaos events',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/c3lingo/tootTranslations',
    author="Adrien Beaucreux",
    author_email='informancer@web.de',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['Mastodon.py'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'pytest', 'hamcrest'],
    },

    entry_points={
        'console_scripts': [
            'tootTranslations=toottranslations:main',
        ],
    },

    project_urls={
        'Bug Reports': 'https://github.com/c3lingo/tootTranslations/issues',
        'Source': 'https://github.com/c3lingo/tootTranslations',
    },
)
