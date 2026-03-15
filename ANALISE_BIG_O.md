# Analise de Complexidade Assintotica (Big-O)

## Exercicio 1
Complexidade: `O(1)`  
Justificativa: verifica se a lista esta vazia e acessa o primeiro elemento. Ambas operacoes sao constantes.

## Exercicio 2
Complexidade: `O(n)`  
Justificativa: percorre toda a lista uma unica vez e soma cada elemento.

## Exercicio 3
Complexidade: `O(log n)`  
Justificativa: a cada iteracao a busca binaria reduz o espaco de busca pela metade.

## Exercicio 4
Complexidade: `O(n^2)`  
Justificativa: dois loops aninhados testam combinacoes de pares da lista.

## Exercicio 5
Complexidade: `O(n^2)`  
Justificativa: bloco 1 custa `O(n)` e bloco 2 custa `O(n^2)`; domina o maior termo.

## Exercicio 6
Complexidade: `O(log n)`  
Justificativa: o valor de `i` dobra a cada repeticao ate atingir `n`.

## Exercicio 7
Complexidade: `O(2^n)`  
Justificativa: a recursao ramifica em duas chamadas e recomputa subproblemas.

## Exercicio 8
Complexidade: `O(n^2)`  
Justificativa: bubble sort faz comparacoes com dois loops aninhados no pior caso.

## Exercicio 9
Complexidade: `O(n^3)`  
Justificativa: multiplicacao de matrizes quadradas com tres loops aninhados.

## Exercicio 10
Complexidade: `O(n log n)`  
Justificativa: divide em metades (`log n` niveis) e intercala todos os elementos por nivel (`n`).
