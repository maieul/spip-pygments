# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE 
# http://geekographie.maieul.net
# Paternité  - Partage des Conditions Initiales à l'Identique 2.0 France (CC BY-SA 2.0)
# http://creativecommons.org/licenses/by-sa/2.0/fr/


from setuptools import setup, find_packages
setup(name='spip',
	version = '0.1.1',
      packages=find_packages(),
      include_package_data = True,
      entry_points="""
      [pygments.lexers]
      spip = spip:spipLexer
      """
      )
