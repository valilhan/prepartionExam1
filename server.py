import queue
from concurrent import futures

import grpc
import proto.unary_pb2
import proto.unary_pb2_grpc

Q = queue.Queue()


class QueueService(proto.unary_pb2_grpc.QueueService):
    def __init__(self, *args, **kwargs):
        pass

    def put(self, request, context):
        newElement = request.element
        Q.put(newElement)
        return proto.unary_pb2.Received(received=1)

    def pick(self, request, context):
        str = Q.queue[0]
        return proto.unary_pb2.newElement(element=str)

    def size(self, request, context):
        size = Q.qsize()
        return proto.unary_pb2.Size(size=size)

    def pop(self, request, context):
        str = Q.get()
        return proto.unary_pb2.newElement(element=str)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto.unary_pb2_grpc.add_QueueServiceServicer_to_server(QueueService(), server)
    server.add_insecure_port('[::]:50001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
