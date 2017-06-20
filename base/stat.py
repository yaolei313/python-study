def normalize(s):
    """
    Convert s to a normalized string
    :param s: 
    :return: 
    """
    keep = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            ' ', '-', "'"
            }
    result = ''
    for c in s:
        if c in keep:
            result += c
        else:
            result += ' '
    return result


def make_freq_stat(s):
    s = normalize(s)
    words = s.split()
    result = {}
    for w in words:
        if w in result:
            result[w] += 1
        else:
            result[w] = 1
    return result


def stat_file():
    fd = open('E:\download\The Life Story of an Otter.txt', 'r', encoding='utf-8')
    body = fd.read()
    num_chars = len(body)
    d = make_freq_stat(body)
    s1 = sum(d[k] for k in d)
    s2 = len(d.keys())
    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()
    i = 1
    for (count, word) in lst[:10]:
        print('%2s %4s %s' % (i, count, word))
        i += 1


str1 = "hello world,li bai!"
print(normalize(str1))

stat_file()
