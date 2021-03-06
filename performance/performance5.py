WHITELIST = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


def parser(string):
    string = str(string)
    local_ord = ord
    local_whitelist = WHITELIST

    result = "".join([
        char if char in local_whitelist
        else "&#%02x;" % local_ord(char)
        for char in string])

    return result


if __name__ == '__main__':
    import time
    start = time.time()
    with open('Amazon_Unlocked_Mobile.csv', 'r') as f:
        for line in f:
            parser(line)
    end = time.time()
    print(end - start)
