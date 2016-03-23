import pydpx_meta

# create instance
dpx = pydpx_meta.DpxHeader("/root/V14_37_26_01_v001.0186.dpx")
# dpx = pydpx_meta.DpxHeader()

# normal access
print dpx.file_header.magic
print dpx.file_header.image_offset
print dpx.image_header.image_element[0].data_sign
print dpx.tv_header.time_code
print dpx.tv_header.frame_rate

# edit and save sample
print "- edit and save sample -"
# change time code
print dpx.tv_header.time_code
dpx.tv_header.time_code = "01:23:45:12"
print dpx.tv_header.time_code
# change orientation
dpx.raw_header.ImageHeader.Orientation = 2
# commit change
dpx.save("/root/test.dpx")

# header table direct access
print dpx.raw_header.FileHeader.Magic
print dpx.raw_header.FileHeader.ImageOffset
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

print dpx.raw_header.OrientHeader.XOriginalSize
print dpx.raw_header.OrientHeader.YOriginalSize
print dpx.raw_header.TvHeader.TimeCode
print dpx.raw_header.TvHeader.UserBits
print dpx.raw_header.TvHeader.FrameRate
