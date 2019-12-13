#####Capítulo 1#####
#No IDLE o que for escrito deve ser salvo antes de realizar a ação
#Atalho: control+S seguido de F5
#O F5 executa
# A primeira função mais utilizada é a função print
# Com ele iremos exibir algo na tela 
# O que for escrito deve estar entre parenteses
print(5)
print('Oi!')
#Variáveis receber atribuições
#Há 4 tipos de variáveis. As inteiras, as flot,as string e as lógicas 
#Cria variável do tipo inteiro
x = 1 # x recebe o 1
#Cria variável do tipo float
y = 3.13
#Cria variável do tipo string
#As strigs  devem estar entre aspas simples ou duplas
m = "Python"
m = 'Python'
#Cria variável do tipo lógica
w = True  
y = False
print(y)
# As variáveis podem receber novos valores
x=1
print(x)
x=4
print(x)
#Elas são usadas para facilitar a atribuição de um valor
salário=1500
aumento=5
print(salário+(salário*aumento/100))
# Se o salário for alterado será obtido um novo resultado
#Exercícios do capítulo 1
#Um programa para exibir o nome na tela
print(input('Qual seu nome:'))#ou
print('Karen')
#Um programa que exiba o resultado de 2a*3b onde a=3 e b=5
a=3
b=5
print((2*a)*(3*b))
#Soma de 3 variáveis
print(a+b+x)
#Calcular o aumento de 15% no salário de 750
salário=750
aumento=15
print(salário+(salário*aumento/100))
#float é igual a inteiro
x=5.00
b=5
print(x==b)
###Capítulo 3###
#Operadores lógicos
#Usam uma variável lógica:True ou False
#3 tipos de operadores lógicos: not, and, or
#not é o oposto
print(not True)
print(not False)
#é o oposto, ou seje, not True é False e not False é True
#operador and
#Só é True: True and True
#As outras 3 combinações são False: False and False, True and False , False and True
print(True and True)
print(True and False)
#operador or
#só False or False será False
#as outras combinações serão True
print(False or False)
print(True or False)
#pode-se construir expressões lógicas com mais de um operador lógico
#a ordem de leitura dos operadores é: not-and-or
#Exemplo
salário=100
idade=20
salário>1000 and idade>18
100>1000 and 20>18
False and True
False
#Exercício: pessoa deve pagar imposto se o salário for maior que 1200,00
salário=1000
print(salário>1200)
salário=1500
print(salário>1200)
#Exercício: aluno é aprovador se tiver nota em todas as matérias maior que 7
matéria1=7
matéria2=8
matéria3=7
print(matéria1>7 and matéria2>7 and matéria3>7)
# a função len determina o tamanho da string
print(len('abc'))
print(len('introdução a pyhton'))
#para manipulação de string usa-se o []
a='abcde'
print(a[1])
# as strings começão a ser contadas do 0 por isso [1] for igual a 'b'
#para obter a letra 'a' é preciso usar o [0]
# sempre lembras de colocar a variável que se quer utilizar no parenteses
# é possível unir dus ou mais strings pela concatenação
print(a+'fgh')
#composição, é o mais abstrato e difícil de entender
x=15
'João tem %d anos' %x
print('João tem %d anos' %x)
#o %d é um marcador, indica a posição dentro da string onde teremos um valor inteiro
#há 3 marcador mais usados, %d=números inteiros, %s= strings, %f=números decimais
#o número entre o% e o 'd' indica quantos números irão aparecer quando a função print for execultada
idade=7
print('%d'%idade)
print('%02d'%idade)
print('%2d'%idade)
print('%-2d'%idade)
# o mesmo ocorre do o %f, só que ele possui números flutuantes após o '.'
valor=34.95
print('%f'%valor)
print('%2.2f'%valor)
#se o número antes do '.' por mais q o número real será adicionado um espaso antes assim como no %d
print('%14.2f'%valor)
#é possível fazer a composição de vários marcadores
nome='Pedro'
idade=35
dinheiro=1050.59
print('%s tem %d anos e R$%4.2f no banco.'%(nome, idade, dinheiro))
# fatiamento de strings
a='abcde'
print(a[0:2])
print(a[:2])
print(a[2:])
#sequência de tempo os valores vão se adicionando
divida=0
compra=100
divida=divida+compra
compra=200
divida=divida+compra
print(divida)
#entrada de dados fornacido pelo usuário a partir da função input, 'in put' como 'colocar dentro' 
x=input('Digite um número:')
print(x)
# o input pode ser controlado como string
nome=input('Digite seu nome:')
print('Você digitou %s' %nome)
print('Olá %s!'%nome)
# a entrada do input é como string para transformar em um número usamos a função int
# a função int converte a string que possui um valor em um número inteiro
# a função float converte a string em um número decimal ou flutuante
anos=int(input('Anos de serviço:'))
valor_ano=float(input('Valor por ano:'))
bonus=anos*valor_ano
print('Bônus de R$%5.2f bônus'%bonus)
#Exercícios
#Pedir 2 números interios e imprimir a soma dos dois
numero1=int(input('Digite um número:'))
numero2=int(input('Digite outro número:'))
soma=numero1+numero2
print('A soma dos números é : %d'%soma)
#Converter um valor em metros em centimetros
metros=float(input('Digite um valor em metros:'))
centimetros=metros*1000
print('O valor em %1.2f metros são %4.2f centimetros' %(metros, centimetros))
#Um programa que leia dias, horas, minutos e segundos e os converta em segundos
horas=int(input('Digite o quantas horas:'))
minutos=int(input('Digite o quantos minutos:'))
segundos=int(input('Digite o quantos segundos:'))
soma_segundos=((horas*3600)+ (minutos*60)+ segundos)
print('%d horas %d minutos e %d segundos são %d segundos'%(horas, minutos, segundos, soma_segundos))
#calcular o aumento de salario, deve pedir o valor do salario a porcentagem do aumento e exibir o valor do aumento e o novo salario
salário=float(input('Digite seu salário:'))
aumento=float(input('Digite a porcentagem do aumento:'))
valor_aumento=salário*(aumento/100)
salário=salário+valor_aumento
print('O valor do aumento é %5.2f e seu novo salário é %5.2f.'%(valor_aumento, salário))
#calcular o desconto de uma mercadoria, deve pedir o preço da mercadoria o percentual de desconto e exibir o valor do desconto e o preço a pargar
mercadoria=float(input('Preço da mercadoria:'))
desconto=float(input('Valor do desconto:'))
valor_desconto=mercadoria*(desconto/100)
mercadoria=mercadoria-valor_desconto
print('O valor do desconto é %5.2f e o novo valor da mercadoria é %5.2f.'%(valor_desconto, mercadoria))
#calcular o tempo de uma viajem, pedir a distância a percorrer e a velocidade média
distância=float(input('Qual a distância a percorrer?'))
velocidade=float(input('Qual a velocidade média?'))
tempo=distância/velocidade
print('O tempo de viajem é de aproximadamente de %3.1f horas'%tempo)
celsius=float(input('Qual a temperatura?'))
fahrenheit=((9*celsius)/5)+32
print(' A temperatura em fahrenheit é de %2.2f graus.'%fahrenheit)
#calcular o preço a pagar pelo aluguel do carro
#perguntar km percorridos, quantos dias e o preço é R$60 por dia e R$0,15 por km
km=float(input('Quantos kilometros foram percorridos?'))
dia=int(input('Quantos dias o carro foi alugado?'))
preço=(km*0.15)+(dia*60)
print('O preço a pagar é de R$%5.2f.'%preço)
#calcular a redução do tempo de vida de um fumante
#quantos cigarros por dia e quantos anos, 10 minutos por cigarro 
cigarros=int(input('Quantos cigarros você fuma por dia?'))
anos=float(input('Quantos anos você fuma?'))
redução=((anos*365)*(cigarros*10))/60
print('A redução de %3.1f dias de vida'%redução)

