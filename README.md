# Mini Sistema Médico em Python

## Descrição

Este projeto é um sistema simples desenvolvido em Python para simular o cadastro e gerenciamento de fichas médicas.

O programa permite registrar informações pessoais do paciente e realizar análises básicas de saúde, incluindo:

- cálculo do IMC
- avaliação de saúde mental
- registro do ciclo menstrual (se o usuário for do sexo feminino) 
- armazenamento das fichas em uma biblioteca médica

Todos os dados são armazenados em memória durante a execução do programa.

---

## Funcionalidades

### Cadastro de pacientes
Permite cadastrar:
- nome completo
- idade
- sexo

### Análise de IMC
Calcula o Índice de Massa Corporal e classifica o resultado em:
- abaixo do peso
- peso ideal
- sobrepeso
- obesidade

### Avaliação de saúde mental
Analisa:
- média de horas de sono
- rotina do paciente
- humor atual

Com base nas respostas, o sistema gera observações de melhoria baseadas na informação das horas de sono.

### Registro de ciclo menstrual
Disponível para pacientes do sexo feminino:
- data da última menstruação
- duração do fluxo
- duração média do ciclo
- observações sobre anomalias

Também calcula a próxima previsão do ciclo.

### Biblioteca médica
Armazena as fichas cadastradas e exibe um relatório geral detalhado.

---

## Tecnologias utilizadas

- Python 3
- Biblioteca `datetime`

---

## Objetivo do Projeto: 
Este projeto foi desenvolvido com fins acadêmicos para praticar conceitos fundamentais de programação em Python, como:

- funções
- estruturas condicionais
- listas e dicionários
- menus interativos
- manipulação de datas com datetime

## Melhorias Futuras: 
- salvar dados em arquivos
- busca de pacientes por nome
- exclusão e edição de fichas
- interface gráfica
- integração com banco de dados

```bash
sistema-medico-python/
│── main.py
│── README.md
