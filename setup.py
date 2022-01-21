import os

from setuptools import find_packages
from setuptools import setup

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, 'src', 'uois', 'version.py')) as fp:
    exec(fp.read())

packages = find_packages('src')

# Ensure that we don't pollute the global namespace.
for p in packages:
    assert p == 'uois' or p.startswith('uois.')

def pkg_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('../..', path, filename))
    return paths

setup(
    name='uois',
    version=__version__,
    author='Chris Xie',
    packages=packages,
    package_dir={'': 'src'},
    python_requires='>=3.6.*, <3.10',
)
