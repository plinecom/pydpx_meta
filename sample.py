import pydpx_meta.pydpx

meta = pydpx_meta.pydpx.header


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


class DpxGenericImageElementBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('DataSign', ctypes.c_uint32),
        ('LowData', ctypes.c_uint32),
        ('LowQuantity',ctypes.c_float),
        ('HighData',ctypes.c_uint32),
        ('HighQuantity',ctypes.c_float),
        ('Descripter',ctypes.c_byte),
        ('Transfer',ctypes.c_byte),
        ('Colorimetric',ctypes.c_byte),
        ('BitSize',ctypes.c_byte),
        ('Packing',ctypes.c_uint16),
        ('Encoding',ctypes.c_uint16),
        ('DataOffset', ctypes.c_uint32),
        ('EndOfLinePadding', ctypes.c_uint32),
        ('EndOfImagePadding', ctypes.c_uint32),
        ('Description',ctypes.c_char*32)
    ]


class DpxGenericImageHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('Orientation', ctypes.c_uint16),
        ('NumberElements', ctypes.c_uint16),
        ('PixelsPerLine',ctypes.c_uint32),
        ('LinesPerElement',ctypes.c_uint32),
        ('ImageElement', DpxGenericImageElementBigEndian*8),
        ('Reserved',ctypes.c_char*52)
    ]


class DpxGenericOrientationHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('XOffset', ctypes.c_uint32),
        ('YOffset', ctypes.c_uint32),
        ('XCenter', ctypes.c_float),
        ('YCenter', ctypes.c_float),
        ('XOriginalSize', ctypes.c_uint32),
        ('YOriginalSize', ctypes.c_uint32),
        ('FileName', ctypes.c_char*100),
        ('TimeData', ctypes.c_char*24),
        ('InputName', ctypes.c_char*32),
        ('InputSN', ctypes.c_char*32),
        ('Border', ctypes.c_uint16*4),
        ('AspectRatio', ctypes.c_uint32*2),
        ('Reserved',ctypes.c_byte*28)
    ]


class DpxIndustryFilmInfoHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('FilmMfgId', ctypes.c_char*2),
        ('FilmType', ctypes.c_char*2),
        ('Offset', ctypes.c_char*2),
        ('Prefix', ctypes.c_char*6),
        ('Count', ctypes.c_char*4),
        ('Format', ctypes.c_char*32),
        ('FramePosition', ctypes.c_uint32),
        ('SequenceLen', ctypes.c_uint32),
        ('HeldCount', ctypes.c_uint32),
        ('FrameRate', ctypes.c_float),
        ('ShutterAngle', ctypes.c_float),
        ('FrameId', ctypes.c_char*32),
        ('SlateInfo', ctypes.c_char*100),
        ('Reserved', ctypes.c_byte*56)
    ]


class DpxIndustryTelevisionInfoHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('TimeCode', ctypes.c_uint32),
        ('UserBits', ctypes.c_uint32),
        ('Interlace', ctypes.c_byte),
        ('FieldNumber', ctypes.c_byte),
        ('VideoSignal', ctypes.c_byte),
        ('Padding', ctypes.c_byte),
        ('HorzSampleRate', ctypes.c_float),
        ('VertSampleRate', ctypes.c_float),
        ('FrameRate', ctypes.c_float),
        ('TimeOffset', ctypes.c_float),
        ('Gamma', ctypes.c_float),
        ('BlackLevel', ctypes.c_float),
        ('BlackGain', ctypes.c_float),
        ('Breakpoint', ctypes.c_float),
        ('WhiteLevel', ctypes.c_float),
        ('IntegrationTimes', ctypes.c_float),
        ('Reserved', ctypes.c_byte*76)
    ]


class DpxBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('FileHeader', DpxGenericHeaderBigEndian),
        ('ImageHeader', DpxGenericImageHeaderBigEndian),
        ('OrientHeader', DpxGenericOrientationHeaderBigEndian),
        ('FilmHeader', DpxIndustryFilmInfoHeaderBigEndian),
        ('TvHeader', DpxIndustryTelevisionInfoHeaderBigEndian)
    ]
fp = open("/root/V14_37_26_01_v001.0186.dpx","rb")
fpw = open("/root/test.dpx","wb")
# read magic

dpx = DpxBigEndian()
fp.readinto(dpx)
print dpx.FileHeader.Magic
print dpx.FileHeader.ImageOffset
print dpx.FileHeader.Version
print dpx.FileHeader.FileSize
print dpx.FileHeader.DittoKey
print dpx.FileHeader.IndustrySize
print dpx.FileHeader.UserSize
print dpx.FileHeader.FileName
print dpx.FileHeader.TimeData
print dpx.FileHeader.Creator
print dpx.FileHeader.Project
print dpx.ImageHeader.Orientation
print dpx.ImageHeader.NumberElements
print dpx.ImageHeader.ImageElement[0].Description
print dpx.OrientHeader.XOriginalSize
print dpx.OrientHeader.YOriginalSize
magic = ""
if magic == "SDPX":
    big_endian = True
fpw.write(dpx)