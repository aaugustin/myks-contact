import os.path

import setuptools

description = "Simple contact form"

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = '\n\n'.join(readme.read().split('\n\n')[1:])

setuptools.setup(
    name='myks-contact',
    version='1.1',
    description=description,
    long_description=long_description,
    url='https://github.com/aaugustin/myks-contact',
    author='Aymeric Augustin',
    author_email='aymeric.augustin@m4x.org',
    license='BSD',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    packages=[
        'contact',
    ],
    package_data={
        'contact': [
            'locale/*/LC_MESSAGES/*',
            'templates/contact/*.html',
            'static/*/*',
        ],
    },
)
