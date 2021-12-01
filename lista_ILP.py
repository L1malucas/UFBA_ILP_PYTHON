 #                                               listas ilp
#    lista 1 //////////////////////////////////////////////////////////////////////////////
#A força de aceleração 
e, t = input().split()
v = int (e) / int (t)
print(str(int(v)))

#B ajude skywalker
a, b, c, d, e = input().split()
R = int (a) - (int (b) + int (c) +int (d) + int (e))
print(str(int(R)))

#C contabilizando pokemons
k, j, h = input().split()
r1, r2, r3 = input().split()
k = int(k)
j = int(j)
h = int (h)
r1 = int(r1)
r2=int(r2)
r3 = int(r3)
k =k + r1
j = j + r2
h = h + r3
print (str(k)+" "+str(j)+" "+str(h))

#D em busca do tesouro perdido
l, z, n, u, s = input().split()
l = int(l); z = int (z); n = int(n); u = int(u); s = int(s)

print(l + z + n + u + s)

#E numedo cdu
n = input()
n = int(n)
c = int(n/100); d = int((n%100)/10); u = int(((n%100)%10)/1)
print (u,d,c)

#F contador de segundos
n = input()
n = int(n)
H = int(n/3600); M = int((n%3600)/60); S = int((n%3600)%60)
print (str(H)+'h',str(M)+'m',str(S)+'s')

#   lista 2 //////////////////////////////////////////////////////////////////////////////
#A drone da amazonia
Xe, Ye = input().split()
Xd, Yd = input().split()
Xe = int(Xe); Ye = int(Ye); Xd = int(Xd); Yd = int(Yd)
if Xe == Xd and Ye == Yd:
    print("Soltar pacote")
else:
    print ("Nao soltar pacote")

#B boliche com tio rubis
a, b, c = input().split()
a = int(a); b = int(b); c = int(c)
X = int(a*b); Y = int (c+1)
if X >= Y:
    print("S")
else:
    print("N")

#C x = int(input())
y = int(input())
if x>0 and y>0:
    print("Quadrante 1")
elif x<0 and y>0:
    print("Quadrante 2")
elif x<0 and y<0:
    print("Quadrante 3")
elif x>0 and y<0:
    print ("Quadrante 4")
else:
    print("Centro")

#D fazendo um gol
z, g = input().split()
d, c = input().split()

if d==z:
    print("Driblado")
    if c==g:
        print("Gol")
    else:
        print("...e o goleiro pega")
else:
    print("Bloqueado")

#E pu-dean
c, o, l, x = input().split()
c=int(c); o=int(o); l=int(l); x=int(x)
c=int(c/4); o=int(o/8); l=int(l/2);x = int(x); total = int (c)
if o <= total:
    total = o
    if l <= total:
        total = l
        if x<= total:
            total = x
    else:
        if x <= total:
            total = x
else:
    if l <= total:
        total = l
        if x<= total:
            total = x
    else:
        if x<= total:
            total = x
total = (total*1259)
print(int(total/3600),"h",int((total%3600)/60), "m",int((total%3600)%60),"s")

#F nivel de maestria
n1, n2, n3, n4, n5, n6 = input().split()
n1 = int(n1); n2=int(n2); n3=int(n3); n4=int(n4); n5=int(n5); n6=int(n6); soma = int(n1+n2+n3+n4+n5+n6)
if soma >= 250:
    print("S+")
elif soma <= 249 and soma >= 200:
    print("S")
elif soma <= 199 and soma >=180:
    print("S-")
elif soma <=179 and soma >=150:
    print("A+")
elif soma <=149 and soma >= 100:
    print("A")
elif soma <=99 and soma >=80:
    print("A-")
elif soma <=79 and soma >=60:
    print("B+")
elif soma <=59 and soma >= 40:
    print("B")
else:
    print("B-")

#   lista 3 //////////////////////////////////////////////////////////////////////////////
#A ocarina of Time
X,Y,Z = input().split()
N = int(input())
i = int(0)

while i < N:
    print (X,Y,Z)
    i += 1

#B fortalecimento de clima
n = int(input())
count = int(0)
for count in range (n):
    p, m = input().split()
    p = int (p); m = int (m)
    print(p+m)

#C missao jedi o retorno
n, x, xpmin = input().split()
n = int(n); x = int(x); xpmin = int(xpmin);

