import pydpx_meta.header as header


class _DpxGenericHeaderEx(header._DpxGenericHeader):
    def __init__(self, raw_header):
        header._DpxGenericHeader.__init__(self, raw_header)

    @property
    def is_dit_to_key(self):
        dit_to_key = self.dit_to_key
        if dit_to_key == 0:
            return False
        else:
            return True

    @is_dit_to_key.setter
    def is_dit_to_key(self, dit_to_key):
        if dit_to_key:
            self.dit_to_key = 1
        else:
            self.dit_to_key = 0


class _DpxGenericImageHeaderEx(header._DpxGenericImageHeader):
    def __init__(self, raw_header):
        header._DpxGenericImageHeader.__init__(self, raw_header)

        self.image_element = []
        for i in range(0, 8):
            self.image_element.append(_DpxGenericImageElementEx(self._raw_header.ImageHeader.ImageElement[i]))

    @property
    def orientation_str(self):
        orient = self.orientation
        if orient == header.DpxImageHeaderOrientaion.LeftToRight_TopToBottom:
            return "LeftToRight_TopToBottom"
        elif orient == header.DpxImageHeaderOrientaion.RightToLeft_TopToBottom:
            return "RightToLeft_TopToBottom"
        elif orient == header.DpxImageHeaderOrientaion.LeftToRight_BottomToTop:
            return "LeftToRight_BottomToTop"
        elif orient == header.DpxImageHeaderOrientaion.RightToLeft_BottomToTop:
            return "RightToLeft_BottomToTop"
        elif orient == header.DpxImageHeaderOrientaion.TopToBottom_LeftToRight:
            return "TopToBottom_LeftToRight"
        elif orient == header.DpxImageHeaderOrientaion.TopTOBottom_RightToLeft:
            return "TopTOBottom_RightToLeft"
        elif orient == header.DpxImageHeaderOrientaion.BottomToTop_LeftToRight:
            return "BottomToTop_LeftToRight"
        elif orient == header.DpxImageHeaderOrientaion.BottomToTop_RightToLeft:
            return "BottomToTop_RightToLeft"
        else:
            return str(orient)


class _DpxGenericImageElementEx(header._DpxGenericImageElement):
    def __init__(self, image_element):
        header._DpxGenericImageElement.__init__(self, image_element)

    @property
    def data_sign_str(self):
        sign = self.data_sign
        if sign == header.DpxImageElementSign.unsigned_value:
            return "Unsigned_value"
        elif sign == header.DpxImageElementSign.signed_value:
            return "Signed_value"
        else:
            return str(sign)

    @property
    def descriptor_str(self):
        desc = self.descriptor
        if desc == header.DpxImageElementDescriptor.User_Defined:
            return "User-Defined"
        elif desc == header.DpxImageElementDescriptor.Red:
            return "Red"
        elif desc == header.DpxImageElementDescriptor.Green:
            return "Green"
        elif desc == header.DpxImageElementDescriptor.Blue:
            return "Blue"
        elif desc == header.DpxImageElementDescriptor.Alpha:
            return "Alpha"
        elif desc == header.DpxImageElementDescriptor.Luminance:
            return "Luminance"
        elif desc == header.DpxImageElementDescriptor.Chrominance:
            return "Chrominance"
        elif desc == header.DpxImageElementDescriptor.Depth:
            return "Depth"
        elif desc == header.DpxImageElementDescriptor.Composite_video:
            return "Composite_video"
        elif desc == header.DpxImageElementDescriptor.RGB:
            return "RGB"
        elif desc == header.DpxImageElementDescriptor.RGBA:
            return "RGBA"
        elif desc == header.DpxImageElementDescriptor.ABGR:
            return "ABGR"
        elif desc == header.DpxImageElementDescriptor.CbYCrY:
            return "CbYCrY"
        elif desc == header.DpxImageElementDescriptor.CbYaCrYa:
            return "CbYaCrYa"
        elif desc == header.DpxImageElementDescriptor.CbYCr:
            return "CbYCr"
        elif desc == header.DpxImageElementDescriptor.CbYCra:
            return "CbYCra"
        elif desc == header.DpxImageElementDescriptor.User_defined_2_component_element:
            return "User-defined 2-component element"
        elif desc == header.DpxImageElementDescriptor.User_defined_3_component_element:
            return "User-defined 3-component element"
        elif desc == header.DpxImageElementDescriptor.User_defined_4_component_element:
            return "User-defined 4-component element"
        elif desc == header.DpxImageElementDescriptor.User_defined_5_component_element:
            return "User-defined 5-component element"
        elif desc == header.DpxImageElementDescriptor.User_defined_6_component_element:
            return "User-defined 6-component element"
        elif desc == header.DpxImageElementDescriptor.User_defined_7_component_element:
            return "User-defined 7-component element"
        elif desc == header.DpxImageElementDescriptor.User_defined_8_component_element:
            return "User-defined 8-component element"
        else:
            return str(desc)

    @property
    def transfer_str(self):
        trans = self.transfer
        if trans == header.DpxImageElementTransfer.User_defined:
            return "User-defined"
        elif trans == header.DpxImageElementTransfer.Printing_density:
            return "Printing density"
        elif trans == header.DpxImageElementTransfer.Linear:
            return "Linear"
        elif trans == header.DpxImageElementTransfer.Logarithmic:
            return "Logarithmic"
        elif trans == header.DpxImageElementTransfer.Unspecified_video:
            return "Unspecified video"
        elif trans == header.DpxImageElementTransfer.SMPTE_240M:
            return "SMPTE 240M"
        elif trans == header.DpxImageElementTransfer.CCIR_709_1:
            return "CCIR 709-1"
        elif trans == header.DpxImageElementTransfer.CCIR_601_2_system_B_or_G:
            return "CCIR 601-2 system B or G"
        elif trans == header.DpxImageElementTransfer.CCIR_601_2_system_M:
            return "CCIR 601-2 system M"
        elif trans == header.DpxImageElementTransfer.NTSC_composite_video:
            return "NTSC composite video"
        elif trans == header.DpxImageElementTransfer.PAL_composite_video:
            return "PAL composite video"
        elif trans == header.DpxImageElementTransfer.Z_linear:
            return "Z linear"
        elif trans == header.DpxImageElementTransfer.Z_homogeneous:
            return "Z homogeneous"
        else:
            return str(trans)

    @property
    def colorimetric_str(self):

        metric = self.colorimetric
        if metric == header.DpxImageElementColorimetric.User_defined:
            return "User-defined"
        elif metric == header.DpxImageElementColorimetric.Printing_density:
            return "Printing density"
        elif metric == header.DpxImageElementColorimetric.Unspecified_video:
            return "Unspecified video"
        elif metric == header.DpxImageElementColorimetric.SMPTE_240M:
            return "SMPTE 240M"
        elif metric == header.DpxImageElementColorimetric.CCIR_709_1:
            return "CCIR 709-1"
        elif metric == header.DpxImageElementColorimetric.CCIR_601_2_system_B_or_G:
            return "CCIR 601-2 system B or G"
        elif metric == header.DpxImageElementColorimetric.CCIR_601_2_system_M:
            return "CCIR 601-2 system M"
        elif metric == header.DpxImageElementColorimetric.NTSC_composite_video:
            return "NTSC composite video"
        elif metric == header.DpxImageElementColorimetric.PAL_composite_video:
            return "PAL composite video"
        else:
            return str(metric)

    @property
    def packing_str(self):
        packing_type = self.packing
        if packing_type == header.DpxImageElementPacking.packed32bit:
            return "Packed 32bit"
        elif packing_type == header.DpxImageElementPacking.filled32bit:
            return "Filled 32bit"
        else:
            return str(packing_type)

    @property
    def encoding_str(self):
        encoding_type = self.encoding
        if encoding_type == header.DpxImageElementEncoding.not_encoded:
            return "Not encoded"
        elif encoding_type == header.DpxImageElementEncoding.run_length_encoded:
            return "Run length encoded (RLE)"
        else:
            return str(encoding_type)


