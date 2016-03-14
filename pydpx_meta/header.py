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


class DpxImageElementSign:
    def __init__(self):
        pass

    values = (
        unsigned_value,
        signed_value
    ) = (0, 1)


class DpxImageElementDescriptor:
    def __init__(self):
        pass

    values = (
        User_Defined,
        Red,
        Green,
        Blue,
        Alpha,
        Luminance,
        Chrominance,
        Depth,
        Composite_video,
        RGB,
        RGBA,
        ABGR,
        CbYCrY,
        CbYaCrYa,
        CbYCr,
        CbYCra,
        User_defined_2_component_element,
        User_defined_3_component_element,
        User_defined_4_component_element,
        User_defined_5_component_element,
        User_defined_6_component_element,
        User_defined_7_component_element,
        User_defined_8_component_element

    ) = (0, 1, 2, 3, 4, 6, 7, 8, 9, 50, 51, 52, 100, 101, 102, 103, 150, 151, 152, 153, 154, 155, 156)


class DpxImageElementTransfer:
    def __init__(self):
        pass

    values = (
        User_defined,
        Printing_density,
        Linear,
        Logarithmic,
        Unspecified_video,
        SMPTE_240M,
        CCIR_709_1,
        CCIR_601_2_system_B_or_G,
        CCIR_601_2_system_M,
        NTSC_composite_video,
        PAL_composite_video,
        Z_linear,
        Z_homogeneous
    ) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)


class DpxImageElementColorimetric:
    def __init__(self):
        pass

    values = (
        User_defined,
        Printing_density,
        Unspecified_video,
        SMPTE_240M,
        CCIR_709_1,
        CCIR_601_2_system_B_or_G,
        CCIR_601_2_system_M,
        NTSC_composite_video,
        PAL_composite_video

    ) = (0, 1, 4, 5, 6, 7, 8, 9, 10)


class DpxImageElementEncoding:
    def __init__(self):
        pass

    values = (
        not_encoded,
        run_length_encoded
    ) = (0, 1)


class DpxImageElementPacking:
    def __init__(self):
        pass

    values = (
        packed32bit,
        filled32bit
    ) = (0, 1)


