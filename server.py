from concurrent import futures
import logging
import grpc
import os
import magnet_pb2_grpc
from magnet_pb2 import MagnetRequest, MagnetReply
from lib.yify import YifyApi, YifyRequest, YifyResponse


_PORT = os.environ["PORT"]


class Magnet(magnet_pb2_grpc.MagnetServicer):
    def GetMagnet(self, request: MagnetRequest, context) -> MagnetReply:
        imdb_id = request.imdb_id
        try:
            logging.info(f"Trying Yify with IMDB ID: {imdb_id}")
            req = YifyRequest(imdb_id=imdb_id)
            query = YifyApi(req)
            if hasattr(query, 'response'):
                return MagnetReply(url=query.response.magnet_link)
            else:
                return MagnetReply(url="")
        except Exception as error:
            logging.error(f"Magnet.GetMagnet Yify failed: {error}")


def _serve(port: str) -> None:
    bind_address = f"[::]:{port}"
    server = grpc.server(futures.ThreadPoolExecutor())
    magnet_pb2_grpc.add_MagnetServicer_to_server(Magnet(), server)
    server.add_insecure_port(bind_address)
    server.start()
    logging.info(f"Listening on {bind_address}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _serve(_PORT)
