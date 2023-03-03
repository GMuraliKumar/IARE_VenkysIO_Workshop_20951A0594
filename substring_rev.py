import threading as th
def rev(st,ar):
    return ar.append(st[::-1])
sta=input("Enter the Statement : ")
st_ar=sta.split(" ")
rev_ls=[]
l2=[]
for st in st_ar:
    ele=th.Thread(target=rev,args=(st,rev_ls))
    l2.append(ele)
for ele in l2:
    ele.start()
for ele in l2:
    ele.join()
print(*rev_ls)