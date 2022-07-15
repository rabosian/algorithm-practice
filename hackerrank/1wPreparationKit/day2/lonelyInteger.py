from collections import Counter

def lonelyinteger(a):
    # using Counter()
    count = Counter(a)
    for k in count:
      if count[k] == 1:
        return k 
    
    # using math
    # listSum = sum(a)
    # setSum = sum(set(a))
    # return setSum * 2 - listSum


a = [1,2,3,4,3,2,1]
print(lonelyinteger(a))