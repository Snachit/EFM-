def fonction(T,F,E):
    u=[]
    for i in range(E,F):
        u.append(T[i])
    return u
t=[]
x=int(input("saisire a taille du tableau:"))


for i in range(x):

    n=int(input(f"saisire l element num {i+1}:"))
    t.append(n)
F=int(input("entrer le 1er nombre : "))
E=int(input("entrer le 2eme nombre :"))
print(fonction(t,E,F))   