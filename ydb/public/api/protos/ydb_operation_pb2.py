# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ydb_operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from protos.annotations import validation_pb2 as protos_dot_annotations_dot_validation__pb2
from protos import ydb_common_pb2 as protos_dot_ydb__common__pb2
from protos import ydb_issue_message_pb2 as protos_dot_ydb__issue__message__pb2
from protos import ydb_status_codes_pb2 as protos_dot_ydb__status__codes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/ydb_operation.proto',
  package='Ydb.Operations',
  syntax='proto3',
  serialized_options=b'\n\010tech.ydbB\017OperationProtosZ=github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Operations\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aprotos/ydb_operation.proto\x12\x0eYdb.Operations\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a#protos/annotations/validation.proto\x1a\x17protos/ydb_common.proto\x1a\x1eprotos/ydb_issue_message.proto\x1a\x1dprotos/ydb_status_codes.proto\"\xb6\x03\n\x0fOperationParams\x12\x45\n\x0eoperation_mode\x18\x01 \x01(\x0e\x32-.Ydb.Operations.OperationParams.OperationMode\x12\x34\n\x11operation_timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0c\x63\x61ncel_after\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12M\n\x06labels\x18\x04 \x03(\x0b\x32+.Ydb.Operations.OperationParams.LabelsEntryB\x10\xaa\xe6*\x05\n\x03\x18\x80\x01\xa2\xe6*\x03\x18\x80\x01\x12\x31\n\x10report_cost_info\x18\x05 \x01(\x0e\x32\x17.Ydb.FeatureFlag.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"D\n\rOperationMode\x12\x1e\n\x1aOPERATION_MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04SYNC\x10\x01\x12\t\n\x05\x41SYNC\x10\x02\"\'\n\x13GetOperationRequest\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\x90\xe6*\x01\"D\n\x14GetOperationResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"*\n\x16\x43\x61ncelOperationRequest\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\x90\xe6*\x01\"m\n\x17\x43\x61ncelOperationResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.Ydb.StatusIds.StatusCode\x12\'\n\x06issues\x18\x02 \x03(\x0b\x32\x17.Ydb.Issue.IssueMessage\"*\n\x16\x46orgetOperationRequest\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\x90\xe6*\x01\"m\n\x17\x46orgetOperationResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.Ydb.StatusIds.StatusCode\x12\'\n\x06issues\x18\x02 \x03(\x0b\x32\x17.Ydb.Issue.IssueMessage\"R\n\x15ListOperationsRequest\x12\x12\n\x04kind\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x04\x12\x12\n\npage_token\x18\x03 \x01(\t\"\xb4\x01\n\x16ListOperationsResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.Ydb.StatusIds.StatusCode\x12\'\n\x06issues\x18\x02 \x03(\x0b\x32\x17.Ydb.Issue.IssueMessage\x12-\n\noperations\x18\x03 \x03(\x0b\x32\x19.Ydb.Operations.Operation\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\"\xea\x01\n\tOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05ready\x18\x02 \x01(\x08\x12)\n\x06status\x18\x03 \x01(\x0e\x32\x19.Ydb.StatusIds.StatusCode\x12\'\n\x06issues\x18\x04 \x03(\x0b\x32\x17.Ydb.Issue.IssueMessage\x12$\n\x06result\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\x12&\n\x08metadata\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12 \n\tcost_info\x18\x07 \x01(\x0b\x32\r.Ydb.CostInfoB]\n\x08tech.ydbB\x0fOperationProtosZ=github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Operations\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,protos_dot_annotations_dot_validation__pb2.DESCRIPTOR,protos_dot_ydb__common__pb2.DESCRIPTOR,protos_dot_ydb__issue__message__pb2.DESCRIPTOR,protos_dot_ydb__status__codes__pb2.DESCRIPTOR,])



_OPERATIONPARAMS_OPERATIONMODE = _descriptor.EnumDescriptor(
  name='OperationMode',
  full_name='Ydb.Operations.OperationParams.OperationMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATION_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SYNC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ASYNC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=601,
  serialized_end=669,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONPARAMS_OPERATIONMODE)


_OPERATIONPARAMS_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='Ydb.Operations.OperationParams.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Ydb.Operations.OperationParams.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Ydb.Operations.OperationParams.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=599,
)

