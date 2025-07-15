FROM apache/airflow:2.8.1-python3.10

USER root
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

COPY airflow/requirements.txt .

USER airflow
RUN pip install --no-cache-dir --user -r requirements.txt

