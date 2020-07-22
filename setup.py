from distutils.core import setup
import setuptools

setup(
  name = 'charts',
  py_modules = ['top40charts', 'fullCharts'],
  version = '0.0.1',
  description = 'A Python Wrapper To Parse Music Chart Data',
  long_description = open('README.md').read(),
  author = 'Thomas Gadfort',
  author_email = 'tgadfort@gmail.com',
  license = "MIT",
  url = 'https://github.com/tgadf/charts',
  keywords = ['music charts', 'billboard'],
  classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  install_requires=['utils==0.0.1', 'discogs==0.0.1', 'multiartist==0.0.1', 'jupyter_contrib_nbextensions'],
  dependency_links=['git+ssh://git@github.com/tgadf/multiartist.git#egg=multiartist-0.0.1',
                    'git+ssh://git@github.com/tgadf/utils.git#egg=utils-0.0.1',
                    'git+ssh://git@github.com/tgadf/discogs.git#egg=discogs-0.0.1']
)
 
