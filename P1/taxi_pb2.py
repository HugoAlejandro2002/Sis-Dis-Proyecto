# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: taxi.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='taxi.proto',
  package='taxi',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntaxi.proto\x12\x04taxi\"^\n\x08TaxiTrip\x12\x0f\n\x07taxi_id\x18\x01 \x01(\x03\x12\x14\n\x0c\x63onductor_id\x18\x02 \x01(\t\x12\x13\n\x0bpasajero_id\x18\x03 \x03(\t\x12\x16\n\x0e\x63osto_estimado\x18\x04 \x01(\x02\x62\x06proto3'
)




_TAXITRIP = _descriptor.Descriptor(
  name='TaxiTrip',
  full_name='taxi.TaxiTrip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='taxi_id', full_name='taxi.TaxiTrip.taxi_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conductor_id', full_name='taxi.TaxiTrip.conductor_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pasajero_id', full_name='taxi.TaxiTrip.pasajero_id', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='costo_estimado', full_name='taxi.TaxiTrip.costo_estimado', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['TaxiTrip'] = _TAXITRIP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaxiTrip = _reflection.GeneratedProtocolMessageType('TaxiTrip', (_message.Message,), {
  'DESCRIPTOR' : _TAXITRIP,
  '__module__' : 'taxi_pb2'
  # @@protoc_insertion_point(class_scope:taxi.TaxiTrip)
  })
_sym_db.RegisterMessage(TaxiTrip)


# @@protoc_insertion_point(module_scope)