###capítulo 4###
#condições: if, else e elif
#if é o mesmo que 'se'
#funciona assim: se a condição for verdadeira faça o seguinte
#modelo: if 'condição' ':'
a=int(input('Primeiro número:'))
b=int(input('Segundo número:'))
if a>b:
    print('O primeiro número é maior!')
if b>a:
    print('O segundo número é maior!')
# atenção aos ':' que vem depois da condição
# atenção que a linha seguida aos ':' está mais a direita que a linha anterior
idade=int(input('Qual a idade do seu carro?'))
if idade<=3:
    print('Seu carro é novo!')
if idade>3:
    print('Seu carro é velho!')
#programa que pergunte a velocidade do carro. Se passar dos 80km/h deve dizer que o usuário foi multado
#quando for multado o valor cobrado será de R$ 5 por km acima dos 80km/h
velocidade=int(input('Qual sua velocidade?'))
if velocidade>80:
    print('Você foi multado!')
if velocidade>80:
    print('Sua multa foi de R$%d'%((velocidade-80)*5))
#calculo do imposto de renda
salário=float(input('Digite o salário para calculo do imposto:'))
base=salário
imposto=0
if base>3000:
    imposto=imposto+((base-3000)*0.35)
    base=3000
if base>1000:
    imposto=imposto+((base-1000)*0.20)
print('Salário: R$%6.2f Imposto a pagar:R$%6.2f'%(salário, imposto))
#um programam que lê 3 números e imprima o maior e o menor
número1=int(input('Primeiro número:'))
número2=int(input('Segundo número:'))
número3=int(input('Terceiro número:'))
if número1>número2 and número1>número3:
    print(número1)
if número1<número2 and número1<número3:
    print(número1)
