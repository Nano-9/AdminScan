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
import json
from BanerAdm import BanerAdm
from validator import way

SESSIONS = requests.Session()
ENTER_USER = sys.argv
tecnologia = []
servidor_web = [] 
if len(ENTER_USER) >= 2 and len(ENTER_USER) <= 6:

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
					for head,dados in info.headers.items():
						if head == "X-Powered-By":
							tecnologia.append(dados)
						elif head == "Server":
							servidor_web.append(dados)
					if info.status_code == 200:
						try:
							subdominios_paraostestes1 = []
							subdominios_encontrados1 = []
							subdominios_deletados1 = []
							print("\n\n\033[1m>>>>>\033[m \033[1;32mSOBRE O SITE:\033[m \033[1m<<<<<\033[m\n")
							print("\033[1;32m[\033[m\033[1m*\033[m\033[1;32m]\033[m \033[1;32m[\033[m\033[1mINFO\033[m\033[1;32m]\033[m \033[1mSERVIDOR:\033[m \033[1;34m{}\033[m".format(servidor_web[0]))
							print("\033[1;32m[\033[m\033[1m*\033[m\033[1;32m]\033[m \033[1;32m[\033[m\033[1mINFO\033[m\033[1;32m]\033[m \033[1mTECNOLOGIA:\033[m \033[1;34m{}\033[m".format(tecnologia[0]))
						except:
							print("\n\n\033[1m>>>>>\033[m \033[1;32mSOBRE O SITE:\033[m \033[1m<<<<<\033[m\n")
							print("\033[1;31m[\033[m\033[1m!\033[m\033[1;31m]\033[m \033[1m Nenhuma informação como servidor e tecnologia disponível!\033[m")

					with open("admin.txt","rt") as count1:
						for diretorio in count1:
							subdominios_paraostestes1.append(diretorio.replace("\n",""))
					count1.close()
					print("\n\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m\033[1m\033[m \033[1mVarredura iniciada no alvo:\033[m \033[1;4;3;31m{}\033[m".format(sys.argv[2]))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mIniciado em:\033[m \033[1;35m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mTipo de busca:\033[m \033[1;33m{}\033[m".format(sys.argv[4].replace("admin","Página de Admin")))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mTamanho da Wordlist:\033[m \033[1;32m{}\033[m\n".format(len(subdominios_paraostestes1)))

					try:
						print("\n\033[1;36m>>>>>\033[m \033[1mBUSCANDO PÁGINAS E DIRETÓRIOS\033[m \033[1;36m<<<<<\033[m\n\n")
						with open("admin.txt","rt") as admin_search:
							for num,adm in enumerate(admin_search):
								try:
									teste = sys.argv[2]+adm.replace("\n","")
									conectar_site = requests.get(teste,timeout=5,verify=True,headers=way.headers)
								except KeyboardInterrupt:
									print("\n[*] Saindo...")
									raise SystemExit
								except requests.exceptions.ConnectionError:
									subdominios_deletados1.append(teste)
									continue
								except requests.exceptions.SSLError:
									subdominios_deletados1.append(teste)
									continue
								except requests.exceptions.InvalidURL:
									subdominios_deletados1.append(teste)
									continue
								except requests.exceptions.TooManyRedirects:
									continue
								else:
									if conectar_site.status_code == 200:
										subdominios_encontrados1.append(teste)
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
									else:
										subdominios_deletados1.append(teste)
										if "--v" in sys.argv[5]:
											print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;31m{}\033[m\033[1m]\033[m \033[1;31mTested:\033[m \033[3;2m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site.status_code,teste))
						admin_search.close()
						print("\n\033[1m >>>>>>\033[m \033[1;32mDETALHES DOS TESTES\033[m \033[1m<<<<<<\033[m\n")
						print("\033[1mSubdomínios testados:\033[m \033[1m[\033[m \033[1;33m{}\033[m \033[1m]\033[m | \033[1m Subdomínios encontrados:\033[m \033[1m[\033[m \033[1;32m{}\033[m \033[1m]\033[m | \033[1m Subdomínios descartados:\033[m \033[1m[\033[m \033[1;31m{}\033[m \033[1m]\033[m\n\n".format(len(subdominios_paraostestes1),len(subdominios_encontrados1),len(subdominios_deletados1)))
					except:
						pass

				elif tipo_busca == "sublinks":
					subdominios_paraostestes = []
					subdominios_encontrados = []
					subdominios_deletados = []
					diretorio_save2 = sys.argv[2].split("/")
					info2 = SESSIONS.get(sys.argv[2],timeout=5,verify=True,headers=way.headers)
					for head,dados in info2.headers.items():
						if head == "X-Powered-By":
							tecnologia.append(dados)
						elif head == "Server":
							servidor_web.append(dados)
					try:
						with open("Subdominios.txt","rt") as count:
							for subs in count:
								subdominios_paraostestes.append(subs.replace("\n",""))
						count.close()
					except FileNotFoundError:
						BanerAdm()
						print("\033[1m[\033[m\033[1;31m!\033[m\033[1m]\033[m Wordlist não encontrada!")
						raise SystemExit
					BanerAdm()
					if info2.status_code == 200:
						try:
							print("\n\n\033[1m>>>>>\033[m \033[1;32mSOBRE O SITE:\033[m \033[1m<<<<<\033[m\n")
							print("\033[1;32m[\033[m\033[1m*\033[m\033[1;32m]\033[m \033[1;32m[\033[m\033[1mINFO\033[m\033[1;32m]\033[m \033[1mSERVIDOR:\033[m \033[1;34m{}\033[m".format(servidor_web[0]))
							print("\033[1;32m[\033[m\033[1m*\033[m\033[1;32m]\033[m \033[1;32m[\033[m\033[1mINFO\033[m\033[1;32m]\033[m \033[1mTECNOLOGIA:\033[m \033[1;34m{}\033[m".format(tecnologia[0]))
						except:
							print("\n\n\033[1m>>>>>\033[m \033[1;32mSOBRE O SITE:\033[m \033[1m<<<<<\033[m\n")
							print("\033[1;31m[\033[m\033[1m!\033[m\033[1;31m]\033[m \033[1m Nenhuma informação como servidor e tecnologia disponível!\033[m")
					print("\n\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m\033[1m\033[m \033[1mVarredura iniciada no alvo:\033[m \033[1;4;3;31m{}\033[m".format(sys.argv[2]))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mIniciado em: {}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S")))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mTipo de busca:\033[m \033[1;33m{}\033[m".format(sys.argv[4].replace("sublinks","subdomínios")))
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mEssa parte pode\033[m \033[1m(\033[m\033[1;31mdemorar\033[m\033[1m)\033[m\033[1m:\033[m")
					print("\033[1;36m[\033[m\033[1m+\033[m\033[1;36m]\033[m \033[1mTamanho da Wordlist:\033[m \033[1;32m{}\033[m".format(len(subdominios_paraostestes)))
					try:
						print("\n\033[1;36m>>>>>\033[m \033[1mBUSCANDO SUBDOMÍNIOS\033[m \033[1;36m<<<<<\033[m\n\n")
						url1 = sys.argv[2].split("/")
						with open("Subdominios.txt","rt") as admin_search2:
							for num2,adm2 in enumerate(admin_search2):
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
									subdominios_deletados.append(url3)
									continue
								except requests.exceptions.SSLError:
									subdominios_deletados.append(url3)
									continue
								except requests.exceptions.InvalidURL:
									subdominios_deletados.append(url3)
									continue
								except requests.exceptions.TooManyRedirects:
									continue
								else:
									if conectar_site2.status_code == 200:
										print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;32m{}\033[m\033[1m]\033[m \033[1;36mSubdomínio:\033[m \033[1m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site2.status_code,url3))
										subdominios_encontrados.append(url3)
									else:
										subdominios_deletados.append(url3)
										if "--v" in sys.argv[5]:
											print("\033[m\033[1m[\033[m\033[1;36m{}\033[m\033[1m]\033[m \033[1m[\033[m\033[1;31m{}\033[m\033[1m]\033[m \033[1;31mTested:\033[m \033[3;2m{}\033[m".format(datetime.datetime.now().strftime("%H:%M:%S"),conectar_site2.status_code,url3))
						admin_search2.close()
						print("\n\033[1m >>>>>>\033[m \033[1;32mDETALHES DOS TESTES\033[m \033[1m<<<<<<\033[m\n")
						print("\033[1mSubdomínios testados:\033[m \033[1m[\033[m \033[1;33m{}\033[m \033[1m]\033[m | \033[1m Subdomínios encontrados:\033[m \033[1m[\033[m \033[1;32m{}\033[m \033[1m]\033[m | \033[1m Subdomínios descartados:\033[m \033[1m[\033[m \033[1;31m{}\033[m \033[1m]\033[m\n\n".format(len(subdominios_paraostestes),len(subdominios_encontrados),len(subdominios_deletados)))
					except FileNotFoundError:
						BanerAdm()
						print("\033[1m[\033[m\033[1;31m!\033[m\033[1m]\033[m Wordlist não encontrada!")
						raise SystemExit
					except KeyboardInterrupt:
						print("[+] Saindo...")
						raise SystemExit
		else:
			BanerAdm()
			print("Verifique a url digitada, protocolo (http ou https) e no final da url adicione uma /")
	elif "--help" in ENTER_USER[1]:
		BanerAdm()
		print("\033[1;36m\n\n#############\033[m \033[1mBEM VINDO AO MENU DE HELP\033[m \033[1;36m#############\033[m")

		print("\033[1;32m\n\n------------ TIPOS DE URL SUPORTADAS ------------\033[m\n\n")
		print("suportada as urls HTTP:// E HTTPS://")
		print("Não se esqueça de colocar a url com o protocolo\n\n")

		print("\033[1;33m\n------------ LINHAS DE COMANDOS ------------\033[m\n\n")
		print("{} --site http://bancocn.com/ --tipo admin".format(sys.argv[0]))
		print("{} --site http://bancocn.com/ --tipo sublinks\n".format(sys.argv[0]))

		print("\033[1;32m\n\n------------ TIPOS DE COMANDOS DISPONÍVEIS ------------\033[m\n\n")
		print("\n{} --help  :  Usado para chamar o painel de ajuda!".format(sys.argv[0]))
		print("{} --site  :  Usado para especificar um site alvo!".format(sys.argv[0]))
		print("{} --tipo  :  Usado para especificar o tipo de wordlist a ser usada!".format(sys.argv[0]))
		print("{} --v     :  Usado para mostrar as saídas das url's que deram erro! \n".format(sys.argv[0]))


		print("\033[1;32m\n\n------------ TIPOS DE WORDLISTS DISPONÍVEIS ------------\033[m\n\n")
		print("Wordlist 1 -> Usada para achar paineis de Admin")
		print("Wordlist 2 -> Usada para achar subdomínios do site alvo\n")

		print("\033[1;32m\n\n------------ USANDO AS WORDLISTS DISPONÍVEIS ------------\033[m\n\n")
		print("{} --site SITE AQUI --tipo admin        :  Usado para especificar que será usada a wordlist de diretório Admin!".format(sys.argv[0]))
		print("{} --site SITE AQUI --tipo sublinks     :  Usado para especificar que será usada a wordlist de sublinks para encontrar outros domínios!".format(sys.argv[0]))
		print("{} --site SITE AQUI --tipo admin --v    :  Usado para especificar que será usada a wordlist de diretório Admin! (com verbose)".format(sys.argv[0]))
		print("{} --site SITE AQUI --tipo sublinks --v :  Usado para especificar que será usada a wordlist de sublinks para encontrar outros domínios! (com verbose)\n".format(sys.argv[0]))


		print("\033[1;32m\n\n------------ ARMAZENAMENTO DAS SÁIDAS DO SCRIPT ------------\033[m\n\n")
		print("Todas as saídas da URL de admin, serão armazenadas dentro das pastas com o nome do site que foi feito o scan!")
		print("Sempre que o script encontrar uma página, ele cria uma pasta com o nome do site e armazena a saída dentro do arquivo Found.txt!\n\n")
else:
	BanerAdm()
	print("\n\033[1m[\033[m\033[1;31m!\033[m\033[1m]\033[m \033[1m Digite: {} --help para saber como funciona!\n".format(sys.argv[0]))
