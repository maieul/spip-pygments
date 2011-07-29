# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer
from pygments.token import *

class SPIPLexer(RegexLexer):
	name = 'SPIP'
	aliases = ['spip']
	filenames = ['*.html']
	
	tokens = {
		'root': [
			(r'#[A-Z_]+\*{0,2}', Keyword),								# balises
			(r'\|[\w:]+',Name.Function),								# filtres
			(r'<:[\w]+(:[\w]+)?:>',Literal.String.Other,'recur'),		# chaînes de langues simple (sans filtres dedans)
			(r':>',Literal.String.Other),								# fin chaîne de langue
			(r'<:[\w]+(:[\w]+)?',Literal.String.Other),					# début chaine
			(r'\{[#\s\w,!=?<>:]+\}',Name.Attribute,'recur'),				# Critères de boucles et arguments de balises ainsi que de filtres
			
			
		],
		
		'recur':[
			(r'#[A-Z_]+\*{0,2}', Keyword),								# balise
			(r'\{[\s\w,!=?]+\}',Name.Attribute,'#push'), 				# critères
			(r'\|[\w:]+',Name.Function),								# filtres
			(r'<:[\w]+(:[\w\{\}=\|]+)?:>',Literal.String.Other,'recur'),#chaînes de langues
			(r':>',Literal.String.Other),								# fin chaîne de langue
			(r'<:[\w]+(:[\w]+)?',Literal.String.Other),					# début chaine

			(r'\}',Name.Attribute),										#fin d'un critères
			(r'\{[\s\w,!=?<>:]+',Name.Attribute),							#debut d'un critères
			

		],
		'chaine':[
			

		]
		
	}