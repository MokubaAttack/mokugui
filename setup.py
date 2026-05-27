from setuptools import setup, find_packages

setup(
	name='mokugui',
	version='1.0.0',
	packages=find_packages(),
	include_package_data=True,
	author='mokuba_attack',
	description='This is a script that I use when I create images by diffusers.',
	url='https://github.com/MokubaAttack/mokugui',
	license='BSD-3-Clause',
	classifiers=[
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python :: 3.12',
	],
	install_requires=[
		"diffusers_anima @ git+https://github.com/hdae/diffusers-anima.git",
		"realesrgan"
	],
)
