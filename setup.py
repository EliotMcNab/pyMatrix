import setuptools

with open("DESCRIPTION.txt", "r") as file:
    long_description = file.read()

REQUIREMENTS = [""]

CLASSIFIERS = [
    "Development Status :: Early Acess",
    "Intended Audience :: Developpers, Mathematicians",
    "Topic :: Mathematics",
    "License :: OSI Approved :: MIT License",
]

setuptools.setup(name = "pyMatrix",
      version = "1.0.0",
      description = "a small module which adds a Matrix class to be used as a new data type",
      long_description = long_description,
      url = "https://github.com/EliotMcNab/pyMatrix.git",
      author = "Eliot McNab",
      author_email = "",
      license = "MIT",
      packages = setuptools.find_packages,
      classifiers = CLASSIFIERS,
      requires = REQUIREMENTS,
      python_requires = ">=3",
      keywords = "Matrix, Matrixes, Mathemacis, Maths, Algebra"
)