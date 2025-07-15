# Case AB InBev - Igor França

Este projeto implementa um pipeline de dados para processamento e análise de dados da AB InBev, com suporte para execução local ou utilizando Apache Airflow como orquestrador.

## Pré-requisitos

- Docker Desktop instalado e em execução
- Git (para clonar o repositório)

## Estrutura do Projeto

```
CASE_AB_INBEV/
├── airflow/
│   ├── Dockerfile
│   └── requirements.txt
├── dags/
│   └── case_abinbev_pipeline.py
├── datalake/
│   ├── bronze/
│   ├── gold/
│   └── silver/
├── etl/
│   ├── extract.py
│   ├── load.py
│   └── transform.py
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

## Como Executar

### Opção 1: Execução Local

Para executar o pipeline localmente utilizando Docker:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/igorffranca/Case_AB_INBEV.git
   cd CASE_AB_INBEV
   ```

2. **Certifique-se de que o Docker Desktop está em execução**

3. **Construa a imagem Docker:**
   ```bash
   docker build -t case-abinbev-igorfranca .
   ```

4. **Execute o container:**
   - No PowerShell (Windows):
     ```powershell
     docker run --rm -v "${PWD}/datalake:/app/datalake" case-abinbev-igorfranca
     ```
   - No Terminal Unix/Linux/Mac:
     ```bash
     docker run --rm -v "$(pwd)/datalake:/app/datalake" case-abinbev-igorfranca
     ```

### Opção 2: Execução com Apache Airflow

Para executar o pipeline utilizando Apache Airflow como orquestrador:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/igorffranca/Case_AB_INBEV.git
   cd CASE_AB_INBEV
   ```

2. **Certifique-se de que o Docker Desktop está em execução**

3. **Construa as imagens Docker:**
   ```bash
   docker compose build
   ```

4. **Inicialize o banco de dados do Airflow:**
   ```bash
   docker compose run airflow-webserver airflow db init
   ```

5. **Crie o usuário administrador:**
   ```bash
   docker compose run airflow-webserver airflow users create --username airflow --password airflow --firstname Igor --lastname França --role Admin --email igorffrancaa@gmail.com
   ```

6. **Inicie os serviços do Airflow:**
   ```bash
   docker compose up
   ```

7. **Acesse a interface web do Airflow:**
   - **URL:** http://localhost:8080
   - **Usuário:** airflow
   - **Senha:** airflow

## Pipeline de Dados

O pipeline implementa a arquitetura de Medallion com três camadas:

- **Bronze:** Dados brutos extraídos das fontes
- **Silver:** Dados limpos e transformados
- **Gold:** Dados agregados e prontos para análise

### Componentes ETL

- **extract.py:** Responsável pela extração de dados das fontes
- **transform.py:** Aplica transformações e limpeza nos dados
- **load.py:** Carrega os dados processados no data lake

## Configuração

### Volumes Docker

O projeto utiliza volumes Docker para persistir os dados processados:

- `./datalake:/app/datalake` - Mapeia a pasta local `datalake` para dentro do container

### Arquivos de Configuração

- **Dockerfile (raiz):** Para execução local
- **airflow/Dockerfile:** Para execução com Airflow
- **docker-compose.yml:** Configuração dos serviços do Airflow
- **requirements.txt:** Dependências Python do projeto

## Logs e Monitoramento

- **Execução Local:** Os logs são exibidos diretamente no terminal
- **Execução com Airflow:** Os logs podem ser visualizados na interface web do Airflow

## Desenvolvimento

Para desenvolver ou modificar o pipeline:

1. Faça as alterações necessárias nos arquivos Python
2. Reconstrua a imagem Docker
3. Execute novamente o container

## Suporte

Para dúvidas ou problemas:

- **Email:** igorffrancaa@gmail.com
- Verifique se o Docker Desktop está em execução
- Confirme se as portas necessárias estão disponíveis (8080 para Airflow)

## Tecnologias Utilizadas

- Python
- Docker
- Apache Airflow
- Pandas (presumido)
- Docker Compose