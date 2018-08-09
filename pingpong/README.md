# Ping Pong Service

## Generating client and server code

- Install the grpcio-tools package:

```
$ pip install grpcio-tools
```

- Install the googleapis-common-proto package which is a collection of generated python classes for some common protos:

```
$ pip install googleapis-common-protos
```

- Use the following command to generate the Python code:

```
$ python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/pingpong.proto
```

## Creating the server

- server.py

```python
"""The Python implementation of the GRPC pingpong.Pingponger server."""

from concurrent import futures
import time
import math

import grpc

import pingpong_pb2
import pingpong_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class PingpongerServicer(pingpong_pb2_grpc.PingpongerServicer):
    """Provides methods that implement functionality of pingpong server."""

    def Ping(self, request, context):
        pingpong_pb2.PongResponse(message='%s, Pong!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    pingpong_pb2_grpc.add_PingpongerServicer_to_server(PingpongerServicer(), server)

    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
```

- client.py

```python
"""The Python implementation of the GRPC pingpong.Pingponger client."""

from __future__ import print_function

import grpc

import pingpong_pb2
import pingpong_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = pingpong_pb2_grpc.PingpongerStub(channel)
        response = stub.Ping(pingpong_pb2.PingRequest(name='Ping'))
    print("Pingpong client received: " + response.message)

if __name__ == '__main__':
    run()
```

## Run service

- Server

```
$ python server.py
```

- Client

```
$ python client.py
```

### Reference
- [https://grpc.io/docs/tutorials/basic/python.html](https://grpc.io/docs/tutorials/basic/python.html)
- [https://github.com/grpc/grpc/blob/v1.14.x/examples/python/helloworld](https://github.com/grpc/grpc/blob/v1.14.x/examples/python/helloworld)

