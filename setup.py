from setuptools import setup, find_packages

version = '0.0.1'

setup(name="helga-shaun",
      version=version,
      description=('SHAAAAAAAAAAAUUUUN'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot shaun',
      author='Shaun Duncan',
      author_email='shaun.duncan@gmail.com',
      url='https://github.com/shaunduncan/helga-shaun',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga-shaun'],
      zip_safe=True,
      entry_points = dict(
          helga_plugins = [
              'shaun= helga_shaun:shaun',
          ],
      ),
)
