# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer,bygroups
from pygments.token import *

class SPIPLexer(RegexLexer):
	name = 'SPIP'
	aliases = ['spip']
	filenames = ['*.html']
	
	tokens = {
		'root': [
			(r'(<BOUCLE[\w]+\([\w]+\))([\s]*\{[#\s\w,\|!=?<>:\{\}]+\}[\s]*)*(>)',bygroups(Name.Class,Name.Attribute,Name.Class)),						# ouverture de la boucle
			
			(r'#[A-Z_]+\*{0,2}', Keyword),								# balises
			(r'\|[\w:]+',Name.Function),								# filtres
			(r'<:[\w]+(:[\w]+)?:>',Literal.String.Other,'recur'),		# chaînes de langues simple (sans filtres dedans)
			(r':>',Literal.String.Other),								# fin chaîne de langue
			(r'<:[\w]+(:[\w]+)?',Literal.String.Other),					# début chaine
			(r'\{[#\s\w,!=?<>:]+\}',Name.Attribute,'recur'),			# Critères de boucles et arguments de balises ainsi que de filtres
			(r'<\/{0,2}B(OUCLE)?[\w]+>',Name.Class),					# partie optionelle des boucles et fermeture
			

		],
		
		#'ouverture_boucle':[
		#	(r'<BOUCLE[\w]+\([\w]+\)',Name.Class),						# debut boucle
		#],
		
		'recur':[
			
			(r'#[A-Z_]+\*{0,2}', Keyword),								# balise
			(r'\{[\s\w,!=?]+\}',Name.Attribute,'#push'), 				# critères
			(r'\|[\w:]+',Name.Function),								# filtres
			(r'<:[\w]+(:[\w\{\}=\|]+)?:>',Literal.String.Other,'recur'),#chaînes de langues
			(r':>',Literal.String.Other),								# fin chaîne de langue
			(r'<:[\w]+(:[\w]+)?',Literal.String.Other),					# début chaine

			(r'\}',Name.Attribute),										#fin d'un critères
			(r'\{[\s\w,!=?<>:]+',Name.Attribute),						#debut d'un critères
			

		],
		'chaine':[
			

		]
		
	}