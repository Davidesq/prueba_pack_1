from setuptools import setup

setup(
    name='test_pkg',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:Davidesq/prueba_pack_1.git',
    author='david',
    author_email='devdavesq@gmail.com',
    license='unlicense',
    # packages=['test_pkg'],
    packages=['test_pkg'],
    install_requires=['opencv-python', 'argparse', 'playsound', 'prettytable'],
    python_requires='>=3.6',
    package_dir={'test_pkg':'test_pkg'},
    scripts=['bin/bin_texto.py', 'bin/bin_imagenes.py', 'bin/bin_audio.py']
)