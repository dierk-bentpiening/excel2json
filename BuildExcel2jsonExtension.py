from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Exel2Json',
    ext_modules=cythonize("src/excel2json.pyx"),
    zip_safe=False,
)