class _DpxGenericOrientationHeaderEx(header._DpxGenericOrientationHeader):
    def __init__(self, raw_header):
        header._DpxGenericOrientationHeader.__init__(self, raw_header)


class _DpxIndustryTelevisionInfoHeaderEx(header._DpxIndustryTelevisionInfoHeader):
    def __init__(self, raw_header):
        header._DpxIndustryTelevisionInfoHeader.__init__(self, raw_header)

    @property
    def is_interlaced(self):

        interlace = self.interlaced
        if interlace == header.DpxIndustryTelevisionInfoHeaderInterlace.not_interlaced:
            return False
        elif interlace == header.DpxIndustryTelevisionInfoHeaderInterlace.interlaced:
            return True
        else:
            return interlace

    @is_interlaced.setter
    def is_interlaced(self, is_interlace):

        if is_interlace:
            self._raw_header.TvHeader.Interlace = 1
        else:
            self._raw_header.TvHeader.Interlace = 0


    @property
    def video_signal_str(self):
        type = self.video_signal

        if type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.Undefined:
            return "Undefined"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.NTSC:
            return "NTSC"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.PAL:
            return "PAL"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.PAL_M:
            return "PAL-M"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.SECAM:
            return "SECAM"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_CCIR_601_2_525_line_2_1_interlace_4_3:
            return "YCBCR CCIR 601-2 525-line 2:1 interlace, 4:3 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_CCIR_601_2_625_line_2_1_interlace_4_3:
            return "YCBCR CCIR 601-2 625-line 2:1 interlace, 4:3 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_CCIR_601_2_525_line_2_1_interlace_16_9:
            return "YCBCR CCIR 601-2 525-line 2:1 interlace, 16:9 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_CCIR_601_2_625_line_2_1_interlace_16_9:
            return "YCBCR CCIR 601-2 625-line 2:1 interlace, 16:9 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_1050_line_2_1_interlace_16_9:
            return "YCBCR 1050-line 2:1 interlace, 16:9 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_1125_line_2_1_interlace_16_9:
            return "YCBCR 1125-line 2:1 interlace, 16:9 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_1250_line_2_1_interlace_16_9:
            return "YCBCR 1250-line 2:1 interlace, 16:9 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_525_line_1_1_progressive_16_9:
            return "YCBCR 525-line 1:1 progressive, 16:9 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_625_line_1_1_progressive_16_9:
            return "YCBCR 625-line 1:1 progressive, 16:9 aspect ratio"
        elif type == header.DpxIndustryTelevisionInfoHeaderVideoSignalType.YCBCR_787_5_line_1_1_progressive_16_9:
            return "YCBCR 787.5-line 1:1 progressive, 16:9 aspect ratio"
        else:
            return str(type)
