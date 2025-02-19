from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="luxury_project",
    version="1.0.0",
    author="Team2",
    author_email="gianluca.filesi@edhec.com",
    description="Luxury-project for Boucheron",
    packages=find_packages(),  # NEW: find packages automatically
    install_requires=requirements,
)