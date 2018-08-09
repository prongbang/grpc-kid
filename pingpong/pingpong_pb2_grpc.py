# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pingpong_pb2 as pingpong__pb2


class PingpongerStub(object):
  """The pingpong service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/pingpong.Pingponger/Ping',
        request_serializer=pingpong__pb2.PingRequest.SerializeToString,
        response_deserializer=pingpong__pb2.PongResponse.FromString,
        )


class PingpongerServicer(object):
  """The pingpong service definition
  """

  def Ping(self, request, context):
    """Sends a ping
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PingpongerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=pingpong__pb2.PingRequest.FromString,
          response_serializer=pingpong__pb2.PongResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pingpong.Pingponger', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))