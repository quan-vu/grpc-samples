# Author: Quan Vu
# Description: A simple implement gRPC 

from concurrent import futures
import logging

import grpc

from products_pb2 import Product, Products
from products_pb2_grpc import productsStub, productsServicer, add_productsServicer_to_server

from storage import Storage

class ProductService(productsServicer):

    storage = Storage()

    def list_products(self, request, context):
        products = self.storage.get_all()
        return Products(products=[{**product} for product in products])
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_productsServicer_to_server(ProductService(), server)
    server.add_insecure_port('[::]:50051')  # Don't use this in production
    server.start()
    print('Started product service at: 127.0.1:50051')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
    