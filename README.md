# Case AB InBev - Igor França

Este projeto implementa um pipeline de dados utilizando Apache Airflow para consumir, transformar e persistir dados da Open Brewery DB, seguindo a arquitetura Medallion (Bronze, Silver e Gold).

**Obs.**: A extração está limitada as 100 primeiras páginas da API para evitar longos tempos de execução, já que o total ultrapassa 3.000 páginas.

## Pré-requisitos

- Docker Desktop instalado e em execução
- Git (para clonar o repositório)

## Estrutura do Projeto

```
CASE_AB_INBEV/
├── airflow/
│ ├── Dockerfile
│ └── requirements.txt
├── dags/
│ └── case_abinbev_pipeline.py
├── datalake/
│ ├── bronze/
│ ├── silver/
│ └── gold/
├── elt/
│ ├── extract.py
│ ├── load.py
│ └── transform.py
├── docker-compose.yml
├── README.md
```

## Como Executar

Para executar o pipeline:

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

### Componentes ELT

- **extract.py:** Responsável pela extração de dados das fontes
- **transform.py:** Aplica transformações e limpeza nos dados
- **load.py:** Carrega os dados processados no data lake

## Configuração

### Volumes Docker

O projeto utiliza volumes Docker para persistir os dados processados:

- `./datalake:/app/datalake` - Mapeia a pasta local `datalake` para dentro do container

### Arquivos de Configuração

- **airflow/Dockerfile**: Configura a imagem do Airflow
- **airflow/requirements.txt**: Dependências do projeto
- **docker-compose.yml**: Orquestra os serviços do Airflow

## Logs e Monitoramento

Todos os logs de execução estão disponíveis na interface web do Airflow, na aba **DAGs > Logs**


## Suporte

Para dúvidas ou problemas:

- **Igor França** 
- **Email:** igorffrancaa@gmail.com
- Verifique se o Docker Desktop está em execução
