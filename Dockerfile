FROM python:latest

WORKDIR /usr/src/app

RUN apt-get update -y && apt-get install -y software-properties-common && \
    apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main' && \
    apt-get update -y && apt-get install -y openjdk-8-jdk && \
    apt-get install -y vim

COPY main.py /usr/src/app/.
COPY configurations.py /usr/src/app/.
COPY config.jmx /usr/src/app/.
COPY impala-autoscale /usr/src/app/.

RUN chmod +x main.py && chmod +x configurations.py && chmod +x impala-autoscale && \
    wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.4.3.tgz && tar -xvzf apache-jmeter-5.4.3.tgz

COPY ImpalaJDBC42.jar /usr/src/app/apache-jmeter-5.4.3/lib/.

ENV PATH="/usr/src/app:${PATH}"