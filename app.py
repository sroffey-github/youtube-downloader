import config, os

msg = '''

█▄█ ▀█▀   █▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
░█░ ░█░   █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄
                                            By sroffey-github
'''

config.clear()
print(msg + '-'*8 + '   OPTIONS   ' + '-'*8)
print('[1] Download MP3\n[2] Download MP4\n[3] Exit\n')

option = input('>>> ')
if option == '1':
    mode = 1
elif option == '2':
    mode = 2
elif option == '3':
    print('[-] Closing...')
    exit()
else:
    print('[!] Invalid Option.')
    exit()

config.clear()
print('-'*8 + '   ENTER SEARCH TERM   ' + '-'*8)
videos = config.search(input('>>> ').lower())

print('-'*8 + '   TOP THREE VIDEOS   ' + '-'*8 + '\n')
for link in videos:
    print('[{}] {}'.format(str(videos.index(link) + 1), link))

print('[i] Downloading the top result...\n')    
download = config.download(videos[0], mode)
if download:
    print('\n[+] Top Result Downloaded')
else:
    config.log(download) # make it return proper error
    print('[!] Error, please check the logs')
    exit()