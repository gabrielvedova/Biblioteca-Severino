#!/usr/bin/python3

loop = int(input())
dados = []
dadosfinal = []

for i in range(1, loop + 1):
    valor = input()
    dados.append(valor)
for i in dados:
    if len(i) == 1:
        dadosfinal.append(f'000{i}')
    elif len(i) == 2:
        dadosfinal.append(f'00{i}')
    elif len(i) == 3:
        dadosfinal.append(f'0{i}')

dadosfinal.sort()

for i in dadosfinal:
    print(i)
