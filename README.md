# Desafio Técnico - Executando o Aplicativo com Docker

Este desafio envolve a execução de um aplicativo utilizando o Docker. Siga as etapas abaixo para garantir um processo tranquilo:

1. **Baixar Arquivos:**
   Comece baixando o arquivo fornecido. Isso contém todos os elementos necessários para executar o aplicativo.

2. **Abrir no Visual Studio:**
   Abra a pasta que você baixou no Visual Studio. Certifique-se de que todos os arquivos estejam acessíveis no ambiente do Visual Studio
   **Atenção selecionar a pasta LoansForGoodProject que fica acima do readme e arrastar para o VisualStudio se arrastar a pasta DesafioTecnico-main ocasionara no erro do comando de construção do conteiner(.5)**

4. **Abrir Novo Terminal:**
   No Visual Studio, abra um novo terminal. Isso é necessário para executar os comandos relacionados ao Docker.

5. **Construir o Contêiner:**
   No terminal, execute o comando:
   ```
   docker build -t execucao-container .
   ```
   Isso criará um contêiner Docker com base nos arquivos fornecidos.

6. **Executar o Contêiner:**
   Após a construção bem-sucedida, execute o contêiner com o comando:
   ```
   docker run -p 8000:8000 execucao-container
   ```
   Isso iniciará o contêiner e redirecionará a porta 8000 do seu sistema para a porta 8000 dentro do contêiner.

7. **Acessar o Aplicativo:**
   Abra seu navegador e insira o seguinte endereço na barra de busca:
   ```
   http://localhost:8000/propostas/registro
   ```
   Isso o levará à página inicial do programa no seu navegador.
   
8. **Para acessar o Admim:**
   Abra seu navegador e insira o seguinte endereço na barra de busca:
   ```
   http://localhost:8000/admin
   ```
   para Username(Nome):
   ```
   thiago
   ```
   para Password(Senha):
   ```
   marasco1401
   ```
   

Essas instruções são projetadas para tornar o processo simples e direto. Certifique-se de seguir cada etapa e observe o aplicativo em execução. Se você encontrar algum problema, verifique se seguiu todas as instruções corretamente.
