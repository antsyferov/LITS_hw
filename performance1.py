WHITELIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def escape_engine(s, on_whitelist, on_ascii, on_unicode):
    pieces = []
    for char in s:
        if char in WHITELIST:
            pieces.append(on_whitelist(char))
        elif ord(char) < 256:
            pieces.append(on_ascii(char))
        else:
            pieces.append(on_unicode(char))
    return "".join(pieces)


def parser(string):
    s = unicode(string)

    escaped = escape_engine(s,
                            on_whitelist=lambda c: c,
                            on_ascii=lambda c: "&#%02x;" % ord(c),
                            on_unicode=lambda c: "&#%02x;" % ord(c)
                            )

    return escaped

import timeit

