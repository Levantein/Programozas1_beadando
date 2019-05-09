'''
12. Feladat
Írj egy programot, ami standard bemenetként kap egy sztring-et. A program számolja
meg, hogy hány darab számot, nagybetűt, kisbetűt, és egyéb karaktert tartalmaz a
bemenetként kapott sztirng.
'''

str=str(input("Adj meg egy karakterláncot: "))
kisbetuk=0
nagybetuk=0
szamok=0
egyeb_karakterek=0
for i in range(0,len(str)):
    if str[i]>="A" and str[i]<="Z":
        nagybetuk=nagybetuk+1
    elif str[i]>="a" and str[i]<="z":
        kisbetuk=kisbetuk+1
    elif str[i]>="0" and str[i]<="9":
        szamok=szamok+1
    else:
        egyeb_karakterek=egyeb_karakterek+1

print("A kisbetűk száma:",kisbetuk)
print("A nagybetűk száma:",nagybetuk)
print("A számok száma:",szamok)
print("Az egyéb karakterek száma:",egyeb_karakterek)