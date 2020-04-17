from __future__ import print_function
import logging

import grpc

from magnet_pb2 import MagnetRequest, MagnetReply
import magnet_pb2_grpc


def run():
    with grpc.secure_channel('grpc-moviedranegetmagnet-eub7v2b6nq-uw.a.run.app:443', grpc.ssl_channel_credentials()) as channel:
    # with grpc.insecure_channel('https://grpc-moviedranegetmagnet-eub7v2b6nq-uw.a.run.app:443') as channel:
        stub = magnet_pb2_grpc.MagnetStub(channel)
        request = MagnetRequest(imdb_id="tt7146812")
        response = stub.GetMagnet(request)
        print(f"Received: {response.url}")
        print(f"Response Type is: {type(response)}")

if __name__ == '__main__':
    logging.basicConfig()
    run()
