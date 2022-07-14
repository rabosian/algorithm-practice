from collections import Counter

# using Counter
def checkMagazine(magazine, note):
    m = Counter(magazine.split())
    n = Counter(note.split())

    if m & n == n:
        print("Yes")
    else:
        print("No")

# using dictionary.pop => remove existing word in magazine ==> runtime error
def checkMagazine2(magazine, note):
    mDict = {i : magazine[i] for i in range(len(magazine))}
    nDict = {i : note[i] for i in range(len(note))}
    
    for i in range(len(nDict)):
        if nDict[i] in mDict.values():
            mDict.pop(list(mDict.keys())[list(mDict.values()).index(nDict[i])])
            continue
            
        else:
            print("No")
            break
    else:
        print("Yes")
        
        
m = "two times three is not four".split()
n = "two times two is four".split()

checkMagazine(m, n)