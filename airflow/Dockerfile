FROM apache/airflow:2.8.1-python3.10

# Etapa root - instalação de sistema
USER root
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Copia requirements antes de mudar de usuário
COPY requirements.txt .

# Muda para usuário airflow depois
USER airflow
RUN pip install --no-cache-dir --user -r requirements.txt

