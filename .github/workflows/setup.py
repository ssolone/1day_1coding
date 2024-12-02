from setuptools import setup, find_pakages

setup(
  name='package',
  version='0.0.1',
  description='python helper fuction',
  author='sora',
  author_email='lightnimpg@gmail.com',
  packages=find_packages(),
  install_requires=['pandas'],
)
