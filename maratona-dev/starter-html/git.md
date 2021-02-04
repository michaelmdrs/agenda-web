op

### Configuração Inicial :gear:

Essa configuração você fará apenas uma vez por computer e o efect if manterá após atualização.

Você também pode mudá-las em qualquer momento rodando esses comandos novamente.



#### Sua identidade :man:

Assim que instalar o git, abra o terminal e digite:



```
$ git config --global user.name "Seu nome"
git config --global user.email seuemail@seumail.com
```

> Isto é importante porque cada commit usa esta informação, e ela é carimbada de forma imutável nos commits que você começa a criar.

#### Editor :spiral_notepad:

Você poderá trocar o editor padrão, que é o VIM, por outro.

```
git config --global core.editor "code -w"
```

#### Ver configurações

```
git config --list
```

```
git config --global color.ui true
```

### Git config

- [ ] Permite ver e atribuir variáveis de configurações como nome e email
- [ ] Estas váriaveis podem ser armazenadas em três lugares diferentes.
  - [ ] 1. /etc/gitconfig: válido para todos os usuários no sistema e todos os seus repositórios. Se você passar a opção --system para git config, ele lê e escreve neste arquivo.
    2. ~/.gitconfig ou ~/.config/git/config: Somente para o seu usuário. Você pode fazer o Git ler e escrever neste arquivo passando a opção --global.
    3. config no diretório Git (ou seja .git/config) de qualquer repositório que você esteja usando: específico para este repositório.

> Cada nível sobrescreve os valores no nível anterior, ou seja em .git/config prevalecem sobre /etc/gitconfig.

> No Windows, o arquivo .gitconfig estará no diretório $HOME que é o C:\Users\$USER

### Git log

Para saber o histórico dos commits já realizado e o nome do author podemos usar o seguinte comando:

```
git log
```

Saber o mesmo histórico de commits de maneira resumida podemos usar o seguinte comando:

```
git log --oneline
```

Agora se queremos saber quais foram os últimos commits recém adicionados podemos usar o seguinte comando:

```
git log -n 5
```

Esse comando irá nos retornar os últimos 5 commits adicionado ao projeto.

Podemos saber o histórico de commits passando uma data específica por exemplo:

```
git log --since=2020-12-01
```

Também podemos saber o histórico de commits antes da data informada ex: :nerd_face:

```
git log --until=2020-10-01
```

Podemos filtar os históricos pelo author:

```
git log --autho=Michael
```

Usando expressões regulares para pesquisar históricos de commits ex:

```
git log --grep='Function'
```

