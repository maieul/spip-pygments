# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer,bygroups
from pygments.token import *

class SPIPLexer(RegexLexer):
	name = 'SPIP'
	aliases = ['spip']
	filenames = ['*.html']
	
	tokens = {
		'root': [
			(r'<BOUCLE[\w]+',Name.Class,'debut_boucle'),								# ouverture de la boucle
			
			(r'#[A-Z_]+\*{0,2}', Keyword),								# balises
			(r'\|[\w:]+',Name.Function),								# filtres
			(r'<:[\w]+(:[\w]+)?:>',Literal.String.Other),				# chaînes de langues simple (sans filtres dedans)
			(r':>',Literal.String.Other),								# fin chaîne de langue
			(r'<:[\w]+(:[\w]+)?',Literal.String.Other),					# début chaine
			(r'<\/{0,2}B(OUCLE)?[\w]+>',Name.Class),					# partie optionelle des boucles et fermeture
			(r'\{',Name.Attribute,'critere'),							#debut d'un critère
			(r'\}',Name.Attribute),										#fin d'un critère
			

		],
		
		'debut_boucle':[
			('>',Name.Class,'#pop'),									# debut boucle
			('\([\w]+\)',Name.Variable.Instance),						# type de boucle
			(r'\{',Name.Attribute,'critere'),							#debut d'un critère
		],
		
		'critere':[
			
			(r'#[A-Z_]+\*{0,2}', Keyword),								# balise
			(r'\|[\w:]+',Name.Function),								# filtres
			(r':>',Literal.String.Other),								# fin chaîne de langue
			(r'<:[\w]+(:[\w]+)?',Literal.String.Other),					# début chaine

			(r'\}',Name.Attribute,'#pop'),								#fin d'un critère
			(r'[\w=,]+',Name.Attribute),								# contenu simple d'un critères
			(r'\{',Name.Attribute,'critere'),						#debut d'un critères
			

		],
		'chaine':[
			

		]
		
	}