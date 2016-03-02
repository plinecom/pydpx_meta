from pydpx_meta import header
import glob
files = []

print files
for file in sorted(files):
    dpx = header.DpxHeader(file)
    print dpx.tv_header.timecode()

#dpx = header.DpxHeader("/root/V14_37_26_01_v001.0186.dpx")
dpx = header.DpxHeader()
print dpx.raw_header.FileHeader.Magic
print dpx.file_header.magic
print dpx.raw_header.FileHeader.ImageOffset
print dpx.file_header.image_offset
print dpx.raw_header.FileHeader.Version
print dpx.raw_header.FileHeader.FileSize
print dpx.raw_header.FileHeader.DittoKey
print dpx.raw_header.FileHeader.IndustrySize
print dpx.raw_header.FileHeader.UserSize
print dpx.raw_header.FileHeader.FileName
print dpx.raw_header.FileHeader.TimeData
print dpx.raw_header.FileHeader.Creator
print dpx.raw_header.FileHeader.Project
print dpx.raw_header.ImageHeader.Orientation
print dpx.raw_header.ImageHeader.NumberElements
print dpx.raw_header.ImageHeader.ImageElement[0].Description
print dpx.image_header.image_element[0].data_sign
print header.DpxImageElementDescriptor.values
print dpx.raw_header.OrientHeader.XOriginalSize
print dpx.raw_header.OrientHeader.YOriginalSize
print dpx.raw_header.TvHeader.TimeCode
print '{0:0>8x}'.format(dpx.raw_header.TvHeader.TimeCode)
timecode_tmp = '{0:0>8x}'.format(dpx.raw_header.TvHeader.TimeCode)
timecode_str = timecode_tmp[0:2]+":"+timecode_tmp[2:4]+":"+timecode_tmp[4:6]+":"+timecode_tmp[6:8]
print timecode_str
print dpx.raw_header.TvHeader.UserBits
print dpx.raw_header.TvHeader.FrameRate

print "test"
print dpx.tv_header.timecode
dpx.tv_header.timecode ="01:23:45:12"
print dpx.tv_header.timecode
# change orientation
dpx.raw_header.ImageHeader.Orientation =2
#dpx.save("/root/test.dpx")

