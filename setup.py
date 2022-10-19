from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='ForMoSA',
      version='v6.0.0',
      description='ForMoSA: Forward Modeling Tool for Spectral Analysis',
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