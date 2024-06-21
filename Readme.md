# Sistema de Cadastro

## Descrição

Este projeto implementa um Sistema de Cadastro completo em Python, utilizando SQLite para gerenciamento de dados e Tkinter para a criação de uma interface gráfica intuitiva. O sistema permite aos usuários cadastrar, visualizar, atualizar e excluir itens do inventário de sua residência, além de realizar pesquisas por itens específicos.

## Funcionalidades

*   Banco de Dados:
        SQLite utilizado para criar e gerenciar o banco de dados local.
        Estrutura da tabela "Inventory" com campos para nome, localização, descrição, marca, data de compra e valor do item.
        Implementação das operações CRUD (Criar, Ler, Atualizar, Excluir) para itens do inventário.
        Integração eficiente com SQLite através de conexões e cursores para consultas e atualizações.
        Gerenciamento de transações para garantir a consistência dos dados.

*   Interface Gráfica:
        Interface amigável e intuitiva desenvolvida com Tkinter.
        Campos de entrada ("Entry") para inserção e edição de dados dos itens.
        Botões ("Button") para realizar as operações CRUD e pesquisar itens.

*   Operações Disponíveis:
        Inserir Item: Adiciona um novo item ao inventário preenchendo todos os campos obrigatórios.
        Visualizar Itens: Lista todos os itens presentes no inventário com suas respectivas informações.
        Atualizar Item: Edita as informações de um item selecionado, atualizando os campos conforme a necessidade.
        Excluir Item: Remove um item específico do inventário após confirmação do usuário.
        Pesquisar Item: Busca um item específico pelo ID e retorna seus dados.

## Estrutura do Banco de Dados

O banco de dados possui uma única tabela chamada "Inventory" com os seguintes campos:

       id: (INTEGER, chave primária autoincrementável)
       name: (TEXT, nome do item)
       location: (TEXT, local do item na residência)
       description: (TEXT, descrição detalhada do item)
       brand: (TEXT, marca do item)
       date_of_purchase: (TEXT, data de compra do item)
       purchase_value: (REAL, valor de compra do item)
Considerações Adicionais

Este projeto oferece uma base sólida para gerenciar inventários domésticos de forma organizada e eficiente.
O sistema pode ser facilmente adaptado para atender às necessidades específicas de diferentes usuários.
A documentação detalhada e o código-fonte completo facilitam a compreensão e o uso do projeto.

