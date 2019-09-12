import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="simplecommit",
	version="0.0.1",
	author="lightning",
	author_email="cx24321@hotmail.com",
	description="a simple git commit message generator",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/lightningchen34/simplecommit",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	]
)