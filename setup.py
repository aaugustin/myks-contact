import distutils.core
import os

# Avoid polluting the .tar.gz with ._* files under Mac OS X
os.putenv('COPYFILE_DISABLE', 'true')

description = 'Simple contact form'

with open(os.path.join(os.path.dirname(__file__), 'README')) as f:
    long_description = '\n\n'.join(f.read().split('\n\n')[1:])

distutils.core.setup(
    name='myks-contact',
    version='0.1',
    author='Aymeric Augustin',
    author_email='aymeric.augustin@m4x.org',
    url='https://github.com/aaugustin/myks-contact',
    description=description,
    long_description=long_description,
    download_url='http://pypi.python.org/pypi/myks-contact',
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
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    platforms='all',
    license='BSD'
)
