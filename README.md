![minha apresentação](https://img.shields.io/static/v1?label=SCANER&message=ADMIN&color=red&style=<STYLE>&logo=<LOGO>)
![minha apresentação](https://img.shields.io/static/v1?label=VARREDURAS-DE&message=DIRETORIOS&color=red&style=<STYLE>&logo=<LOGO>)
![minha apresentação](https://img.shields.io/static/v1?label=VARREDURAS-DE&message=SUBDOMÍNIOS&color=red&style=<STYLE>&logo=<LOGO>)
![minha apresentação](https://img.shields.io/static/v1?label=LISTAGEM-DE&message=SITES&color=red&style=<STYLE>&logo=<LOGO>)
![minha apresentação](https://img.shields.io/static/v1?label=SCANNER&message=SITES&color=red&style=<STYLE>&logo=<LOGO>)
![minha apresentação](https://img.shields.io/static/v1?label=BRUTE-FORCE&message=DIRETÓRIOS&color=red&style=<STYLE>&logo=<LOGO>)
![minha apresentação](https://img.shields.io/static/v1?label=BRUTE-FORCE&message=SUBDOMÍNIOS&color=red&style=<STYLE>&logo=<LOGO>)

![baner](https://github.com/user-attachments/assets/9fdf11f3-4939-4bda-9da9-d5ed77408882)

# Sobre o script:

<h5>
  - Foi desenvolvido para ser um brute-force de diretórios e subdomínios open source no intuito de ajudar desenvolvedores a tornar a página administradora mais segura!<br><br>
  - O uso indevido desse script não é minha responsabilidade!<br><br>
  - O script não encontra somente páginas administrativas, ele também pode encontrar Diretório Listing (index of), por isso recomendo abrir cada url que ele retornar 200!<br><br>
  - O script está atualmente em desenvolvimento por mim, e no final, contará com mais opções de mapeamentos como:<br><br>
  - Blocos de Redes de um site (net block/ans)<br><br>
  - Listagem de todos os CNAMES de todos os Subdomínios<br><br>
  - Analise de vulnerabilidades de Mail Spoofing no servidor e entre outras<br><br>
</h5>

# Modo de uso:
<h5>
  
  - python scan.py --site http://bancocn.com/ --tipo admin (SEM VERBOSE)
  
  - python scan.py --site http://bancocn.com/ --tipo sublinks (SEM VERBOSE)
  
  - python scan.py --site http://bancocn.com/ --tipo admin --v (COM VERBOSE)
  
  - python scan.py --site http://bancocn.com/ --tipo sublinks --v (COM VERBOSE)

  - Adicione a url e no final não esqueça da -> /<br><br>
      
</h5>

# Sobre as wordlists:
<h5>
  - A wordlist admin.txt de listagem de diretórios, atualmente contém 3000 palavras possíveis de diretórios admin<br><br>
  - A wordlist Subdominios.txt contém mais de 1 Milhão de palavras possíveis para nomes de subdomínios de um site!<br><br>
</h5>

# Sobre as atualizações:

<h5>
  - Cada atualização feita, será adicionada aqui abaixo para que fique bem esclarecido o que foi adicionado e também como usar<br><br>
  - Dentro do script no comando --help também terá instruções o que cada comando faz!<br><br>
</h5>
