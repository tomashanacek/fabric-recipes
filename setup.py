import os
from setuptools import setup
from fabric_recipes import __version__

root_dir = os.path.dirname(__file__)

with open(os.path.join(root_dir, "requirements.txt")) as f:
    install_requires = [r.strip() for r in f if "#egg=" not in r]


setup(
    name="fabric-recipes",
    version=__version__,
    description=("Fabric recipes"),
    author="Tomas Hanacek",
    author_email="tomas.hanacek1@gmail.com",
    packages=["fabric_recipes"],
    install_requires=install_requires,
    include_package_data=True
)
