# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE 
# http://geekographie.maieul.net
# Paternité - Pas d'Utilisation Commerciale - Partage des Conditions Initiales à l'Identique 2.0 France (CC BY-NC-SA 2.0)
# http://creativecommons.org/licenses/by-nc-sa/2.0/fr/


from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from spip import SPIPLexer

code 	= open('exemple.html','r').read()
output 	= open('output.html','w+')
highlight(code, SPIPLexer(), HtmlFormatter(),output)

output.close()