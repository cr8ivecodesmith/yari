#!/usr/bin/env python

from setuptools import find_packages, setup


with open('README.md', encoding='utf8') as fh:
    readme = fh.read()


with open('requirements.txt') as fh:
    requirements = fh.read().splitlines()


with open('requirements-dev.txt') as fh:
    dev_requirements = fh.read().splitlines()


setup(
    name='yari',
    version='0.0.0',
    description='A Kivy-based game engine.',
    long_description=readme,
    long_description_content_tye='text/markdown',
    author='Matt Lebrun',
    author_email='matt@lebrun.org',
    url='https://github.com/cr8ivecodesmith/yari',
    packages=find_packages(exclude=['doc', 'tests', 'examples']),
    include_package_data=True,
    install_requires=requirements,
    tests_require=dev_requirements,
    extras_require={'test': dev_requirements},
    license='MIT license',
    zip_safe=False,
    keywords=['yari', 'kivy', 'game-engine'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
)
