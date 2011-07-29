from pygments.lexer import RegexLexer
from pygments.token import *

class SPIPLexer(RegexLexer):
	name = 'SPIP'
	aliases = ['spip']
	filenames = ['*.html']
	
	tokens = {
		'root': [
			(r'#[A-Z_]+\*{0,2}', Keyword),
			(r'\|[\w]+',Name.Function)
		]
		
	}