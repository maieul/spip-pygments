# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer
from pygments.token import *

class SPIPLexer(RegexLexer):
	name = 'SPIP'
	aliases = ['spip']
	filenames = ['*.html']
	
	tokens = {
		'root': [
			(r'#[A-Z_]+\*{0,2}', Keyword),			# balises
			(r'\|[\w]+',Name.Function),				# filtres
			(r'\{[\s\w,!=?]+\}',Name.Attribute)		# Critères de boucles et arguments de balises ainsi que de filtres
		]
		
	}