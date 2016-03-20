from pydpx_meta import header
import pydpx_meta
import glob
files = []

print files
for file in sorted(files):
    dpx = pydpx_meta.DpxHeader(file)
    print dpx.tv_header.timecode

#dpx = pydpx_meta.DpxHeaderEx("/root/V14_37_26_01_v001.0186.dpx")


dpx = pydpx_meta.DpxHeaderEx()
dpx.describe()


#dpx.save("/root/test.dpx")

