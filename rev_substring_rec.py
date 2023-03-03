def rev(st):
    if len(st)<=0 | len(st)==1:
        return st
    else:
        return rev(st[1:])+st[0]
def revs(sta):
    sts=sta.split()
    revs=" ".join(list(map(rev,reversed(sts))))
    return revs
stin= input("Statement : ")
revs=revs(stin)
print("Statement after reversal : ",revs)