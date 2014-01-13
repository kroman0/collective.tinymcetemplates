import os
from setuptools import setup, find_packages

version = '1.0b4qg'
shortdesc = "TinyMCE Plugin for templates and snippets"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()

setup(name='collective.tinymcetemplates',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Environment :: Web Environment',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      author='Rob Gietema',
      author_email='rob@fourdigits.nl',
      url='http://pypi.python.org/pypi/collective.tinymcetemplates',
      license='General Public Licence',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.registry',
          'Products.TinyMCE',
      ],
      extras_require={
          'test': ['collective.testcaselayer', ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
