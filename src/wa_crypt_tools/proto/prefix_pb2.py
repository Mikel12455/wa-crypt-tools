# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prefix.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import wa_crypt_tools.proto.C14_cipher_pb2 as C14__cipher__pb2
import wa_crypt_tools.proto.C15_IV_pb2 as C15__IV__pb2
import wa_crypt_tools.proto.key_type_pb2 as key__type__pb2
import wa_crypt_tools.proto.version_features_pb2 as version__features__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cprefix.proto\x1a\x10\x43\x31\x34_cipher.proto\x1a\x0c\x43\x31\x35_IV.proto\x1a\x0ekey_type.proto\x1a\x16version_features.proto\"\x93\x01\n\x06prefix\x12\x1b\n\x08key_type\x18\x01 \x01(\x0e\x32\t.Key_Type\x12!\n\nc14_cipher\x18\x02 \x01(\x0b\x32\x0b.C14_cipherH\x00\x12\x19\n\x06\x63\x31\x35_iv\x18\x03 \x01(\x0b\x32\x07.C15_IVH\x00\x12\x1f\n\x04info\x18\x04 \x01(\x0b\x32\x11.Version_FeaturesB\r\n\x0b\x63ipher_infob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'prefix_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PREFIX']._serialized_start=89
  _globals['_PREFIX']._serialized_end=236
# @@protoc_insertion_point(module_scope)
