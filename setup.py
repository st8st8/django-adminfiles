from setuptools import setup
import subprocess
import os.path

long_description = (open('README.rst').read() +
                    open('CHANGES.rst').read() +
                    open('TODO.rst').read())

setup(
    name='django-adminfiles',
    version='1.1.0',
    description='File upload manager and picker for Django admin',
    author='Carl Meyer',
    author_email='carl@oddbird.net',
    long_description=long_description,
    url='http://bitbucket.org/carljm/django-adminfiles/',
    packages=['adminfiles', 'adminfiles.templatetags', 'adminfiles.migrations', \
              'adminfiles.management', 'adminfiles.management.commands'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    test_suite='tests.runtests.runtests',
    package_data={'adminfiles': ['static/adminfiles/*.*',
                                 'static/adminfiles/mimetypes/*.png',
                                 'templates/adminfiles/render/*.html',
                                 'templates/adminfiles/render/image/*.html',
                                 'templates/adminfiles/uploader/*.html',
                                 'locale/*/LC_MESSAGES/*']}
)
