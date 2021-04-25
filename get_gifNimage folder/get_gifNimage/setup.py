from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3'
    ]


setup(
    name='get_gifNimage',
    version='0.1.5',
    description='Downloading image from URL, displaying from the drive',
    long_description=open('README.TXT').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url="https://github.com/Drill-N-Bass/get_gifNimage.git",
    author='Pawel Pedryc',
    author_email='pawel.pedryc@gmail.com',
    classifiers=classifiers,
    keywords='get_gifNimage',
    packages=find_packages(include=['get_gifNimage', 'get_gifNimage.init_folder']),
    install_requires=['wget', 'svglib', 'reportlab', 'IPython', 'requests']
)