from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12\x08\x63ommonpb\"\x07\n\x05\x45mpty\"N\n\x07Request\x12\r\n\x05\x41sync\x18\x01 \x01(\x08\x12\x0f\n\x07Timeout\x18\x02 \x01(\x03\x12\x10\n\x08\x42\x65\x61\x63onID\x18\x08 \x01(\t\x12\x11\n\tSessionID\x18\t \x01(\t\"H\n\x08Response\x12\x0b\n\x03\x45rr\x18\x01 \x01(\t\x12\r\n\x05\x41sync\x18\x02 \x01(\x08\x12\x10\n\x08\x42\x65\x61\x63onID\x18\x08 \x01(\t\x12\x0e\n\x06TaskID\x18\t \x01(\t\"\"\n\x04\x46ile\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0c\n\x04\x44\x61ta\x18\x02 \x01(\x0c\"\x81\x01\n\x07Process\x12\x0b\n\x03Pid\x18\x01 \x01(\x05\x12\x0c\n\x04Ppid\x18\x02 \x01(\x05\x12\x12\n\nExecutable\x18\x03 \x01(\t\x12\r\n\x05Owner\x18\x04 \x01(\t\x12\x14\n\x0c\x41rchitecture\x18\x07 \x01(\t\x12\x11\n\tSessionID\x18\x05 \x01(\x05\x12\x0f\n\x07\x43mdLine\x18\x06 \x03(\t\"$\n\x06\x45nvVar\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\tB/Z-github.com/bishopfox/sliver/protobuf/commonpbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/bishopfox/sliver/protobuf/commonpb'
  _EMPTY._serialized_start=26
  _EMPTY._serialized_end=33
  _REQUEST._serialized_start=35
  _REQUEST._serialized_end=113
  _RESPONSE._serialized_start=115
  _RESPONSE._serialized_end=187
  _FILE._serialized_start=189
  _FILE._serialized_end=223
  _PROCESS._serialized_start=226
  _PROCESS._serialized_end=355
  _ENVVAR._serialized_start=357
  _ENVVAR._serialized_end=393