import low_header_big_endian
import low_header_little_endian
import header
import header_ex
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
        self.file_header = header_ex._DpxGenericHeaderEx(self.raw_header)

    def describe(self):
        output = "----------------\n"
        output += "DPX Header Info\n"
        output += "----------------\n"
        output += "Generic Header\n"
        output += "----------------\n"
        output += "Magic: " + self.file_header.magic + "\n"
        output += "Endian: " + self.endian() + "\n"
        output += "Image offset: " + str(self.file_header.image_offset) + " bytes\n"
        output += "DPX version: " + self.file_header.version + "\n"
        output += "File size: " + str(self.file_header.file_size) + " bytes\n"
        output += "Dit to key: " + str(self.file_header.is_dit_to_key) + "\n"
        output += "Generic Header size: " + str(self.file_header.generic_size) + " bytes\n"
        output += "Industry Header size: " + str(self.file_header.industry_size) + " bytes\n"
        output += "User size: " + str(self.file_header.user_size) + " bytes\n"
        output += "File name: " + self.file_header.file_name + "\n"
        output += "TimeDate :" + self.file_header.time_date + "\n"

        output += str(self.raw_header.FileHeader.Creator)
        output += str(self.raw_header.FileHeader.Project)
        output += str(self.raw_header.ImageHeader.Orientation)
        output += str(self.raw_header.ImageHeader.NumberElements)
        output += str(self.raw_header.ImageHeader.ImageElement[0].Description)
        output += str(self.image_header.image_element[0].data_sign)
        output += str(self.raw_header.OrientHeader.XOriginalSize)
        output += str(self.raw_header.OrientHeader.YOriginalSize)
        output += str(self.raw_header.TvHeader.TimeCode)
        output += str(self.raw_header.TvHeader.UserBits)
        output += str(self.raw_header.TvHeader.FrameRate)
        output += str(self.tv_header.time_code)

        return output

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
