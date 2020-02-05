from setuptools import setup
from setuptools import find_packages

with open("DESCRIPTION.txt", "r") as file:
    long_description = file.read()

REQUIREMENTS = []

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(name = "matrixHandler",
      version = "1.0.0",
      description = "a small module which adds a Matrix class to be used as a new data type",
      long_description = long_description,
      url = "https://github.com/EliotMcNab/pyMatrix.git",
      author = "Eliot McNab",
      author_email = "",
      license = "MIT",
      packages = [],
      classifiers = CLASSIFIERS,
      requires = REQUIREMENTS,
      python_requires = ">=3",
      keywords = "Matrix, Matrixes, Mathemacis, Maths, Algebra",
)