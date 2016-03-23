import header


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



class _DpxIndustryTelevisionInfoHeaderEx(header._DpxIndustryTelevisionInfoHeader):
    def __init__(self, raw_header):
        header._DpxIndustryTelevisionInfoHeader.__init__(self, raw_header)

    @property
    def is_interlaced(self):
        interlace = self._raw_header.TvHeader.Interlace
        if interlace == 0:
            return False
        elif interlace == 1:
            return True
        else:
            return interlace

    @is_interlaced.setter
    def is_interlaced(self, is_interlace):

        if is_interlace:
            self._raw_header.TvHeader.Interlace = 1
        else:
            self._raw_header.TvHeader.Interlace = 0


