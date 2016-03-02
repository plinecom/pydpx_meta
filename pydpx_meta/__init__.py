import low_header_big_endian
import low_header_little_endian
import header
import shutil


class DpxHeader:
    def __init__(self, file_path=None):

        self._file_path = file_path
        _header = low_header_big_endian.DpxHeaderBigEndian()

        if file_path is not None:
            fp = open(file_path, "rb")
            fp.readinto(_header)
            fp.close()

            if _header.FileHeader.Magic != 'SDPX':
                _header = low_header_little_endian.DpxHeaderLittleEndian()
                fp = open(file_path, "rb")
                fp.readinto(_header)
                fp.close()

        self.raw_header = _header
        self.raw_data = None

        self.file_header = header._DpxGenericHeader(self.raw_header)
        self.image_header = header._DpxGenericImageHeader(self.raw_header)
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
