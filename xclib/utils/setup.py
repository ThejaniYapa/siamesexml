from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension("_sparse", ["_sparse.pyx"],
              include_dirs=[numpy.get_include()])
]

setup(
    name='_sparse',
    ext_modules=cythonize(extensions),
    zip_safe=False,  # Required when using Cython extensions
)
