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
			(r'\|[\w:]+',Name.Function),				# filtres
			(r'\{[#\s\w,!=?]+\}',Name.Attribute,'criteres')		# Critères de boucles et arguments de balises ainsi que de filtres
		],
		
		'criteres':[
			(r'#[A-Z_]+\*{0,2}', Keyword),					# balise
			(r'\{[\s\w,!=?]+\}',Name.Attribute,'criteres'), # critères
			(r'\|[\w:]+',Name.Function),				# filtres
			(r'\}',Name.Attribute),							#fin d'un critères
			(r'\{[\s\w,!=?]+',Name.Attribute)				#debut d'un critères
		]
		
	}