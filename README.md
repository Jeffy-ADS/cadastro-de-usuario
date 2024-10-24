# cadastro-de-usuario
# Gerenciamento de Usuários com Tkinter e Banco de Dados

Este projeto cria uma aplicação GUI (interface gráfica) para o gerenciamento de usuários, utilizando a biblioteca Tkinter em Python. O aplicativo permite buscar, inserir, alterar e excluir informações de usuários em um banco de dados.

## Funcionalidades

- **Inserção de usuários**: Preencha os campos (nome, telefone, email, usuário e senha) e insira um novo registro.
- **Alteração de usuários**: Altere os dados de um usuário existente a partir de seu ID.
- **Exclusão de usuários**: Exclua um usuário pelo seu ID.
- **Busca de usuários**: Busque um usuário pelo ID e visualize os dados na interface.

## Estrutura do Projeto

- **`Usuarios`**: Um módulo (não incluído neste repositório) que manipula os dados de usuário no banco de dados (inserir, atualizar, excluir e buscar).
- **`Application`**: Classe principal que gerencia a interface gráfica e chama os métodos de manipulação de dados fornecidos pela classe `Usuarios`.

### Principais Componentes

- **Tkinter**: Biblioteca padrão do Python usada para criar a interface gráfica.
- **Containers e Widgets**: A interface está dividida em containers (`Frame`), com widgets como `Label`, `Entry` e `Button` organizados em cada container.
- **Métodos CRUD**: O projeto possui métodos para Inserir (`inserirUsuario`), Alterar (`alterarUsuario`), Excluir (`excluirUsuario`) e Buscar (`buscarUsuario`) registros no banco de dados.

## Requisitos

- Python 3.x
- Tkinter (incluso na maioria das distribuições do Python)
- Módulo `Usuarios` para manipulação do banco de dados (presumivelmente criado separadamente)

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone ou faça o download deste repositório.
3. Implemente ou adicione o módulo `Usuarios` que se conecta ao banco de dados.
4. Execute o arquivo principal que contém o código da aplicação GUI.

```bash
python nome_do_arquivo.py
