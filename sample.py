import pydpx_meta.pydpx

meta = pydpx_meta.pydpx.header

import struct
import ctypes
class Dpx_Bigendian(ctypes.BigEndianStructure):
    _fields_ = [
        ('Magic', ctypes.c_char*4),
        ('ImageOffset',ctypes.c_uint32)
    ]
fp = open("/root/V14_37_26_01_v001.0186.dpx","rb")

# read magic

dpx = Dpx_Bigendian()
fp.readinto(dpx)
print dpx.magic[0:4]
print dpx.ImageOffset
magic = ""
if magic == "SDPX":
    big_endian = True
