# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE 
# http://geekographie.maieul.net
# Paternité  - Partage des Conditions Initiales à l'Identique 2.0 France (CC BY-SA 2.0)
# http://creativecommons.org/licenses/by-sa/2.0/fr/
from pygments.lexer import RegexLexer,bygroups
from pygments.token import *
import re
class spipLexer(RegexLexer):
	name = 'spip'
	aliases = ['SPIP','spip']
	filenames = ['*.html']
	flags=re.U
	
	tokens = {
		'root': [
			(r'<BOUCLE[\w]+',Name.Class,'debut_boucle'),								# ouverture de la boucle
			
			(r'#', Keyword,'balise'),								# balises
			(r'\|[\w:]+',Name.Function),								# filtres
			(r'<:[\w]+(:[\w]+)?:>',Literal.String.Other),				# chaînes de langues simple (sans filtres dedans)
			(r':>',Literal.String.Other),								# fin chaîne de langue
			(r'<:[\w]+(:[\w]+)?',Literal.String.Other),					# début chaine
			(r'<\/{0,2}B(OUCLE)?[\w]+>',Name.Class),					# partie optionelle des boucles et fermeture
			(r'\{',Name.Attribute,'critere'),							#debut d'un critère
			(r'\}',Name.Attribute),										#fin d'un critère
			(r'.',Text)													#tout ce qui se situe en dehors de boucle, filtre, critère etc.

		],
		'balise':[
			(r'(\A:){0}[A-Z_]\*{0,2}',Keyword),							#balise de la boucle courante
			(r'[\w]+:',Keyword.Type),									#indication de la boucle concernée
			(r'\{',Name.Attribute,'critere'),							#debut d'un parametre
			(r'\|[\w:]+',Name.Function),								# filtres
			(r'.',Text,'#pop'),										#fin de la balise
			(r'\|[\w:]+',Name.Function),								# filtres	
		],
		
		'debut_boucle':[
			('\/|>',Name.Class,'#pop'),									# debut boucle
			('\([\w]+[\s]*\??\)',Name.Variable.Instance),						# type de boucle
			(r'\{',Name.Attribute,'critere'),							#debut d'un critère
			(r'\s',Name.Class)
		],
		
		'critere':[
			
			(r'#[A-Z_]+\*{0,2}', Keyword),								# balise
			(r'\|[\w:]+',Name.Function),								# filtres
			(r':>',Literal.String.Other),								# fin chaîne de langue
			(r'<:[\w]+(:[\w]+)?',Literal.String.Other),					# début chaine

			(r'\}',Name.Attribute,'#pop'),								#fin d'un critère
			(r'[\w=,!\?\'\"\s\[\(\)\]\.\?\!\¡\¿\&\~]+',Name.Attribute),								# contenu simple d'un critères
			(r'\{',Name.Attribute,'critere'),						#debut d'un critères
			

		]
		
	}