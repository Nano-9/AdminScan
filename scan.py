#!/usr/bin/python

# Versão 2 do meu script Admin-Finder
# Versão melhorada
# Coded by Nano
# Telegram: t.me/rdzin9

import os
import sys
import requests
import time
import datetime
from BanerAdm import BanerAdm
from validator import way

SESSIONS = requests.Session()
ENTER_USER = sys.argv

if len(ENTER_USER) >= 2 and len(ENTER_USER) <= 5:

	if "--site" in ENTER_USER:
		validar_entrada = way.ValidEnter(msg=sys.argv[2])
		if validar_entrada:
			site_alvo = sys.argv[2]
			if "--tipo" in ENTER_USER:
				tipo_busca = sys.argv[4].lower()
				if tipo_busca == "admin":
					diretorio_save = sys.argv[2].split("/")
					BanerAdm()
					info = SESSIONS.get(sys.argv[2],timeout=5,verify=True,headers=way.headers)
					if info.status_code == 200:
						try:
							tecnologia = info.headers["X-Powered-By"]
							servidor_web = info.headers["server"]
							print("\n\n\033[1m>>>>>\033[m \033[1;32mSOBRE O SITE:\033[m \033[1m<<<<<\033[m\n")
							print("\033[1;32m[\033[m\033[1m*\033[m\033[1;32m]\033[m \033[1;32m[\033[m\033[1mINFO\033[m\033[1;32m]\033[m \033[1mSERVIDOR:\033[m \033[1;34m{}\033[m".format(servidor_web))
							print("\033[1;32m[\033[m\033[1m*\033[m\033[1;32m]\033[m \033[1;32m[\033[m\033[1mINFO\033[m\033[1;32m]\033[m \033[1mTECNOLOGIA:\033[m \033[1;34m{}\033[m".format(tecnologia))
						except:
							print("\n\n\033[1m>>>>>\033[m \033[1;32mSOBRE O SITE:\033[m \033[1m<<<<<\033[m\n")
							print("\033[1;31m[\033[m\033[1m!\033[m\033[1;31m]\033[m \033[1m Nenhuma informação como servidor e tecnologia disponível!\033[m")

					wordlist_size = open("admin.txt","rt")
					print("\n\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m\033[1m\033[m \033[1mVarredura iniciada no alvo:\033[m \033[1;4;3;31m{}\033[m".format(sys.argv[2]))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mIniciado em: {}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mTipo de busca:\033[m \033[1;33m{}\033[m".format(sys.argv[4]))
					if sys.platform == "linux":
						print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mTamanho da Wordlist:\033[m \033[1;32m{}\033[m\n".format(len(wordlist_size.readlines())))
					else:
						print()


					try:
						with open("admin.txt","rt") as admin_search:
							for num,adm in enumerate(admin_search):
								try:
									teste = sys.argv[2]+adm.replace("\n","")
									conectar_site = requests.get(teste,timeout=5,verify=True,headers=way.headers)
								except KeyboardInterrupt:
									print("\n[*] Saindo...")
									raise SystemExit
								except requests.exceptions.ConnectionError:
									continue
								except requests.exceptions.SSLError:
									continue
								except requests.exceptions.InvalidURL:
									continue
								else:
									if conectar_site.status_code == 200:
										if teste.endswith(".php"):
											print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;32m{}\033[m\033[1m]\033[m \033[1;36mArquivo php:\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site.status_code,teste))
										elif teste.endswith(".txt"):
											print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;32m{}\033[m\033[1m]\033[m \033[1;36mArquivo Robots:\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site.status_code,teste))
										else:
											print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;32m{}\033[m\033[1m]\033[m \033[1;36mDiretório:\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site.status_code,teste))
										if sys.platform == "win32":
											os.makedirs(diretorio_save[2],exist_ok=True)
											with open(str(os.getcwd())+str(r"\\"+diretorio_save[2])+r"\\Found.txt","a") as save1:
												save1.write("--------------------------------------\n")
												save1.write("Site: {}\n".format(sys.argv[2]))
												save1.write("Admin Page: {}\n".format(teste))
												save1.write("--------------------------------------\n\n")
												save1.close()
										if sys.platform == "linux":
											os.makedirs(diretorio_save[2],exist_ok=True)
											with open(str(os.getcwd())+str("/"+diretorio_save[2])+"/Found.txt","a") as save2:
												save2.write("--------------------------------------\n")
												save2.write("Site: {}\n".format(sys.argv[2]))
												save2.write("Admin Page: {}\n".format(teste))
												save2.write("--------------------------------------\n\n")
												save2.close()
									elif conectar_site.status_code == 404:
										print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;31m{}\033[m\033[1m]\033[m \033[1;31mTesting:\033[m \033[3;2m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site.status_code,teste))
									elif conectar_site.status_code == 403:
										print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;33m{}\033[m\033[1m]\033[m \033[1;33mTesting:\033[m \033[3;2m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site.status_code,teste))
					except:
						pass

				elif tipo_busca == "sublinks":
					BanerAdm()
					diretorio_save2 = sys.argv[2].split("/")
					info2 = SESSIONS.get(sys.argv[2],timeout=5,verify=True,headers=way.headers)
					if info2.status_code == 200:
						try:
							tecnologias = info2.headers["X-Powered-By"]
							servidor_webs = info2.headers["server"]
							print("\n\n\033[1m>>>>>\033[m \033[1;32mSOBRE O SITE:\033[m \033[1m<<<<<\033[m\n")
							print("\033[1;32m[\033[m\033[1m*\033[m\033[1;32m]\033[m \033[1;32m[\033[m\033[1mINFO\033[m\033[1;32m]\033[m \033[1mSERVIDOR:\033[m \033[1;34m{}\033[m".format(servidor_webs))
							print("\033[1;32m[\033[m\033[1m*\033[m\033[1;32m]\033[m \033[1;32m[\033[m\033[1mINFO\033[m\033[1;32m]\033[m \033[1mTECNOLOGIA:\033[m \033[1;34m{}\033[m".format(tecnologias))
						except:
							print("\n\n\033[1m>>>>>\033[m \033[1;32mSOBRE O SITE:\033[m \033[1m<<<<<\033[m\n")
							print("\033[1;31m[\033[m\033[1m!\033[m\033[1;31m]\033[m \033[1m Nenhuma informação como servidor e tecnologia disponível!\033[m")
					wordlist_size2 = open("Subdominios.txt","rt")
					print("\n\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m\033[1m\033[m \033[1mVarredura iniciada no alvo:\033[m \033[1;4;3;31m{}\033[m".format(sys.argv[2]))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mIniciado em: {}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mTipo de busca:\033[m \033[1;33m{}\033[m".format(sys.argv[4]))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mEssa parte pode\033[m \033[1;31m(demorar):\033[m")
					if sys.platform == "linux":
						print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mTamanho da Wordlist:\033[m \033[1;32m{}\033[m\n".format(len(wordlist_size2.readlines())))
					else:
						print()

					try:
						url1 = sys.argv[2].split("/")
						with open("Subdominios.txt","rt") as admin_search:
							for num2,adm2 in enumerate(admin_search):
								try:
									try:
										url2 = url1[2].replace("www.","")
									except:
										pass
									url3 = url1[0]+"//"+adm2.replace("\n","")+"."+url2
									conectar_site2 = requests.get(url3,timeout=5,verify=True,headers=way.headers)
								except KeyboardInterrupt:
									print("\n[*] Saindo...")
									raise SystemExit
								except requests.exceptions.ConnectionError:
									continue
								except requests.exceptions.SSLError:
									continue
								except requests.exceptions.InvalidURL:
									continue
								else:
									if conectar_site2.status_code == 200:
										print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;32m{}\033[m\033[1m]\033[m \033[1;36mSubdomínio:\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site2.status_code,url3))
									elif conectar_site2.status_code == 401:
										print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;31m{}\033[m\033[1m]\033[m \033[1;31mTesting:\033[m \033[3;2m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site2.status_code,url3))
									elif conectar_site2.status_code == 403:
										print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;31m{}\033[m\033[1m]\033[m \033[1;31mTesting:\033[m \033[3;2m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site2.status_code,url3))
									elif conectar_site2.status_code == 404:
										print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;31m{}\033[m\033[1m]\033[m \033[1;31mTesting:\033[m \033[3;2m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site2.status_code,url3))


					except:
						pass

	elif "--help" in ENTER_USER:
		BanerAdm()
		print("\n\n############# BEM VINDO AO MENU DE HELP #############")

		print("\n\n------------ TIPOS DE URL SUPORTADAS ------------\n")
		print("suportada as urls HTTP:// E HTTPS://")
		print("Não se esqueça de colocar a url com o protocolo junto como abaixo")
		print("{} --site http://bancocn.com/ --tipo admin\n".format(sys.argv[0]))

		print("\n------------ TIPOS DE COMANDOS DISPONÍVEIS ------------\n")
		print("\n{} --help  :  Usado para chamar o painel de ajuda!".format(sys.argv[0]))
		print("{} --site  :  Usado para especificar um site alvo!".format(sys.argv[0]))
		print("{} --tipo  :  Usado para especificar o tipo de wordlist a ser usada!\n".format(sys.argv[0]))

		print("\n------------ TIPOS DE WORDLISTS DISPONÍVEIS ------------\n")
		print("Wordlist 1 -> Usada para achar paineis de Admin")
		print("Wordlist 2 -> Usada para achar subdomínios do site alvo\n")

		print("\n------------ USANDO AS WORDLISTS DISPONÍVEIS ------------\n")
		print("{} --site SITE AQUI --tipo admin :  Usado para especificar que será usada a wordlist de diretório Admin!".format(sys.argv[0]))
		print("{} --site SITE AQUI --tipo sublinks :  Usado para especificar que será usada a wordlist de sublinks para encontrar outros domínios!\n".format(sys.argv[0]))

		print("\n------------ ARMAZENAMENTO DAS SÁIDAS DO SCRIPT ------------\n")
		print("Todas as saídas da URL de admin, serão armazenadas dentro das pastas com o nome do site que foi feito o scan!")
		print("Sempre que o script encontrar uma página, ele cria uma pasta com o nome do site e armazena a saída dentro do arquivo Found.txt!\n\n")
else:
	BanerAdm()
	print("\n\033[1m[\033[m\033[1;31m!\033[m\033[1m]\033[m \033[1m Digite: {} --help para saber como funciona!\n".format(sys.argv[0]))
