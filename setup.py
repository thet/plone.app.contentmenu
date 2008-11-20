from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='plone.app.contentmenu',
      version=version,
      description="Plone's content menu implementation",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[],
      keywords='plone contentmenu menu',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.app.contentmenu',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages = ['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'plone.locking',
        'plone.memoize',
        'plone.app.content',
      ],
      )
