# cadastro-usuario-challenge
Aplicação Fullstack de cadastro de usuários. desafio PontoTel

### Relato de desenvolvimento
Duas semanas intensas de estudos e muito aprendizado, infelizmente não consegui completar todos os quesitos e foquei em desenvolver os pontos que seriam mais desafiadores para mim como focar na stack da pontotel Vue + Flask (não deu tempo de implantar um BD postgres ☹️ ), dockerizar a aplicação, fazer o docker compose e o deploy de um monorepo no Heroku, onde esse último se tornou o maior desafio e consumiu muito tempo, não sobrando espaço para refinamentos requeridos.

## Como rodar a aplicação


## Checklist
### Nível 1 (Backend/Fullstack/Frontend):

 ✅ Enquanto o usuário não estiver “logado”, apresentar uma página que diga "Olá visitante".
 
 ✅ Se o usuário estiver “logado”, ao invés da página do "Olá Visitante", apresentar "Olá {NOME_DO_USUARIO}"
 
 ⚠️ Apresente campo de login por email, CPF ou PIS + senha - **Login somente email + senha**
 
 ✅ Apresente botão que leva para página de cadastro de usuário
 
 ✅ botão de logout
 
 ✅ botão que leve para a página de edição dos dados cadastrais.
 
 ✅ botão de remoção do usuário que o desloga em seguida.
 
 ### Nível 1 (Bônus):
  
 ✅ Use variáveis de ambiente
 
 ✅ Use Docker
 
 ✅ botão de remoção do usuário que o desloga em seguida.
 
 ✅ Suba a aplicação(back e front) no heroku ou similar.
 
 ### Nível 2 (Front/Fullstack):
 
 ✅ Criar frontend que realize as funcionalidades acima em SPA - **Feito em Vuejs**
 
 ✅ Criar API REST completa para manipulação dos usuários
 
 ✅ Realizar autenticação via token JWT
 
 ### Nível 2 (Bônus):
 
 ✅ front adaptado para web e mobile. **App possui boa navegação no mobile, porém foquei mais em outros aspectos da aplicação como o docker e deploy no heroku**

  ⚠️ Escreva um arquivo de docker-compose contendo a configuração dos 3 serviços(back, banco, front). Torne o banco de dados acessível apenas para o back. **docker-compose contempla somente as aplicações front e back, não consegui tempo para integrar uma DB postgres ao projeto**
  
 ### Nível 3 (Backend/Fullstack/Front):
  
 ❌ Implementar autenticação OAUTH2 usando uma conta gratuita do Auth0
  
 ❌ Implementar autenticação com firebase
  
 ### Demais requisitos:
   
 ⚠️  validar os dados de entrada do usuário adequadamente. **Somente validação de email e verificação de campo não vazio**
 
 ❌ armazenar as informações em banco de dados relacional. **Aplicação rodando com sqlite3**
 
 ✅ armazenar a sessão do usuário em cookie
 
 ❌ apresentar testes unitários

 
  
  
