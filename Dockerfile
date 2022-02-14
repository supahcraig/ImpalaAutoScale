FROM python:latest

WORKDIR /usr/src/app

RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main' && \
    apt-get update -y && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y vim && \
    wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.4.3.tgz && \
    tar -xvzf apache-jmeter-5.4.3.tgz && \
    rm apache-jmeter-5.4.3.tgz

COPY ias /usr/src/app/.
COPY runtime_jmx.py /usr/src/app/.
COPY configurations.py /usr/src/app/.
COPY config.jmx /usr/src/app/.
COPY impala-autoscale.sh /usr/src/app/.

RUN chmod +x ias && chmod +x impala-autoscale.sh && \
    echo 'export PS1="\[\e[1;38;5;202m\]ImpalaAutoscale \w \[\e[0m\]\\$> "' >> /root/.bashrc

COPY ImpalaJDBC42.jar /usr/src/app/apache-jmeter-5.4.3/lib/.

ENV PATH="/usr/src/app:${PATH}"

CMD ["/bin/bash"]