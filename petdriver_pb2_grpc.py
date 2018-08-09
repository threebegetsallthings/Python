# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import petdriver_pb2 as petdriver__pb2


class PetDriverStub(object):
  """The pet driver service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendCommand = channel.unary_unary(
        '/driver.PetDriver/SendCommand',
        request_serializer=petdriver__pb2.Command.SerializeToString,
        response_deserializer=petdriver__pb2.CommandReply.FromString,
        )
    self.AcquireData = channel.unary_unary(
        '/driver.PetDriver/AcquireData',
        request_serializer=petdriver__pb2.AcqParam.SerializeToString,
        response_deserializer=petdriver__pb2.CommandReply.FromString,
        )


class PetDriverServicer(object):
  """The pet driver service definition
  """

  def SendCommand(self, request, context):
    """send command to pet driver and return command result
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AcquireData(self, request, context):
    """start acquire data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PetDriverServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendCommand': grpc.unary_unary_rpc_method_handler(
          servicer.SendCommand,
          request_deserializer=petdriver__pb2.Command.FromString,
          response_serializer=petdriver__pb2.CommandReply.SerializeToString,
      ),
      'AcquireData': grpc.unary_unary_rpc_method_handler(
          servicer.AcquireData,
          request_deserializer=petdriver__pb2.AcqParam.FromString,
          response_serializer=petdriver__pb2.CommandReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'driver.PetDriver', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
