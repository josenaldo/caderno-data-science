# Plano de estudo: Formação Python - Fase 2

Plano de estudo e registro da Fase 2 do Curso Formação Python, na Alura. Essa fase não consta, na Alura, como uma formação. Eu que decidi fazer uma entensão da formação, vendo tópicos adicionais do Python.

## Testes

- [x] [Testes em Python: trabalhando com dublês de testes]([URL](https://cursos.alura.com.br/course/python-testes-com-dubles))
  - Repositório: [https://github.com/josenaldo/alura-python-testes-dubles](https://github.com/josenaldo/alura-python-testes-dubles)
  - Tipo: Curso
  - Idioma: Português
  - Pago: Sim
  - Data de conclusão: 06/10/2021
  - Curso sobre como trabalhar com dublês de testes em Python.
    - Precisamos de dublês para simular acesso a, ou substituir, partes do sistema que não estão implementadas
    - Os dublês servem para simular comportamentos para que os testes tenham resultados determinísticos
    - Dummy: um dublê que serve para substituir parâmetros obrigatórios, mas não são usados na verificação do caso de teste e, por isso, são irrelevantes
    - Como implementar Dummy sem a biblioteca unittest.mock
    - Como implementar Dummy com a biblioteca unittest.mock
    - Stub: um dublê que serve para fornecer dados fabricados, ou comportamentos esperados, para serem usados na verificação do caso de teste
    - Como usar o dublê Stub para substituir o resultado de uma requisição a uma página da Internet, sem que a requisição de fato ocorra
    - Como implementar nosso próprio Stub, sem usar a biblioteca unittest.mock
    - Como implementar Stub com a biblioteca unittest.mock
    - Como testar quando exceções são levantadas
    - Como testar quando quando exceções foram "logadas"
    - Spy: Um dublê que serve para capturar saídas indiretas para serem usadas na verificação do caso de teste.
    - Como usar o dublê Spy para verificar que exceções foram levantadas ou registradas
    - Como usar o dublê Spy para verificar valores dos parâmetros da função substituída
    - Como implementar nosso próprio Spy sem usar a biblioteca unittest.mock
    - Como implementar Spy com a biblioteca unittest.mock
    - Mock: um dublê que serve, ao mesmo tempo, para programar comportamento esperado e capturar as saídas indiretas para serem usados na verificação do caso de teste
    - Como usar o dublê Mock para verificar as chamadas das funções que substituiu nos casos de teste e para programar o resultado das mesmas
    - Como implementar nosso próprio Mock, sem usar a biblioteca unittest.mock
    - Como implementar Mock com a biblioteca unittest.mock
    - Fake: um dublÊ que serve como uma implementação simplificada de uma dependência da unidade sob teste
    - Como usar o dublê Fake para simular uma operação no banco de dados sem ter o efeito colateral nele
    - Como implementar Fake, sem usar a biblioteca unittest.mock
    - Como implementar Fake com a biblioteca unittest.mock
    - Alguns pontos de atenção ao usar os dublês de testes

- [x] [Montando cenários de testes com o Pytest](https://www.alura.com.br/artigos/montando-cenarios-de-testes-com-o-pytest)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo

- [x] [Mocks, Stubs, Dummies, Fakes, Spies - Dublês de Teste](https://www.youtube.com/watch?v=9w4GpaOeX7M)
  - Tipo: Vídeo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Vídeo sobre os tipos de dublês de testes

- [x] [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
  - Tipo: Artigo
  - Idioma: Inglês
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo, do Martin Fowler, sobre mock objects e suas diferenças para com os stubs

- [x] [The Little Mocker](https://blog.cleancoder.com/uncle-bob/2014/05/14/TheLittleMocker.html)
  - Tipo: Artigo
  - Idioma: Inglês
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo simulando uma conversa sobre stubs e mocks

- [x] [Imutabilidade de Strings no Python](https://blog.saldanha.dev/imutabilidade-de-strings-no-python/)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre a imutabilidade de strings no Python

## Tratamento de erros

- [x] [Python 3: Entendendo o Tratamento de Erros](https://cursos.alura.com.br/course/python-exceptions-entendendo-o-tratamento-de-erros)
  - Repositório: [https://github.com/josenaldo/alura-python-entendendo-o-tratamento-de-erros](https://github.com/josenaldo/alura-python-entendendo-o-tratamento-de-erros)
  - Tipo: Curso
  - Idioma: Português
  - Pago: Sim
  - Data de conclusão: 08/10/2021
  - Curso sobre o tratamento de erros no Python
    - Como lançar exceções com o comando `raise`.
    - Qual o fluxo de execução quando um erro é disparado.
    - Como usar o `except` para capturar diferentes tipos de exceção.
    - Como adicionar Propriedades em nossas classes.
    - Quais são as vantagens de usar properties.
    - Python é uma linguagem de escopo aberto e por isso não possui modificadores de acesso.
    - Como usar o padrão "__"(double under) para marcar atributos e métodos privados.
    - Como usar a função `breakpoint` dentro do código, para não poluirmos nosso código na hora de debugar.
    - Como usar o debbuger para analisar o código linha a linha de forma iterativa e achar erros.
    - Como criar nossas próprias exceções, para informar erros de maneira mais contextualizada.
    - Devemos sempre herdar da classe Exception na hora de criar nossos erros.
    - As vantagens de enriquecer os objetos de erro com mais informação.
    - Como usar os parâmetros args e kwargs em nossos erros.
    - A lançar exceções a partir de um bloco `except`.
    - Como sobrescrever o atributo args, de uma exceção, para evitar que informações vazem pelas mensagens de erro.
    - A sintaxe de `raise <Exception> from E`, onde lançamos uma nova exceção a partir de uma já tratada.
    - Como usar a cláusula `finally` para fechamento de recursos e operações que independem do acontecimento ou não de um erro.
    - Como facilitar o entendimento e termos um código seguro com o `with`.
    - A importância de liberar recursos compartilhados do sistema como arquivos externos.

- [x] [Python: Lidando com erros e exceções](https://www.alura.com.br/artigos/tratamento-de-excecoes-no-python)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre como lidar com erros e exceções no Python
    - Erros que podem acontecer durante a execução de um programa.
    - O problema do fechamento do arquivo
    - Garantindo a execução de um código com um bloco `try/finally`
    - Tratando exceções com o bloco `try/except`
    - Capturando exceções específicas com `except`
    - "E se tudo der certo?" com a cláusula `else`
    - Gerenciadores de contexto
    - Tratando erros com elegância

- [x] [Conhecendo as assignment expressions - PEP 572 aceita!](https://www.alura.com.br/artigos/conhecendo-as-assignment-expressions-pep-572-aceita)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: 27/10/2021  
  - Artigo sobre as expressões de atribuição, um novo recurso do Python em que uma atribuição pode ocorrer no meio de uma expressão.

## Trabalhando com arquivos

## Padrões de projetos

## Boas práticas