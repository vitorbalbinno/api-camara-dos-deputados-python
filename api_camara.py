import requests
import pandas as pd

id_candidato = int(input('Digite o ID do candidato: '))
ano = int(input('Digite o ano: '))

headers = {'accept': 'application/json'}
url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_candidato}/despesas'
params = {'ano': ano, 'itens': 50, 'pagina': 1}

despesas = []

while True:
    dados = requests.get(url, headers=headers, params=params).json()['dados']
    if not dados:
        break
    despesas.extend(dados)
    params['pagina'] += 1

dicionario = {}
for despesa in despesas:
    if despesa['tipoDespesa'] not in dicionario:
        dicionario[despesa['tipoDespesa']] = 0
    dicionario[despesa['tipoDespesa']] += despesa['valorDocumento']

print(f'\n{"TIPO DE DESPESA".ljust(70)}\tTOTAL\n')
for tipo, valor in dicionario.items():
    print(f'{tipo.ljust(71)}\tR$ {valor:.2f}'.replace('.', ','))
print(f'--' * 36)
print(f'{"VALOR TOTAL:".ljust(71)} R$ {sum(dicionario.values())}')
