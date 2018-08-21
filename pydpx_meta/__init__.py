import pydpx_meta.low_header_big_endian
import pydpx_meta.low_header_little_endian
import pydpx_meta.header
import pydpx_meta.header_ex
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

            if _header.FileHeader.Magic != b'SDPX':
                _header = low_header_little_endian.DpxHeaderLittleEndian()
                self._is_big_endian = False
                fp = open(file_path, "rb")
                fp.readinto(_header)
                fp.close()

        self.raw_header = _header
        self.raw_data = None

        self.file_header = header._DpxGenericHeader(self.raw_header)
        self.image_header = header._DpxGenericImageHeader(self.raw_header)
        self.orient_header = header._DpxGenericOrientationHeader(self.raw_header)
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
        self.image_header = header_ex._DpxGenericImageHeaderEx(self.raw_header)
        self.orient_header = header_ex._DpxGenericOrientationHeaderEx(self.raw_header)
        self.tv_header = header_ex._DpxIndustryTelevisionInfoHeaderEx(self.raw_header)

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
        output += "Creator :" + self.file_header.creator + "\n"
        output += "Project :" + self.file_header.project + "\n"
        output += "Copyright :" + self.file_header.copyright + "\n"
        output += "Encrypt Key: " + "{0:0>8X}".format(self.file_header.encrypt_key) + "\n"
        output += "----------------\n"
        output += "Image Header\n"
        output += "----------------\n"
        output += "Orientation: " + self.image_header.orientation_str + "\n"
        output += "Number of elements: " + str(self.image_header.number_elements) + " images\n"
        output += "Pixels per line: " + str(self.image_header.pixels_per_line) + " pixels\n"
        output += "Lines per element: " + str(self.image_header.lines_per_element) + " lines\n"
        for i in range(0,7):
            output += "  --------------\n"
            output += "  Image Element " + str(i) +"\n"
            output += "  --------------\n"
            output += "  Data Sign: " + self.image_header.image_element[i].data_sign_str + "\n"
            output += "  Low Data: " + str(self.image_header.image_element[i].low_data) + "\n"
            output += "  Low Quantity: " + str(self.image_header.image_element[i].low_quantity) + "\n"
            output += "  High Data: " + str(self.image_header.image_element[i].high_data) + "\n"
            output += "  High Quantity: " + str(self.image_header.image_element[i].high_quantity) + "\n"
            output += "  Descriptor: " + self.image_header.image_element[i].descriptor_str + "\n"
            output += "  Transfer: " + self.image_header.image_element[i].transfer_str + "\n"
            output += "  Colormetric: " + self.image_header.image_element[i].colorimetric_str + "\n"
            output += "  Bits size: " + str(self.image_header.image_element[i].bit_size) + " bits\n"
            output += "  Packing: " + self.image_header.image_element[i].packing_str + "\n"
            output += "  Encoding: "+ self.image_header.image_element[i].encoding_str + "\n"
            output += "  DataOffset: " + str(self.image_header.image_element[i].data_offset) + " bytes\n"
            output += "  End of line padding: {0:d} bytes\n".format(
                self.image_header.image_element[i].end_of_line_padding)
            output += "  End of image padding: {0:d} bytes\n".format(
                self.image_header.image_element[i].end_of_image_padding)
            output += "  Description: " + self.image_header.image_element[i].description + "\n"

        output += "----------------\n"
        output += "Orient Header\n"
        output += "----------------\n"
        output += "X offset: {0:d} pixels\n".format(self.orient_header.x_offset)
        output += "Y offset: {0:d} pixels\n".format(self.orient_header.y_offset)
        output += "X center: {0:f} pixels\n".format(self.orient_header.x_center)
        output += "Y center: {0:f} pixels\n".format(self.orient_header.y_center)
        output += "X original size: {0:d} pixels\n".format(self.orient_header.x_original_size)
        output += "Y original size: {0:d} pixels\n".format(self.orient_header.y_original_size)
        output += "File name: {0}\n".format(self.orient_header.file_name)
        output += "Time Date: {0}\n".format(self.orient_header.time_date)
        output += "Input device name: {0}\n".format(self.orient_header.input_name)
        output += "Input device Serial Number: {0}\n".format(self.orient_header.input_sn)
        output += "Border X Left: {0:d}\n".format(self.orient_header.border_x_left)
        output += "Border X Right: {0:d}\n".format(self.orient_header.border_x_right)
        output += "Border Y Top: {0:d}\n".format(self.orient_header.border_y_top)
        output += "Border Y Bottom: {0:d}\n".format(self.orient_header.border_y_bottom)
        output += "AspectRatio: H:{0:d} V:{0:d}\n".format(
            self.orient_header.aspect_ratio_h, self.orient_header.aspect_ratio_v)
        output += "----------------\n"
        output += "Film Header\n"
        output += "----------------\n"
        output += "Film manufacturer ID code: {0}\n".format(self.film_header.film_mfg_id)
        output += "Film type: {0}\n".format(self.film_header.film_type)
        output += "Film perforations offset: {0}\n".format(self.film_header.offset)
        output += "Prefix code: {0}\n".format(self.film_header.prefix)
        output += "Count code: {0}\n".format(self.film_header.count)
        output += "Film format: {0}\n".format(self.film_header.format)
        output += "Frame sequence position: {0:d} frame\n".format(self.film_header.frame_position)
        output += "Sequence length: {0:d} frames\n".format(self.film_header.sequence_length)
        output += "Held Count: {0:d}\n".format(self.film_header.held_count)
        output += "Frame rate: {0:f} fps\n".format(self.film_header.frame_rate)
        output += "Shutter Angle: {0:f} degrees\n".format(self.film_header.shutter_angle)
        output += "Frame ID: {0}\n".format(self.film_header.frame_id)
        output += "Slate info: {0}\n".format(self.film_header.slate_info)
        output += "----------------\n"
        output += "TV Header\n"
        output += "----------------\n"
        output += "Time code: {0}\n".format(self.tv_header.time_code)
        output += "User bits: {0}\n".format(self.tv_header.user_bits)
        output += "Interlace: " + str(self.tv_header.is_interlaced) + "\n"
        output += "Field Number: {0:d} field\n".format(self.tv_header.field_number)
        output += "Video signal: {0}\n".format(self.tv_header.video_signal_str)
        output += "Padding: {0:d}\n".format(self.tv_header.padding)
        output += "Horizontal sampling rate: {0:f} Hz\n".format(self.tv_header.horizontal_sample_rate)
        output += "Vertical sampling rate: {0:f} Hz\n".format(self.tv_header.vertical_sample_rate)
        output += "Frame rate: {0:f} Hz\n".format(self.tv_header.frame_rate)
        output += "Time offset: {0:f} micro-seconds\n".format(self.tv_header.time_offset)
        output += "Gamma: {0:f}\n".format(self.tv_header.gamma)
        output += "Black level: {0:f}\n".format(self.tv_header.black_level)
        output += "Black gain: {0:f}\n".format(self.tv_header.black_gain)
        output += "Break point {0:f}\n".format(self.tv_header.break_point)
        output += "White level: {0:f}\n".format(self.tv_header.white_level)
        output += "Integration times: {0:f}\n".format(self.tv_header.integration_times)

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