if número2>número1 and número2>número3:
    print(número2)
if número2<número1 and número2<número3:
    print(número2)  
if número3>número2 and número3>número1:
    print(número3)
if número3<número2 and número3<número1:
    print(número3)
#programa q pergunta o salário do funcionário e calcula o aumento
#salário>1250.00 aumento de 10% salário<=1250.00 aumento de 15%
salário=float(input('Qual seu salário?'))
if salário>1250.00:
    print('Seu aumento é de R$%5.4f'%(salário*0.10))
if salário<1250.00:
    print('Seu aumento é de R$%5.4f'%(salário*0.15))
#else é usado caso o resultado da primeira condição for falsa para não usar outro if
#usando o exeplo do carro
idade=int(input('Qual a idade do seu carro?'))
if idade<=3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
#um programa que pergunta a distância que o passageiro deseja percorrer em km
#o preço da passagem para viajens até 200km é de R$0,50 por km e R$0,45 para viajens mais longas
distância=int(input('Qual distãncia você deseja percorrer?'))
if distância>200:
    print('Preço a pagar é de R$%5.2f.'%(distância*0.50))
else:
    print('Preço a pagar é de R$%5.2f.'%(distância*0.45))
#estruturas aninhadas, as vezes é preciso colocar um if dentro de outro if ou dentro de um else
#para isso eles devem ser posicionado mais a direita
minutos=int(input('Quantos minutos você utilizou este mês?'))
if minutos<200:
    preço=0.20
else:
    if minutos<400:
        preço=0.18
    else:
        preço=0.15
print('Você vai ter que pagar R$%6.2f esse mês'%(minutos*preço))
#Há exemplos em que se precisa fazer varias categorias uma dentro da outra
categoria=int(input('Digite a categoria do produto:'))
if categoria==1:
    preço=10
else:
    if categoria==2:
        preço=18
    else:
        if categoria==3:
            preço=23
        else:
            if categoria==4:
                preço=26
            else:
                if categoria==5:
                    preço=31
                else:
                    print('Categoria inválida, digite um valor entre 1 e 5!')
                    preço=0
print('O preço do produto é: R$%6.2f'%preço)
#em um problema com multiplos if aninhados. O elif substitui um par de else e if sem criar outro nível na estrutura
categoria=int(input('Digite a categoria do produto:'))
if categoria==1:
    preço=10
elif categoria==2:
    preço=18
elif categoria==3:
    preço=23
elif categoria==4:
    preço=26
elif categoria==5:
    preço=31
else:
    print('Categoria inválida, digite um valor entre 1 e 5!')
    preço=0
print('O preço do produto é:R$%6.2f' %preço)
#um programa que leia dois números e pergunta qual operação deseja fazer
#pode ser soma, subtração, multiplicação ou divisão
numero1=int(input('Digite o primeiro número:'))
numero2=int(input('Digite o segundo número:'))
operação=(input('Qual operação deseja realizar?'))
if operação=='-':
    print(numero1-numero2)
elif operação=='+':
    print(numero1+numero2)
elif operação=='*':
    print(numero1*numero2)
elif operação=='/':
    print(numero1/numero2)
#um programa de emprestimo de uma casa
# o programa deve perguntar o valor da casa, o salario e a quantidade de anos a pagar
#a prestação não deve ser maior q 30% do salário
#o valor da prestação deve ser o valor da casa dividido pelo número de meses a pagar
casa=float(input('Qual o valor da casa?'))
salario=float(input('Qual o seu salário?'))
tempo=(int(input('Quantos anos a pagar?')))*12
prestação=casa/tempo
if prestação>(0.30*salario):
    print('Emprestimo negado')
else:
        print('Sua prestação será de R$%6.2f.'%prestação)
#um programa que calcule o preço a pagar pela energia elétrica
#pergunte a quantidade kWh consumida e e o tipo de instalação: R-residência, I-industria, C-comércio
energia=int(input('Qual a quantidade em kWh foi consumido? '))
instalação=input('Qual o tipo de instalação?')
if instalação=='R':
    if energia<500:
        print('O valor é de R$ 0,40.')
    else:
        print('O valor é de R$ 0,65.')
if instalação=='C':
    if energia<1000:
        print('O valor é de R$ 0,55.')
    else:
        print('O valor é de R$ 0,60.')
if instalação=='I':
    if energia<5000:
        print('O valor é de R$ 0,55.')
    else:
        print('O valor é de R$ 0,60.')
else:
    break
###Capítulo 5###
#Repetições são usadas para execultar a mesma parte de um programam várias vezes
#elas normalmente dependem de uma condição
#para fazer o print de 3 números em sequência pode-se fazer por várias formas
print(1)
print(2)
print(3)
#ou
x=1
print(x)
x=2
print(x)
x=3
print(x)
#ou
x=1
print(x)
x=x+1
print(x)
x=x+1
print(x)
# a função while repete um bloco enquanto a condição for verdadeira
# estrutura do while:
#while <condição>
#   bloco
#exemplo
x=1
while x<=3:
    print(x)
    x=x+1
