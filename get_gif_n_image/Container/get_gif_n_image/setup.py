import setuptools
with open("README.md", "r") as fh:
    longdescription « fh.read()
setuptools.setup(
	name=“get_gif_n_image", 
	version=“0.0.1”, 
	author=”Paul Pedryc", 
	author_email='pawelpedryc@gmail.com', 
	description="A small graphics library", 
	long_description=long_description, 
	long_description_content_type=“text/raarkdown 
	url="https://github.com/Drill-N-Bass/get_gif_n_image.git",
	packages=setuptools.find packages(),             ##############Tu skończyłeś
	classifiers=[
		"Progranming Language :: Python :: 3”,
		“License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires = '>=3.6'