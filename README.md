# Derivative Calculator
 
 * Arthur Henrique Chaves 
 * Júlio Lage
 * Lucas Caetano
 * Rian

## Contexto

Esse trabalho foi feito para a disciplina de Calculo 1 na PUC Minas, ele busca 
realizar a derivada de polinomios simples, descobrir o resultado da função em um 
determinado valor de `X` e retornar a função da reta tangente

## Organização do repositório

Ele foi feito no modelo MVC (Model View Controler) que separa os codigos de 
visualização na pasta view, os codigo que realiza o calculo da derivada esta na 
pasta model, e os controlers servem para interligar os codigos das duas outras 
pastas.

```
├── Trabalho ISI
│
│
├── controler/
│   └── controler.py (Codigo que recebe as entradas do usuario da view manda para o
│       código que calcula e retorna os resultados para a view)
│
├── docs/ (documentos do projeto)
│   └── trabalho cálculo 1.pdf (pdf que tem as informações do trabalho)
│
├── model/ 
│   └── calc.py (Código que calcula a derivada e retorna os valores para o model)
│
├── view/ 
│   ├── entries.py (arquivo que cria o local de entrada da função)
│   │
│   ├── popUp.py (arquivo que cria o popUp que tem o tutorial de como inserir a 
│   │   função)
│   │
│   ├── resultados.py (Código que cria e mostra os resultados das derivada)
│   │
│   └── view.py (código principal, ele contem as informações iniciais e a tela 
│       principal)
│
└── README.md

```