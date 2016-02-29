# import os.path
# import sys
import ctypes
import shutil


class DpxHeader:
    def __init__(self, file_path):

        self._file_path = file_path
        header = _DpxHeaderBigEndian()

        fp = open(file_path, "rb")
        fp.readinto(header)
        fp.close()

        if header.FileHeader.Magic != 'SDPX':
            header = _DpxHeaderLittleEndian()
            fp = open(file_path, "rb")
            fp.readinto(header)
            fp.close()

        self.raw_header = header
        self.raw_data = None

        self.file_header = _DpxGenericHeader(self.raw_header)
        self.tv_header = _DpxIndustryTelevisionInfoHeader(self.raw_header)

#        print os.path.getsize(file_path) - sys.getsizeof(header)
#        print sys.getsizeof(header)

    def save(self, file_path=None):
        if file_path is None:
            file_path = self._file_path

        if self._file_path != file_path:
            shutil.copyfile(self._file_path, file_path)

        fp = open(file_path, "rb+")
        fp.write(self.raw_header)
        fp.close()


class _DpxGenericHeader:
    def __init__(self, header):
        self._raw_header = header

    @property
    def magic(self):
        return str(self._raw_header.FileHeader.Magic)

    @magic.setter
    def magic(self, magic):
        if magic == "SDPX" or magic == "XPDS":
            self._raw_header.FileHeader.Magic = magic

    @property
    def image_offset(self):
        return self._raw_header.FileHeader.ImageOffset

    @image_offset.setter
    def image_offset(self, offset):
        self._raw_header.FileHeader.ImageOffset = offset

    @property
    def version(self):
        return str(self._raw_header.FileHeader.Version)

    @version.setter
    def version(self, ver):
        self._raw_header.FileHeader.Version = ver

    @property
    def file_size(self):
        return self._raw_header.FileHeader.FileSize

    @file_size.setter
    def file_size(self, size):
        self._raw_header.FileHeader.FileSize = size

    @property
    def dit_to_key(self):
        return self._raw_header.FileHeader.DittoKey

    @dit_to_key.setter
    def dit_to_key(self, value):
        self._raw_header.FileHeader.DittoKey = value

    @property
    def generic_size(self):
        return self._raw_header.FileHeader.GenericSize

    @generic_size.setter
    def generic_size(self, size):
        self._raw_header.FileHeader.GenericSize = size

    @property
    def industry_size(self):
        return self._raw_header.FileHeader.IndustrySize

    @industry_size.setter
    def industry_size(self, size):
        self._raw_header.FileHeader.IndustrySize = size

    @property
    def user_size(self):
        return self._raw_header.FileHeader.UserSize

    @user_size.setter
    def user_size(self, size):
        self._raw_header.FileHeader.UserSize = size

    @property
    def file_name(self):
        return str(self._raw_header.FileHeader.FileName)

    @file_name.setter
    def file_name(self, name):
        self._raw_header.FileHeader.FileName = name

    @property
    def time_data(self):
        return str(self._raw_header.FileHeader.TimeData)

    @time_data.setter
    def time_data(self, time):
        self._raw_header.FileHeader.TimeData = time

    @property
    def creator(self):
        return str(self._raw_header.FileHeader.Creator)

    @creator.setter
    def creator(self, creator_name):
        self._raw_header.FileHeader.Creator = creator_name

    @property
    def project(self):
        return str(self._raw_header.FileHeader.Project)

    @project.setter
    def project(self, project_name):
        self._raw_header.FileHeader.Project = project_name

    @property
    def copyright(self):
        return str(self._raw_header.FileHeader.Copyright)

    @copyright.setter
    def copyright(self, name):
        self._raw_header.FileHeader.Copyright = name

    @property
    def encrypt_key(self):
        return self._raw_header.FileHeader.EncryptKey

    @encrypt_key.setter
    def encrypt_key(self, key):
        self._raw_header.FileHeader.EncryptKey = key


class _DpxIndustryTelevisionInfoHeader:
    def __init__(self, header):
        self._raw_header = header

    @property
    def timecode(self):
        timecode_tmp = '{0:0>8x}'.format(self._raw_header.TvHeader.TimeCode)
        timecode_str = timecode_tmp[0:2]+":"+timecode_tmp[2:4]+":"+timecode_tmp[4:6]+":"+timecode_tmp[6:8]

        return str(timecode_str)

    @timecode.setter
    def timecode(self, timecode):
        timecode = timecode.lower()
        timecode_hex = "".join(timecode.split(":"))
        tc_dpx = int(timecode_hex, 16)
        self._raw_header.TvHeader.TimeCode = tc_dpx


