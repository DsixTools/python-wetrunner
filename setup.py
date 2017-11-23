from setuptools import setup, find_packages

setup(name='wetrunner',
      version='0.1',
      author='Jason Aebischer, Xuanyou Pan, David M. Straub',
      author_email='jason.aebischer@tum.de, xuanyou.pan@tum.de, david.straub@tum.de',
      url='https://github.com/DsixTools/python-wetrunner',
      description='A Python package for the renormalization group evolution in the Weak Effective Theory (WET).',
      license='MIT',
      packages=find_packages(),
      package_data={
      'smeftrunner':['tests/data/*',
              ]
      },
      install_requires=['numpy'],
    )