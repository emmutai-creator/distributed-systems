import grpc
import hello_pb2
import hello_pb2_grpc

with grpc.insecure_channel(
    'localhost:50051'
) as channel:

    stub = hello_pb2_grpc.GreeterStub(channel)

    response = stub.SayHello(
        hello_pb2.HelloRequest(name='World')
    )

    print(response.message)