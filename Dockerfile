FROM alpine:latest

RUN apk add --update curl python3 bash

COPY deps/python.txt /

RUN curl -s https://bootstrap.pypa.io/get-pip.py | python3
RUN pip install --disable-pip-version-check -r python.txt

COPY src/ src/

RUN pip install /src/

RUN adduser -D myuser
USER myuser

CMD bot
