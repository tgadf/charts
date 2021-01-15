from distutils.core import setup
import setuptools

setup(
  name = 'charts',
  py_modules = ['top40Data', 'top40Charts', 'top40', 'billboardData', 'billboardCharts', 'billboardYE', 'billboardYECharts', 'artistIgnores'],
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
  install_requires=['utils==0.0.1', 'music==0.0.1', 'dbmaster==0.0.1', 'multiartist==0.0.1', 'jupyter_contrib_nbextensions'],
  dependency_links=['git+ssh://git@github.com/tgadf/multiartist.git#egg=multiartist-0.0.1',
                    'git+ssh://git@github.com/tgadf/utils.git#egg=utils-0.0.1',
                    'git+ssh://git@github.com/tgadf/music.git#egg=music-0.0.1',
                    'git+ssh://git@github.com/tgadf/dbmaster.git#egg=dbmaster-0.0.1',
                    'git+ssh://git@github.com/tgadf/matchAlbums.git#egg=music-0.0.1',
                    'git+ssh://git@github.com/tgadf/musicnames.git#egg=musicnames-0.0.1']
)
 