class _DpxGenericHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('Magic', ctypes.c_char*4),
        ('ImageOffset', ctypes.c_uint32),
        ('Version', ctypes.c_char*8),
        ('FileSize', ctypes.c_uint32),
        ('DittoKey', ctypes.c_uint32),
        ('GenericSize', ctypes.c_uint32),
        ('IndustrySize', ctypes.c_uint32),
        ('UserSize', ctypes.c_uint32),
        ('FileName', ctypes.c_char*100),
        ('TimeData', ctypes.c_char*24),
        ('Creator', ctypes.c_char*100),
        ('Project', ctypes.c_char*200),
        ('Copyright', ctypes.c_char*200),
        ('EncryptKey', ctypes.c_uint32),
        ('Reserved', ctypes.c_char*104)
    ]


class _DpxGenericImageElement:
    def __init__(self, header):
        self._raw_header = header

    @property
    def magic(self):
        return str(self._raw_header.FileHeader.Magic)

    @magic.setter
    def magic(self, magic):
        if magic == "SDPX" or magic == "XPDS":
            self._raw_header.FileHeader.Magic = magic

    @property
    def image_offset(self):
        return self._raw_header.FileHeader.ImageOffset

    @image_offset.setter
    def image_offset(self, offset):
        self._raw_header.FileHeader.ImageOffset = offset


class _DpxGenericImageElementBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('DataSign', ctypes.c_uint32),
        ('LowData', ctypes.c_uint32),
        ('LowQuantity', ctypes.c_float),
        ('HighData', ctypes.c_uint32),
        ('HighQuantity', ctypes.c_float),
        ('Descriptor', ctypes.c_byte),
        ('Transfer', ctypes.c_byte),
        ('Colorimetric', ctypes.c_byte),
        ('BitSize', ctypes.c_byte),
        ('Packing', ctypes.c_uint16),
        ('Encoding', ctypes.c_uint16),
        ('DataOffset', ctypes.c_uint32),
        ('EndOfLinePadding', ctypes.c_uint32),
        ('EndOfImagePadding', ctypes.c_uint32),
        ('Description', ctypes.c_char*32)
    ]


class DpxImageHeaderOrientaion:
    def __init__(self):
        pass
    (
        LeftToRight_TopToBottom,
        RightToLeft_TopToBottom,
        LeftToRight_BottomToTop,
        RightToLeft_BottomToTop,
        TopToBottom_LeftToRight,
        TopTOBottom_RightToLeft,
        BottomToTop_LeftToRight,
        BottomToTop_RightToLeft
    ) = range(0, 8)


class _DpxGenericImageHeader:
    def __init__(self, header):
        self._raw_header = header

    @property
    def orientation(self):
        orient = self._raw_header.ImageHeader.Orientation
        if orient == 0:
            return DpxImageHeaderOrientaion.LeftToRight_TopToBottom
        elif orient == 1:
            return DpxImageHeaderOrientaion.RightToLeft_TopToBottom
        elif orient == 2:
            return DpxImageHeaderOrientaion.LeftToRight_BottomToTop
        elif orient == 3:
            return DpxImageHeaderOrientaion.RightToLeft_BottomToTop
        elif orient == 4:
            return DpxImageHeaderOrientaion.TopToBottom_LeftToRight
        elif orient == 5:
            return DpxImageHeaderOrientaion.TopTOBottom_RightToLeft
        elif orient == 6:
            return DpxImageHeaderOrientaion.BottomToTop_LeftToRight
        elif orient == 7:
            return DpxImageHeaderOrientaion.BottomToTop_RightToLeft
        else:
            return orient

    @orientation.setter
    def orientation(self, orient):
        if 0 <= orient < 8:
            self._raw_header.ImageHeader.Orientation = orient

    @property
    def image_offset(self):
        return self._raw_header.FileHeader.ImageOffset

    @image_offset.setter
    def image_offset(self, offset):
        self._raw_header.FileHeader.ImageOffset = offset


