FROM alpine:latest

ADD src /app

ENV PYUSB_DEBUG_LEVEL=debug

RUN apk add --no-cache \
    python3 \
    libusb-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

WORKDIR /app
RUN pip install -r requirements.txt

#ENTRYPOINT [ "python3" ]
#CMD [ "app.py" ]
CMD ["/bin/sh"]
