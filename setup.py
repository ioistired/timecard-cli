#!/usr/bin/env python3

import re
import setuptools
from pathlib import Path

HERE = Path(__file__).parent

with open(HERE / 'README.md') as f:
	README = f.read()

with open(HERE / 'requirements.txt') as f:
	install_requires = f.readlines()

setuptools.setup(
	name='timecard-cli',
	url='https://github.com/iomintz/pythonpy-clone',
	version='0.0.0',
	packages=['timecard'],
	license='MIT',
	description='Generate SpongeBob-style time cards',
	long_description=README,
	long_description_content_type='text/markdown; variant=GFM',
	install_requires=install_requires,
	python_requires='>=3.6.0',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: End Users/Desktop',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: MIT License',
		'License :: Other/Proprietary License',
	],
	entry_points={
		'console_scripts': ['timecard = timecard:main'],
	},
	package_data={
		'timecard': [
			'res/kp.ttf',
			'res/images/*.png',
		],
	},
)
