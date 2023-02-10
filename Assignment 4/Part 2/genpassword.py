from datetime import datetime
from cryptography.fernet import Fernet

def main():
    key = 'bVWr0JQAm9vRPNWyEuUTLbWVn7jfDNVPmGVE4lVxuE0='
    aes128 = Fernet(key)
    uid = (str(input('\nEnter user ID: '))).strip()
    pwd = (str(input('\nEnter password: '))).strip()
    if uid not in open('password').read().replace('\n',' ').strip().split(' '):
        print()
        time = datetime.now().strftime('%H:%M:%S')
        encode = pwd.encode('utf-8')
        encpass = aes128.encrypt(encode)
        with open('password', 'a+') as f:
            f.write('{} {} {}\n'.format(uid, encpass.decode('utf-8'), time))
        choice = input('More ID and password (Y/N)? ').upper()
        if choice == 'Y':
            main()
        elif choice == 'N':
            exit(0)
        else:
            print('\nInvalid choice\n')
            exit(0)
    else:
        print('\nID exists')
        main()

if __name__ == '__main__':
    open('password', 'a+').close()
    main()