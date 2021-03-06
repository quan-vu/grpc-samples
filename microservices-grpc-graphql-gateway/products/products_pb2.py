# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='products.proto',
  package='products',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0eproducts.proto\x12\x08products\"i\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x1a\n\x12passenger_capacity\x18\x03 \x01(\x05\x12\x15\n\rmaximum_speed\x18\x04 \x01(\x05\x12\x10\n\x08in_stock\x18\x05 \x01(\x05\"/\n\x08Products\x12#\n\x08products\x18\x01 \x03(\x0b\x32\x11.products.Product\"\x18\n\nGetProduct\x12\n\n\x02id\x18\x01 \x01(\x05\"\r\n\x0bGetProducts2\xb6\x01\n\x08products\x12\x36\n\x0bget_product\x12\x14.products.GetProduct\x1a\x11.products.Product\x12\x36\n\x0e\x63reate_product\x12\x11.products.Product\x1a\x11.products.Product\x12:\n\rlist_products\x12\x15.products.GetProducts\x1a\x12.products.Productsb\x06proto3'
)




_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='products.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='products.Product.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='products.Product.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passenger_capacity', full_name='products.Product.passenger_capacity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_speed', full_name='products.Product.maximum_speed', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in_stock', full_name='products.Product.in_stock', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=133,
)


_PRODUCTS = _descriptor.Descriptor(
  name='Products',
  full_name='products.Products',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='products', full_name='products.Products.products', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=182,
)


_GETPRODUCT = _descriptor.Descriptor(
  name='GetProduct',
  full_name='products.GetProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='products.GetProduct.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=208,
)


_GETPRODUCTS = _descriptor.Descriptor(
  name='GetProducts',
  full_name='products.GetProducts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=223,
)

_PRODUCTS.fields_by_name['products'].message_type = _PRODUCT
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Products'] = _PRODUCTS
DESCRIPTOR.message_types_by_name['GetProduct'] = _GETPRODUCT
DESCRIPTOR.message_types_by_name['GetProducts'] = _GETPRODUCTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:products.Product)
  })
_sym_db.RegisterMessage(Product)

Products = _reflection.GeneratedProtocolMessageType('Products', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTS,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:products.Products)
  })
_sym_db.RegisterMessage(Products)

GetProduct = _reflection.GeneratedProtocolMessageType('GetProduct', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCT,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:products.GetProduct)
  })
_sym_db.RegisterMessage(GetProduct)

GetProducts = _reflection.GeneratedProtocolMessageType('GetProducts', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTS,
  '__module__' : 'products_pb2'
  # @@protoc_insertion_point(class_scope:products.GetProducts)
  })
_sym_db.RegisterMessage(GetProducts)



_PRODUCTS = _descriptor.ServiceDescriptor(
  name='products',
  full_name='products.products',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=226,
  serialized_end=408,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_product',
    full_name='products.products.get_product',
    index=0,
    containing_service=None,
    input_type=_GETPRODUCT,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='create_product',
    full_name='products.products.create_product',
    index=1,
    containing_service=None,
    input_type=_PRODUCT,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='list_products',
    full_name='products.products.list_products',
    index=2,
    containing_service=None,
    input_type=_GETPRODUCTS,
    output_type=_PRODUCTS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCTS)

DESCRIPTOR.services_by_name['products'] = _PRODUCTS

# @@protoc_insertion_point(module_scope)
