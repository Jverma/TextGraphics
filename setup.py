#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import sys

sys.path.insert(0,'TextGraphics')

sys.path.pop(0)

packages = ['TextGraphics',
			'TextGraphics.src',
			'TextGraphics.Data',
			'TextGraphics.Applications',
            'TextGraphics.Analysis',
			'TextGraphics.Stopwords']

setup(
    name='textgraphics',
    version='0.20',
    author='Janu Verma',
    author_email='jv367@cornell.edu',
    description='A Python Package for Graphical Methods in Text Analysis',
    #url='https://github.com/er432/TASSELpy',
    platforms=['Linux','Mac OSX', 'Windows', 'Unix'],
    keywords=['Genomics','Quantitative genetics', 'java'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Retrieval',
        'Topic :: Scientific/Engineering :: Machine Learning',
		'Topic :: Scientific/Engineering :: Natural Language Processing'
    ],
    packages=packages,
    package_data={'TextGraphics':['Data/*.txt']},
    license='MIT'
    )			