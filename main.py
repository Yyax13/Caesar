from libs.colors import *
import os

hashtag = fr"{c.cyan('[')}{c.yellow('#')}{c.cyan(']')}"
num1 = fr"{c.cyan('[')}{c.yellow('1')}{c.cyan(']')}"
num2 = fr"{c.cyan('[')}{c.yellow('2')}{c.cyan(']')}"

def screen(): 
  def banner():
    
    
    ban1 = rf""" 
{c.green('  ██████  ██▓███   ▄▄▄       ▄████▄  ▓█████  ██▓    ▄▄▄      ▒██   ██▒▓██   ██▓')}
{c.green('▒██    ▒ ▓██░  ██▒▒████▄    ▒██▀ ▀█  ▓█   ▀ ▓██▒   ▒████▄    ▒▒ █ █ ▒░ ▒██  ██▒')}
{c.blue('░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▒███   ▒██░   ▒██  ▀█▄  ░░  █   ░  ▒██ ██░')}
{c.blue('  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██░   ░██▄▄▄▄██  ░ █ █ ▒   ░ ▐██▓░')}
{c.blue('▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░░▒████▒░██████▒▓█   ▓██▒▒██▒ ▒██▒  ░ ██▒▓░')}
{c.yellow('▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░░ ▒░▓  ░▒▒   ▓▒█░▒▒ ░ ░▓ ░   ██▒▒▒ ')}
{c.yellow('░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░  ░  ▒    ░ ░  ░░ ░ ▒  ░ ▒   ▒▒ ░░░   ░▒ ░ ▓██ ░▒░ ')}
{c.yellow('░  ░  ░  ░░         ░   ▒   ░           ░     ░ ░    ░   ▒    ░    ░   ▒ ▒ ░░  ')}
{c.yellow('      ░                 ░  ░░ ░         ░  ░    ░  ░     ░  ░ ░    ░   ░ ░     ')}
{c.yellow('                            ░                                          ░ ░     ')}
{c.yellow('Lang select / Selecionar idioma')}"""
    
    print(ban1) 
  os.system('cls' if os.name == 'nt' else 'clear') 
  banner() 

screen()
opt = input(rf"""
    {num1} {c.cyan('Portuguese (PT-BR)')}
    {num2} {c.cyan('English (EN-US)')}

    {hashtag} {c.cyan('Choose an option / Selecione uma opção: ')}""")

if opt == "1":
  os.system('python main/main-pt.py')
elif opt == "2":
  os.system('python main/main-en.py')

#HENRY, ME DA 1ST POSITION
