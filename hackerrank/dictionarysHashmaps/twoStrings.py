def twoStrings(s1, s2):
    if set(s1) & set(s2):
        print("Yes")
    else:
        print("No")


s1 = "hel"
s2 = "world"
twoStrings(s1, s2)