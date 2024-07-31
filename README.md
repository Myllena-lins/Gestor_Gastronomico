# Gestor Gastronômico
Este projeto foi elaborado no módulo 1 (Python) do curso de dados da Ada Tech. O módulo consistiu em criar um sistema com as características do CRUD, no qual foram aprendidas durante a aula. Além das funções básicas, foi incluída a funcionalidade de manipulação de arquivos para salvar e carregar dados.

## Funcionalidades do Sistema
### Funções Principais
- Salvar e Carregar Dados: Permite salvar os dados dos restaurantes e pedidos em arquivos de texto e carregá-los quando necessário.
- Cadastrar Restaurante e Cardápio: Funções para adicionar novos restaurantes e pratos ao sistema.
- Ver e Mudar Cardápio: Visualizar e alterar o cardápio de um restaurante.
- Excluir Restaurante: Remover um restaurante do sistema.
- Listar Restaurantes e Pratos: Listar todos os restaurantes cadastrados e os pratos disponíveis.
- Listar e Cancelar Pedidos: Visualizar e cancelar pedidos realizados.
- Menu Principal: Interface principal que permite navegação entre as opções do sistema.

### Descrição da Funcionalidade
1. Menu Principal:
    - Entrar como Prestador de Serviços (Restaurante):
        1. Cadastrar Restaurante: Incluir nome do restaurante.
        2. Cadastrar Cardápio: Incluir nome do prato, preço e tempo de entrega.
        3. Ver Cardápio: Listar pratos já cadastrados.
        4. Ajustar Cardápio: Alterar nome, preço ou tempo de entrega de um prato já cadastrado no sistema.
        5. Excluir Restaurante: Deletar todas os dados do restaurante.
        6. Sair.

    - Entrar como Cliente:
        1. Conhecer Restaurantes: Listar restaurantes cadastrados.
        2. Fazer Pedido: Digitar o nome do restaurante escolhido, ver a lista de pratos disponíveis e realizar o pedido.
        3. Ver Pedido: Visualizar os detalhes do pedido.        
        4. Cancelar Pedido: Deletar o pedido.
        5. Sair.

    - Sair: Encerrar o sistema.
## Estrutura do Código
O código principal está estruturado em diversas funções que permitem a realização das operações descritas. As funções de salvar e carregar dados garantem a persistência das informações entre as execuções do programa.

## Observações Finais
A criação desse sistema foi uma solução simples e aplicável em qualquer sistema de gerenciamento de restaurantes. Qualquer sugestão para melhoria do mesmo será bem-vinda!
