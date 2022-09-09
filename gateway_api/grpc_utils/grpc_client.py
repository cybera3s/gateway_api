import grpc

from .user_proto import user_pb2
from .user_proto.user_pb2_grpc import UserControllerStub
from api.models import User


class Client:
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        # bind the client and the server
        self.stub = UserControllerStub(self.channel)
