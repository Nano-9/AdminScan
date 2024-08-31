import os
import sys

system = sys.platform


def BanerAdm():
      """ Baner script """

      if system == "win32":
            os.system("cls")
            print(r"""
             ,\
             \\\,_
              \` ,\
         __,.-" =__)    [+] Coded by Nano
       ."        )      [+] Telegram: t.me/rdzin9
    ,_/   ,    \/\_     [+] Saída dentro da pasta do site
    \_|    )_-\ \_-`
      `-----` `--`""")
      elif system == "linux":
            os.system("clear")
            print(r"""
             ,\
             \\\,_
              \` ,\
         __,.-" =__)    [+] Coded by Nano
       ."        )      [+] Telegram: t.me/rdzin9
    ,_/   ,    \/\_     [+] Saída dentro da pasta do site
    \_|    )_-\ \_-`
      `-----` `--`  """)
