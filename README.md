# service-face-detection-queue

## Objetivo:

O objetivo principal deste projeto é a prática da modelagem tática e padrões do Domain-Driven Design (DDD)¹. O escopo inclui a varredura de uma pasta FTP², verificação do padrão de nomenclatura AAAA-MM-DD (ano-mês-dia) nas subpastas e, em seguida, a publicação de mensagens em um sistema de filas, como RabbitMQ. A abordagem adotada visa aprimorar a análise de modelos para criar uma aplicação mais próxima das condições de produção.

### Desafios:

1. Identificar e isolar a lógica:
   - Isolar a lógica em uma classe ou módulo separado, dedicado exclusivamente à comunicação com o serviço de mensageria. Essa classe atuará como uma "porta" para o domínio de publicação de mensagens.

2. Definir uma interface para comunicação:
   - Criar uma interface que descreva os métodos necessários para interagir com o sistema de mensagens. Exemplo de métodos incluem publicação de mensagens, estabelecimento de conexões, entre outros.

3. Implementar a classe Publisher utilizando a interface:
   - A classe Publisher deve utilizar essa interface para interagir com o serviço. Esse desacoplamento da lógica específica do serviço torna a classe mais genérica e independente da infraestrutura.

4. Tratar a formatação das mensagens como um serviço:
   - Se houver lógica significativa para formatar as mensagens antes do envio para o serviço, essa tarefa pode ser isolada em um serviço separado.

Essas diretrizes proporcionam uma visão geral do processo. Em essência, a aplicação do DDD envolve a identificação e separação das preocupações específicas do domínio (publicação de mensagens), além da criação de interfaces e abstrações que desacoplam a lógica do domínio da infraestrutura técnica.

<< ------------------ >>

### Referências:
1. [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)
2. FTP (A fazer)
3. Mensageria (A fazer)