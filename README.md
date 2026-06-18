# Sistema de Registro Nacional de Pessoas

## 📌 Sobre o Projeto

O **Sistema de Registro Nacional de Pessoas** é uma aplicação desenvolvida em **Python**, utilizando os princípios da **Programação Orientada a Objetos (POO)** e persistência de dados com **SQLite**.

O objetivo do sistema é simular um ambiente de gerenciamento de registros civis, permitindo o cadastro, consulta, renovação e revogação de documentos relacionados à identificação de cidadãos e estrangeiros, de forma organizada e segura.

O projeto foi desenvolvido como atividade da disciplina de **Engenharia de Software**, aplicando conceitos de modelagem, organização em camadas, reutilização de código e controle de versões com Git.

---

##  Funcionalidades

O sistema oferece as seguintes funcionalidades:

* Cadastro de Documentos de Identidade;
* Cadastro de Autorizações de Residência;
* Cadastro de Autorizações de Refúgio;
* Consulta de registros por número do documento;
* Consulta por nome do solicitante;
* Consulta por tipo de trâmite;
* Renovação de documentos (atualização da data de emissão);
* Revogação (remoção) de registros;
* Geração de relatórios básicos;
* Contagem de registros por tipo;
* Controle de acesso por perfis de usuários.

---

##  Perfis de Usuários

O sistema possui diferentes tipos de usuários, cada um representando um papel dentro do processo de registro nacional:

* **Administrador**
* **Supervisor**
* **Funcionário de Registro**
* **Solicitante**

Cada perfil pode executar operações específicas de acordo com suas responsabilidades no sistema.

---

##  Tipos de Trâmites

O sistema gerencia três categorias principais:

### Documento de Identidade

Contém informações como:

* Nome;
* Número do documento;
* Fotografia;
* Impressão digital;
* Data de emissão.

### Autorização de Residência

Além dos dados básicos, registra:

* País de origem;
* Data de vencimento da autorização.

### Autorização de Refúgio

Além das informações comuns, inclui:

* País de origem;
* Motivo do pedido de refúgio.

---

##  Persistência de Dados

Os registros são armazenados em um banco de dados **SQLite**, permitindo que as informações permaneçam salvas mesmo após o encerramento da aplicação.

A camada de persistência realiza automaticamente operações como:

* Inserção de registros;
* Busca por documento;
* Busca por nome;
* Busca por tipo;
* Listagem completa;
* Atualização de dados;
* Exclusão de registros;
* Geração de estatísticas por categoria.

---

##  Estrutura do Projeto

```text
RegistroNacional/
│
├── atores/
│   ├── administrador.py
│   ├── funcionario_registro.py
│   ├── pessoa.py
│   ├── solicitante.py
│   └── supervisor.py
│
├── dados/
│   └── banco.py
│
├── modelos/
│   ├── tramite.py
│   ├── documento_identidade.py
│   ├── autorizacao_residencia.py
│   └── autorizacao_refugio.py
│
├── servicos/
│   ├── cadastro.py
│   ├── consulta.py
│   ├── renovacao.py
│   ├── revogacao.py
│   └── relatorios.py
│
├── main.py
├── README.md
└── .gitignore
```

---

##  Tecnologias Utilizadas

* Python 3
* SQLite
* Programação Orientada a Objetos (POO)
* JSON
* Git
* GitHub

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/LetiMonteiro/Registronacionaldepessoas.git
```

Entre na pasta do projeto:

```bash
cd Registronacionaldepessoas
```

Execute a aplicação:

```bash
python main.py
```

---

## Conceitos Aplicados

Durante o desenvolvimento foram utilizados conceitos importantes de Engenharia de Software e Programação Orientada a Objetos, como:

* Encapsulamento;
* Herança;
* Polimorfismo;
* Abstração;
* Modularização;
* Separação de responsabilidades;
* Persistência de dados com SQLite;
* Controle de versão utilizando Git e GitHub.

---

##  Autora

**Letícia Monteiro**

Estudante de Ciência da Computação.

Projeto desenvolvido para a disciplina de **Engenharia de Software**, com o objetivo de aplicar conceitos de orientação a objetos, persistência de dados e boas práticas de desenvolvimento de software.
