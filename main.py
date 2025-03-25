def selecao_maxmin(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    meio = len(arr) // 2

    menor_esq, maior_esq = selecao_maxmin(arr[:meio])
    menor_dir, maior_dir = selecao_maxmin(arr[meio:])

    menor_total = min(menor_esq, menor_dir)
    maior_total = max(maior_esq, maior_dir)

    return menor_total, maior_total