# ele exibe de 1 até 3
# para exibir entre 50 e 100
# o programa não entende se for colocado 50<x>100
# para funcionar deve-se usar as condições
x=50
while x>=50 and x<=100:
    print(x)
    x=x+1
#para exibir da 10 a 0 em forma decrescente e ao final exibir 'Fogo' ao final
x=10
while x<=10:
    print(x)
    x=x-1
    if x==1:
        print('Fogo!')
# ou seja a condição while é seguida de uma condição q pode usar and,or,not
# após a condição usar os ':'
#o enter após os dois pontos é cabível um bloco com outras funções
#e o while segue até a condição não ser verdadeira
# para uma condição em que x>1 print(x) o programa vai execultar a função até um número muito grande
#o while tem diversas atribuições
# como contadores
# um exemplo em que o usuário digite o número limite
fim=int(input('Digite um número a imprimir'))
x=1
while x<=fim:
    print(x)
    x=x+1
    if x==fim:
        print('Fim')
#na função while escrita anteriormente o x seve como um contador, ou seja, a variável é usada para contar o número de ocorrências de um evento
#se for utilizado o número 0 como resultado do input, 1<=0 que é falso logo o bloco não irá se repetir
#para imprimir os números pares entre 0 e um número digitado pelo usuário
fim=int(input('Digite o últimp número a imprimir:'))
x=0
while x<=fim:
    if x%2==0:
        print(x)
    x=x+1
# a função '%' é que o resulta de uma divisão, ou seja, 5%2=1
# para realizar a mesma função sem o if pode-se adicionar o 2 a todos os números o que os torna par
fim=int(input('Digite um número:'))
x=0
while x<=fim:
    print(x)
    x=x+2
#imprimir do 1 até o número digitado, mas apenas os ímpares
fim=int(input('Digite um número:'))
x=1
while x<=fim:
    print(x)
    x=x+2
#imprimir os 10 primeiros mútiplos de 3
x=1
y=1
while x>=0 and y<=10:
	print(x)
	y=y+1
	x=y*3
#uma tabuada simple de n+1,n+2,n+3...
n=int(input('Tabuada de:'))#n é o número fornecido pelo usuário
x=1
while x<=10:#como a adição de um número vai até o 10 ñ pode passar de 10
    print(n+x)# número fornecido +x que varia de 1 a 10
    x=x+1
#tabuada de multiplicação
n=int(input('Tabuada de:'))
x=1
while x<=10:
    print(n*x)
    x=x+1
#uma tabuada que o usuario indique o inicio e o fim
n=int(input('tabuada de:'))
inicio=int(input('digite o inicio de tabuada:'))
fim=int(input('digite o fim da tabuada:'))
x=inicio
while x>=inicio and x<=fim:
	print(n*x)
	x=x+1
#uma tabuada que multiplique 2 numeros fornecidos pelo usuario mas que utiize apenas soma e subtração
#ex:4*5=5+5+5+5=4+4+4+4+4
p=int(input('Digite o primeiro número'))
s=int(input('Digite o segundo número'))
x=1
r=0
while y<=s:
    r=r+p
    x=x-1
    print('%d*%d=%d'%(p,s,r))
#assim como a multiplicação é possivel fazer
dividendo=int(input('Dividendo;'))
divisor=int(input('Divisor:'))
quociente=0
x=dividendo
while x>=divisor:
	x=x-divisor
	quociente=quociente+1
	resto=x
	print('%d/%d=%d (quociente) %d(resto)'%(dividendo, divisor, quociente, resto))
# o python pode ser usado para contagem de questões corretas
#exemplo:
pontos=0
questão=1
while questão<=3:
    resposta=input('Resposta da questão %d:'%questão)
    if questão==1 and resposta=='b':
     pontos=pontos+1 # deve ter um espaço para o começo dessa linha 
    if questão==2 and resposta=='c':
     pontos=pontos+1
    if questão==3 and resposta=='d':
     pontos=pontos+1
    questão+=1    # se não colocar esse comando sempre será a questão 1 e todas as alternativas serão corretas
    print('O aluno fez %d pontos'%pontos)
# o python há diferença entre as letra maiusculas e minisculas, ou seja, 'a' é diferente de 'A'
# para que a questão assuma tanto letras maiusculas quanto minusculas ela deve assumir as duas alternativas
pontos=0
questão=1
while questão<=3:
    resposta=input('Resposta da questão %d:'%questão)
    if questão==1 and resposta=='b'or resposta=='B':
     pontos=pontos+1 
    if questão==2 and resposta=='c' or resposta=='C':
     pontos=pontos+1
    if questão==3 and resposta=='d'or resposta=='D':
     pontos=pontos+1
    questão+=1    
    print('O aluno fez %d pontos'%pontos)
