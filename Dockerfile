FROM python:3.9

LABEL maintainer="cybera.3s@gmail.com"
LABEL version="1.0.0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /gateway
# copy and install requirements
ADD gateway/requirements.txt .
# RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ADD gateway/gateway_api/ .

# Create user with associated group and assign permissions of current directory to it
RUN groupadd -r api && useradd --no-log-init -r -s /bin/bash -g api api && \
    chown -R api /gateway && chmod -R 777 /gateway
USER api

# Generate protobufs from user proto schema
RUN python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./grpc_utils/protos/user.proto

EXPOSE 8000
CMD python3 manage.py collectstatic --noinput && \
    gunicorn -b 0.0.0.0:8000 config.wsgi