for i in range(n):
    xp,q = input().split()
    xp = int(xp); q=int(q)
    if xp >= xpmin:
        print((x+xp), (q+1))
    else:
        print (xp, q)

#D vulcao
t = int(input())
p = int(input())
aux = int(0)
while p!=0:
    if p > t:
        aux = 1
    p = int(input())
if aux >= 1:
    print("ALARME")
else:
    print("O Havai pode dormir tranquilo")

#E e, p = input().split()
e = int(e); p = int(p); aux = int(0)
while e > 0 and p>0:
    e = e - p
    p = p - 1
    aux = aux + 1
if e>0 and p<=0:
    print (" F ")
else:
    print(aux)

#F  as poções do geraldo 2
n, m = input().split()
n=int(n);m=int(m);count=int(0)

for i in range(n):
    p = map(int,input().split())
    aux = sum(p)
    if aux > count:
        count = aux
print(count)

#   lista 4 //////////////////////////////////////////////////////////////////////////////
#A mochileiro metodico
n= int(input())
p=list()
p = input().split()
vetores=[]

for i in range (n):
    vetores.append (p[i] )
vetores = [int(i) for i in p]
vetores.reverse()
print(*vetores)

#B em busca da esmeralda
n=int(input())
p = input().split()
c=input()
aux=int(0); no = int(-1)
for i in range(n):
    if c == p[i]:
        aux +=1
    i+=1
if aux > 0:

    print(int(c))
else:
    print(no)

#C o sitio de alice
#o sitio de alice
n = int(input())
vetor = [int(n) for n in input().split()]
soma = int(sum(vetor) / 2); result = int(0); aux = int(0)

for i in range(len(vetor) -1):
    aux = int(vetor[i] + aux)
    if aux == soma:
        result = i+1

print(result)

#D blasphemous
n = int(input())
x = list(map(int,input().split()))
m = int(input())
auxVida = int(0)
auxVida = m
for i, fase in enumerate(x):
    if auxVida <=0:
        break
    else:
        if fase == 1:
            auxVida = m
        if fase > 1:
            auxVida -= fase
if auxVida > 0:
    print("Yes, you can")
else:
    print("You Died")

#E a grande travessia
#a grande travessia
s, n = input().split()
s = int(s); n = int(n); caminho = [0] * n

for pulo in range(s):
	p = int(input())
	for j in range(0, n, p):
		if caminho[j] == 0:
			caminho[j] = 1
for saida in caminho:
	print(saida, end=" ")

#F among us
n=int(input())
x= input().split()
vetor=[]

for i in range(n):
    vetor.append(x[i])
vetor.sort(key=int)
print(*vetor)

#G vamos jogar um jogo
s = str(input())
q, p = input().split() #q = quantidade e p igual palavra
q = int(q);p = str(p); aux = int(0) #aux = ocorrencias da palavra na string
#retira os espaços em branco
s = s.replace(" ", "")


#imprime resultado encontrado
if q == s.count(p):
    print(s.count(p))
    print("SIM!")
else:
    print(s.count(p))
    print("NAO!")

#H organização de autores
#organização dos autores
qtd=int(input())
ultimo = str()
for autor in range(qtd):
     nome = [str(x) for x in input().split(" ")]
     saida = []
     for i in range(len(nome)):
        saida.append(nome[i][0]+". ")
        saida = [valor.upper() for valor in saida]
        if i == len(nome)-1:
            saida.pop(-1)
            saida.append(nome[i][0:1].upper())
            ultimo = (nome[i][1:].lower())
     print(''.join(saida), ultimo, sep='')

#I palindromos
st = str(input().upper())
st = st.replace(" ","")
strAux = st[::-1]

if st == strAux:
    print("Palindromo")
else:
    print("!Palindromo")

#       lista 5 //////////////////////////////////////////////////////////////////////////////
#A busca de leonidas
p=int(input())
L = C = int(10); aux=int(0)
matriz = []
for i in range(L):
   linha = [int(x) for x in input().split()]
   matriz.append(linha)

for x in range(L):
    for y in range(C):
        if matriz[x][y] == p:
            aux+=1

if aux >= 1:
    print("sim")
else:
    print("nao")

#B subtração de matrizes
LINHA, COLUNA = [int (i) for i in input().split()]
a = []; b = []; c = []
for line in range (LINHA):
    linha1 = [int (j) for j in input().split()]
    a.append (linha1)

for line in range (LINHA):
    linha2 = [int (k) for k in input().split()]
    b.append (linha2)