#acumuladores
#os contadores utilizam 1 variavel já os acumuladores podem ser usados 2 variáveis    
#soma de números fornecidos pelo usuario
n=1
soma=0
while n<=10:
    x=int(input('Digite o número %d:'%n))
    soma=soma+x # um acumulador com duas variáveis
    n=n+1 # um contador
    print('Soma:%d'%soma)
# tambem pode ser usado para calculo de média 
x=1
soma=0
while x<=5:
    n=int(input('Digite o número %d:'%x))
    soma=soma+n
    x=x+1
    print('Média:%5.2f'%(soma/5))
#exercío: um programa que pergunte o deposito inicial e a taxa de juros de uma poupança e exiba os valores 24 meses com o total ganho com juros
x=1
soma=0
inicial=int(input('Deposito inicial'))
juros=float(input('Juros por mês'))
while x<=24:
    soma=soma+(inicial*juros)
    x=x+1
    print('Ganho %5.2f'%soma)
    
#um programa semelhante ao anterior mas deve perguntar tambem o valor depositado mensalmente
x=1
soma=0
inicial=int(input('Deposito inicial'))
juros=float(input('Juros por mês'))
while x<=24:
    mes=int(input('Valor dos depositos mensais'))
    soma=soma+(mes*juros)+(inicial*juros)
    x=x+1
    print('Ganho %5.2f'%soma)
    
#programa  que pergunte o valor da dívida o juros mensal e o valor mensal que ser pago 
# em quantos meses a divida será paga o total pago e o total de juros pago
divida=float(input('Dívida:'))
taxa=float(input('Juros:'))
pagamento=float(input('Pagamento mensal:'))
saldo=divida
jtotal=0
tempo=0
while saldo>pagamento:
        juros=saldo*taxa/100
        saldo=saldo+juros-pagamento
        jtotal=jtotal + juros
        print('Saldo da divida do mês %d é de R$%6.2f.'%(tempo, saldo))
        tempo+=1 #o tempo será acrecido de 1 em 1 
#para interromper uma repetição é possíveç usar a função break
#exemplo
s=0 
while True: # o while vai funcionar em loop até o comendo de saida 
    v=int(input('Digite um número ou 0 pra sair:'))
    if v==0:
        break # na situação em que o 0 for digitado  o programa vai parar de ser execultado
    else:
        s=s+v
        print(s)
#exercicios
#um programa que leia numeros inteiros até o usuário digitar 0 e depois exiba a quantidade de números digitados assim como a soma e a média
x=0
soma=0
quantidade=0
while True:
    numero=int(input('Digite um número ou 0 para parar:'))
    if numero==0:
        break
    else:
        soma=soma + numero
        quantidade+=1
print('Foram digitados %d números, cuja a soma é %d e a média é de %5.2f'%(quantidade,soma,(soma/quantidade)))
#uma pequena máquina registradora que solicite o código do produto e a quantidade
while True:
    codigo=int(input('Digite o código do produto ou 0 para para:'))
    if codigo==1:
        quantidade=int(input('Qual a quantidade do produto?'))
        preço1=quantidade*0.5
    elif codigo==2:
        quantidade=int(input('Qual a quantidade do produto?'))
        preço2=quantidade*1
    elif codigo==3:
        quantidade=int(input('Qual a quantidade do produto?'))
        preço3=quantidade*4
    elif codigo==4:
        quantidade=int(input('Qual a quantidade do produto?'))
        preço4=quantidade*7
    elif codigo==5:
        quantidade=int(input('Qual a quantidade do produto?'))
        preço5=quantidade*8
    elif codigo==0:
        break
    else:
        print('Código inválido')
print('O preço total foi de R$%5.2f'%(preço1+preço2+preço3+preço4+preço5))
#listagem para a contagem de cédulas
valor=int(input('Digite o valor a pagar:'))
cedula=0
atual=50
apagar=valor
while True:
    if atual<=apagar:
        apagar-=atual
        cedula+=1
    else:
        print('%d cédula(s) de R$%d'%(cedula,atual))
        if apagar==0:
            break
        if atual==50:#se substituir atual por apagar o programa vai dar erro em alguns valores 
            atual=20
        elif atual==20:
            atual=10
        elif atual==10:
            atual=5
        elif atual==5:
            atual=1
        cedula=0
#para parar o programa quando ele estiver em um loop infinito é só clicar CONTROL+C        
# exercicios
#para que o programa tambem trabalhe om notas de 100
valor=int(input('Digite o valor a pagar:'))
cedula=0
atual=100
apagar=valor
while True:
    if atual<=apagar:
        apagar-=atual
        cedula+=1
    else:
        print('%d cÃ©dula(s) de R$%d'%(cedula,atual))
        if apagar==0:
            break
        if atual==100:
            atual=50
        elif atual==50:
            atual=20
        elif atual==20:
            atual=10
        elif atual==10:
            atual=5
        elif atual==5:
            atual=1
        cedula=0
