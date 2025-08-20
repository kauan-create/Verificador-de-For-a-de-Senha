# Verificador de Força de Senha Web

Sobre o projeto, ele é um aplicativo web que te ajuda a testar se suas senhas são seguras, tudo direto no navegador. Você digita uma senha, e ele te diz se ela é forte, moderada ou fraca, com dicas para deixá-la ainda melhor. Além disso, ele guarda os resultados (de forma super segura!) num banco de dados. É como ter um amigo te ajudando a proteger suas contas online!

### O que esse projeto faz?

Você coloca uma senha na página, e o programa verifica se ela:

- Tem **pelo menos 8 caracteres** (senhas curtas não rolam, né?).
- Inclui **letras maiúsculas** (tipo A, B, C).
- Tem **letras minúsculas** (como a, b, c).
- Contém **números** (1, 2, 3...).
- Usa **caracteres especiais** (como !, @, #, $).

Depois, ele te dá um feedback estilo: "Nossa, sua senha é uma fortaleza!" ou "Que tal adicionar um número ou caractere especial?". As verificações são salvas com segurança (usando hash) num banco de dados SQLite, e você pode ver as últimas cinco na tela.

## Como usar

É muito simples, até quem nunca mexeu com programação consegue! Siga esses passos:

1. **Clone o repositório** para o seu computador:

   - Copie o link do repositório no GitHub (ex.: `https://github.com/seu_usuario/password_strength_checker_web.git`) e use seu cliente Git favorito para clonar, ou baixe o ZIP e descompacte.

2. **Entre na pasta do projeto**:

   - Navegue até a pasta `password_strength_checker_web` usando seu gerenciador de arquivos ou terminal.

3. **Instale as dependências** (você precisa ter o Python instalado):

   - No terminal, execute:

     ```
     pip install flask 
     ```

4. **Rode o programa**:

   - Ainda no terminal, na pasta do projeto, execute:

     ```
     python app.py
     ```

5. Abra seu navegador e vá para `http://localhost:5000`. Digite uma senha, clique em "Verificar" e veja o resultado! O histórico das últimas verificações aparece logo abaixo.

**Dica**: Um arquivo chamado `database.db` será criado automaticamente na pasta do projeto para armazenar os resultados.

## Tecnologias que usei

Aqui está o que faz a mágica acontecer:

- **Python**: A linguagem que dá vida ao projeto, fácil e poderosa.
- **Flask**: Um framework leve para criar a página web num piscar de olhos.
- **SQLite**: Um banco de dados simples que guarda as verificações (você encontra o `database.db` na pasta do projeto).
- **Werkzeug**: Para transformar suas senhas em hashes seguros, mantendo tudo protegido.
- **HTML/CSS**: Para deixar a página bonita e fácil de usar.
- **Expressões regulares (re)**: Um truque do Python para checar os tipos de caracteres na senha.

- **Segurança com senhas**  
  Entendi a importância dos hashes para proteger dados sensíveis. Usei `pbkdf2:sha256` com o **Werkzeug** para armazenar senhas de forma segura.

- **Trabalhar com Flask**  
  Aprendi a criar rotas, lidar com formulários e usar mensagens flash. Foi meu primeiro contato real com a estrutura de um app web completo.

- **Banco de dados na prática**  
  Foi minha primeira vez integrando **SQLite** com Flask. Aprendi a criar tabelas, inserir dados e realizar consultas para exibir resultados.

- **Regex na validação**  
  Tive alguns desafios com expressões regulares, principalmente para validar caracteres especiais, mas consegui dominar o básico para aplicar nas verificações.

> Cada bug foi um desafio… e cada correção, uma pequena vitória!

## Ideias para se divertir com o projeto

- **Teste senhas diferentes**: Experimente `123`, `SuperSenha123!` ou até `abc!@#` e veja o que o programa acha.
- **Explore o banco de dados**: Use uma ferramenta como DB Browser for SQLite para dar uma olhada no `database.db` e ver os hashes e resultados salvos.
- **Personalize**: Que tal adicionar um botão para limpar o histórico ou mudar as cores da página? Solte a criatividade!
