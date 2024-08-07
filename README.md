<h1>Bank System Python</h1>
Sistema Bancário em Python que simula operações de depósito, saque e extrato, desenvolvido para um banco focado em monetizar suas operações.


## Descrição

O projeto é um excercício prático do curso de Python Backend Developer do site da DIO.

O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema foi desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, tive a chance de aplicar meus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Estou preparado para aprimorar minhas habilidades e demonstrar que tenho capacidade de desenvolver soluções práticas e eficientes.


## Funcionalidades

**Depósito:** Permite que o usuário deposite um valor positivo em sua conta, aumentando o saldo.
**Saque:** Permite que o usuário realize saques, desde que possua saldo suficiente, respeite o limite diário de saque e o número máximo de saques permitidos.
**Extrato:** Exibe todas as movimentações da conta (depósitos e saques) e o saldo atual.


## Explicação do Código

**Menu Interativo:** O código inicia com a definição de um menu interativo que oferece opções para depósito, saque, visualização de extrato ou saída do programa.

**Depósito (d):** O usuário pode depositar um valor positivo, que será adicionado ao saldo. Se o valor for inválido (por exemplo, negativo), uma mensagem de erro será exibida e se for algo além de uma número o bloco except entra em ação e uma mensagem de erro também será exibida.

**Saque (s):** O usuário pode sacar um valor, desde que tenha saldo suficiente, não ultrapasse o limite diário de R$500 e respeite o limite de até 3 saques por dia.
Se o valor solicitado exceder o saldo, limite ou o número máximo de saques, uma mensagem de erro será exibida.

**Extrato (e):** Exibe todas as transações realizadas (depósitos e saques) e o saldo atual. Caso não tenha ocorrido nenhuma transação, o extrato exibirá uma mensagem informando que não houve movimentações.

**Saída (q):** Permite ao usuário sair do sistema.


## Como Executar

**Clone o Repositório:** git clone https://github.com/EduAraujo2/bank-system-python.git

**Navegue até o Diretório do Projeto:** cd bank-system-python

**Execute o Script:** python sistema_bancario.py


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
