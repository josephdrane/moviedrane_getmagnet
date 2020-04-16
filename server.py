from concurrent import futures
import logging

import grpc

import magnet_pb2_grpc
from magnet_pb2 import MagnetRequest, MagnetReply


class Magnet(magnet_pb2_grpc.MagnetServicer):
    
    def GetMagnet(self, request: MagnetRequest, context) -> MagnetReply:
        print(f"Received Request: {request.imdb_id}")
        print(f"Request Type is : {request}")
        return MagnetReply(url="SOME URL HERE")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    magnet_pb2_grpc.add_MagnetServicer_to_server(Magnet(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()