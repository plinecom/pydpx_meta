from pydpx_meta import header
import pydpx_meta
import timecode
import glob
files = []

# time code sample
files = glob.glob("/root/test/*.dpx")
files = sorted(files)

print("-------------------")

# display time code
for file in files:
    dpx = pydpx_meta.DpxHeader(file)
    print(dpx.tv_header.time_code)

print("-------------------")

# increment 1 frame to time code
dpx = pydpx_meta.DpxHeader(files[0])

tc = timecode.Timecode(dpx.tv_header.frame_rate_for_tc, dpx.tv_header.time_code)
delta_tc = timecode.Timecode(dpx.tv_header.frame_rate_for_tc, "00:00:00:00")

for file in files:
    dpx = pydpx_meta.DpxHeader(file)
    tc += delta_tc
    dpx.tv_header.time_code = tc
    print(dpx.tv_header.time_code)
