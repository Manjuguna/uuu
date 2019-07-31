apec,bart=map(int,input().split())
lt=[]
for _ in range(apec):
    lt.append(input())
for c in range(len(lt)):
    if('0' in lt[c]):
        lt[c]=lt[c].replace('0','')
    lt[c]=lt[c].replace(' ','')
lengths=[]
for c in lt:
    if(len(c)>0):
        lengths.append(len(c))
bart=min(lengths)
rat1='1 '*bart
rat1=rat1.strip()
for c in range(bart):
    print(rat1)
