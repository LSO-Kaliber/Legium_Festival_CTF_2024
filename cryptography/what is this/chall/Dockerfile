FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 socat python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pycryptodome egcd

RUN mkdir -p /opt/chall

WORKDIR /opt/chall

COPY *.py .

EXPOSE 42062

SHELL ["/bin/bash", "-c"]

CMD socat TCP-LISTEN:42062,reuseaddr,fork EXEC:"python3 -u server.py"