_OPERATIONPARAMS = _descriptor.Descriptor(
  name='OperationParams',
  full_name='Ydb.Operations.OperationParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_mode', full_name='Ydb.Operations.OperationParams.operation_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_timeout', full_name='Ydb.Operations.OperationParams.operation_timeout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cancel_after', full_name='Ydb.Operations.OperationParams.cancel_after', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='Ydb.Operations.OperationParams.labels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\346*\005\n\003\030\200\001\242\346*\003\030\200\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='report_cost_info', full_name='Ydb.Operations.OperationParams.report_cost_info', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_OPERATIONPARAMS_LABELSENTRY, ],
  enum_types=[
    _OPERATIONPARAMS_OPERATIONMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=669,
)


_GETOPERATIONREQUEST = _descriptor.Descriptor(
  name='GetOperationRequest',
  full_name='Ydb.Operations.GetOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Ydb.Operations.GetOperationRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=671,
  serialized_end=710,
)


_GETOPERATIONRESPONSE = _descriptor.Descriptor(
  name='GetOperationResponse',
  full_name='Ydb.Operations.GetOperationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Operations.GetOperationResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=712,
  serialized_end=780,
)


_CANCELOPERATIONREQUEST = _descriptor.Descriptor(
  name='CancelOperationRequest',
  full_name='Ydb.Operations.CancelOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Ydb.Operations.CancelOperationRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=782,
  serialized_end=824,
)


_CANCELOPERATIONRESPONSE = _descriptor.Descriptor(
  name='CancelOperationResponse',
  full_name='Ydb.Operations.CancelOperationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Ydb.Operations.CancelOperationResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issues', full_name='Ydb.Operations.CancelOperationResponse.issues', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=826,
  serialized_end=935,
)


_FORGETOPERATIONREQUEST = _descriptor.Descriptor(
  name='ForgetOperationRequest',
  full_name='Ydb.Operations.ForgetOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Ydb.Operations.ForgetOperationRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=937,
  serialized_end=979,
)


_FORGETOPERATIONRESPONSE = _descriptor.Descriptor(
  name='ForgetOperationResponse',
  full_name='Ydb.Operations.ForgetOperationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Ydb.Operations.ForgetOperationResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issues', full_name='Ydb.Operations.ForgetOperationResponse.issues', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=981,
  serialized_end=1090,
)


_LISTOPERATIONSREQUEST = _descriptor.Descriptor(
  name='ListOperationsRequest',
  full_name='Ydb.Operations.ListOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='Ydb.Operations.ListOperationsRequest.kind', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='Ydb.Operations.ListOperationsRequest.page_size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='Ydb.Operations.ListOperationsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1092,
  serialized_end=1174,
)


_LISTOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='ListOperationsResponse',
  full_name='Ydb.Operations.ListOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Ydb.Operations.ListOperationsResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issues', full_name='Ydb.Operations.ListOperationsResponse.issues', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='Ydb.Operations.ListOperationsResponse.operations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='Ydb.Operations.ListOperationsResponse.next_page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1177,
  serialized_end=1357,
)


_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='Ydb.Operations.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Ydb.Operations.Operation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ready', full_name='Ydb.Operations.Operation.ready', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='Ydb.Operations.Operation.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issues', full_name='Ydb.Operations.Operation.issues', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='Ydb.Operations.Operation.result', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='Ydb.Operations.Operation.metadata', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_info', full_name='Ydb.Operations.Operation.cost_info', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1360,
  serialized_end=1594,
)

