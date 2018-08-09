
"""The Python implementation of the GRPC pingpong.Pingponger server."""

from concurrent import futures
import time
import math

import grpc

import pingpong_pb2
import pingpong_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Pingponger(pingpong_pb2_grpc.PingpongerServicer):

    def Ping(self, request, context):
        print("Request: %s" % request.name)
        return pingpong_pb2.PongResponse(message='%s, Pong' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pingpong_pb2_grpc.add_PingpongerServicer_to_server(Pingponger(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()