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



=====================================================================================================================================================
// ENERGIA ACELERACAO
// #include <iostream>

// using namespace std;

// int main()
// {
// 	long int massa, velocidade, energia;
// //   massa entre 40 e 100 ; velocidade entre 0 e 300.000.000
// 	cin >> massa;
// 	cin >> velocidade;
// 	energia = massa * (velocidade *velocidade);
// 	cout << energia;
// 	return 0;
// }
// CONTINHA
// #include <iostream>
// #include <iomanip> // para configurar a precisão decimal

// int main() {
//     int A, B, C, D, E, F;
    
//     // Lendo os valores de entrada
//     std::cin >> A >> B >> C >> D >> E >> F;
    
//     // Calculando o resultado da expressão
//     double resultado = ((A + B) * (C - D) * (E + F)) / 2.0;
    
//     // Saída formatada com uma casa decimal
//     std::cout << "Eu sou FERA nas continhas e o resultado é " << std::fixed << std::setprecision(1) << resultado << std::endl;
    
//     return 0;
// }
// MEDIA PONDERADA
// #include <iostream>
// #include <iomanip>

// using namespace std;

// int main() {
//     double prova1, prova2, trabalho;
//     cin >> prova1 >> prova2 >> trabalho;
//     double mediaPonderada = ((prova1 * 4) + (prova2 * 4) + (trabalho * 2)) / 10.0;
//     cout << fixed << setprecision(2) << mediaPonderada << endl;
//     return 0;
// }
//  PENTATLO
// #include <iostream>
// #include <iomanip>

// using namespace std;

// int main() {
//     int lima_inscricao, lima_n1, lima_n2, lima_n3, lima_n4, lima_n5;
//     cin >> lima_inscricao >> lima_n1 >> lima_n2 >> lima_n3 >> lima_n4 >> lima_n5;
//     double lima_media = (lima_n1 + lima_n2 + lima_n3 + lima_n4 + lima_n5) / 5.0;
//     cout << lima_inscricao << " " << fixed << setprecision(1) << lima_media << endl;
//     return 0;
// }
//AJUDE SKYWALKER
// #include <iostream>
// using namespace std;

// int main() {
//     int lima_a, lima_b, lima_c, lima_d, lima_e;
//     cin >> lima_a >> lima_b >> lima_c >> lima_d >> lima_e;
//     int lima_inimigas = lima_a - (lima_b + lima_c + lima_d + lima_e);
//     cout << lima_inimigas << endl;
//     return 0;
// }

// AS NOVAS MISSÕES JEDI

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_n, lima_xp, lima_xpi_yoda, lima_xpi_luke, lima_xpi_ahsoka;
//     cin >> lima_n >> lima_xp;
//     cin >> lima_xpi_yoda >> lima_xpi_luke >> lima_xpi_ahsoka;
//     int lima_xp_total = lima_n * lima_xp;
//     cout << "Yoda " << lima_xpi_yoda + lima_xp_total << endl;
//     cout << "Luke " << lima_xpi_luke + lima_xp_total << endl;
//     cout << "Ahsoka " << lima_xpi_ahsoka + lima_xp_total << endl;
//     return 0;
// }

// Incursão da Divisão de Reconhecimento

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_n;
//     cin >> lima_n;
//     int lima_titans_levi = 20;
//     int lima_titans_soldier = 5;
//     int lima_total_kills = lima_titans_levi + (lima_n / lima_titans_soldier);
//     int lima_required_soldiers = (lima_n - lima_titans_levi) / lima_titans_soldier;
//     cout << max(0, lima_required_soldiers) << endl;
//     return 0;
// }

