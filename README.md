# testes_de_software

Desafios de testes de software usando pytest (Python).

## Como instalar

```
pip install pytest
```

## Como rodar

Entre na pasta do desafio e rode:

```
pytest
```

## Lista 1

### Desafio 1 - Par ou ímpar

Função simples que diz se um número é par ou ímpar.

### Desafio 2 - Situação do aluno pela nota

Função que classifica a nota do aluno em reprovado, recuperação ou aprovado,
com testes nos limites de cada faixa (boundary value analysis).

### Desafio 3 - Testando erros e exceções

Função de saque de conta bancária que lança erro quando o valor é inválido
ou maior que o saldo. Testa o caminho feliz e os casos de exceção com
`pytest.raises`.

### Desafio 4 - Muitos casos com testes parametrizados

Função que valida se uma senha é forte, testada com `@pytest.mark.parametrize`
cobrindo vários casos de uma vez. Também mostra um caso que passa no teste
mas ainda representa uma senha fraca na prática.

### Desafio 5 - Isolando dependências com test doubles

Função que calcula o total de um carrinho consultando um serviço de preços
externo, recebido por injeção de dependência. O teste substitui esse serviço
por um mock, usando uma fixture para o setup compartilhado.

## Lista 2

### Desafio 1 - Conversor de números romanos

Função que converte um número inteiro (1 a 3999) em algarismos romanos.

### Desafio 2 - Calculadora de strings

Função que soma números passados em uma string separados por vírgula.

### Desafio 3 - Calculadora em notação polonesa reversa (RPN)

Calculadora que avalia expressões RPN usando uma pilha.

### Desafio 4 - Placar de boliche

Função que calcula a pontuação de uma partida de boliche a partir das
jogadas.

### Desafio 5 - Jogo da velha: quem venceu?

Função que recebe o tabuleiro (lista de listas 3x3) e diz se venceu o X, o
O, se deu empate ou se o jogo está em andamento.
