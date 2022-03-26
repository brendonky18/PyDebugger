from setuptools import setup

setup(
    name='PyDebugger', # What the package is listed as
    version='0.0.1',
    description='Simple python program to make printing, logging and debugging easier.',
    url='git@github.com:brendonky18/PyDebugger.git',
    author='Brendon Ky',
    author_email='brendonky18@gmail.com',
    license='unlicense',
    packages=['debugger'], # How the package is imported
    zip_safe=False
)
