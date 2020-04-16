from __future__ import print_function
import logging

import grpc

from magnet_pb2 import MagnetRequest, MagnetReply
import magnet_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = magnet_pb2_grpc.MagnetStub(channel)
        request = MagnetRequest(imdb_id="SOME VALUE")
        response = stub.GetMagnet(request)
        print(f"Received: {response.url}")
        print(f"Response Type is: {type(response)}")

if __name__ == '__main__':
    logging.basicConfig()
    run()
