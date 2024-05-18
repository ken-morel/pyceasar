def ceasar(txt, offset):
    ret = ""
    for char in txt:
        if char.isalpha():
            #print("alpha:", char)
            base = 'A' if char.isupper() else 'a'
            char = chr(
                (
                    ord(
                        char
                    )-ord(
                        base
                    )+offset
                )%26+ord(base)
            )
        ret += char
    return ret

def countWords(txt, dict_url):
    c = 0
    for word in open(dict_url):
        if word.strip() in txt.split(' '):
            c+= 1
    return c
            
        
def unceasar(txt, dict_url="dictionary.txt"):
    best = None
    bestNum = -1
    bestIdx = -1
    for i in range(26):
        test = ceasar(txt, i)
        count = countWords(test, dict_url)
        print("  -", i, "counts:", count)
        if bestNum < count:
            bestNum = count
            best = test
            bestIdx = i
        elif bestNum == count:
            n = '\n'
            msg = f"""conflicting {bestIdx} and {i}
1. {test[:20].replace(n, '')!r}
2. {best[:20].replace(n, '')!r}
enter 'r' for 1. to replace 2."""
            if input(msg) == 'r':
                bestNum = count
                best = test
                bestIdx = i
            
    return best
