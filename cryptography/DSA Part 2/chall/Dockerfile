FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 socat python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pycryptodome sympy

RUN mkdir -p /opt/chall

WORKDIR /opt/chall

COPY *.py .

EXPOSE 42061

CMD socat TCP-LISTEN:42061,reuseaddr,fork EXEC:"python3 -u chall.py"
