SPIP Pygments Lexer
===================

This is a [Pygments][1] [lexer][2] for the [SPIP template language][3]. When
it's finished, I'll be submitting it for inclusion within Pygments.

[1]: http://pygments.org/
[2]: http://pygments.org/docs/lexerdevelopment/
[3]: http://www.spip.net/en_article2042.html

Pour installer :
	- necessite pygmentize
	- necessite que pygmentize fonctionne bien avec la version de python correspondant à easy_install
	- il faut faire les lignes suivante :
		python setup.py build
		python setup.py bdist_egg
		cd dist
		easy_install *egg
