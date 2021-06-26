from setuptools import setup, find_packages
install_requires = ['numpy','flake8']
setup_requires = ['pytest-runner']
tests_require = ['pytest','pytest-runner']

# setup symlinks src. so you can import src from any directory.
# all packages in install_requires is installed when "python setup.py develop".
# packages in extras_require are only run in certain scenarios. in this case when "python setup.py test" is run.
setup(name='src', setup_requires = setup_requires, install_requires = install_requires, tests_require = tests_require,
      packages = find_packages(exclude='test*'), extras_require={'test': tests_require})
