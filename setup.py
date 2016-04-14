import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-exception-blame',
    version='0.1',
    packages=['exceptionblame'],
    description='Show blame in a exception.',
    long_description=README,
    url='https://github.com/gdelfresno/django-exception-blame/',
    license='MIT',
    author='gdelfresno',
    author_email='gdelfrenso@gmail.com',
    install_requires=[
        'Django>=1.6',
        'GitPython'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Version Control'
    ],
)
