#!/usr/bin/python3

def ft_strlen(s:str):

    count = 0

    try:
        while s[count]:
            count += 1
    except:
        return count


def ft_split(s:str , c:str) -> list[str]:
    split  : list[str] = []
    size = ft_strlen(s) - 1
    i = 0
    while (i < size):
        while (s[i] == c[0] and i < size):
            i += 1
        if (s[i] != c[0] and i < size):
            start = i
            while(i <= size and s[i] != c[0]):
                i += 1
            word = s[start:i]
            split.append(word)
    return (split)