// Entregas do Lobo Mau

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_t, lima_d, lima_v, lima_p;
//     cin >> lima_t >> lima_d;
//     cin >> lima_v >> lima_p;
//     int lima_total_distance_cost = lima_t * lima_v;
//     int lima_total_toll_count = (lima_t / lima_d);
//     int lima_total_toll_cost = lima_total_toll_count * lima_p;
//     int lima_total_cost = lima_total_distance_cost + lima_total_toll_cost;
//     cout << lima_total_cost << endl;
//     return 0;
// }

// Contador de segundos

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_n;
//     cin >> lima_n;
//     int lima_hours = lima_n / 3600;
//     int lima_minutes = (lima_n % 3600) / 60;
//     int lima_seconds = lima_n % 60;
//     cout << lima_hours << "h " << lima_minutes << "m " << lima_seconds << "s" << endl;
//     return 0;
// }
// Drone da Amazônia

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_x1, lima_y1, lima_x2, lima_y2;
//     cin >> lima_x1 >> lima_y1;
//     cin >> lima_x2 >> lima_y2;
//     if (lima_x1 == lima_x2 && lima_y1 == lima_y2) {
//         cout << "Soltar pacote" << endl;
//     } else {
//         cout << "Nao soltar pacote" << endl;
//     }
//     return 0;
// }

// Altura

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_a, lima_b, lima_c;
//     cin >> lima_a >> lima_b >> lima_c;
//     int lima_maior_altura = max(lima_a, max(lima_b, lima_c));
//     cout << lima_maior_altura << endl;
//     return 0;
// }
// Cai pro x1

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_l, lima_p;
//     int lima_total_lucas = 0, lima_total_pedro = 0;
//     for (int i = 0; i < 3; i++) {
//         cin >> lima_l >> lima_p;
//         lima_total_lucas += lima_l;
//         lima_total_pedro += lima_p;
//     }
//     if (lima_total_lucas > lima_total_pedro) {
//         cout << "Lucas" << endl;
//     } else if (lima_total_pedro > lima_total_lucas) {
//         cout << "Pedro" << endl;
//     } else {
//         cout << "Empate" << endl;
//     }
//     return 0;
// }

// Exame Chunin

// #include <iostream>
// using namespace std;
// int main() {
//     char lima_p1, lima_p2;
//     cin >> lima_p1 >> lima_p2;
//     if ((lima_p1 == 'N' || lima_p2 == 'N') || (lima_p1 == lima_p2)) {
//         cout << "eliminado" << endl;
//     } else {
//         cout << "classificado" << endl;
//     }
//     return 0;
// }

// Super Mario Bros

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_sc, lima_mm, lima_ck;
//     cin >> lima_sc >> lima_mm >> lima_ck;
//     int lima_faltando_sc = 30 - lima_sc;
//     int lima_faltando_mm = 6 - lima_mm;
//     int lima_faltando_ck = 3 - lima_ck;
//     if (lima_faltando_sc <= 0) {
//         cout << "PROXIMO MUNDO" << endl;
//     } else {
//         cout << lima_faltando_sc << " " << lima_faltando_mm << " " << lima_faltando_ck << endl;
//     }
//     return 0;
// }

// Forjando Espadas

// #include <iostream>
// using namespace std;
// int main() {
//     int lima_a, lima_m, lima_c;
//     cin >> lima_a >> lima_m >> lima_c;
//     int lima_espadas_a = lima_a / 2;
//     int lima_espadas_m = lima_m / 3;
//     int lima_espadas_c = lima_c / 5;
//     int lima_max_espadas = min(lima_espadas_a, min(lima_espadas_m, lima_espadas_c));
//     cout << lima_max_espadas << endl;
//     return 0;
// }

// Fazendo um gol

// #include <iostream>
// using namespace std;
// int main() {
//     char z, g, d, c;
//     cin >> z >> g;
//     cin >> d >> c;

//     if (d == z) {
//         cout << "Driblado" << endl;
//         if (c == g) {
//             cout << "Gol" << endl;
//         } else {
//             cout << "...e o goleiro pega" << endl;
//         }
//     } else {
//         cout << "Bloqueado" << endl;
//     }
//     return 0;
// }