for line in range (LINHA):
    linha3 = [0] * COLUNA
    c.append (linha3)
    for column in range (COLUNA):
        c [line] [column] = a [line] [column] - b [line] [column]
        print( c [line] [column], end=" ")
    print()

#C campo de aboboras
n = int(input())
matriz = []
somaHarry = int(0); somaRon = int(0)

for indice in range (n):
    linha = [int(i) for i in input().split()]
    matriz.append(linha)

linha, coluna = input().split()
linha = int(linha); coluna = int(coluna)

if linha > coluna:
    for j in range (n):
        somaHarry = somaHarry + matriz [linha] [j]
        matriz [linha] [j] = 0
        somaRon = somaRon + matriz [j] [coluna]
else:
    for k in range (n):
        somaRon = somaRon + matriz [k] [coluna]
        matriz [k] [coluna] = 0
        somaHarry = somaHarry + matriz [linha] [k]
print("Harry",somaHarry)
print("Ron", somaRon)

#       lista 6 //////////////////////////////////////////////////////////////////////////////
#A seleção de quadribol
#seleção de quadribol
n = int(input())
lista = [int (i) for i in input().split()]
aux = []; total = int(8)
#selection sort verificando maior valor
for i in range(len(lista)-1, 0, -1):
    maior = 0
    for j in range(1, i+1):
        if lista[j] > lista[maior]:
            maior = j
        lista[maior], lista[i] = lista[i], lista[maior]
#adicionando oito valores ao vetor
for indice in range(total):
    aux.append(lista[indice])
print(*(aux))

#B dança dos casais
n = int(input())
h = []
m = []
h = input().split()
m = input().split()
aux = []

h.sort(key=int, reverse=True)
m.sort(key=int)

for i in range(n):
    print(h[i], m[i])

#C srt intergalatica
#intergalatica
n = int(input())
lista = []; aux = []
#leitura dos itens
for i in range(n):
    i, r = input().split()
    i = int(i); r = int(r)
    lista.append(r)
    aux.append(i)
#organizando decrescente (bubble sort)
for  i in range(len(lista)):
    for j in range(len(lista) -1):
        if lista[j+1]>lista[j]:
            lista[j+1], lista[j] = lista[j], lista[j+1]
            aux[j+1], aux[j] = aux[j], aux[j+1]

#impresão linha a linha
for j in range (n):
    print(aux[j], lista[j])

#D temos que pegar
#temos que pegar
qtd, tipo, ordem = input().split()
qtd=int(qtd); nomes = []; nivel = []
#recebendo dados
for linha in range(qtd):
    n, l = input().split()
    l = int(l)
    nomes.append(n); nivel.append(l)

if ordem == 'D':              #verifica ordem de organização decrescente
    if tipo == 'N':           #organiza por nomes decrescente
        for i in range(qtd):  #bubble sort decrescente
            for j in range(len(nomes) -1):
                if nomes[j+1] > nomes[j]:
                    nomes[j+1], nomes[j] = nomes[j], nomes[j+1]
                    nivel[j+1], nivel[j] = nivel[j], nivel[j+1]
    else:                     #organiza por nivel decrescente
        for i in range (qtd): #bubble sort
            for j in range (len(nivel) -1):
                if nivel[j+1] > nivel[j]:
                    nivel[j+1], nivel[j] = nivel[j], nivel[j+1]
                    nomes[j+1], nomes[j] = nomes[j], nomes[j+1]
  #  for saida in range (len(nomes)):#print do resultado
 #       print(nomes[saida], nivel[saida])
if ordem == 'C':              #verifica ordem de organização decrescente
    if tipo == 'N':           #organiza por nomes crescente
        for i in range (qtd): #bubble sort crescente
            for j in range(len(nomes)-1):
                if nomes[j] > nomes[j+1]:
                    nomes[j], nomes[j+1] = nomes[j+1], nomes[j]
                    nivel[j], nivel[j+1] = nivel[j+1], nivel[j]
    else:                     #organiza por nivel crescente
        for i in range(qtd): #bubble sort
            for j in range(len(nivel) -1):
                if nivel[j] > nivel[j+1]:
                    nivel[j], nivel[j+1] = nivel[j+1], nivel[j]
                    nomes[j], nomes[j+1] = nomes[j+1], nomes[j]
for saida in range (len(nivel)):#print do resultado
  print(nomes[saida], nivel[saida])

