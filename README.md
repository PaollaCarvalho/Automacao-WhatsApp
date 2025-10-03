# Automacao-WhatsApp
Automação simples de envio de mensagens por WhatsApp

Este projeto é um exemplo de automação para enviar mensagens personalizadas a clientes via WhatsApp, desenvolvido em Python.
O objetivo é demonstrar automação de processos repetitivos e ganho de eficiência. No projeto em questão, estamos fazendo o envio diário de mensagens para os clientes aniversáriantes, focado em processos de pós vendas. 

💡 Flexível e expansível  
Embora o exemplo atual foque em mensagens de aniversário, a automação pode ser facilmente adaptada para outros contextos de pós-venda, como solicitar feedback, lembrar de ofertas ou promoções, ou qualquer outra situação que envolva envio automático de mensagens.

🔧 Como Funciona?

Esta automação inicia de uma planilha Excel (clientes.xlsx), que contém dados dos clientes, como nome, telefone, data de nascimento, data de última compra, etc. A partir dessas informações, oO script verifica condições definidas (ex.: aniversário) e envia automaticamente mensagens personalizadas.

A automação executa esse processo: 
1. Lê os dados de clientes de uma planilha com pandas;
2. Verifica a data de aniversário de cada cliente e cria uma lista com os aniversariantes do dia.
3. Acessa o WhatsaApp para cada cliente com a biblioteca PyWhatKit;
4. Digita e enviar mensagem (personalizada diretamente no script) com PyAutoGUI, simulando ação do usuário;
5. Repete o processo até concluir a lista completa;

Para rodar a automação é necessário que o WhatsApp esteja vinculado e aberto no navegador.
Nossa automação é acionada pelo Gerenciador de Tarefas e pode ser configurada para rodar diariamente, semanalmente ou mensalmente.

💻 Tecnologias e Bibliotecas: Python, Pandas, PyWhatKit e PyAutoGUI

⚠️ Aviso Importante  
O uso inadequado pode violar as políticas do WhatsApp e resultar em bloqueio de contas.
