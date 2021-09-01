from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3'
    ]


setup(
    name='get_gifNimage',
    version='0.4.1',
    description='Downloading image from URL, displaying from the drive',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Drill-N-Bass/get_gifNimage.git",
    author='Pawel Pedryc',
    author_email='pawel.pedryc@gmail.com',
    classifiers=classifiers,
    keywords='get_gifNimage',
    py_modules=['get_gifNimage'], # this code will find get_gifNimage.py file in current folder
    install_requires=['wget', 'svglib', 'reportlab', 'IPython', 'requests'] # all necessary libraries
)