#para acrecentar valores decimais tambem
valor=float(input('Digite o valor a pagar:'))
cedula=0
atual=100
apagar=valor
while True:
    if atual<=apagar:
        apagar-=atual
        cedula+=1
    else:
        print('%d cÃ©dula(s) de R$%5.2f'%(cedula,atual))
        if apagar<0.01:# colocar esse break para valores menores que 0.01 pq se nao ele entre em loop
            break
        if atual==100:
            atual=50
        elif atual==50:
            atual=20
        elif atual==20:
            atual=10
        elif atual==10:
            atual=5
        elif atual==5:
            atual=1
        elif atual==1:
            atual=0.5
        elif atual==0.5:
            atual=0.10
        elif atual==0.10:
            atual=0.05
        elif atual==0.05:
            atual=0.02
        elif atual==0.02:
            atual=0.01
        cedula=0
#repetições alinhadas
#while dentro while
#exemplo
#tabuada de 1 a 10
tabuada=1 #começa com a tabuada de 1
while tabuada<=10: #vai até a tabuada de 10
    numero=1 #o primeiro numero será 1
    while numero<=10:#vai até o numero 10
        print('%d x %d = %d'%(tabuada,numero,(tabuada*numero)))
        numero+=1 # é igual a: numero=numero+1
    tabuada+=1
#exercicios
#fazer um programa que exiba um menu e imprima a operação até que  opção de saida seja escolhida
while True:# enquanto não selecionar o 5 irá apresentar o menu
    print('Menu') 
    print('1-Adição')
    print('2-Subtração')
    print('3-Multiplicação')
    print('4-Divisão')
    print('5-Sair')
    opçao=int(input('Escolha uma opção:'))
    if opçao==5:#para sair do primeiro while setado
            break
    elif opçao>=1 and opçao <5:
            n=int(input('Tabuada de:'))
            x=1
            while x<=10:#para parar quando x for maior que 10
                if opçao==1:
                    print('%d+%d=%d'%(n,x,(n+x)))
                elif opçao==2:
                     print('%d-%d=%d'%(n,x,(n-x)))
                elif opçao==3:
                     print('%dx%d=%d'%(n,x,(n*x)))
                elif opçao==4:
                     print('%d/%d=%d'%(n,x,(n/x)))
                x+=1# para que a tabuada de valores 1 a 10 seja relizada
    else:
        print('Opção inválida')
#um programa que leia um número e verifique se ele é primo ou não 
#tem que ser um número cujo resto da divisão por 2 não é 0
numero=int(input('Divite um número:'))
if not numero%2==0:
    print('Esse número é primo')
else:
    print('Esse número não é primo')
#um programa que imprima os primos anteriores a ele
numero=int(input('Divite um número:'))
while numero>=0:# tem que ser maior q 0 
    if not numero%2==0:
        print('Esse número é primo')
        print(numero)
        numero=numero-2
    else:
        print('Esse número não é primo')
#não fiz 2 dos ultimos exercicios o do palindromo e o da raiz quadrada
###Caítulo 6###
#listas
#listas representam o armazenamento de valores acessados por um indice
#podem ter vários tipos de estrutura na mesma lista (string, int,float) e até mesmo outra lista
#seu tamanho é igual a quantidades de elementos que ela tem 
# a primeira posição da lista é a 0 lista[0] é a primeira posição
#para criar uma lista usa-se os colchetes [] e uma igualdade
#as unidades da lista devem ser separadas por virgula
z=[15,8,9]
#para acessar um elemento da lista é só indicar a lista e a sua posição entre colchetes
z[1]
#para mudar um intem é só indicar a posição e colocar a igualdade
z[1]=90
print(z)
#programa para o calculo da média das notas de um aluno
notas=[6,7,5,8,9]
soma=0
x=0 
while x<5:# são 5 notas, outra forma de escrever é while x<len(notas) a função len dá o tamanho
    soma+=notas[x] #soma= soma+notas[posição da lista]
    x+=1 #vai aumentando as pocições da lista de notas e retorna o que está dentro da lista
print('Média:%5.2f'%(soma/x)) 
#para criar uma lista de notas com valores de input
notas=[0,0,0,0,0]#a lista com elementos=0 pois eles serão substituidos pelo input
soma=0
x=0#posição dos elementos da lista
while x<len(notas):#posição vai ser de 0 a 4 
    notas[x]=float(input('Nota %d:' %x))# input vai substituir o elemento na posição x da lista 
    soma+=notas[x]#acumunla a soma conforme as posições aumentam
    x+=1
