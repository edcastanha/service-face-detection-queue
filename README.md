# service-face-detection-queue
Consumers para tratamento de frames de CFTV para detectar faces e encaminhar para fila de proximo tratamento.

## Do Objetivo:

O objetivo, além de praticar a modelagem tática e pattern do DDD¹.

Escopo - percorrer uma pasta FTP², verificar se as subpastas seguem um padrão de nomenclatura AAAA-MM-DD (ano-mês-dia) e, em seguida, publicar mensagens em um sistema de mensagens (possivelmente um sistema de filas, como RabbitMQ).
Usaremos uma abordagem afim de praticar a analise de modelos para criação da aplicação mais proxima a uma produção.

DESAFIOS:

* Identificar e isolar a lógica.
    - Isolar essa lógica em uma classe ou módulo separado que lidará exclusivamente com a comunicação com o serviço de mensageria. 
    - Essa classe será uma espécie de "porta" para o domínio de publicação de mensagens.

* Definir uma interface para essa comunicação: 
    - Criar uma interface que descreva os métodos necessários para interagir com o sistema de mensagens. 
    Por exemplo, métodos para publicar mensagens, estabelecer conexões, etc.

* Implementar a classe Publisher usando essa interface: 
    - A classe Publisher agora usaria essa interface para interagir com o serviço. Isso desacoplará a lógica específica do serviço da classe Publisher, tornando-a mais genérica e independente da infraestrutura.

* Tratar a formatação das mensagens como um serviço: 
    - Se houver lógica significativa para formatar as mensagens antes de enviá-las para o serviço.
    Isso poderá ser isolado em um serviço separado.

Essas são apenas algumas diretrizes gerais. Em essência, aplicar o DDD envolverá a identificação e a separação das preocupações do domínio específico (publicação de mensagens) e a criação de interfaces e abstrações que desacoplam a lógica do domínio da infraestrutura técnica.


<< ------------------ >>
Referencias: 
1 - Domain-Driven Design: !A fazer!
2 - FTP : !A fazer!
3 - Mensageria: !A fazer!