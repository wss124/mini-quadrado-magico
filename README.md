# 🔢 Quadrado Mágico 3x3 - Algoritmo em Python

## 📜 Descrição

Este projeto implementa um algoritmo em Python para gerar um **Quadrado Mágico 3x3** utilizando **backtracking por meio de permutações**.

Um **Quadrado Mágico 3x3** é uma matriz que usa os números de **1 a 9 sem repetir**, onde a soma de cada **linha, coluna e das duas diagonais** é sempre igual a **15**.

---

## 🚀 Como Funciona

O código realiza as seguintes etapas:

1. **Gera todas as permutações possíveis dos números de 1 a 9** usando a função `itertools.permutations`.
   
2. Para cada permutação, ele monta uma matriz 3x3.

3. Verifica se a soma das **linhas, colunas e diagonais** é igual a 15 utilizando a função `eh_quadrado_magico()`.

4. Ao encontrar a **primeira solução válida**, o código imprime a matriz correspondente como quadrado mágico.

---

## 🔧 Funcionalidades do Código

### ✔️ Funções Principais:

- **`eh_quadrado_magico(matriz)`**
  - Verifica se uma matriz 3x3 atende às condições de um quadrado mágico.
  - Checa a soma de linhas, colunas e diagonais.

- **`gerar_quadrado_magico()`**
  - Gera permutações dos números de 1 a 9.
  - Retorna o **primeiro quadrado mágico válido** encontrado.

- **`imprimir_quadrado(matriz)`**
  - Exibe a matriz formatada no terminal.
