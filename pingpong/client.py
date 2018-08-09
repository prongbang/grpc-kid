"""The Python implementation of the GRPC pingpong.Pingponger client."""

from __future__ import print_function

import grpc

import pingpong_pb2
import pingpong_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = pingpong_pb2_grpc.PingpongerStub(channel)
        response = stub.Ping(pingpong_pb2.PingRequest(name='Ping'))
        print("Pingpong client received: " + str(response.message))

if __name__ == '__main__':
    run()