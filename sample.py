import pydpx_meta.pydpx

meta = pydpx_meta.pydpx.header

import struct
import ctypes


class DpxGenericHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('Magic', ctypes.c_char*4),
        ('ImageOffset',ctypes.c_uint32),
        ('Version',ctypes.c_char*8),
        ('FileSize',ctypes.c_uint32),
        ('DittoKey',ctypes.c_uint32),
        ('GenericSize',ctypes.c_uint32),
        ('IndustrySize',ctypes.c_uint32),
        ('UserSize',ctypes.c_uint32),
        ('FileName',ctypes.c_char*100),
        ('TimeData',ctypes.c_char*24),
        ('Creator',ctypes.c_char*100),
        ('Project',ctypes.c_char*200),
        ('Copyright',ctypes.c_char*200),
        ('EncryptKey',ctypes.c_uint32),
        ('Reserved',ctypes.c_char*104)
    ]


class DpxGenericImageHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('Orientation', ctypes.c_uint16),
        ('NumberElements', ctypes.c_uint16),
        ('PixelsPerLine',ctypes.c_uint32),
        ('LinesPerElement',ctypes.c_uint32),
        ('Reserved',ctypes.c_char*52)
    ]


class DpxBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('GenericHeader',DpxGenericHeaderBigEndian),
        ('GenericImageHeader',DpxGenericImageHeaderBigEndian)
    ]
fp = open("/root/V14_37_26_01_v001.0186.dpx","rb")
fpw = open("/root/test.dpx","wb")
# read magic

dpx = DpxBigEndian()
fp.readinto(dpx)
print dpx.GenericHeader.Magic
print dpx.GenericHeader.ImageOffset
print dpx.GenericHeader.Version
print dpx.GenericHeader.FileSize
print dpx.GenericHeader.DittoKey
print dpx.GenericHeader.IndustrySize
print dpx.GenericHeader.UserSize
print dpx.GenericHeader.FileName
print dpx.GenericHeader.TimeData
print dpx.GenericHeader.Creator
print dpx.GenericHeader.Project
print dpx.GenericImageHeader.Orientation
print dpx.GenericImageHeader.NumberElements
magic = ""
if magic == "SDPX":
    big_endian = True
fpw.write(dpx)