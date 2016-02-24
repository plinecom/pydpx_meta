import pydpx_meta.pydpx

meta = pydpx_meta.pydpx.header

import struct
import ctypes
class Dpx_Bigendian(ctypes.BigEndianStructure):
    _fields_ = [
        ('Magic', ctypes.c_char*4),
        ('ImageOffset',ctypes.c_uint32),
        ('Version',ctypes.c_char*8),
        ('FileSize',ctypes.c_uint32),
        ('DittoKey',ctypes.c_uint32),
        ('GenericSize',ctypes.c_uint32),
        ('IndustrySize',ctypes.c_uint32),
        ('UserSize',ctypes.c_uint32)
    ]
fp = open("/root/V14_37_26_01_v001.0186.dpx","rb")
fpw = open("/root/test.dpx","wb")
# read magic

dpx = Dpx_Bigendian()
fp.readinto(dpx)
print dpx.Magic
print dpx.ImageOffset
print dpx.Version
print dpx.FileSize
print dpx.DittoKey
print dpx.IndustrySize
print dpx.UserSize
magic = ""
if magic == "SDPX":
    big_endian = True
fpw.write(dpx)