_OPERATIONPARAMS_LABELSENTRY.containing_type = _OPERATIONPARAMS
_OPERATIONPARAMS.fields_by_name['operation_mode'].enum_type = _OPERATIONPARAMS_OPERATIONMODE
_OPERATIONPARAMS.fields_by_name['operation_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_OPERATIONPARAMS.fields_by_name['cancel_after'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_OPERATIONPARAMS.fields_by_name['labels'].message_type = _OPERATIONPARAMS_LABELSENTRY
_OPERATIONPARAMS.fields_by_name['report_cost_info'].enum_type = protos_dot_ydb__common__pb2._FEATUREFLAG_STATUS
_OPERATIONPARAMS_OPERATIONMODE.containing_type = _OPERATIONPARAMS
_GETOPERATIONRESPONSE.fields_by_name['operation'].message_type = _OPERATION
_CANCELOPERATIONRESPONSE.fields_by_name['status'].enum_type = protos_dot_ydb__status__codes__pb2._STATUSIDS_STATUSCODE
_CANCELOPERATIONRESPONSE.fields_by_name['issues'].message_type = protos_dot_ydb__issue__message__pb2._ISSUEMESSAGE
_FORGETOPERATIONRESPONSE.fields_by_name['status'].enum_type = protos_dot_ydb__status__codes__pb2._STATUSIDS_STATUSCODE
_FORGETOPERATIONRESPONSE.fields_by_name['issues'].message_type = protos_dot_ydb__issue__message__pb2._ISSUEMESSAGE
_LISTOPERATIONSRESPONSE.fields_by_name['status'].enum_type = protos_dot_ydb__status__codes__pb2._STATUSIDS_STATUSCODE
_LISTOPERATIONSRESPONSE.fields_by_name['issues'].message_type = protos_dot_ydb__issue__message__pb2._ISSUEMESSAGE
_LISTOPERATIONSRESPONSE.fields_by_name['operations'].message_type = _OPERATION
_OPERATION.fields_by_name['status'].enum_type = protos_dot_ydb__status__codes__pb2._STATUSIDS_STATUSCODE
_OPERATION.fields_by_name['issues'].message_type = protos_dot_ydb__issue__message__pb2._ISSUEMESSAGE
_OPERATION.fields_by_name['result'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_OPERATION.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_OPERATION.fields_by_name['cost_info'].message_type = protos_dot_ydb__common__pb2._COSTINFO
DESCRIPTOR.message_types_by_name['OperationParams'] = _OPERATIONPARAMS
DESCRIPTOR.message_types_by_name['GetOperationRequest'] = _GETOPERATIONREQUEST
DESCRIPTOR.message_types_by_name['GetOperationResponse'] = _GETOPERATIONRESPONSE
DESCRIPTOR.message_types_by_name['CancelOperationRequest'] = _CANCELOPERATIONREQUEST
DESCRIPTOR.message_types_by_name['CancelOperationResponse'] = _CANCELOPERATIONRESPONSE
DESCRIPTOR.message_types_by_name['ForgetOperationRequest'] = _FORGETOPERATIONREQUEST
DESCRIPTOR.message_types_by_name['ForgetOperationResponse'] = _FORGETOPERATIONRESPONSE
DESCRIPTOR.message_types_by_name['ListOperationsRequest'] = _LISTOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListOperationsResponse'] = _LISTOPERATIONSRESPONSE
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationParams = _reflection.GeneratedProtocolMessageType('OperationParams', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _OPERATIONPARAMS_LABELSENTRY,
    '__module__' : 'protos.ydb_operation_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Operations.OperationParams.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _OPERATIONPARAMS,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.OperationParams)
  })
_sym_db.RegisterMessage(OperationParams)
_sym_db.RegisterMessage(OperationParams.LabelsEntry)

GetOperationRequest = _reflection.GeneratedProtocolMessageType('GetOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATIONREQUEST,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.GetOperationRequest)
  })
_sym_db.RegisterMessage(GetOperationRequest)

GetOperationResponse = _reflection.GeneratedProtocolMessageType('GetOperationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATIONRESPONSE,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.GetOperationResponse)
  })
_sym_db.RegisterMessage(GetOperationResponse)

CancelOperationRequest = _reflection.GeneratedProtocolMessageType('CancelOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELOPERATIONREQUEST,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.CancelOperationRequest)
  })
_sym_db.RegisterMessage(CancelOperationRequest)

CancelOperationResponse = _reflection.GeneratedProtocolMessageType('CancelOperationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELOPERATIONRESPONSE,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.CancelOperationResponse)
  })
_sym_db.RegisterMessage(CancelOperationResponse)

ForgetOperationRequest = _reflection.GeneratedProtocolMessageType('ForgetOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORGETOPERATIONREQUEST,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.ForgetOperationRequest)
  })
_sym_db.RegisterMessage(ForgetOperationRequest)

ForgetOperationResponse = _reflection.GeneratedProtocolMessageType('ForgetOperationResponse', (_message.Message,), {
  'DESCRIPTOR' : _FORGETOPERATIONRESPONSE,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.ForgetOperationResponse)
  })
_sym_db.RegisterMessage(ForgetOperationResponse)

ListOperationsRequest = _reflection.GeneratedProtocolMessageType('ListOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONSREQUEST,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.ListOperationsRequest)
  })
_sym_db.RegisterMessage(ListOperationsRequest)

ListOperationsResponse = _reflection.GeneratedProtocolMessageType('ListOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONSRESPONSE,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.ListOperationsResponse)
  })
_sym_db.RegisterMessage(ListOperationsResponse)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'protos.ydb_operation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Operations.Operation)
  })
_sym_db.RegisterMessage(Operation)


DESCRIPTOR._options = None
_OPERATIONPARAMS_LABELSENTRY._options = None
_OPERATIONPARAMS.fields_by_name['labels']._options = None
_GETOPERATIONREQUEST.fields_by_name['id']._options = None
_CANCELOPERATIONREQUEST.fields_by_name['id']._options = None
_FORGETOPERATIONREQUEST.fields_by_name['id']._options = None
_LISTOPERATIONSREQUEST.fields_by_name['kind']._options = None
# @@protoc_insertion_point(module_scope)
