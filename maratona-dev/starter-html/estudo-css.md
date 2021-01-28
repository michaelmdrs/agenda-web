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

```
background-color: #000;

background-image: url(images/bg.jpg);

background-repeat: no-repeat;

background-position: left top;
```

**Background shorthand**

```
background: #000 url(images/bg.pjg) no-repeat left top;
```

**Font properties**

```
font-style: italic;

font-weight: bold;

font-size: .8em;

line-height: 1.2;

font-family: Ubuntu, sans-serif;
```

**Font shorthand**

```
font: italic bold .8em/1.2 Ubuntu, sans-serif;
```



#### Detalhes

- Não irá considerar propriedades anteriores
- Valores não especificados irão assumir o valor padrão
- Geralmente, a ordem descrita não importa, mas, se houver muitas propriedades com valores semelhantes, podermos encontrar problemas.

### Funções :man_technologist:

- Nome seguido de abre e fecha parentesis
- Recebe argumentos

#### Exemplo

```
@import url("https://urlaqui.com/style.css");
```



```
{

​	color: rgb(255, 0, 100);

​	width: calc(100% - 10px);

}
```



### Vendor Prefixes

​	Permite que browsers adicione features a fim de colocar em uso algum novidade que vemos no CSS.

#### Exemplo



```
p {
	-webkit-background-clip: text;  // Chrome, Safari, iOS e Android
	-moz-background-clip: text;    // Mozilla
	-ms-backgroun-clip: text;     // Internet Explorer
	-0-background-clip: text;    // Opera
}
```

#### Consultas :round_pushpin:

[ http://ireade.github.io/wich-vendor-prefix/ ]

[ http://caniuse.com ]

------



### Controle de Versão

- [ ] Registro de alterações em um ou mais arquivos
- [ ] Lembrar versões específicas mais tarde
- [ ] Reverter para o estado anterior determinados arquivos ou um projeto inteiro
- [ ] Compare as mudanças ao longo do tempo
- [ ] Veja quem modificou pela última vez algo que pode estar causando um problema
- [ ] Quem introduziu um problema ou quando
- [ ] Se você estragar tudo ou perder arquivos, você pode facilmente recuperar
- [ ] E muito mais

> VCS - Version Control Systemos

------



### Tipos de Controle de Versão :gear:

#### Sistemas Locais

- [ ] Copiar os arquivos para outro diretório
- [ ] Muito comum e muito simples
- [ ] Incrívelmente propensa a erros
- [ ] Fácil de sobreescrever arquivos, caso haja feito uma cópia errada

> **Para superar os possíveis erros, existe o RCS - Revision Control System**

- [ ] Ferramenta popular (antigamente) para controle de versão
- [ ] Mantém conjuntos de alterações, ou seja, as diferenças entre os arquivos
- [ ] Formato especial no disco
- [ ] Re-criar como qualquer arquivo se parecia em qualquer ponto no tempo, adicionando-se todas as alterações ao arquivo.

> **E se você precisar colaborar com desenvolvedores em outros sistemas?**

------



### Sistemas Centralizados :dvd:

> CVS, Subversion e Perforce

- [ ] Um único servidor que contém todos os arquivos de controle de versão
- [ ] Vários clientes usam arquivos a partir desse lugar central.

> *Por muitos anos, este tem sido o padrão para controle de versão*

------



### Vantagens sobre VCSs locais

- [ ] Controle sobre atividades dos colaboradores no projeto
- [ ] Os administradores têm controle refinado sobre quem pode fazer o que
- [ ] Mais fácil de administrar um CVCS do que lidar com bancos de dados locais em cada cliente

### Desvantagens

- [ ] Se esse servidor der problemas por uma hora, durante essa hora ninguém pode colaborar ou salvar as alterações de versão para o que quer que eles estejam trabalhando
- [ ] Se o disco rígido do banco de dados central for corrompido, você perde absolutamente tudo
- [ ] Sistemas VCS locais sofrem com esse mesmo problema

> **Sempre que você tenha toda a história do projeto em um único lugar, há o risco de perder tudo**



------

### Sistemas Distribuídos :penguin:

> *Git, Mercurial, Bazaar ou Darcs*

- [ ] Duplicar (clonar) localmente o repositório completo
- [ ] Se qualquer servidor morrer, e esses sistemas estiverem colaborados por meio dele, qualquer um dos repositórios do cliente poderá ser copiado de volta para o servidor
- [ ] Cada clone é de fto um backup completo de todos os dados
- [ ] Clientes usam o estado mais recentes dos arquivos

------

### O que é Git?

- [ ] Sistema de controle de versão distribuído 
- [ ] Open-source
- [ ] Pontos na história: *commit* (viagem no tempo) 
  - [ ] Histórico de alterações no código
  - [ ] Voltar para qualquer ponto na história
- [ ] Controlar o fluxo de novas funcionalidades
  - [ ] Ramificações: *branch* (universos paralelos)
  - [ ] Vários devs no mesmo projeto
  - [ ] Análise e resolução de conflitos