WHITELIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def parser(string):
    string = str(string)

    result = []
    result_append = result.append
    for char in string:
        if char in WHITELIST:
            result_append(char)
        else:
            result_append("&#%02x;" % ord(char))

    return "".join(result)


if __name__ == '__main__':
    import time
    start = time.time()
    with open('Amazon_Unlocked_Mobile.csv', 'r') as f:
        for line in f:
            parser(line)
    end = time.time()
    print(end - start)
