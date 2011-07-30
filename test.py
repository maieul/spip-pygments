# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE 
# http://geekographie.maieul.net
# Paternité - Pas d'Utilisation Commerciale - Partage des Conditions Initiales à l'Identique 2.0 France (CC BY-NC-SA 2.0)
# http://creativecommons.org/licenses/by-nc-sa/2.0/fr/


from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from spip import spipLexer
import codecs

code 	= codecs.open('exemple.html','r','utf-8').read()
output 	= codecs.open('output.html','w+','utf-8')
output.write('<html><head>'+'<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'+'<style>'+HtmlFormatter().get_style_defs('.highlight')+'</style></head><body>')
highlight(code, spipLexer(), HtmlFormatter(),output)

output.write('</body></html>')
output.close()