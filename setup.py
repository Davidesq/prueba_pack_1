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
#     packages=setuptools.find_packages(),
    install_requires=['opencv-python', 'argparse', 'playsound', 'prettytable'],
    python_requires='>=3.6',
    package_dir={'test_pkg':'src', 'imagenes':'src', 'functions':'src'},
    scripts=['test_pkg/texto.py', 'test_pkg/imagenes.py', 'test_pkg/audio.py']
)
