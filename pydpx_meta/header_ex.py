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


