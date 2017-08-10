#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TrieTree(object):
    def __init__(self):
        self.tree = {}

    def add(self, word):
        tree = self.tree
        for char in word:
            if char in tree:
                tree = tree[char]
            else:
                tree[char] = {}
                tree = tree[char]
        tree['exist'] = True

    def find(self, word):
        tree = self.tree
        for char in word:
            if char in tree:
                tree = tree[char]
            else:
                return False

        return 'exist' in tree and tree['exist'] is True


def load_dict():
    tree = TrieTree()
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            slst = l.split()
            if len(slst) == 2:
                name = slst[1]
                if name == '市辖区':
                    continue
                else:
                    tree.add(name)
            else:
                print('invalid record', l)
    return tree


# (1) 如果p1到达句子首位置，分词结束；
# (2) p2 = p1 - m；
# (3) 如果p1和p2之间的字符串S'在词表中不存在，p2++，重复(3)；
# (4) 如果p1和p2之间的字符串S'在词表中存在，则S'是一个词，p1 = p2-1，转(1)；
def match(word, dict, max_pattern_len=10):
    result = []
    if not word:
        return result
    word_length = len(word)
    m = min(word_length, max_pattern_len)
    p1 = word_length
    while p1 != 0:
        p2 = max(p1 - m, 0)
        sub_word = word[p2, p1]
        while sub_word != '' and not dict.find(sub_word):
            p2 = p2 + 1
            sub_word = word[p2, p1]
        result.append(sub_word)
        p1 = p2 - 1
    return result


if __name__ == '__main__':
    content = '永和服装有限公司'
    mydict = TrieTree()
    mydict.add("服装")
    mydict.add("有限公司")
    mydict.add("公司")
    mydict.add("和服")
    rl = match(content, mydict, 4)
    print(rl)