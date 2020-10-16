from setuptools import setup

setup(
    name='test_pkg',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:Davidesq/prueba_pack_1.git',
    author='david',
    author_email='devdavesq@gmail.com',
    license='unlicense',
    packages=['test_pkg'],
    install_requires=['opencv-python', 'argparse'],
    zip_safe=False
)