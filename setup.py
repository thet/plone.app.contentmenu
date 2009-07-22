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
      extras_require=dict(
          test=[
            'plone.locking',
            'zope.publisher',
            'zope.testing',
            'Plone',
            'Products.PloneTestCase',
          ]
      ),
      install_requires=[
        'setuptools',
        'plone.memoize',
        'plone.navigation',
        'zope.component',
        'zope.contentprovider',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.site',
        'zope.app.publisher',
        'Products.CMFCore',
        'Products.CMFDynamicViewFTI',
        'Acquisition',
        'Zope2',
      ],
      )
