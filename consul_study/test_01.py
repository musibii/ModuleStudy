# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test_01.py
# __time__  : 2020/5/18 1:56 下午

import os
import signal
import socket
import sys
import time
from concurrent.futures.thread import ThreadPoolExecutor

import consul
import grpc
import logging

from apollo.services.stubs.health_check import (
    health_check_pb2_grpc
)
from apollo.services.health_check import (
    HealthCheckService
)
from apollo.services.stubs.auth import (
    auth_pb2_grpc
)
from apollo.services.auth import (
    AuthService
)


def register(service_name, ip, port):
    c = consul.Consul(host=os.getenv('APOLLO_CONSUL_HOST'))
    logging.info(f"register {service_name}")
    check = {
        'name': 'grpc server health check',
        'grpc': f'{ip}:{port}',
        'interval': '10s'
    }
    c.agent.service.register(service_name, f"{service_name}-{ip}-{port}",
                             address=ip, port=port, check=check)
    logging.info(f"register success {service_name}")


def unregister(service_name, ip, port):
    c = consul.Consul(host=os.getenv('APOLLO_CONSUL_HOST'))
    logging.info(f"deregister {service_name}")
    c.agent.service.deregister(f'{service_name}-{ip}-{port}')
    logging.info(f"deregister success {service_name}")


def serve():
    service_name = 'apollo'
    ip = socket.gethostbyname(socket.gethostname())
    port = 58550

    def exit_handler(signal, frame):
        unregister(service_name, ip, port)

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    health_check_pb2_grpc.add_HealthServicer_to_server(
        HealthCheckService(), server)
    auth_pb2_grpc.add_AuthServicer_to_server(AuthService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    register(service_name, ip, port)
    signal.signal(signal.SIGTERM, exit_handler)

    while True:
        time.sleep(1)


if __name__ == '__main__':
    serve()