class _DpxGenericImageHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('Orientation', ctypes.c_uint16),
        ('NumberElements', ctypes.c_uint16),
        ('PixelsPerLine', ctypes.c_uint32),
        ('LinesPerElement', ctypes.c_uint32),
        ('ImageElement', _DpxGenericImageElementBigEndian*8),
        ('Reserved', ctypes.c_char*52)
    ]


class _DpxGenericOrientationHeaderBigEndian(ctypes.BigEndianStructure):
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
        ('Reserved', ctypes.c_byte*28)
    ]


class _DpxIndustryFilmInfoHeaderBigEndian(ctypes.BigEndianStructure):
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


class _DpxIndustryTelevisionInfoHeaderBigEndian(ctypes.BigEndianStructure):
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


class _DpxHeaderBigEndian(ctypes.BigEndianStructure):
    _fields_ = [
        ('FileHeader', _DpxGenericHeaderBigEndian),
        ('ImageHeader', _DpxGenericImageHeaderBigEndian),
        ('OrientHeader', _DpxGenericOrientationHeaderBigEndian),
        ('FilmHeader', _DpxIndustryFilmInfoHeaderBigEndian),
        ('TvHeader', _DpxIndustryTelevisionInfoHeaderBigEndian)
    ]


class _DpxGenericHeaderLittleEndian(ctypes.LittleEndianStructure):
    _fields_ = [
        ('Magic', ctypes.c_char*4),
        ('ImageOffset', ctypes.c_uint32),
        ('Version', ctypes.c_char*8),
        ('FileSize', ctypes.c_uint32),
        ('DittoKey', ctypes.c_uint32),
        ('GenericSize', ctypes.c_uint32),
        ('IndustrySize', ctypes.c_uint32),
        ('UserSize', ctypes.c_uint32),
        ('FileName', ctypes.c_char*100),
        ('TimeData', ctypes.c_char*24),
        ('Creator', ctypes.c_char*100),
        ('Project', ctypes.c_char*200),
        ('Copyright', ctypes.c_char*200),
        ('EncryptKey', ctypes.c_uint32),
        ('Reserved', ctypes.c_char*104)
    ]


class _DpxGenericImageElementLittleEndian(ctypes.LittleEndianStructure):
    _fields_ = [
        ('DataSign', ctypes.c_uint32),
        ('LowData', ctypes.c_uint32),
        ('LowQuantity', ctypes.c_float),
        ('HighData', ctypes.c_uint32),
        ('HighQuantity', ctypes.c_float),
        ('Descriptor', ctypes.c_byte),
        ('Transfer', ctypes.c_byte),
        ('Colorimetric', ctypes.c_byte),
        ('BitSize', ctypes.c_byte),
        ('Packing', ctypes.c_uint16),
        ('Encoding', ctypes.c_uint16),
        ('DataOffset', ctypes.c_uint32),
        ('EndOfLinePadding', ctypes.c_uint32),
        ('EndOfImagePadding', ctypes.c_uint32),
        ('Description', ctypes.c_char*32)
    ]


class _DpxGenericImageHeaderLittleEndian(ctypes.LittleEndianStructure):
    _fields_ = [
        ('Orientation', ctypes.c_uint16),
        ('NumberElements', ctypes.c_uint16),
        ('PixelsPerLine', ctypes.c_uint32),
        ('LinesPerElement', ctypes.c_uint32),
        ('ImageElement', _DpxGenericImageElementLittleEndian*8),
        ('Reserved', ctypes.c_char*52)
    ]


class _DpxGenericOrientationHeaderLittleEndian(ctypes.LittleEndianStructure):
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
        ('Reserved', ctypes.c_byte*28)
    ]


class _DpxIndustryFilmInfoHeaderLittleEndian(ctypes.LittleEndianStructure):
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


class _DpxIndustryTelevisionInfoHeaderLittleEndian(ctypes.LittleEndianStructure):
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


class _DpxHeaderLittleEndian(ctypes.LittleEndianStructure):
    _fields_ = [
        ('FileHeader', _DpxGenericHeaderLittleEndian),
        ('ImageHeader', _DpxGenericImageHeaderLittleEndian),
        ('OrientHeader', _DpxGenericOrientationHeaderLittleEndian),
        ('FilmHeader', _DpxIndustryFilmInfoHeaderLittleEndian),
        ('TvHeader', _DpxIndustryTelevisionInfoHeaderLittleEndian)
    ]