class _DpxGenericImageElement:
    def __init__(self, image_element):
        self._raw_image_element = image_element

    @property
    def data_sign(self):
        sign = self._raw_image_element.DataSign
        if sign == 0:
            return DpxImageElementSign.unsigned_value
        elif sign == 1:
            return DpxImageElementSign.signed_value
        else:
            return sign

    @data_sign.setter
    def data_sign(self, sign):
        if 0 <= sign <= 1:
            self._raw_image_element.DataSign = sign

    @property
    def low_data(self):
        return self._raw_image_element.LowData

    @low_data.setter
    def low_data(self, min_value):
        self._raw_image_element.LowData = min_value

    @property
    def low_quality(self):
        return self._raw_image_element.LowQuality

    @low_quality.setter
    def low_quality(self, quality):
        self._raw_image_element.LowQuality = quality

    @property
    def high_data(self):
        return self._raw_image_element.HighData

    @high_data.setter
    def high_data(self, max_value):
        self._raw_image_element.HighData = max_value

    @property
    def high_quality(self):
        return self._raw_image_element.HighQuality

    @high_quality.setter
    def high_quality(self, quality):
        self._raw_image_element.HighQuality = quality

    @property
    def descriptor(self):
        desc = self._raw_image_element.Descriptor
        if desc == 0:
            return DpxImageElementDescriptor.User_Defined
        elif desc == 1:
            return DpxImageElementDescriptor.Red
        elif desc == 2:
            return DpxImageElementDescriptor.Green
        elif desc == 3:
            return DpxImageElementDescriptor.Blue
        elif desc == 4:
            return DpxImageElementDescriptor.Alpha
        elif desc == 6:
            return DpxImageElementDescriptor.Luminance
        elif desc == 7:
            return DpxImageElementDescriptor.Chrominance
        elif desc == 8:
            return DpxImageElementDescriptor.Depth
        elif desc == 9:
            return DpxImageElementDescriptor.Composite_video
        elif desc == 50:
            return DpxImageElementDescriptor.RGB
        elif desc == 51:
            return DpxImageElementDescriptor.RGBA
        elif desc == 52:
            return DpxImageElementDescriptor.ABGR
        elif desc == 100:
            return DpxImageElementDescriptor.CbYCrY
        elif desc == 101:
            return DpxImageElementDescriptor.CbYaCrYa
        elif desc == 102:
            return DpxImageElementDescriptor.CbYCr
        elif desc == 103:
            return DpxImageElementDescriptor.CbYCra
        elif desc == 150:
            return DpxImageElementDescriptor.User_defined_2_component_element
        elif desc == 151:
            return DpxImageElementDescriptor.User_defined_3_component_element
        elif desc == 152:
            return DpxImageElementDescriptor.User_defined_4_component_element
        elif desc == 153:
            return DpxImageElementDescriptor.User_defined_5_component_element
        elif desc == 154:
            return DpxImageElementDescriptor.User_defined_6_component_element
        elif desc == 155:
            return DpxImageElementDescriptor.User_defined_7_component_element
        elif desc == 156:
            return DpxImageElementDescriptor.User_defined_8_component_element
        else:
            return desc

    @descriptor.setter
    def descriptor(self, desc):
        if desc in DpxImageElementDescriptor.values:
            self._raw_image_element.Descriptor = desc

    @property
    def transfer(self):
        trans = self._raw_image_element.Transfer
        if trans == 0:
            return DpxImageElementTransfer.User_defined
        elif trans == 1:
            return DpxImageElementTransfer.Printing_density
        elif trans == 2:
            return DpxImageElementTransfer.Linear
        elif trans == 3:
            return DpxImageElementTransfer.Logarithmic
        elif trans == 4:
            return DpxImageElementTransfer.Unspecified_video
        elif trans == 5:
            return DpxImageElementTransfer.SMPTE_240M
        elif trans == 6:
            return DpxImageElementTransfer.CCIR_709_1
        elif trans == 7:
            return DpxImageElementTransfer.CCIR_601_2_system_B_or_G
        elif trans == 8:
            return DpxImageElementTransfer.CCIR_601_2_system_M
        elif trans == 9:
            return DpxImageElementTransfer.NTSC_composite_video
        elif trans == 10:
            return DpxImageElementTransfer.PAL_composite_video
        elif trans == 11:
            return DpxImageElementTransfer.Z_linear
        elif trans == 12:
            return DpxImageElementTransfer.Z_homogeneous
        else:
            return trans

    @transfer.setter
    def transfer(self, description):
        if description in DpxImageElementTransfer.values:
            self._raw_image_element.Transfer = description

    @property
    def colorimetric(self):

        metric = self._raw_image_element.Colorimetric
        if metric == 0:
            return DpxImageElementColorimetric.User_defined
        elif metric == 1:
            return DpxImageElementColorimetric.Printing_density
        elif metric == 4:
            return DpxImageElementColorimetric.Unspecified_video
        elif metric == 5:
            return DpxImageElementColorimetric.SMPTE_240M
        elif metric == 6:
            return DpxImageElementColorimetric.CCIR_709_1
        elif metric == 7:
            return DpxImageElementColorimetric.CCIR_601_2_system_B_or_G
        elif metric == 8:
            return DpxImageElementColorimetric.CCIR_601_2_system_M
        elif metric == 9:
            return DpxImageElementColorimetric.NTSC_composite_video
        elif metric == 10:
            return DpxImageElementColorimetric.PAL_composite_video
        else:
            return metric

    @colorimetric.setter
    def colorimetric(self, metric):
        if metric in DpxImageElementColorimetric.values:
            self._raw_image_element.Colorimetric = metric

    @property
    def bit_size(self):
        return self._raw_image_element.BitSize

    @bit_size.setter
    def bit_size(self, bit):
        if bit in (1, 8, 10, 12, 16, 32, 64):
            self._raw_image_element.BitSize = bit

    @property
    def packing(self):
        packing_type = self._raw_image_element.Packing
        if packing_type == 0:
            return DpxImageElementPacking.packed32bit
        elif packing_type == 1:
            return DpxImageElementPacking.filled32bit
        else:
            return packing_type

    @packing.setter
    def packing(self, packing_type):
        if packing_type in DpxImageElementPacking.values:
            self._raw_image_element.Packing = packing_type

    @property
    def encoding(self):
        packing_type = self._raw_image_element.Encoding
        if packing_type == 0:
            return DpxImageElementEncoding.not_encoded
        elif packing_type == 1:
            return DpxImageElementEncoding.run_length_encoded
        else:
            return packing_type

    @packing.setter
    def packing(self, encoding_type):
        if encoding_type in DpxImageElementEncoding.values:
            self._raw_image_element.Encoding = encoding_type

    @property
    def data_offset(self):
        return self._raw_image_element.DataOffset

    @data_offset.setter
    def data_offset(self, offset_byte):
        self._raw_image_element.DataOffset = offset_byte

    @property
    def end_of_line_padding(self):
        return self._raw_image_element.EndOfLinePadding

    @end_of_line_padding.setter
    def end_of_line_padding(self, padding_byte):
        self._raw_image_element.EndOfLinePadding = padding_byte

    @property
    def end_of_image_padding(self):
        return self._raw_image_element.EndOfImagePadding

    @end_of_image_padding.setter
    def end_of_image_padding(self, padding_byte):
        self._raw_image_element.EndOfImagePadding = padding_byte

    @property
    def description(self):
        return str(self._raw_image_element.Description)

    @description.setter
    def description(self, text):
        self._raw_image_element.Description = text


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
        self.image_element = []
        for i in range(0, 8):
            self.image_element.append(_DpxGenericImageElement(self._raw_header.ImageHeader.ImageElement[i]))

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
    def number_elements(self):
        return self._raw_header.ImageHeader.NumberElements

    @number_elements.setter
    def number_elements(self, num):
        if 0 <= num <= 8:
            self._raw_header.ImageHeader.NumberElements = num

    @property
    def pixels_per_line(self):
        return self._raw_header.ImageHeader.PixelsPerLine

    @pixels_per_line.setter
    def pixels_per_line(self, pixels):
        self._raw_header.ImageHeader.PixelsPerLine = pixels

    @property
    def lines_per_element(self):
        return self._raw_header.ImageHeader.LinesPerElement

    @lines_per_element.setter
    def lines_per_element(self, lines):
        self._raw_header.ImageHeader.LinesPerElement = lines


