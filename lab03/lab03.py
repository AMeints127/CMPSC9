def multiply(x,y):
    if y == 0:
        return 0

    return x + multiply(x, y-1)

def collectMultiples(inList, n):
    if inList != []:
        multiples = []
        i = 0
        if inList[i] % n == 0:
            multiples.append(inList[i])
            inList.remove(inList[i])
            return multiples + collectMultiples(inList, n)
        else:
            inList.remove(inList[i])
            return collectMultiples(inList, n)
    else:
        return []
    
def countVowels(s):
    if s != '':
        i = 0
        if s[i] in ['A','a','E','e','I','i','O','o','U','u']:
            count = 1
            s = s[1:]
            return count + countVowels(s)
        else:
            s = s[1:]
            count = 0
            return count + countVowels(s)
    else:
        return 0
            
def reverseVowels(s):
    if s != '':
        vowels = ''
        i = len(s) - 1
        if s[i] in ['A','a','E','e','I','i','O','o','U','u']:
            vowels += s[i]
            s = s[:i]
            return vowels + reverseVowels(s)
        else:
            s = s[:i]
            return vowels + reverseVowels(s)
    else:
        return ''

def removeSubString(s,sub):
    if sub not in s:
        return s
    if sub in s:
        sindex = s.index(sub)
        s = s[:sindex] + s[sindex + len(sub):]
        return removeSubString(s,sub)



    
