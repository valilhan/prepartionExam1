import grpc
import grpc_tools.protoc

import proto.unary_pb2
import proto.unary_pb2_grpc

with grpc.insecure_channel("localhost:50001") as chanel:
    stub = proto.unary_pb2_grpc.QueueServiceStub(channel=chanel)
    while True:
        command = input()
        command = command.split()
        if command[0] == 'size':
            size = stub.size(proto.unary_pb2.Empty(send=1))
            print(size)
        elif command[0] == 'put':
            put = stub.put(proto.unary_pb2.newElement(element=command[1]))
            print(put)
        elif command[0] == 'pop':
            pop = stub.pop(proto.unary_pb2.Empty(send=1))
            print(pop)
        elif command[0] == 'pick':
            pick = stub.pick(proto.unary_pb2.Empty(send=1))
            print(pick)
