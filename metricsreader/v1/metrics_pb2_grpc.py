# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from metricsreader.v1 import metrics_pb2 as src_dot_controlplane_dot_metricsreader_dot_mrpb_dot_v1_dot_metrics__pb2


class MetricsReaderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RangeQuery = channel.unary_unary(
                '/gml.internal.controlplane.metricsreader.v1.MetricsReaderService/RangeQuery',
                request_serializer=src_dot_controlplane_dot_metricsreader_dot_mrpb_dot_v1_dot_metrics__pb2.RangeQueryRequest.SerializeToString,
                response_deserializer=src_dot_controlplane_dot_metricsreader_dot_mrpb_dot_v1_dot_metrics__pb2.RangeQueryResponse.FromString,
                )


class MetricsReaderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RangeQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetricsReaderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RangeQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.RangeQuery,
                    request_deserializer=src_dot_controlplane_dot_metricsreader_dot_mrpb_dot_v1_dot_metrics__pb2.RangeQueryRequest.FromString,
                    response_serializer=src_dot_controlplane_dot_metricsreader_dot_mrpb_dot_v1_dot_metrics__pb2.RangeQueryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gml.internal.controlplane.metricsreader.v1.MetricsReaderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MetricsReaderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RangeQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gml.internal.controlplane.metricsreader.v1.MetricsReaderService/RangeQuery',
            src_dot_controlplane_dot_metricsreader_dot_mrpb_dot_v1_dot_metrics__pb2.RangeQueryRequest.SerializeToString,
            src_dot_controlplane_dot_metricsreader_dot_mrpb_dot_v1_dot_metrics__pb2.RangeQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)