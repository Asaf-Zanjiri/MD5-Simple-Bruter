from hashlib import md5

CHARSET = 'abcdefghijklmnopqrstuvwxyz'
ORIGINAL_PASSWD = 'zzz'
HASHED_PASSWD = md5(ORIGINAL_PASSWD.encode()).hexdigest()


def check_hash(word):
    hash = md5(word.encode()).hexdigest()
    print('Trying: {word} - {hash}'.format(word=word, hash=hash))
    if hash == HASHED_PASSWD:
        print('Password Found!\n {word} - {hash}'.format(word=word, hash=hash))
        return True
    return False


def main():
    print('Asaf\'s Bruteforce tool\n-----------------------------\nPassword: {original_passwd}\nHash: {hashed_passwd}\n\n'.format(original_passwd=ORIGINAL_PASSWD, hashed_passwd=HASHED_PASSWD))
    passwd_len = int(input('Enter password length to begin the bruteforce: '))
    index_list = [0] * passwd_len
    stop_brute = False

    while not stop_brute:
        # Goes over the the charset chars by index and checks if their hash matches.
        for ch in range(len(CHARSET)):
            passwd = ''
            for i in range(passwd_len):
                passwd += CHARSET[index_list[i]]
            if check_hash(passwd) is True:
                stop_brute = True
                break
            index_list[-1] += 1

        # Make sure all of the indexes are within the range of valid characters.
        for i in range(1, passwd_len + 1):
            # If the index is out of bound it'd add +1 to the index of the char to its left and reset its value to 0.
            if index_list[passwd_len - i] % len(CHARSET) == 0 and index_list[passwd_len - i] != 0:
                # Stops the bruting if the password wasn't found within the password length range.
                if passwd_len - i - 1 < 0:
                    stop_brute = True
                    break
                index_list[passwd_len - i - 1] += 1
                index_list[passwd_len - i] = 0
            else:
                break
    if index_list[0] == len(CHARSET):
        print('Password wasn\'t found within the given range!')


if __name__ == '__main__':
    main()
