#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Setup dot py."""
from __future__ import absolute_import, print_function

# import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read description files."""
    path = join(dirname(__file__), *names)
    with open(path, encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


# previous approach used to ignored badges in PyPI long description
# long_description = '{}\n{}'.format(
#     re.compile(
#         '^.. start-badges.*^.. end-badges',
#         re.M | re.S,
#         ).sub(
#             '',
#             read('README.rst'),
#             ),
#     re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read(join('docs', 'CHANGELOG.rst')))
#     )

long_description = '{}\n{}'.format(
    read('README.rst'),
    read('CHANGELOG.rst'),
    )

setup(
    name='my_first_telegram_chatbot',
    version='0.0.1',
    description='My very first chatbot.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='No License',
    author='Jose Antonio Quevedo',
    author_email='joseantonio.quevedo@gmail.com',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        # 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        #'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: No License',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        #'Operating System :: POSIX',
        #'Operating System :: MacOS',
        #'Operating System :: Microsoft',
        'Operating System :: OS Independant',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
    project_urls={
        'webpage': 'https://github.com/jaqmcgi/my_first_telegram_chatbot ',
        'Documentation': 'https://my_first_telegram_chatbot .readthedocs.io/en/latest/',
        'Changelog': 'https://github.com/jaqmcgi/my_first_telegram_chatbot/blob/master/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/jaqmcgi/my_first_telegram_chatbot/issues',
        'Discussion Forum': 'https://github.com/jaqmcgi/my_first_telegram_chatbot/discussions',
        },
    keywords=[
        'ci', 'continuous-integration', 'telegram', 'chatbot',
        'sample-project',
        # eg: 'keyword1', 'keyword2', 'keyword3',
        ],
    python_requires='>=3.8, <4',
    install_requires=[
        # https://stackoverflow.com/questions/14399534
        'matplotlib>=3',
        ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
        },
    setup_requires=[
        #   'pytest-runner',
        #   'setuptools_scm>=3.3.1',
        ],
    entry_points={
        'console_scripts': [
            'samplecli1= my_first_telegram_chatbot.cli_int1:main',
            ]
        #
        },
    # cmdclass={'build_ext': optional_build_ext},
    # ext_modules=[
    #    Extension(
    #        splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
    #        sources=[path],
    #        include_dirs=[dirname(path)]
    #    )
    #    for root, _, _ in os.walk('src')
    #    for path in glob(join(root, '*.c'))
    # ],
    )