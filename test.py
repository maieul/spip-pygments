# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE 
# http://geekographie.maieul.net
# Paternité - Pas d'Utilisation Commerciale - Partage des Conditions Initiales à l'Identique 2.0 France (CC BY-NC-SA 2.0)
# http://creativecommons.org/licenses/by-nc-sa/2.0/fr/


from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from spip import spipLexer


code 	= open('exemple.html','r').read()
output 	= open('output.html','w+')
output.write('<html><head><style>'+HtmlFormatter().get_style_defs('.highlight')+'</style></head><body>')
highlight(code, spipLexer(), HtmlFormatter(),output)

output.write('</body></html>')
output.close()