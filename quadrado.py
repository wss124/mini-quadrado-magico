import itertools

# Função para verificar se uma matriz 3x3 é um quadrado mágico
def eh_quadrado_magico(matriz):
    soma_ideal = 15
    
    # Verifica linhas
    for linha in matriz:
        if sum(linha) != soma_ideal:
            return False
    
    # Verifica colunas
    for col in range(3):
        if sum(matriz[row][col] for row in range(3)) != soma_ideal:
            return False
    
    # Verifica diagonais
    if sum(matriz[i][i] for i in range(3)) != soma_ideal:
        return False
    if sum(matriz[i][2 - i] for i in range(3)) != soma_ideal:
        return False

    return True


# Função para gerar quadrados mágicos utilizando backtracking
def gerar_quadrado_magico():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for perm in itertools.permutations(numeros):
        matriz = [
            [perm[0], perm[1], perm[2]],
            [perm[3], perm[4], perm[5]],
            [perm[6], perm[7], perm[8]]
        ]
        if eh_quadrado_magico(matriz):
            return matriz  # Retorna a primeira solução encontrada


# Exibir o quadrado mágico encontrado
def imprimir_quadrado(matriz):
    print("\nQuadrado Mágico Encontrado:")
    for linha in matriz:
        print(linha)


if __name__ == "__main__":
    resultado = gerar_quadrado_magico()
    imprimir_quadrado(resultado)
