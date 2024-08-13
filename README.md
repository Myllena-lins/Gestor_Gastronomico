# Gestor Gastronômico
Este projeto foi elaborado no módulo 1 (Python) do curso de dados da Ada Tech. O sistema permite que restaurantes se registrem, adicionem pratos ao seu cardápio e atualizem suas ofertas, além de permitir que clientes façam pedidos, visualizem e cancelem pedidos. Os dados são salvos em arquivos de texto e podem ser carregados na inicialização do programa.

## Funcionalidades
- Cadastro de Restaurantes: Restaurantes podem se cadastrar e adicionar pratos ao seu cardápio.
- Gerenciamento do Cardápio:
    - Adicionar Pratos: Restaurantes podem adicionar novos pratos ao cardápio.
    - Visualizar Cardápio: Restaurantes podem visualizar os pratos atualmente disponíveis.
    - Atualizar Pratos: Restaurantes podem alterar as informações de pratos existentes.
    - Excluir Restaurante: Restaurantes podem ser removidos do sistema.
- Clientes:
    - Listar Restaurantes: Clientes podem visualizar todos os restaurantes cadastrados.
    - Fazer Pedido: Clientes podem visualizar o cardápio dos restaurantes e fazer pedidos.
    - Visualizar Pedido: Clientes podem visualizar os itens em seu pedido atual.
    - Cancelar Pedido: Clientes podem cancelar seus pedidos antes da confirmação.
- Persistência de Dados:
    - Salvar Dados: O sistema salva informações de restaurantes e pedidos em arquivos de texto (dados.txt e pedido.txt).
    - Carregar Dados: O sistema carrega dados salvos quando iniciado.

## Estrutura de Dados
- dados.txt: Armazena informações dos restaurantes e seus cardápios.
- pedido.txt: Armazena os pedidos feitos pelos clientes.

## Tecnologias Utilizadas
- Python (módulos padrão: os, sys)

## Observações Finais
A criação desse sistema foi uma solução simples e aplicável em qualquer sistema de gerenciamento de restaurantes. Qualquer sugestão para melhoria do mesmo será bem-vinda!
