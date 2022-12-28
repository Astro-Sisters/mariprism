from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mariprism',
      version='v1.0.0',
      description='mariprism: the prettiest colors, colormaps and ideas for your plots!',
      long_description=long_description,
      author='P. Cáceres-Burgos, P. Palma-Bifani',
      url='https://github.com/Astro-Sisters/mariprism',
      author_email='paulina.palma-bifani@oca.eu',
      license='',
      packages=['mariprism'],
      install_requires=['numpy'],
      include_package_data = True,
      zip_safe=False,
      python_requires='>=3.9')