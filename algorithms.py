# -*- coding: utf-8 -*-

def linear_search(arranjo, procurado):
    '''
    Realiza uma busca linear do valor procurado e retorna o indice.
    Caso não localize o valor procurado retorna -1.
    '''
    retorno = -1
    for i in range(len(arranjo)):
        if arranjo[i] == procurado:
            retorno = i

    return retorno

def better_linear_search(arranjo, procurado):
    '''
    Realiza uma busca linear otimizada do valor procurado e retorno o indice.
    Caso não localize o valor procurado retorna -1.
    '''
    for i in range(len(arranjo)):
        if arranjo[i] == procurado:
            return i

    return -1

def sentinel_linear_search(arranjo, procurado):
    '''
    Realiza uma busca linear sem necessitar verificar o fim do array porque
    utiliza um sentinela para a condição de parada do laço.
    Caso não localize retorna -1.
    '''
    n = len(arranjo) - 1
    ultimo = arranjo[n]
    arranjo[n] = procurado

    i = 0
    while arranjo[i] != procurado:
        i += 1

    arranjo[n] = ultimo
    if i < n or arranjo[n] == procurado:
        return i

    return -1

def binary_search(arranjo, procurado):
    '''
    '''
    p = 0
    r = len(arranjo) - 1
    while p <= r:
        q = (p + r)/2

        if arranjo[q] == procurado:
            return q
        elif arranjo[q] > procurado:
            r = q - 1
        else:
            p = q + 1

    return -1

def selection_sort(arranjo):
    '''
    '''
    for i in range(len(arranjo)):
        for j in range(i + 1, len(arranjo)):
            if arranjo[i] > arranjo[j]:
                arranjo[i], arranjo[j] = arranjo[j], arranjo[i]
    return arranjo

def bubble_sort(arranjo):
    '''
    Retorna uma lista ordenada de valores.
    Melhor O(n)
    Pior O(n^2)
    '''
    n = len(arranjo)

    for i in range(n):
        for j in range(i + 1, n):
            if arranjo[i] > arranjo[j]:
                arranjo[i], arranjo[j] = arranjo[j], arranjo[i]

    return arranjo

def insertion_sort(arranjo):
    '''
    '''
    n = len(arranjo)

    for indice in range(1, n):
        chave = arranjo[indice]
        j = indice - 1

        while j >= 0 and arranjo[j] > chave:
            arranjo[j + 1] = arranjo[j]
            j -= 1

        arranjo[j + 1] = chave
    return arranjo

def merge_sort(arranjo, p, r):
    '''
    Ordena o arranjo do menor para o maior.
    Pior e Mehor caso: 0(nlg n)
    Como é realizada diversas cópias de partes do vetor, esse algoritmo
    utiliza-se de mais memória em comparação com os outros algoritmos de ordenação.

    # CASO 1
    dados = [4]
    #n = sort(dados, 0, len(dados) - 1)

    # CASO 2
    dados = [4,2,1,5,3,7,6]
    #n = sort(dados, 0, len(dados) - 1)
    print(n)

    # CASO 3
    dados = [4,2,1,5,3,7,6,8]
    n = sort(dados, 0, len(dados) - 1)
    print(n)

    '''
    #print('Sub-vetor a ser ordenado: ' + str(arranjo[p:r+1]))

    if p >= r:
        return arranjo

    q = (p + r) / 2
    #print('esquerdo: ' + str(arranjo[p:q + 1]))
    merge_sort(arranjo, p, q)

    #print('direito: ' + str(arranjo[q + 1:r + 1]))
    merge_sort(arranjo, q + 1, r)

    return merge(arranjo, p, q , r)

def merge(arranjo, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    b = arranjo[p : q + 1]
    b.append(sys.maxint) # parada

    c = arranjo[q + 1 : r + 1]
    c.append(sys.maxint) # parada

    i = 0
    j = 0
    k = p

    while k <= r:
        if b[i] < c[j]:
            arranjo[k] = b[i]
            i += 1
        else:
            arranjo[k] = c[j]
            j += 1

        k += 1

    return arranjo

def quicksort(arranjo, p, r):
    if p >= r:
        return arranjo

    q = partition(arranjo, p, r)

    quicksort(arranjo, p, q - 1)
    quicksort(arranjo, q + 1, r)

    return arranjo

def partition(arranjo, p, r):
    q = p

    for u in range(p, r):
        if arranjo[u] <= arranjo[r]:
            arranjo[q], arranjo[u] = arranjo[u], arranjo[q]
            q += 1

    arranjo[q], arranjo[r] = arranjo[r], arranjo[q]

    return q

def count_keys_equal(arranjo, n, m):
    '''
    arranjo => Lista
    n => numero de elementos
    m =>

    lista = [1,1,0,1,1,0,0,0,1]
    count_keys_equal(lista, len(lista)-1, 2)
    '''
    equal = (m + 1) * [0] # because of the zero

    for i in range(n):
        key = arranjo[i]
        equal[key] += 1

    print 'equal: ' + str(equal)
    return equal

def count_keys_less(equal, m):
    '''
    '''
    less = [0] * m

    for j in range(m):
        if j > 0:
            less[j] = less[j - 1] + equal[j - 1]
        else:
            less[j] = less[j] + equal[j]

    print 'less: ' + str(less)
    return less
