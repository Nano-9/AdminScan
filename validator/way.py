# arquivo para armazenar as funções de validação de caminho e também de url!
# para quando o usuário quiser usar uma wordlist dele mesmo

import re

def ValidWay(way=False):
	way_valid = re.search(r"^((C:\\|/)?)([a-zA-Z0-9])+(\\|/){1}[a-zA-Z0-9]+(\\|/){1}([a-zA-Z0-9])+(\\|/){1}([a-zA-Z0-9])+(\\|/){1}([a-zA-Z0-9])+\.(txt)$", way,flags=re.IGNORECASE)
	if way_valid != None:
		return True
	else:
		return False

def ValidEnter(msg=False):
	validar = re.search(r"^(http://|https://){1}.+(\/)$",msg,flags=re.IGNORECASE)
	if validar != None:
		return True
	else:
		return False

headers = {

			'user-agent': 'Googlebot'
			                      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
			                      'Chrome/55.0.2883.87 Safari/537.36'
			                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
			                      'AppleWebKit/537.36 (KHTML, like Gecko) '
			                      'Chrome/51.0.2704.103 Safari/537.36'
			                      'Mozilla/5.0 (Windows NT 6.1) '
			                      'AppleWebKit/537.36 (KHTML, like Gecko) '
			                      'Chrome/55.0.2883.87 Safari/537.36'
			                      'Mozilla/5.0 (Windows NT 6.1; rv:45.0)'
			                      'Gecko/20100101 Firefox/45.0'