class _DpxGenericOrientationHeader:
    def __init__(self, header):
        self._raw_header = header
        self.image_element = []
        for i in range(0, 8):
            self.image_element.append(_DpxGenericImageElement(self._raw_header.ImageHeader.ImageElement[i]))

    @property
    def x_offset(self):
        return self._raw_header.OrientHeader.XOffset

    @x_offset.setter
    def x_offset(self, pixels):
        self._raw_header.OrientHeader.XOffset = pixels

    @property
    def y_offset(self):
        return self._raw_header.OrientHeader.YOffset

    @y_offset.setter
    def y_offset(self, pixels):
        self._raw_header.OrientHeader.YOffset = pixels

    @property
    def x_center(self):
        return self._raw_header.OrientHeader.XCenter

    @x_center.setter
    def x_center(self, position):
        self._raw_header.OrientHeader.XCenter = position

    @property
    def y_center(self):
        return self._raw_header.OrientHeader.YCenter

    @y_center.setter
    def y_center(self, position):
        self._raw_header.OrientHeader.YCenter = position

    @property
    def x_original_size(self):
        return self._raw_header.OrientHeader.XOriginalSize

    @x_original_size.setter
    def x_original_size(self, size):
        self._raw_header.OrientHeader.XOriginalSize = size

    @property
    def y_original_size(self):
        return self._raw_header.OrientHeader.YOriginalSize

    @y_original_size.setter
    def y_original_size(self, size):
        self._raw_header.OrientHeader.YOriginalSize = size

    @property
    def file_name(self):
        return str(self._raw_header.OrientHeader.FileName)

    @file_name.setter
    def file_name(self, name):
        self._raw_header.OrientHeader.FileName = name

    @property
    def time_data(self):
        return str(self._raw_header.OrientHeader.TimeData)

    @time_data.setter
    def time_data(self, time_str):
        self._raw_header.OrientHeader.FileName = time_str

    @property
    def input_name(self):
        return str(self._raw_header.OrientHeader.InputName)

    @input_name.setter
    def input_name(self, name):
        self._raw_header.OrientHeader.InputName = name

    @property
    def input_sn(self):
        return str(self._raw_header.OrientHeader.InputSN)

    @input_sn.setter
    def input_sn(self, sn_str):
        self._raw_header.OrientHeader.InputSN = sn_str

    @property
    def border_x_left(self):
        return self._raw_header.OrientHeader.Border[0]

    @border_x_left.setter
    def border_x_left(self, x_left):
        self._raw_header.OrientHeader.Border[0] = x_left

    @property
    def border_x_right(self):
        return self._raw_header.OrientHeader.Border[1]

    @border_x_right.setter
    def border_x_right(self, x_right):
        self._raw_header.OrientHeader.Border[1] = x_right

    @property
    def border_y_top(self):
        return self._raw_header.OrientHeader.Border[2]

    @border_y_top.setter
    def border_y_top(self, y_top):
        self._raw_header.OrientHeader.Border[2] = y_top

    @property
    def border_y_bottom(self):
        return self._raw_header.OrientHeader.Border[3]

    @border_y_bottom.setter
    def border_y_bottom(self, y_bottom):
        self._raw_header.OrientHeader.Border[3] = y_bottom

    @property
    def aspect_ratio_h(self):
        return self._raw_header.OrientHeader.AspectRatio[0]

    @aspect_ratio_h.setter
    def aspect_ratio_h(self, aspect_h):
        self._raw_header.OrientHeader.AspectRatio[0] = aspect_h

    @property
    def aspect_ratio_v(self):
        return self._raw_header.OrientHeader.AspectRatio[1]

    @aspect_ratio_v.setter
    def aspect_ratio_v(self, aspect_v):
        self._raw_header.OrientHeader.AspectRatio[1] = aspect_v


