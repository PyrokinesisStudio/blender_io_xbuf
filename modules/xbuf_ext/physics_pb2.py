# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xbuf_ext/physics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import xbuf.primitives_pb2

from xbuf.primitives_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='xbuf_ext/physics.proto',
  package='xbuf_ext',
  serialized_pb=_b('\n\x16xbuf_ext/physics.proto\x12\x08xbuf_ext\x1a\x15xbuf/primitives.proto\"\xc4\x01\n\x0bPhysicsData\x12&\n\trigidbody\x18\x01 \x01(\x0b\x32\x13.xbuf_ext.RigidBody\x12(\n\nconstraint\x18\x02 \x01(\x0b\x32\x14.xbuf_ext.Constraint\"c\n\x0cPhysicsShape\x12\t\n\x05smesh\x10\x01\x12\x0b\n\x07ssphere\x10\x02\x12\t\n\x05shull\x10\x03\x12\x08\n\x04sbox\x10\x04\x12\x0c\n\x08scapsule\x10\x05\x12\r\n\tscylinder\x10\x06\x12\t\n\x05scone\x10\x07\"d\n\nConstraint\x12\n\n\x02id\x18\x01 \x02(\t\x12\r\n\x05\x61_ref\x18\x02 \x02(\t\x12\r\n\x05\x62_ref\x18\x03 \x02(\t\x12,\n\x07generic\x18\x04 \x01(\x0b\x32\x1b.xbuf_ext.ConstraintGeneric\"\xe5\x01\n\x11\x43onstraintGeneric\x12\x1a\n\x06pivotA\x18\x01 \x02(\x0b\x32\n.xbuf.Vec3\x12\x1a\n\x06pivotB\x18\x02 \x02(\x0b\x32\n.xbuf.Vec3\x12$\n\x10upperLinearLimit\x18\x03 \x02(\x0b\x32\n.xbuf.Vec3\x12$\n\x10lowerLinearLimit\x18\x04 \x02(\x0b\x32\n.xbuf.Vec3\x12%\n\x11upperAngularLimit\x18\x05 \x02(\x0b\x32\n.xbuf.Vec3\x12%\n\x11lowerAngularLimit\x18\x06 \x02(\x0b\x32\n.xbuf.Vec3\"\xe8\x03\n\tRigidBody\x12\n\n\x02id\x18\x01 \x02(\t\x12\x36\n\x04type\x18\x02 \x01(\x0e\x32!.xbuf_ext.RigidBody.RigidBodyType:\x05tnone\x12\x38\n\x05shape\x18\x03 \x01(\x0e\x32\".xbuf_ext.PhysicsData.PhysicsShape:\x05smesh\x12\x0f\n\x04mass\x18\x04 \x01(\x02:\x01\x31\x12\x13\n\x08\x66riction\x18\x05 \x01(\x02:\x01\x31\x12\x19\n\x0e\x61ngularDamping\x18\x06 \x01(\x02:\x01\x30\x12\x18\n\rlinearDamping\x18\x07 \x01(\x02:\x01\x30\x12\x11\n\x06margin\x18\x08 \x01(\x02:\x01\x30\x12\x16\n\x0brestitution\x18\t \x01(\x02:\x01\x30\x12!\n\rangularFactor\x18\n \x01(\x0b\x32\n.xbuf.Vec3\x12 \n\x0clinearFactor\x18\x0b \x01(\x0b\x32\n.xbuf.Vec3\x12\x1a\n\x0bisKinematic\x18\x0c \x01(\x08:\x05\x66\x61lse\x12\x19\n\x0e\x63ollisionGroup\x18\r \x01(\x05:\x01\x31\x12\x18\n\rcollisionMask\x18\x0e \x01(\x05:\x01\x31\"A\n\rRigidBodyType\x12\t\n\x05tnone\x10\x01\x12\x0b\n\x07tstatic\x10\x02\x12\x0c\n\x08tdynamic\x10\x03\x12\n\n\x06tghost\x10\x04P\x00')
  ,
  dependencies=[xbuf.primitives_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PHYSICSDATA_PHYSICSSHAPE = _descriptor.EnumDescriptor(
  name='PhysicsShape',
  full_name='xbuf_ext.PhysicsData.PhysicsShape',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='smesh', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ssphere', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='shull', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sbox', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='scapsule', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='scylinder', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='scone', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=157,
  serialized_end=256,
)
_sym_db.RegisterEnumDescriptor(_PHYSICSDATA_PHYSICSSHAPE)

_RIGIDBODY_RIGIDBODYTYPE = _descriptor.EnumDescriptor(
  name='RigidBodyType',
  full_name='xbuf_ext.RigidBody.RigidBodyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='tnone', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tstatic', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tdynamic', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tghost', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1016,
  serialized_end=1081,
)
_sym_db.RegisterEnumDescriptor(_RIGIDBODY_RIGIDBODYTYPE)


_PHYSICSDATA = _descriptor.Descriptor(
  name='PhysicsData',
  full_name='xbuf_ext.PhysicsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rigidbody', full_name='xbuf_ext.PhysicsData.rigidbody', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='constraint', full_name='xbuf_ext.PhysicsData.constraint', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PHYSICSDATA_PHYSICSSHAPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=256,
)


_CONSTRAINT = _descriptor.Descriptor(
  name='Constraint',
  full_name='xbuf_ext.Constraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xbuf_ext.Constraint.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a_ref', full_name='xbuf_ext.Constraint.a_ref', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b_ref', full_name='xbuf_ext.Constraint.b_ref', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generic', full_name='xbuf_ext.Constraint.generic', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=358,
)


_CONSTRAINTGENERIC = _descriptor.Descriptor(
  name='ConstraintGeneric',
  full_name='xbuf_ext.ConstraintGeneric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pivotA', full_name='xbuf_ext.ConstraintGeneric.pivotA', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pivotB', full_name='xbuf_ext.ConstraintGeneric.pivotB', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upperLinearLimit', full_name='xbuf_ext.ConstraintGeneric.upperLinearLimit', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lowerLinearLimit', full_name='xbuf_ext.ConstraintGeneric.lowerLinearLimit', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upperAngularLimit', full_name='xbuf_ext.ConstraintGeneric.upperAngularLimit', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lowerAngularLimit', full_name='xbuf_ext.ConstraintGeneric.lowerAngularLimit', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=590,
)


_RIGIDBODY = _descriptor.Descriptor(
  name='RigidBody',
  full_name='xbuf_ext.RigidBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xbuf_ext.RigidBody.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='xbuf_ext.RigidBody.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape', full_name='xbuf_ext.RigidBody.shape', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mass', full_name='xbuf_ext.RigidBody.mass', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friction', full_name='xbuf_ext.RigidBody.friction', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angularDamping', full_name='xbuf_ext.RigidBody.angularDamping', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linearDamping', full_name='xbuf_ext.RigidBody.linearDamping', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='margin', full_name='xbuf_ext.RigidBody.margin', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restitution', full_name='xbuf_ext.RigidBody.restitution', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angularFactor', full_name='xbuf_ext.RigidBody.angularFactor', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linearFactor', full_name='xbuf_ext.RigidBody.linearFactor', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isKinematic', full_name='xbuf_ext.RigidBody.isKinematic', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collisionGroup', full_name='xbuf_ext.RigidBody.collisionGroup', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collisionMask', full_name='xbuf_ext.RigidBody.collisionMask', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RIGIDBODY_RIGIDBODYTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=593,
  serialized_end=1081,
)

_PHYSICSDATA.fields_by_name['rigidbody'].message_type = _RIGIDBODY
_PHYSICSDATA.fields_by_name['constraint'].message_type = _CONSTRAINT
_PHYSICSDATA_PHYSICSSHAPE.containing_type = _PHYSICSDATA
_CONSTRAINT.fields_by_name['generic'].message_type = _CONSTRAINTGENERIC
_CONSTRAINTGENERIC.fields_by_name['pivotA'].message_type = xbuf.primitives_pb2._VEC3
_CONSTRAINTGENERIC.fields_by_name['pivotB'].message_type = xbuf.primitives_pb2._VEC3
_CONSTRAINTGENERIC.fields_by_name['upperLinearLimit'].message_type = xbuf.primitives_pb2._VEC3
_CONSTRAINTGENERIC.fields_by_name['lowerLinearLimit'].message_type = xbuf.primitives_pb2._VEC3
_CONSTRAINTGENERIC.fields_by_name['upperAngularLimit'].message_type = xbuf.primitives_pb2._VEC3
_CONSTRAINTGENERIC.fields_by_name['lowerAngularLimit'].message_type = xbuf.primitives_pb2._VEC3
_RIGIDBODY.fields_by_name['type'].enum_type = _RIGIDBODY_RIGIDBODYTYPE
_RIGIDBODY.fields_by_name['shape'].enum_type = _PHYSICSDATA_PHYSICSSHAPE
_RIGIDBODY.fields_by_name['angularFactor'].message_type = xbuf.primitives_pb2._VEC3
_RIGIDBODY.fields_by_name['linearFactor'].message_type = xbuf.primitives_pb2._VEC3
_RIGIDBODY_RIGIDBODYTYPE.containing_type = _RIGIDBODY
DESCRIPTOR.message_types_by_name['PhysicsData'] = _PHYSICSDATA
DESCRIPTOR.message_types_by_name['Constraint'] = _CONSTRAINT
DESCRIPTOR.message_types_by_name['ConstraintGeneric'] = _CONSTRAINTGENERIC
DESCRIPTOR.message_types_by_name['RigidBody'] = _RIGIDBODY

PhysicsData = _reflection.GeneratedProtocolMessageType('PhysicsData', (_message.Message,), dict(
  DESCRIPTOR = _PHYSICSDATA,
  __module__ = 'xbuf_ext.physics_pb2'
  # @@protoc_insertion_point(class_scope:xbuf_ext.PhysicsData)
  ))
_sym_db.RegisterMessage(PhysicsData)

Constraint = _reflection.GeneratedProtocolMessageType('Constraint', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRAINT,
  __module__ = 'xbuf_ext.physics_pb2'
  # @@protoc_insertion_point(class_scope:xbuf_ext.Constraint)
  ))
_sym_db.RegisterMessage(Constraint)

ConstraintGeneric = _reflection.GeneratedProtocolMessageType('ConstraintGeneric', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRAINTGENERIC,
  __module__ = 'xbuf_ext.physics_pb2'
  # @@protoc_insertion_point(class_scope:xbuf_ext.ConstraintGeneric)
  ))
_sym_db.RegisterMessage(ConstraintGeneric)

RigidBody = _reflection.GeneratedProtocolMessageType('RigidBody', (_message.Message,), dict(
  DESCRIPTOR = _RIGIDBODY,
  __module__ = 'xbuf_ext.physics_pb2'
  # @@protoc_insertion_point(class_scope:xbuf_ext.RigidBody)
  ))
_sym_db.RegisterMessage(RigidBody)


# @@protoc_insertion_point(module_scope)
