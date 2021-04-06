from config import *

msg = ''' __   __                  __        __   ___  __  
|  \ /  \ |  | |\ | |    /  \  /\  |  \ |__  |__) 
|__/ \__/ |/\| | \| |___ \__/ /~~\ |__/ |___ |  \ 
                                            By s-r0ff3y
'''

def main():
    mode = 0
    count = 1
    
    clear()
    print(msg)

    print('-'*8 + '   OPTIONS   ' + '-'*8)
    print('[1] Download MP3\n[2] Download MP4')
    option = input('>>> ')
    print('\n[?] Path to save files?')
    path = input('>>> ')

    if option == '1':
        mode = 1
    elif option == '2':
        mode = 2
    else:
        print('[!] Invalid Option.')
        exit()

    print('[?] Would you like to download a playlist? (y/n)')
    playlist = input('>>> ')
    if playlist.lower().strip() == 'y':
        if mode == 1:
            mode = 3
            clear()
            print('-'*8 + '   PLAYLIST URL   ' + '-'*8)
            url = input('>>> ')
            if download(mode, url, path):
                print('[+] Playlist downloaded.')
                exit()
            else:
                print('[!] Error downloading playlist.')
                exit()
            exit()
        elif mode == 2:
            mode = 4
            clear()
            print('-'*8 + '   PLAYLIST URL   ' + '-'*8)
            url = input('>>> ')
            if download(mode, url, path):
                print('[+] Playlist downloaded.')
                exit()
            else:
                print('[!] Error downloading playlist.')
                exit()
            exit()
        else:
            print('[!] Invalid Option.')
            exit()
    else:
        pass

    clear()
    print('-'*8 + '   ENTER KEY WORDS   ' + '-'*8)
    key = input('>>> ')

    key = key.replace(' ', '+')

    top = search(key)

    if top:
        clear()
        print('-'*8 + '   TOP THREE VIDEOS   ' + '-'*8)
        for link in top:
            print('[{}] {}'.format(str(count), link))
            count += 1
        if download(mode, top[0], path):
            print('[+] Download Complete.')
            input()
            main()
        else:
            print('[!] Error Downloading Video.')
            input()
            main()
    else:
        print('[!] Error Finding Video.')
        input()
        main()

if os.path.isdir('downloads'):
    pass
else:
    os.mkdir('downloads')

main()