x=0 # para imprimir a lista deve reiniciar o x para 0
while x<len(notas):
    print('Nota %d:%5.2f.'%(x,notas[x]))#deve ser a posição da nota não a lista 
    x+=1
print('Média é:%5.2f'%(soma/x))

#indice 
#deve pedir o input e armazenar na lista 
#quando soloicitado a posição, realizar o print do item correspondente
numeros=[0,0,0,0,0] #preparar lista para receber os inputs
x=0
while x<5:
    numeros[x]=float(input('Digite o número %d para a lista:'%(x+1)))# o x+1 foi usado pq a posição da lista começa em 0
    x+=1
while True:
    escolhido= int(input('Qual posição quer imprimir ou 0 para sair:'))
    if escolhido==0:
        break
    else:
        print('Você escolheu o número %d'%(numeros[escolhido-1]))
#cópia de lista
#quando temos duas listas e as igualamos(=) elas estão atribuidas uma a outra 
#quando fazemos a substituição em uma delas a outra é automaticamente alterada
#uma lista é objeto espelho da outra quando alteramos uma a outra tem a mesma referência
#para criar uma cópia independente colocamos o (:) na frente da nova cópia a é criado uma nova memória
#as listas podem ser selecionadas parecidos com funçoes semelhantes as strings
x=[1,2,3,4,5]
print(x[:2])#referentes aos numeros antes de posição
print(x[2:]) #referentes aos numeros depois da posição
#tamanho da lista 
#é usado a função len
print(len(x))
#repetição usado len
l=[3,7,8]
x=0
while x<len(l):#o limite de repetição é o tamanho da lista
    print(l[x])
    x+=1
#adição de elementos a uma lista
#usa-se a função append que é usada após o objeto com um ponto e o valor a ser adicionado fica entre parenteses
#objeto.append(novo valor)
#criação de uma lista com valores inputado
l=[]#lista vazia para a adição de elementos
while True:
    n=int(input('Adicione o valor a lista ou 0 para sair:'))
    if n==0:
        break
    l.append(n)#adiciona os valores até a parada do programa 
x=0
while x<len(l):#programa para montar a lista com os valores recem acessados
    print(l[x])
    x+=1
#outra forma de adicionar valores a lista é:
#l=l+[valor] um objeto com uma mais na frente 
#mas assim como a função append só pode ser adicionado uma valor por vez 
#se a função append for usada para adicionar mais de um valor ela vai gerar uma pequena lista
#ela transforma toda a pequena lista em um objeto e a insere
#para a adicionar mais de um valor a lista usa-se a função extend

l=[1]
l.append(7)# a função append só adiciona um objeto
l.extend([9,1,4])#se forem colocados mais de 2 numeros tem que colocar colchetes[]
print(l)
#exercicio 6.2
lista1=[]
while True:
    n1=int(input('Digite valor para a contrução da primeira lista ou 0 para sair:'))
    if n1==0:
        break
    lista1.append(n1)
print(lista1)
lista2=[]
while True:
    n2=int(input('Digite valor para a contrução da segunda lista ou 0 para sair:'))
    if n2==0:
        break
    lista2.append(n2)
print(lista2)
lista3=lista1[:]
lista3.extend(lista2)
print(lista3)
#exercicio 6.3
# um programa que percorra duas lista e gere uma terceira sem numero repetido
lista1=[]
while True:
    n1=int(input('Digite valor para a contrução da primeira lista ou 0 para sair:'))
    if n1==0:
        break
    lista1.append(n1)
print(lista1)
lista2=[]
while True:
    n2=int(input('Digite valor para a contrução da segunda lista ou 0 para sair:'))
    if n2==0:
        break
    lista2.append(n2)
print(lista2)
lista3=lista1[:]
lista3.extend(lista2)#junção das duas listas
lista4=[]#uma nova lista deve ser criada e nela serão adicionados os nunmeros não repetidos
x=0#posição inicial da lista 3
while x<len(lista3):#até a lista 3 acabar
    y=0#posição inicial da lista 4
    while y<len(lista4):
        if lista3[x]==lista4[y]:#se o número já estiver na lista quebra o loop e vai para o próximo item
            break
        y=y+1
    if y==len(lista4):
        lista4.append(lista3[x])
    x+=1
