# Plano de estudo: Formação Python - Fase 2 - Aprimoramento

Plano de estudo e registro da Fase 2 do Curso Formação Python, na Alura. Essa fase não consta, na Alura, como uma formação. Eu que decidi fazer uma entensão da formação, vendo tópicos adicionais do Python.

O plano original pode ser visto em [https://cursos.alura.com.br/python-fase-2-josenaldo-1634664880417-p237519.html](https://cursos.alura.com.br/python-fase-2-josenaldo-1634664880417-p237519.html).

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

- [x] [Python 3: Trabalhando com I/O](https://cursos.alura.com.br/course/python-3-trabalhando-com-io)
  - Repositório: [https://github.com/josenaldo/alura-python-trabalhando-com-io](https://github.com/josenaldo/alura-python-trabalhando-com-io)
  - Tipo: Curso
  - Idioma: Português
  - Pago: Sim
  - Data de conclusão: 11/10/2021
  - Curso sobre como trabalhar com arquivos em Python
    - Como abrir arquivos com o Python
    - O que é o encoding
    - Como ler as linhas de um arquivo com os métodos readline() e readlines()
    - Ler as linhas de um arquivo percorrendo ele através de um loop
    - Os modos de abertura de um arquivo para escrita
    - Como podemos escrever em um arquivo
    - O momento em que é realizada a escrita do arquivo
    - O comportamento do método flush()
    - Como percorrer arquivos com o seek()
    - A importância de liberar um recurso
    - Como gerenciar contextos utilizando a cláusula with
    - Algumas exceções comuns ao se trabalhar com arquivos
    - A diferença dos modos de escrita e de leitura na hora de abrir um arquivo que não existe
    - Como funciona a leitura e a escrita de dados por baixo dos panos
    - A classe bytes
    - Como funciona o buffer de leitura e de escrita
    - Como utilizar os módulos csv, json, pickle
    - Como serializar e desserializar objetos
    - Como retornar o dicionário de atributos de um objeto
    - Como desempacotar objetos com Python

- [x] [Python: O que significa if __name__ == '__main__'?](https://www.alura.com.br/artigos/o-que-significa-if-name-main-no-python)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre a instrução `__name__ == '__main__'`
    - A variável `__name__`
    - Usando if `__name__ == '__main__'` para controle de escopo de execução
    - Quando usar a checagem de escopo de execução?

## Padrões de projetos

- [x] [Design Patterns Python I: Boas práticas de programação](https://cursos.alura.com.br/course/design-patterns-python)
  - Repositório: [https://github.com/josenaldo/alura-python-design-patterns-1](https://github.com/josenaldo/alura-python-design-patterns-1)
  - Tipo: Curso
  - Idioma: Português
  - Pago: Sim
  - Data de conclusão: 19/10/2021
  - Curso sobre padrões de projetos e sua implementação no Python:
    - Strategy
    - Chain of Responsibility
    - Template Method
    - Decorator
    - State
    - Builder
    - Observer
    - Além dos padrões de projeto

- [x] [State](https://refactoring.guru/pt-br/design-patterns/state)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: 27/10/2021
  - Artigo sobre o padrão de projeto State

- [x] [Programação funcional no Python](https://blog.caelum.com.br/programacao-funcional-no-python/)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre programação funcional no Python
    - Utilizando a função map()
    - Cuidados com funções de alta ordem
    - Passando nossa própria função para o map()
    - Funções anônimas com lambda
    - Filtrando valores de um iterável com a função filter()
    - Utilizando a função reduce() para reduzir um iterável a um só valor

- [x] [Conhecendo as tuplas no Python](https://www.alura.com.br/artigos/conhecendo-as-tuplas-no-python)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre tuplas no Python

- [x] [Semana de dados - Qual perfil de cientista de dados o mercado está pedindo?](https://www.youtube.com/watch?v=Qj-N2bLgCM4)
  - Tipo: Vídeo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: 18/10/2021
  - Vídeo sobre os perfis de profissionais de dados que o mercado está pedindo.

- [x] [O que é Test-Driven Development (TDD)?](https://cursos.alura.com.br/o-que-e-test-driven-development-tdd--c1137)
  - Tipo: Vídeo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Vídeo sobre o que é TDD, como ele funciona e como ele pode ser utilizado.

- [x] [Os testes e os dublês - Parte 1](https://klauslaube.com.br/2014/08/07/os-testes-e-os-dubles-parte-1.html)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Primeira parte do artigo sobre dublês de teste.
    - Porque usar dublês de teste?
    - Tipos de dublês de teste

- [x] [Os testes e os dublês - Parte 2](https://klauslaube.com.br/2015/06/29/os-testes-e-os-dubles-parte-2.html)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Segunda parte do artigo sobre dublês de teste
    - Instalação da biblioteca mock (hoje não é mais utilizada)
    - Dummys
    - Fakes
    - Mocks
    - Stubs
    - Spies

- [x] [Design Patterns Python II: Boas práticas de programação](https://cursos.alura.com.br/course/design-patterns-python-2)
  - Repositório: [https://github.com/josenaldo/alura-python-design-patterns-2](https://github.com/josenaldo/alura-python-design-patterns-2)
  - Tipo: Curso
  - Idioma: Português
  - Pago: Sim
  - Data de conclusão: 22/10/2021
  - Segundo curso sobre padrões de projetos e sua implementação no Python:
    - Fábricas
    - Memento
    - Interpreter
    - Visitor
    - Command

- [x] [Memento](https://refactoring.guru/design-patterns/memento)
  - Tipo: Artigo
  - Idioma: Inglês
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre o padrão de projeto Memento

- [x] [Interpreter Design Pattern](https://sourcemaking.com/design_patterns/interpreter)
  - Tipo: Artigo
  - Idioma: Inglês
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre o padrão de projeto Interpreter

- [x] [Visitor](https://refactoring.guru/pt-br/design-patterns/visitor)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre o padrão de projeto Visitor

- [x] [Visitor e o Double Dispatch](https://refactoring.guru/pt-br/design-patterns/visitor-double-dispatch)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre o uso da técnica do Double Dispatch na implementação do padrão Visitor

- [x] [Command](https://refactoring.guru/pt-br/design-patterns/command)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre o padrão de projeto Command

## Boas práticas

- [x] [Python: Boas práticas de código com PEP8](https://cursos.alura.com.br/course/pep8-linters-python)
  - Repositório: [https://github.com/josenaldo/alura-python-boas-praticas-de-codigo-com-pep8](https://github.com/josenaldo/alura-python-boas-praticas-de-codigo-com-pep8)
  - Tipo: Curso
  - Idioma: Português
  - Pago: Sim
  - Data de conclusão: 26/10/2021
  - Curso sobre como escrever bons códigos no python com o PEP8 e como utilizar o ferramentas de verificação de código
  - Técnicas de Type hints
  - Conceitos de PEP8
  - Como escrever classes utilizando a PEP8
  - A diferença entre uma classe que usa a PEP8 e uma que não usa
  - Como instalar e usar o MyPy
  - Como instalar e configurar o Flake8
  - Como alertar erros de estilo no commit
  - Como bloquear um commit que tenha problemas de estilo de código
  - Mais regras do PEP8
  - O que é uma classe abstrata
  - O que é um Template Method
  - Sobre o padrão de projeto Factory
  - Como trabalhar com constantes seguindo o PEP8
  - Mais técnicas de Type Hints
  - Como reduzir a quantitade de ifs em seus códigos
  - Sobre o padrão de projeto Injeção de dependências
  - Sobre o conceito de responsabilidades nos seus códigos

- [x] [Como publicar seu código Python no PyPI](https://www.alura.com.br/artigos/como-publicar-seu-codigo-python-no-pypi)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: Indeterminada
  - Artigo sobre como publicar um código Python no PyPI

- [x] [Injeção de Dependência](https://medium.com/@eduardolanfredi/inje%C3%A7%C3%A3o-de-depend%C3%AAncia-ff0372a1672)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: 26/10/2021
  - Artigo sobre como utilizar o padrão de projeto Injeção de Dependência
    - Injeção de Dependência e Inversão de Controle
    - Injeção por construtor
    - Injeção por interface
    - Injeção por propriedade (getter e setter)
    - Framework de Injeção de Dependência

- [x] [Como fazer uma cópia de uma lista no Python](https://www.alura.com.br/artigos/como-fazer-copia-de-lista-python)
  - Tipo: Artigo
  - Idioma: Português
  - Pago: Não
  - Data de conclusão: 26/10/2021
  - Artigo sobre como fazer uma cópia de uma lista no Python
    - Fazer uma cópia de uma lista, por atribuição, é uma fonte de problemas
    - Listas são objetos mutáveis
    - Fazendo a cópia de uma lista
    - O problema das cópias rasas
    - Fazendo uma cópia profunda de uma lista

- [x] [The pass Statement: How to Do Nothing in Python](https://realpython.com/python-pass/)
  - Tipo: Artigo
  - Idioma: Inglês
  - Pago: Não
  - Data de conclusão: 26/10/2021
  - Artigo sobre a expressão `pass` e suas alternativas
    - Python pass Statement: Syntax and Semantics
    - Usos temporários do `pass`
      - Uso do `pass` como marcador de código futuro
      - Uso do pass para funções cujo código foi comentado
      - Uso do pass como marcador de depuração
      - Uso do pass como corpo de função vazia
      - Uso do pass como corpo de classe vazia
      - Uso do pass como corpo de métodos de marcação
    - Alternativas ao `pass`
      - Docstrings
      - Ellipsis
      - Levantar um Error
    - Usos permanentes do Pass
      - Uso do pass como tratamento de exceção
      - Uso do pass como encadeamento elif

- [x] [Case Styles: Camel, Pascal, Snake, and Kebab Case](https://betterprogramming.pub/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841)
  - Tipo: Artigo
  - Idioma: Inglês
  - Pago: Não
  - Data de conclusão: 27/10/2021
  - Artigo sobre os tipos de casos mais usados  em programação
    - camelCase
    - PascalCase
    - cnake_case
    - kebab-case