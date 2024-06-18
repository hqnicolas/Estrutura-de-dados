· SITUAÇÃO PROBLEMA

1 - Uma pequena Empresa Transportadora da região Sudeste de Santa Catarina, envia diariamente seu caminhão para 08 cidades para fazer as entregas.

A rota de cidades visitadas pelo caminhão muda de acordo com o destino das entregas a serem feitas. Sabendo-se antecipadamente por quantas cidades é necessário passar, o administrador da empresa consegue planejar um itinerário (rota) que o caminhão deverá seguir para fazer as entregas.

No entanto, para algumas cidades de destino, existem múltiplos caminhos de acesso a elas. Isso significa que, nem todo itinerário planejado garantirá os menores caminhos a serem percorridos. Logo, é possível que um planejamento inadequado possa implicar em maiores distâncias percorridas, maior tempo entre as entregas e maior consumo de combustível. Isto evidencia maior custo no serviço de entregas e consequentemente, redução na margem de lucros da empresa.

O modelo deste problema pode ser observado no Grafo ilustrado na Figura 01, onde alguns nós possuem múltiplos caminhos (arestas) de acesso:

· MODELO DE PROBLEMA

2 - Este problema pode ser modelado como um Problema do Caminho Mínimo, que é um problema clássico da teoria dos grafos. O objetivo é encontrar o caminho que minimize a distância total percorrida, considerando as restrições e múltiplos caminhos entre as cidades.

· ABORDAGEM

3 - Uma abordagem para resolver esse problema é utilizar algoritmos de otimização, como o Algoritmo do Caminho Mínimo ou o Algoritmo de Estrela A. Esses algoritmos podem ser implementados utilizando em Python.

Este problema envolve a otimização de um caminho para ser seguido por um caminhão que visita várias cidades para fazer entregas. O objetivo é encontrar o caminho que minimize a distância total percorrida, ou seja, o caminho que esteja mais próximo do caminho ideal.

Para solucionar esse problema, podemos usar uma árvore binária de pesquisa, que é uma estrutura de dados que permite encontrar rapidamente um elemento mínimo ou máximo em um conjunto de elementos. Em nosso caso, o elemento será a cidade de destino, e o conjunto de elementos será o ponto de partida (São Joaquim) e os pontos intermediários que já foram visitados pelo caminhão.

A árvore binária de pesquisa começa na raiz da árvore, que representa o ponto de partida e cada nó interno da árvore tem um elemento que é uma cidade intermediária visitada pelo caminhão, e dois filhos que são as cidades próximas a serem visitadas.

Cada nó externo da árvore tem um elemento que é uma cidade de destino que ainda não foi visitada, e um apontador para o nó interno que é o caminho mais curto para chegar a essa cidade.

A função de avaliação do nó é a distância entre o elemento do nó e o elemento do apontador. O nó com a função de avaliação mais baixa no caminho de pesquisa é expandido, ou seja, seu filho é adicionado ao caminho de saída.
