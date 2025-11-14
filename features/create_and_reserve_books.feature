Feature: DemoQA API - criar usuário e reservar livros
Como um testador
Quero criar um usuário, autorizar, listar livros e reservar dois livros


Scenario: Criar usuário, gerar token, reservar 2 livros e verificar detalhes
Given que eu gero um username e password aleatórios
When eu crio o usuário no sistema
And eu gero um token para o usuário
Then o usuário deve estar autorizado
When eu recupero a lista de livros disponíveis
And eu escolho 2 livros e os adiciono à conta do usuário
Then ao recuperar os detalhes do usuário, devo ver os 2 livros reservados
