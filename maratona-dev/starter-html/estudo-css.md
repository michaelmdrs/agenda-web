### Table :bookmark_tabs:

- Prós
  - Visualização de dados via linhas e colunas.
  - Boa acessibilidade para leitura dos dados.
- Contras
  - Pouco flexível
  - Precisa de estilização para melhor visualização
- Não usar
  - Para criar layout de site

### Meta :dart:

- atributos
  - charset
  - name
  - content

### O que significa CSS? :art:

- Cascading Style Sheet
- Código para criar estilos no HTML
- HTML é a estrutura, e o CSS é a beleza
- Não é uma linguagem de programação
- É uma linguagem de style sheet

### Cascata

​	A escolha do browser de qual regra aplicar, caso haja muitas regras para o mesmo elemento.

* Seu estilo é lido de cima para baixo

##### São levados em consideração 3 fatores

1. Origem do estilo
2. Especificidade
3. Importância

#### Origem do estilo

inline > tag style > tag link

#### Especificidade

​	É um cálculo matemático, onde cada tipo de seletor e orige do estilo, possuem valores a serem considerados.

0. Universal selector, combinators and negation pseudo-class (:not())
1. Element type selector e pseudo-elements (::before, ::after)

10. Class e attribute selectors ([type="radio"

100. ID selector

1000. Inline

#### A regra de importância

- Cuidado, evite o uso
- Não é uma boa prática
- quebra o fluxo natural da cascata

### At-rules :man_artist:

- Está relacionado ao comportamento CSS
- Começa com o símbolo de @ seguido do identificador e valor

##### Exemplos comuns

- @import				// incluir um CSS externo
- @media                // regras condicionais para dispositivos móveis
- @font-face           // fontes externas
- @keyframes       // Animation

### Shorthand

- Junção de propriedades
- Resumido
- Legível

#### Exemplos :art:

**Background property**

background-color: #000;

background-image: url(images/bg.jpg);

background-repeat: no-repeat;

background-position: left top;

**Background shorthand**

background: #000 url(images/bg.pjg) no-repeat left top;

**Font properties**

font-style: italic;

font-weight: bold;

font-size: .8em;

line-height: 1.2;

font-family: Ubuntu, sans-serif;

**Font shorthand**

font: italic bold .8em/1.2 Ubuntu, sans-serif;



#### Detalhes

- Não irá considerar propriedades anteriores
- Valores não especificados irão assumir o valor padrão
- Geralmente, a ordem descrita não importa, mas, se houver muitas propriedades com valores semelhantes, podermos encontrar problemas.

### Funções :man_technologist:

- Nome seguido de abre e fecha parentesis
- Recebe argumentos

#### Exemplo

@import url("https://urlaqui.com/style.css");

{

​	color: rgb(255, 0, 100);

​	width: calc(100% - 10px);

}









