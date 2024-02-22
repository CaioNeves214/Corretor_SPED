# BIBLIOTECAS
import os
from tkinter import filedialog as fd
import math
import requests

# DEFINIR VARIAVEIS E ABRIR ARQUIVO FISCAL SELECIONADO
# caminho = fd.askopenfilename()
with open('C:/Users/acer003/Documents/GitHub/New-Project/SPED FISCAL BARRACA AMARELA JANEIRO.txt', 'r') as sped:
    consulta_cnpj_url = 'https://api-publica.speedio.com.br/buscarcnpj?cnpj='
    os.system('cls')
    nova_linha = ''
    lista = []
    ler = sped.readlines()
    for i in ler:

        # EMITENTES
        if i.startswith('|0150|'):
            linha = i.split('|')
            cnpj = linha[5].split()
            nome = linha[3]
            insc_estadual = linha[7].split()        
            cod_estadual = linha[8].split()   
            for cont in insc_estadual:
                lista_num = list(cont)      
            for cont1 in cod_estadual:
                lista_num1 = list(cont1)
            
            if nome == '':
                resposta_api = requests.get(consulta_cnpj_url+str(cnpj))
                if resposta_api.status_code == 200:
                    dados = resposta_api.json()
                    # dados = "{'NOME FANTASIA': '', 'RAZAO SOCIAL': 'JOAO ALVES -DOCES SANTA ELIZA', 'CNPJ': '19127802000195', 'STATUS': 'ATIVA', 'SETOR': 'Comercio Por Atacado', 'CNAE PRINCIPAL DESCRICAO': 'Fabricação de laticínios', 'CNAE PRINCIPAL CODIGO': '1052000', 'CEP': '37273000', 'DATA ABERTURA': '05/12/1972', 'DDD': '35', 'TELEFONE': '97430000', 'EMAIL': 'joaoalvesjr03@gmail.com', 'TIPO LOGRADOURO': 'RUA', 'LOGRADOURO': 'ARLINDO ALVES', 'NUMERO': 'SN', 'COMPLEMENTO': '', 'BAIRRO': 'CENTRO', 'MUNICIPIO': 'Aguanil', 'UF': 'MG'}"
                    format_nome = str(dados['RAZAO SOCIAL'])
                    novo_nome = format_nome.strip('-')                                
                            
            if cont1[0:1] != '31':
                lista_num = ''           
            if len(lista_num) != 13:
                lista_num = ''
                                                     
            linha[7] = ''.join(lista_num)
            if nome == '':
                linha[3] = ''.join(novo_nome)
            nova_linha = '|'.join(linha)
        
        # PRODUTOS
        if i.startswith('|0200|'):
            linha = i.split('|')
            produto = linha[3].split()
            try:
                c1 = produto.count('-')
                if c1 >= 1:
                    for a in range(0,c1):
                        position = produto.index('-')
                        produto.pop(position)
                        
                c2 = produto.count('.')
                if c2 >= 1:
                    for a in range(0,c2):
                        position = produto.index('.')
                        produto.pop(position)
                        
                c3 = produto.count('*')
                if c3 >= 1:
                    for a in range(0,c3):
                        position = produto.index('*')
                        produto.pop(position)
                        
                c4 = produto.count('%')
                if c4 >= 1:
                    for a in range(0,c4):
                        position = produto.index('%')
                        produto.pop(position)                
            except:
                pass
            linha[3] = ' '.join(produto)
            nova_linha = '|'.join(linha)
        
        # NOTAS (ENTRADA)    
        if i.startswith('|C100|0'):
            linha = i.split('|')
            linha[6] = '08'
            nova_linha = "|".join(linha)
            
        # PRODUTOS DE NOTAS
        if i.startswith('|C170|'):
            linha = i.split('|')
            produto = linha[4].split()
            try:
                c1 = produto.count('-')
                if c1 >= 1:
                    for a in range(0,c1):
                        position = produto.index('-')
                        produto.pop(position)
                        
                c2 = produto.count('.')
                if c2 >= 1:
                    for a in range(0,c2):
                        position = produto.index('.')
                        produto.pop(position)
                        
                c3 = produto.count('*')
                if c3 >= 1:
                    for a in range(0,c3):
                        position = produto.index('*')
                        produto.pop(position)
                        
                c4 = produto.count('%')
                if c4 >= 1:
                    for a in range(0,c4):
                        position = produto.index('%')
                        produto.pop(position)                
            except:
                pass
            linha[4] = ' '.join(produto)
            nova_linha = '|'.join(linha)

        # ADICIONAR LINHA MODIFICADA AO ARQUIVO
        if nova_linha != '':    
            lista.append(nova_linha)
            nova_linha = ''
        else:
            lista.append(i)
    sped_str = ''.join(lista)
    
    # SALVAR ARQUIVO NO LOCAL SELECIONADO
    files = [('Escrituração Fiscal', '*.txt')]
    sped_novo = fd.asksaveasfile(defaultextension='.txt', mode="w", filetypes=files)
    sped_novo.write(sped_str)