class _DpxIndustryFilmInfoHeader:
    def __init__(self, header):
        self._raw_header = header

    @property
    def film_mfg_id(self):
        return str(self._raw_header.FilmHeader.FilmMfgId)

    @film_mfg_id.setter
    def film_mfg_id(self, id_str):
        self._raw_header.FilmHeader.FilmMfgId = id_str

    @property
    def film_type(self):
        return str(self._raw_header.FilmHeader.FilmType)

    @film_type.setter
    def film_type(self, type_str):
        self._raw_header.FilmHeader.FilmType = type_str

    @property
    def offset(self):
        return str(self._raw_header.FilmHeader.Offset)

    @offset.setter
    def offset(self, film_perforations_offset_str):
        self._raw_header.FilmHeader.Offset = film_perforations_offset_str

    @property
    def prefix(self):
        return str(self._raw_header.FilmHeader.Prefix)

    @prefix.setter
    def prefix(self, prefix_str):
        self._raw_header.FilmHeader.Prefix = prefix_str

    @property
    def count(self):
        return str(self._raw_header.FilmHeader.Count)

    @count.setter
    def count(self, count_str):
        self._raw_header.FilmHeader.Count = count_str

    @property
    def format(self):
        return str(self._raw_header.FilmHeader.Format)

    @format.setter
    def format(self, format_str):
        self._raw_header.FilmHeader.Format = format_str

    @property
    def frame_position(self):
        return self._raw_header.FilmHeader.FramePosition

    @frame_position.setter
    def frame_position(self, frame_pos):
        self._raw_header.FilmHeader.FramePosition = frame_pos

    @property
    def held_count(self):
        return self._raw_header.FilmHeader.HeldCount

    @held_count.setter
    def held_count(self, count):
        self._raw_header.FilmHeader.HeldCount = count

    @property
    def frame_rate(self):
        return self._raw_header.FilmHeader.FrameRate

    @frame_rate.setter
    def frame_rate(self, fps):
        self._raw_header.FilmHeader.FrameRate = fps

    @property
    def shutter_angle(self):
        return self._raw_header.FilmHeader.ShutterAngle

    @shutter_angle.setter
    def shutter_angle(self, degrees):
        self._raw_header.FilmHeader.ShutterAngle = degrees

    @property
    def frame_id(self):
        return str(self._raw_header.FilmHeader.FrameId)

    @frame_id.setter
    def frame_id(self, id_str):
        self._raw_header.FilmHeader.FrameId = id_str

    @property
    def slate_info(self):
        return str(self._raw_header.FilmHeader.SlateInfo)

    @slate_info.setter
    def slate_info(self, info_str):
        self._raw_header.FilmHeader.SlateInfo = info_str


class DpxIndustryTelevisionInfoHeaderInterlace:
    def __init__(self):
        pass

    values = (
        not_interlaced,
        interlaced
    ) = (0, 1)


