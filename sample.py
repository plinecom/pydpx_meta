from pydpx_meta import header

fpw = open("/root/test.dpx","wb")
# read magic

dpx = header.DpxHeader("/root/V14_37_26_01_v001.0186.dpx")
print dpx.header.FileHeader.Magic
print dpx.header.FileHeader.ImageOffset
print dpx.header.FileHeader.Version
print dpx.header.FileHeader.FileSize
print dpx.header.FileHeader.DittoKey
print dpx.header.FileHeader.IndustrySize
print dpx.header.FileHeader.UserSize
print dpx.header.FileHeader.FileName
print dpx.header.FileHeader.TimeData
print dpx.header.FileHeader.Creator
print dpx.header.FileHeader.Project
print dpx.header.ImageHeader.Orientation
print dpx.header.ImageHeader.NumberElements
print dpx.header.ImageHeader.ImageElement[0].Description
print dpx.header.OrientHeader.XOriginalSize
print dpx.header.OrientHeader.YOriginalSize

magic = ""
if magic == "SDPX":
    big_endian = True

fpw.write(dpx.header)
