from setuptools import setup, find_packages

setup(name='ide_notebook_db',
      version='1.0.0',
      url="https://github.com/fabiano-teichmann/ide_notebook_db",
      license="MIT",
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.8",
      ],
      author='Fabiano Teichmann',
      author_email='fabiano.geek@gmail.com',
      description='Convert imports to magic run databrics, and convert magic run databricks to import',
      packages=find_packages(exclude='example_notebooks'),
      long_description=open('README.md').read(),
      install_requires=['GitPython', 'click'])
