import grpc

from .protos import user_pb2
from .protos.user_pb2_grpc import UserControllerStub
from api.models import User


class Client:
    """
        Used for initializing GRPC client and communicate with GRPC Server
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        # bind the client and the server
        self.stub = UserControllerStub(self.channel)

    def get_users_list(self) -> list:
        """
            returns list of all users fetched from GRPC server
        """
        return list(self.stub.List(user_pb2.UserListRequest()))

    def create_new_user(self, user: User) -> user_pb2.User:
        """
            creates a new User with provided user object
            then returns newly created user as response
        """
        response = self.stub.Create(
            user_pb2.User(
                username=user.username,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                password=user.password
            )
        )
        return response

    def get_user_by_id(self, id: int) -> user_pb2.User:
        """
            get a user by provided id then returns fetched User as response
        """
        return self.stub.Retrieve(user_pb2.UserRetrieveRequest(id=id))

    def update_user(self, id: int, user: User) -> user_pb2.User:
        """
            updates an existing user with provided user ID and User model as payload
            then returns updated user object as response
        """
        response = self.stub.Update(
            user_pb2.User(id=id,
                          username=user.username,
                          first_name=user.first_name,
                          last_name=user.last_name,
                          email=user.email,
                          password=user.password
                          ))
        return response

    def delete_user_by_id(self, id: int):
        """
            Deletes a user with provided user ID
        """
        return self.stub.Destroy(user_pb2.User(id=id))
