# Sistema de Análise de Desempenho Acadêmico

## Descrição
Esse projeto foi desenvolvido para ajudar a analisar o desempenho dos alunos de forma mais rápida e organizada.

A ideia é automatizar o cálculo das médias, identificar quem está em recuperação e também destacar o aluno com melhor desempenho.



## Objetivo
- Calcular a média dos alunos
- Identificar alunos em recuperação (média menor que 7)
- Identificar o aluno com maior média (Top Student)
- Gerar um relatório em arquivo `.txt`



## Tecnologias utilizadas
- Python
- Git e GitHub



## Mapa de Empatia

![Mapa de Empatia](./img/mapa-empatia.png)



## Kanban

### Print
![Kanban](./img/kanban.png)

### Link
[Ver Kanban](COLE_AQUI_O_LINK)



## Requisitos Funcionais
- Ler lista de alunos e suas notas  
- Validar se os dados estão corretos  
- Calcular média das notas  
- Identificar alunos em recuperação  
- Identificar o melhor aluno  
- Gerar relatório em arquivo  



## Requisitos Não Funcionais
- Código organizado em arquivos separados  
- Tratamento de dados inválidos  
- Código simples e fácil de entender  
- Uso de Git com commits e branches  



## Regras de Negócio
- Média menor que 7 → recuperação  
- Maior média → Top Student  
- Dados inválidos são ignorados  


## Como executar

1. Clone o repositório:
https://github.com/igorViniciws/desempenho-academico-senai

2. Ente na pasta:

cd desempenho-academico-senai


3. Rode o programa:

python main.py


---

## Saída do sistema

O programa gera um arquivo "resultado.txt" com o resultado da análise.

Por exemplo:


RELATÓRIO DE DESEMPENHO ACADÊMICO

Alunos em Recuperação:
Maria - Média: 5.50

Top Student:
João - Média: 9.33



## Autor
Igor Vinicius Santos Vicente