// INTERVALOS

// #include <iostream>
// using namespace std;
// int main() {
//     int x, y, w, z, n;
//     cin >> x >> y;
//     cin >> w >> z;
//     cin >> n;
//     bool inFirst = (n > x && n <= y);
//     bool inSecond = (n >= w && n < z);
//     if (inFirst && inSecond) {
//         cout << "Ambos!" << endl;
//     } else if (inFirst) {
//         cout << "Primeiro intervalo!" << endl;
//     } else if (inSecond) {
//         cout << "Segundo intervalo!" << endl;
//     } else {
//         cout << "Nenhum!" << endl;
//     }
//     return 0;
// }

// Fortalecimento de clima
// #include <iostream>
// using namespace std;
// int main() {
//     int lima_n, lima_p, lima_m;
//     cin >> lima_n;
//     for (int i = 0; i < lima_n; i++) {
//         cin >> lima_p >> lima_m;
//         cout << lima_p + lima_m << endl;
//     }
//     return 0;
// }

// Escolha do Campeão
// #include <iostream>
// using namespace std;
// int main() {
//     int lima_n, lima_poder, lima_max_poder = 0;
//     cin >> lima_n;
//     for (int lima_i = 0; lima_i < lima_n; lima_i++) {
//         cin >> lima_poder;
//         if (lima_poder > lima_max_poder) {
//             lima_max_poder = lima_poder;
//         }
//     }
//     cout << lima_max_poder << endl;
//     return 0;
// }

// Ajude o pequeno Kurumin
// #include <iostream>
// using namespace std;
// int main() {
//     int lima_n, lima_a, lima_b, lima_c, lima_d, lima_s = 0;
//     cin >> lima_n;
//     for (int lima_i = 0; lima_i < lima_n; lima_i++) {
//         cin >> lima_a >> lima_b >> lima_c >> lima_d;
//         int lima_resultado = lima_a + lima_b + lima_c + lima_d;
//         if (lima_resultado >= 100) {
//             lima_resultado = lima_a - lima_b - lima_c - lima_d;
//         }
//         lima_s += lima_resultado;
//     }
//     cout << lima_s << " anos de vida" << endl;
//     return 0;
// }


// Clones das sombras
// #include <iostream>
// using namespace std;
// int main() {
//     int lima_n;
//     cin >> lima_n;
//     if (lima_n > 0 && (lima_n & (lima_n - 1)) == 0) {
//         cout << "Dattebayo" << endl;
//     } else {
//         cout << "Tururuuu" << endl;
//     }
//     return 0;
// }

// Pirâmide de limonadas
// #include <iostream>
// using namespace std;
// int main() {
//     int lima_n;
//     cin >> lima_n;
//     for (int lima_j = 1; lima_j <= lima_n; ++lima_j) {
//         for (int lima_k = 0; lima_k < lima_n - lima_j; ++lima_k) {
//             cout << " ";
//         }
//         for (int lima_k = 0; lima_k < (lima_j * 2 - 1); ++lima_k) {
//             cout << lima_j;
//         }
//         cout << endl;
//     }
//     return 0;
// }

// Desenhista
// #include <iostream>
// using namespace std;
// int main() {
//     int lima_p;
//     cin >> lima_p;
//     for (int lima_i = 1; lima_i <= lima_p; ++lima_i) {
//         for (int lima_j = 0; lima_j < lima_p - lima_i; ++lima_j) {
//             cout << ">";
//         }
//         for (int lima_j = 0; lima_j < lima_i; ++lima_j) {
//             cout << "#";
//         }
//         cout << endl;
//     }
//     return 0;
// }

