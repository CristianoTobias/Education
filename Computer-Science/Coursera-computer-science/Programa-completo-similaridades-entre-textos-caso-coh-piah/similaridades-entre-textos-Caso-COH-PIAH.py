import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))


    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []


    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
        '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
        similaridade = []
        for item in as_a:
            sum = 0
            for i in range(len(item)):
                sum += abs(item[i] - as_b[i])
            similaridade.append(sum / 6)
        return  similaridade

def calcula_assinatura(textos):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = []
    frases = []
    palavras = []
    tamanho_medio_sentenca = []
    numeros_caracters_sentenca = []
    tamanho_medio_frase = []
    num_total_frases = []
    num_total_sentencas = []
    complexidade_sentencas = []
    tamanho_medio_palavras = []
    soma_tamanho_palavras = []
    numero_total_palavras = []
    relacao_type_token = []
    numero_palavras_diferentes = []
    razao_hapax_legoma = []
    palavras_unica_vez = []
    assinatura = []

    for texto in textos:
        temp = separa_sentencas(texto).copy()
        sentencas.append(separa_sentencas(texto))
        temp1 = []
        temp3 = []
        for sentenca in temp:
            temp1 += separa_frases(sentenca)
        frases.append(temp1)
        temp2 = temp1.copy()
        for frase in temp2:
            temp3 += separa_palavras(frase)
        palavras.append(temp3)
    for frase in frases:
        sum = 0
        for item in frase:
            sum += len(item)
        if len(frase) != 0:
            tamanho_medio_frase.append(sum / len(frase))
            num_total_frases.append(len(frase))

    for sentenca in sentencas:
        num_total_sentencas.append(len(sentenca))
        sum = 0
        for item in sentenca:
            sum += len(item)
        numeros_caracters_sentenca.append(sum)

    if numeros_caracters_sentenca != 0:
        complexidade_sentencas = [num_total_frases[i] / num_total_sentencas[i] for i in range(len(sentencas))]

    for palavra in palavras:
        sum = 0
        numero_palavras_diferentes.append(n_palavras_diferentes(palavra))
        palavras_unica_vez.append(n_palavras_unicas(palavra))
        for item in palavra:
            sum += len(item)
        soma_tamanho_palavras.append(sum)
        numero_total_palavras.append(len(palavra))
    if numero_total_palavras != 0:
        tamanho_medio_palavras = [soma_tamanho_palavras[i] / numero_total_palavras[i] for i in
                             range(len(sentencas))]
        relacao_type_token = [numero_palavras_diferentes[i] / numero_total_palavras[i] for i in
                          range(len(sentencas))]
        razao_hapax_legoma = [palavras_unica_vez[i] / numero_total_palavras[i] for i in range(len(sentencas))]
    if num_total_sentencas != 0:
        tamanho_medio_sentenca = [numeros_caracters_sentenca[i] / num_total_sentencas[i] for i in range(len(sentencas))]
    for item in range(len(sentencas)):
        temp = ""
        temp = [tamanho_medio_palavras[item], relacao_type_token[item], razao_hapax_legoma[item], tamanho_medio_sentenca[item], complexidade_sentencas[item], tamanho_medio_frase[item]]
        assinatura.append(temp)
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    infectado = compara_assinatura(calcula_assinatura(textos), ass_cp)
    index = infectado.index(min(infectado))
    return index + 1


avalia_textos(le_textos(),  le_assinatura())


















