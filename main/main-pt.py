#importando libs (passa no meu github, https://github.com/Yyax13)
#mereco nota extra so pelo brute force caesar

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
{c.yellow('Versão em Português')}"""
    
    print(ban1) 
  os.system('cls' if os.name == 'nt' else 'clear') 
  banner() 



def crypt(text, shift): 
    encrypted_text = "" 
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text #retorna o texto

def decrypt(encrypted_text, shift):
    return crypt(encrypted_text, -shift)

def decrypt_all_possible(text, max_shift=25):
    results = []
    
    for shift in range(max_shift + 1):
        decrypted_text = decrypt(text, shift)
        results.append(decrypted_text)
    
    return results

def format_output(decrypted_list):
    output = ""
    for decrypted in decrypted_list:
        output += f"# {c.green(decrypted)} | "
    return output

def main():
    screen()
    opt = input(rf"""
    {num1} {c.cyan('Criptografar em Caesar')}
    {num2} {c.cyan('Descriptografar em Caesar')}
    
    {hashtag} {c.cyan('Escolha uma opção: ')}""")
   
    if opt == "1":
      text4crypt = input(rf"    {hashtag} {c.cyan('Texto para criptografar: ')}")
      caesar_key = int(input(f"    {hashtag} {c.cyan('Chave de criptografia: ')}"))
      final_crypted_text = crypt(text=text4crypt, shift=caesar_key)
      print(rf""" 
    {c.cyan('Texto final criptografado na chave')} {c.yellow(caesar_key)}:
    {final_crypted_text}""")
    elif opt == "2":
       opt_d = input(rf""" 
    {num1} {c.cyan('Coloque a chave')}
    {num2} {c.cyan('Força Bruta')}

    {hashtag} {c.cyan('Escolha uma opção: ')}""" )
       if opt_d == "1":
          text4decrypt = input(f"    {hashtag} {c.cyan('Texto criptografado: ')}")
          caesar_dkey = int(input(f"    {hashtag} {c.cyan('Chave Caesar: ')}"))
          final_dcrypted_text = decrypt(encrypted_text=text4decrypt, shift=caesar_dkey)
       elif opt_d == "2":
          text4decrypt = input(f"    {hashtag} {c.cyan('Texto descriptografado: ')}")
          final_dcrypted_text = decrypt_all_possible(text=text4decrypt)
          finalD_format = format_output(final_dcrypted_text)
          print("\n")
          print(finalD_format)     

    input(f"{c.red('Pressione Enter para sair')}")

if __name__ == "__main__":
   main()