// Desafio Tático
// #include <iostream>
// using namespace std;
// int main() {
//     int lima_p, lima_s;
//     cin >> lima_p >> lima_s;
//     for (int lima_i = 0; lima_i < lima_p; ++lima_i) {
//         int lima_ataque_total = 0, lima_defesa_total = 0;
//         for (int lima_j = 0; lima_j < lima_s; ++lima_j) {
//             int lima_ataque, lima_defesa;
//             cin >> lima_ataque >> lima_defesa;
//             lima_ataque_total += lima_ataque;
//             lima_defesa_total += lima_defesa;
//         }
//         cout << lima_ataque_total << " " << lima_defesa_total << endl;
//     }
//     return 0;
// }


// Em Busca da Esmeralda
// #include <iostream>
// #include <vector>
// using namespace std;
// int main() {
//     int lima_n;
//     cin >> lima_n;
//     vector<int> lima_caixas(lima_n);
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_caixas[lima_i];
//     }
//     int lima_c;
//     cin >> lima_c;
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         if (lima_caixas[lima_i] == lima_c) {
//             cout << lima_c << endl;
//             return 0;
//         }
//     }
//     cout << -1 << endl;
//     return 0;
// }


// Dr. Strange e as Multidimensões
// #include <iostream>
// #include <vector>
// using namespace std;
// int main() {
//     int lima_n;
//     cin >> lima_n;
//     vector<int> lima_u(lima_n), lima_v(lima_n), lima_d(lima_n);
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_u[lima_i];
//     }
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_v[lima_i];
//     }
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_d[lima_i];
//     }
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         if (lima_u[lima_i] + lima_v[lima_i] != lima_d[lima_i]) {
//             cout << "NOPE :(" << endl;
//             return 0;
//         }
//     }
//     cout << "OK" << endl;
//     return 0;
// }


// Ajude a Imperial
// #include <iostream>
// #include <vector>
// using namespace std;
// int main() {
//     int lima_n;
//     cin >> lima_n;
//     vector<int> lima_x(lima_n), lima_y(lima_n);
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_x[lima_i];
//     }
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_y[lima_i];
//     }
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         if (lima_x[lima_i] == 0) {
//             cout << 0 << " ";
//         } else {
//             cout << (lima_y[lima_i] * 100 / lima_x[lima_i]) << " ";
//         }
//     }
//     cout << endl;
//     return 0;
// }

// Pulando até o tesouro!
// #include <iostream>
// #include <vector>
// using namespace std;
// int main() {
//     int lima_n, lima_s;
//     cin >> lima_n;
//     vector<int> lima_a(lima_n);
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_a[lima_i];
//     }
//     cin >> lima_s;
//     int lima_count = 0;
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         if (lima_a[lima_i] <= lima_s) {
//             lima_count++;
//         } else {
//             break;
//         }
//     }
//     cout << lima_count << endl;
//     cout << (lima_count == lima_n ? 1 : 0) << endl;
//     return 0;
// }

// AVATAR: HABILIDADES DOS DOBRADORES
// #include <iostream>
// #include <vector>
// using namespace std;
// int main() {
//     int lima_n, lima_y;
//     cin >> lima_n;
//     vector<int> lima_e(lima_n), lima_x(lima_n);
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_e[lima_i];
//     }
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cin >> lima_x[lima_i];
//     }
//     cin >> lima_y;
//     bool lima_found = false;
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         if (lima_e[lima_i] == lima_y) {
//             if (lima_found) {
//                 cout << " ";
//             }
//             cout << lima_x[lima_i];
//             lima_found = true;
//         }
//     }
//     if (!lima_found) {
//         cout << "Nenhum";
//     }
//     cout << endl;
//     return 0;
// }

// A grande travessia
// #include <iostream>
// #include <vector>
// using namespace std;
// int main() {
//     int lima_s, lima_n;
//     cin >> lima_s >> lima_n;
//     vector<int> lima_pulos(lima_s);
//     vector<int> lima_pedras(lima_n, 0);
//     for (int lima_i = 0; lima_i < lima_s; ++lima_i) {
//         cin >> lima_pulos[lima_i];
//     }
//     for (int lima_i = 0; lima_i < lima_s; ++lima_i) {
//         int lima_pulo = lima_pulos[lima_i];
//         for (int lima_pos = 0; lima_pos < lima_n; lima_pos += lima_pulo) {
//             lima_pedras[lima_pos] = 1;
//         }
//     }
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         cout << lima_pedras[lima_i];
//         if (lima_i < lima_n - 1) cout << " ";
//     }
//     cout << endl;
//     return 0;
// }

// Em Busca das Esferas do Dragão
// #include <iostream>
// #include <set>
// #include <vector>
// #include <algorithm>
// using namespace std;
// int main() {
//     int lima_n;
//     cin >> lima_n;
//     set<int> lima_esferas;
//     vector<int> lima_encontradas;
//     for (int lima_i = 0; lima_i < lima_n; ++lima_i) {
//         int lima_e;
//         cin >> lima_e;
//         if (lima_e >= 1 && lima_e <= 7) {
//             lima_esferas.insert(lima_e);
//         }
//     }
//     for (int lima_j = 1; lima_j <= 7; ++lima_j) {
//         if (lima_esferas.count(lima_j)) {
//             lima_encontradas.push_back(lima_j);
//         }
//     }
//     for (int lima_k : lima_encontradas) {
//         cout << lima_k << " ";
//     }
//     cout << endl;
//     if (lima_encontradas.size() == 7) {
//         cout << "Saia Shenlong e realize o meu desejo" << endl;
//     } else {
//         cout << "Nao encontramos todas" << endl;
//     }
//     return 0;
// }


// blasphemous
// #include <iostream>
// #include <vector>
// using namespace std;
// int main() {
//     int lima_n, lima_m, lima_auxVida = 0;
//     cin >> lima_n;
//     vector<int> lima_x(lima_n);
//     for (int i = 0; i < lima_n; i++) {
//         cin >> lima_x[i];
//     }
//     cin >> lima_m;
//     lima_auxVida = lima_m;
//     for (int i = 0; i < lima_n; i++) {
//         if (lima_auxVida <= 0) {
//             break;
//         } else {
//             if (lima_x[i] == 1) {
//                 lima_auxVida = lima_m;
//             }
//             if (lima_x[i] > 1) {
//                 lima_auxVida -= lima_x[i];
//             }
//         }
//     }
//     if (lima_auxVida > 0) {
//         cout << "Yes, you can" << endl;
//     } else {
//         cout << "You Died" << endl;
//     }
//     return 0;
// }
// xeroque holmes
// #include <iostream>
// #include <vector>

// using namespace std;

// int main() {
//     int entrada = 6;
//     vector<int> count;
//     string lima_temp;

//     for (int lima_loop = 0; lima_loop < entrada; lima_loop++) {
//         cin >> lima_temp;
//         count.push_back(lima_temp.length());
//     }

//     for (int length : count) {
//         cout << length;
//     }
//     return 0;
// }
// inventario caotico
// #include <iostream>
// #include <string>

// int main() {
//     std::string frase, palavra;
//     int quantidade;

//     std::getline(std::cin, frase);
//     std::cin >> quantidade >> palavra;

//     std::string fraseSemEspaco = "";
//     for (char c : frase) {
//         if (c != ' ') {
//             fraseSemEspaco += c;
//         }
//     }

//     int contagem = 0;
//     for (int i = 0; i <= fraseSemEspaco.length() - palavra.length(); i += palavra.length()) {
//         if (fraseSemEspaco.substr(i, palavra.length()) == palavra) {
//             contagem++;
//         }
//     }

//     std::cout << contagem << std::endl;

//     if (contagem == quantidade) {
//         std::cout << "SIM!" << std::endl;
//     } else {
//         std::cout << "NAO!" << std::endl;
//     }

//     return 0;
// }

