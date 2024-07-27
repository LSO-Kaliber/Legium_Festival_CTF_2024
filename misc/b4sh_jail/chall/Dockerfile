FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 socat python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pycryptodome sympy

WORKDIR /home

COPY 159df48875627e2f7f66dae584c5e3a5 159df48875627e2f7f66dae584c5e3a5

COPY *.py .

SHELL ["/bin/bash", "-c"]

EXPOSE 42051

CMD socat TCP-LISTEN:42051,reuseaddr,fork EXEC:"python3 -u bash_jail.py"