x=0
print(lista4)
#para remover elementos da lista
#usa-se a função del
#del lista[posição do elemento na lista]
#para remover uma fatia de uma lista usa-se a funçã del tambem
l=list(range(101))#ira criar uma lista com uma amplitude de 0 a 100
print(l)
del l[1:99]
print(l)
#usando lista como fila 
#em uma fila a inclusão é sempre realizada no fim e a remoção ocorre no inicio
#regra do first in first out 
#para que o elemento seja retirado sem ser excluido usa-se a função pop
#o pop retorma o valor do elemento depois o exclui
ultimo=10 #o ultimo elemento será o 10
fila=list(range(1,ultimo+1))#listagem da amplitude de 1 até o ultimo
while True:
    print('\n Existem %d clientes na fila'%len(fila))
    print('Fila atualf:',fila)
    print('Digite F para adicionar 1 cliente no fim da fila, ou A para realizar o atendimento, ou S para sair:')
    operaçao=input('Operação(F,A ou S)')
    if operaçao=='A':
        if (len(fila))>0:
            atendido=fila.pop(0)# o atendido vai ser extraido mas antes de ser extraido ele será apresentado
            print('Cliente %d atendido'%atendido)
        else:
            print('Fila vazia!Niguem para atender')
    elif operaçao=='F':
        ultimo+=1
        fila.append(ultimo)#acrescimo de mais um ao fim da fila
    elif operaçao=='S':
        break
    else:
        print('Operação invalida!Digite A,F ou S')
#listas tambem podem ser usadas como pilhe de pratos
#regra last in first out
#o ultimo a chegar é o primeiro a sair
pratos=10 #serão 10 pratos e o ultimo é o 10
pilha=list(range(1,pratos+1))#lista de amplitude do primeiro ao ultimo
while True:
    print('Existem %d pratos'%len(pilha))
    print('Digite E para empilhar um novo prato, ou D para desempilhar ou S para sair')
    operaçao=input('Digite a operação(D,E ou S):')
    if operaçao=='D':
        if (len(pilha))>0:
            lavado=pilha.pop(-1)#essa é a diferença entre lista em fila e a lista em pilha, pois será retirado o ultimo a ser colocado
            print('%d pratos lavados'%lavado)
        else:
            print('Pilha vazia')
    elif operaçao=='E':
        pratos+=1#novo prato adicionado
        pilha.append(pratos)
    elif operaçao=='S':
        break
    else: 
        print('Operação invalida')
#exercicio 6.7
#criar uma pilha para verificar se os parenteses foram abertos e fechados na ordem correta
parenteses=input('Indique a sequência de parenteses para ser verificado a ordem:')
x=0
pilha=[]#pilha usada para verificação
while x<len(parenteses):#verificação completa do input 
    if parenteses[x]=='(': # se tiver o parenteses aberto ele adiciona um item a pilha
        pilha.append(0)
    if parenteses[x]==')':# se tiver o parenteses fechado ele retira um item a pilha
        if len(pilha)>0: #apenas se a pilha já estive sido aberta
            pilha.pop(0)
        else:
            pilha.append(')')
            break
    x+=1
if len(pilha)==0:#adiciona e retira o mesmo valor igualmente logo a pilha estará vazia
    print('OK')
else:
    print('Erro!')
# é possível realizar pesquisas em determinada lista afim de verificar se o elemento está na lista
#para isso deve passar do primeiro ao ultimo item da lista e analisar se o correspondente está disponível
l=[15,7,27,39]#lista inicial a ser usada como banco
p=int(input('Digite o valor a procurar:'))#será o valor do input a ser procurado na lista fornecida
achou=False #essa booleana é usada para verificar se saiu da repetição porque já achou oq estava procurando ou se já percorreu todos os elementos e não achou
x=0#posição inicial da lista
while x<len(l):#procurar por todos os elementos da lista
    if l[x]==p:
        achou=True #o achou só será verdadeiro se o elemento procurado for igual ao encontrado
        break
    x+=1
if achou:#verifica o achou para ver oque vei ser impresso
    print('%d achado na posição %d'%(p,x))#pode ser x+1 pois a lista se inicia pelo posição 0
else:
    print('%d não encontrado'%p)
#exercicio 6.8
# realizar a procura sem a variavel achou
l=[15,7,27,39]
p=int(input('Digite o valor a procurar:'))
x=0
while x<len(l):
    if l[x]==p:
        break
    x+=1
if x<len(l): #a dica dizia para verificar a consição de saida do while logo a codição do if = a do while
    print('%d achado na posição %d'%(p,x))
else:
    print('%d não encontrado'%p)
#exercicio 6.9 e 6.10
# realizar a procura com dois valores e indicar qual foi encontrado primeiro
l=[15,7,27,39,56,34,98,76,4,1,35]
p=int(input('Digite o valor a procurar:'))
v=int(input('Digite outro valor a procurar:'))
achoup=False
achouv=False
x=0
y=0
while x<len(l):
    if l[x]==p:
        achoup=True
        break
    x+=1
while y<len(l):
    if l[y]==v:
        achouv=True
        break
    y+=1
if achoup and achouv and x<y: 
    print('%d achado na posição %d foi encontrado primeiro e %d foi encontrado depois na posição %d.'%(p,x,v,y))
elif achouv and y<x:
    print('%d achado na posição %d foi encontrado primeiro e %d foi encontrado depois na posição %d.'%(v,y,p,x))
else:
    print('%d e %d não encontrado'%(p,v))
        
