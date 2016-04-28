#from distutils.core import setup
from setuptools import setup, find_packages


VERSION = __import__("auth_remote").__version__

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
]

install_requires = [
]

setup(
    name="django-auth-remote",
    description="subclass of django.contrib.auth.backends.RemoteUserBackend"
            "to custom authenticate backend on remote server.",
    version=VERSION,
    author="bGN4",
    author_email="git@github.com",
    license='MIT License',
    platforms=['OS Independent'],
    url="https://github.com/bGN4/django-auth-remote",
    packages=['auth_remote',],
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
