import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m
import

       _________   _____  .___   _____   
 /   _____/  /  _  \ |   | /     \  
 \_____  \  /  /_\  \|   |/  \ /  \ 
 /        \/    |    \   /    Y    \
/_______  /\____|__  /___\____|__  /
        \/         \/            \/    
 \033[1;32m. /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$                             
 \033[1;36m.| $$$ | $$ /$$__  $$| $$__  $$| $$_____/                             
 \033[1;32m.| $$$$| $$| $$  \__/| $$  \ $$| $$                                   
 \033[1;36m.| $$ $$ $$|  $$$$$$ | $$  | $$| $$$$$                                
 \033[1;32m.| $$  $$$$ \____  $$| $$  | $$| $$__/                                
 \033[1;36m.| $$\  $$$ /$$  \ $$| $$  | $$| $$                                   
 \033[1;32m.| $$ \  $$|  $$$$$$/| $$$$$$$/| $$$$$$$$                             
 \033[1;36m.|__/  \__/ \______/ |_______/ |________/                             
  ╔═══════════════════Note═══════════════════╗                 
  【𝘼𝙃𝙎𝘼𝙉 𝙆𝘼 𝙅𝙄𝙅𝙐 𝙋𝙍𝙄𝙉𝘾𝙀 𝙓 𝘼𝙔𝙐𝙎𝙃 𝘽𝙍𝘼𝙉𝘿 𝙄𝙉𝙓𝙄𝘿𝙀】
  ╚══════════════════════════════════════════╝
\033[1;92m.Author    :  𝘼𝙃𝙎𝘼𝙉 𝙆𝘼 𝙅𝙄𝙅𝘼 𝙋𝙍𝙄𝙉𝘾𝙀 𝙄𝙉𝙓𝙄𝘿𝙀|
\033[1;31m.Brother  : 𝙋𝙍𝙄𝙉𝘾𝙀 𝙄𝙉𝙓𝙄𝘿𝙀 | 𝘼𝙔𝙐𝙎𝙃 𝙃𝙀𝙍𝙀  |
 \033[1;36mGithub    : 𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘽𝙃𝙀𝙉 𝙆𝙄 𝙓𝘾𝙃𝙐𝙏 𝙆𝙊 𝘾𝙃𝙀𝙀𝙍𝙉𝙔 𝙒𝘼𝙇𝘼 𝙏𝙊𝙊𝙇     |
 \033[1;32m.Facebook  :𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝐁𝐇𝐄𝐍 𝐊𝐈 𝙂𝘼𝘽𝘿 𝙆𝙄 𝙉𝘼𝙎 𝙁𝘼𝘿𝙉𝙔 𝙒𝘼𝙇𝘼 𝙋𝙍𝙄𝙉𝘾𝙀 𝙃𝙀𝙍𝙀
 \033[1;34mTool Name : 𝘼𝙃𝙎𝘼𝙉 𝐊 𝘼𝙇𝙇 𝙋𝙄𝙇𝙇𝙔 𝐊𝐈 𝘽𝙃𝙀𝙉 𝙆𝙊 𝙓𝘾𝙃𝙊𝘿𝙉𝙔 𝙒𝘼𝙇𝘼 𝘼𝙎𝙃𝙄𝙌 𝙋𝙍𝙄𝙉𝘾𝙀   |
 \033[1;36mType type : 𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘽𝙃𝙀𝙉 𝙆𝙊 𝘾𝙃𝙊𝘿𝙉𝙔 𝐊𝘼𝙇𝙀𝘼 𝙇𝙄𝙔𝙀 𝙁𝙍𝙀𝙀 𝙆𝘼 𝙏𝙊𝙊𝙇 |
  ───────────────────────────────────────────────────────
   𖣘︎𖣘︎𖣘︎𖣘︎𖣘︎︻╦デ╤━╼【★𝙋𝙍𝙄𝙉𝘾𝙀 𝙓 𝘼𝙔𝙐𝙎𝙃 𝙏𝙊𝙊𝙇 𝙊𝙒𝙉𝙀𝙍★】╾━╤デ╦︻𖣘︎𖣘︎𖣘︎𖣘︎𖣘︎
 ───────────────────────────────────────────────────────
\033[1;32m【𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘽𝙃𝙀𝙉 𝙆𝙄 𝙓𝘾𝙃𝙐𝙏 𝙈𝙀 𝙐𝙉𝙂𝙇𝙄  𝘿𝘼𝙇 𝘽𝙃𝙊𝙏𝙃 𝙏𝙀𝙕  𝘾𝙃𝙇𝘼𝙂𝘼】
 \033[1;36m       𖣘︎𖣘︎𖣘︎【𝙋𝙍𝙄𝙉𝘾𝙀 𝙓 𝘼𝙔𝙐𝙎𝙃 𝘿𝘼𝘿 𝙄𝙉𝙓𝙄𝘿𝙀】𖣘︎𖣘︎𖣘︎""" )

def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;32m[√]𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘽𝙃𝙀𝙉  𝙆𝙄 𝙓𝘾𝙃𝙐𝙏 𝙈𝙀 𝙋𝙐𝙍𝘼 𝙇𝘼𝙉𝘿 𝘾𝙃𝙇𝘼 𝙂𝙔𝘼】  {} of Convo\033[1;35m {} \033[1;33msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;32m  - Time: {}".format(current_time))
                else:
                    print("\033[1;32m[x] MESSEGE FAIL HO GYA BHOSDI KE TOKAN SAHI DAL  {} of Convo \033[1;34m{} with Token \033[1;36m{}: \n\033[1;36m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;33m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;35m[!] An error occurred: {}".format(e))
def main():	
    print(logo)   
    print(' \033[1;31m[•] 𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘿𝙄𝘿𝙄 𝙆𝙄 𝙓𝘾𝙃𝙐𝙏 𝙈𝙀 𝙏𝙊𝙆𝙀𝙉 𝙁𝙄𝙇𝙀 𝘿𝘼𝙇➼')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;36m[•] 𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘽𝙃𝙀𝙉 𝙆𝙊 𝙆𝙃𝘼 𝘾𝙃𝙊𝘿𝙉𝘼 𝙐𝙄𝘿 𝘿𝘼𝙇➼ ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[•] 𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘽𝙃𝙀𝙉 𝙆𝙄 𝘾𝙃𝙐𝙏 𝙈𝙀 𝐒3 𝙁𝙄𝙇𝙀 𝙉𝙄𝙆𝘼𝐋 𝙆𝙒𝙍 𝐃𝐀𝐋 ➼')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[•] 𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘽𝙃𝙀𝙉 𝐊𝘼 𝙔𝘼𝙍𝐎 𝐊𝘼 𝙉𝘼𝙈𝙀 𝘿𝘼𝐋➼')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;34m[•] 𝘼𝙃𝙎𝘼𝙉 𝙆𝙄 𝘽𝙃𝙀𝙉 𝐊𝙊 𝙆𝙄𝙏𝙉𝙄 𝙎𝙋𝙀𝙀𝘿  𝙎𝙀 𝘾𝙃𝙊𝘿𝙉𝙎 𝙃𝙀➼' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
