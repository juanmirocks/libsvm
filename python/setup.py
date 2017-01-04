from setuptools import setup
from setuptools import find_packages


def readme():
	with open('README', encoding='utf-8') as file:
		return file.read()


def copyright():
	with open('../COPYRIGHT', encoding='utf-8') as file:
		return file.read()


setup(
	name='LIBSVM',
	version='3.22',
	description='A Library for Support Vector Machines',
	long_description=readme(),
	license=copyright(),
	url='https://github.com/cjlin1/libsvm',
	author='Chih-Chung Chang and Chih-Jen Lin',
	author_email='cjlin@csie.ntu.edu.tw',

	packages=find_packages(exclude=['tests']),

	test_suite='pytest-runner',
	setup_requires=['pytest']
)
