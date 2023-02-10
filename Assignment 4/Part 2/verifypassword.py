from cryptography.fernet import Fernet

def read_password():
    pass_lookup = {}
    with open ('password', 'r') as f:
        for line in f:
            fields = line.split()
            pass_lookup[fields[0]] = [fields[1], fields[2]]
    return pass_lookup

def main():
    key = 'bVWr0JQAm9vRPNWyEuUTLbWVn7jfDNVPmGVE4lVxuE0='
    aes128 = Fernet(key)
    passlookup = read_password()
    uid = (str(input('\nEnter user ID: '))).strip()
    pwd = (str(input('\nEnter password: '))).strip()
    if uid in passlookup:
        encpass = passlookup[uid][0]
        encode = encpass.encode('utf-8')
        decpass = aes128.decrypt(encode)
        decode = decpass.decode('utf-8')
        if str(decode) != pwd:
            print('\nincorrect password\n')
        else:
            print('\ncorrect password. The password creation time was {0}\n'.format(passlookup[uid][1]))
    else:
        print('\nID does not exist')
        main()

if __name__ == '__main__':
    main()