class DpxIndustryTelevisionInfoHeaderVideoSignalType:
    def __init__(self):
        pass

    values = (
        Undefined,
        NTSC,
        PAL,
        PAL_M,
        SECAM,
        YCBCR_CCIR_601_2_525_line_2_1_interlace_4_3_aspect_ratio,
        YCBCR_CCIR_601_2_625_line_2_1_interlace_4_3_aspect_ratio,
        YCBCR_CCIR_601_2_525_line_2_1_interlace_16_9_aspect_ratio,
        YCBCR_CCIR_601_2_625_line_2_1_interlace_16_9_aspect_ratio,
        YCBCR_CCIR_1050_line_2_1_interlace_16_9_aspect_ratio,
        YCBCR_CCIR_1125_line_2_1_interlace_16_9_aspect_ratio,
        YCBCR_CCIR_1250_line_2_1_interlace_16_9_aspect_ratio,
        YCBCR_525_line_1_1_progressive_16_9_aspect_ratio,
        YCBCR_625_line_1_1_progressive_16_9_aspect_ratio,
        YCBCR_787_5_line_1_1_progressive_16_9_aspect_ratio
    ) = (0, 1, 3, 4, 50, 51, 100, 101, 150, 151, 152, 200, 201, 202,203)

class _DpxIndustryTelevisionInfoHeader:
    def __init__(self, header):
        self._raw_header = header

    @property
    def time_code(self):
        time_code_tmp = '{0:0>8x}'.format(self._raw_header.TvHeader.TimeCode)
        time_code_str = "{0}:{1}:{2}:{3}".format(time_code_tmp[0:2], time_code_tmp[2:4], time_code_tmp[4:6],
                                                 time_code_tmp[6:8])

        return str(time_code_str)

    @time_code.setter
    def time_code(self, time_code):
        time_code = time_code.lower()
        time_code_hex = "".join(time_code.split(":"))
        tc_dpx = int(time_code_hex, 16)
        self._raw_header.TvHeader.TimeCode = tc_dpx

    @property
    def user_bits(self):
        user_bits_tmp = '{0:0>8x}'.format(self._raw_header.TvHeader.UserBits)
        user_bits_str = "{0}:{1}:{2}:{3}".format(user_bits_tmp[0:2], user_bits_tmp[2:4], user_bits_tmp[4:6],
                                                 user_bits_tmp[6:8])
        return str(user_bits_str)

    @user_bits.setter
    def user_bits(self, bits):
        bits = bits.lower()
        bits_hex = "".join(bits.split(":"))
        user_bits_dpx = int(bits_hex, 16)
        self._raw_header.TvHeader.UserBits = user_bits_dpx

    @property
    def interlaced(self):
        interlace = self._raw_header.TvHeader.Interlace
        if interlace == 0:
            return DpxIndustryTelevisionInfoHeaderInterlace.not_interlaced
        elif interlace == 1:
            return DpxIndustryTelevisionInfoHeaderInterlace.interlaced
        else:
            return interlace

    @interlaced.setter
    def interlaced(self, interlace):
        if interlace in DpxIndustryTelevisionInfoHeaderInterlace.values:
            self._raw_header.TvHeader.Interlace = interlace

    @property
    def field_number(self):
        return self._raw_header.TvHeader.FieldNumber

    @field_number.setter
    def field_number(self, number):
        self._raw_header.TvHeader.FieldNumber = number

    @property
    def video_signal(self):
        video_signal_type = self._raw_header.TvHeader.VideoSignal

        if video_signal_type == 0:
            return DpxIndustryTelevisionInfoHeaderVideoSignalType.Undefined
        elif video_signal_type == 1:
            return DpxIndustryTelevisionInfoHeaderVideoSignalType.NTSC
        elif video_signal_type == 2:
            return DpxIndustryTelevisionInfoHeaderVideoSignalType.PAL
        elif video_signal_type == 3:
            return DpxIndustryTelevisionInfoHeaderVideoSignalType.PAL_M
        elif video_signal_type == 4:
            return DpxIndustryTelevisionInfoHeaderVideoSignalType.SECAM
        elif video_signal_type == 50:
            return DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_CCIR_601_2_525_line_2_1_interlace_4_3_aspect_ratio
