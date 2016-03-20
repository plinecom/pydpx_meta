from __future__ import print_function
import low_header_big_endian
import low_header_little_endian
import header
import shutil



class DpxHeader:
    def __init__(self, file_path=None):

        self.load(file_path)

    def load(self, file_path):
        self._file_path = file_path
        self._is_big_endian = True
        _header = low_header_big_endian.DpxHeaderBigEndian()
        if file_path is not None:
            fp = open(file_path, "rb")
            fp.readinto(_header)
            fp.close()

            if _header.FileHeader.Magic != 'SDPX':
                _header = low_header_little_endian.DpxHeaderLittleEndian()
                self._is_big_endian = False
                fp = open(file_path, "rb")
                fp.readinto(_header)
                fp.close()

        self.raw_header = _header
        self.raw_data = None

        self.file_header = header._DpxGenericHeader(self.raw_header)
        self.image_header = header._DpxGenericImageHeader(self.raw_header)
        self.film_header = header._DpxIndustryFilmInfoHeader(self.raw_header)
        self.tv_header = header._DpxIndustryTelevisionInfoHeader(self.raw_header)

    # import os.path
    # import sys
    #       print os.path.getsize(file_path) - sys.getsizeof(header)
    #        print sys.getsizeof(header)

    def save(self, file_path=None):
        if file_path is None:
            file_path = self._file_path

        if self._file_path != file_path:
            shutil.copyfile(self._file_path, file_path)

        fp = open(file_path, "rb+")
        fp.write(self.raw_header)
        fp.close()


class DpxHeaderEx(DpxHeader):

    def __init__(self, file_path=None):
        DpxHeader.__init__(self, file_path)

    def describe(self):
        print("DPX Header Info")
        print("Magic: " + self.file_header.magic)
        print(self.raw_header.FileHeader.ImageOffset)
        print(self.file_header.image_offset)
        print(self.raw_header.FileHeader.Version)
        print(self.raw_header.FileHeader.FileSize)
        print(self.raw_header.FileHeader.DittoKey)
        print(self.raw_header.FileHeader.IndustrySize)
        print(self.raw_header.FileHeader.UserSize)
        print(self.raw_header.FileHeader.FileName)
        print(self.raw_header.FileHeader.TimeData)
        print(self.raw_header.FileHeader.Creator)
        print(self.raw_header.FileHeader.Project)
        print(self.raw_header.ImageHeader.Orientation)
        print(self.raw_header.ImageHeader.NumberElements)
        print(self.raw_header.ImageHeader.ImageElement[0].Description)
        print(self.image_header.image_element[0].data_sign)
        print(self.raw_header.OrientHeader.XOriginalSize)
        print(self.raw_header.OrientHeader.YOriginalSize)
        print(self.raw_header.TvHeader.TimeCode)
        print(self.raw_header.TvHeader.UserBits)
        print(self.raw_header.TvHeader.FrameRate)
        print(self.tv_header.time_code)

    def endian(self):
        if self._is_big_endian:
            return "BigEndian"
        else:
            return "LittleEndian"

    @property
    def is_little_endian(self):
        return not self._is_big_endian

    @property
    def is_big_endian(self):
        return self._is_big_endian
