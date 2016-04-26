from OCCUtils.Construct import *
from OCCUtils.Topology import Topo
from OCC.KBE.face import Face
box = make_box(1,1,1)
# get a face
f = Topo(box).faces().next()
# PythonOCC's KBE module is a pretty nice compact API
F = Face(f)
# find the domain of the surface
F.domain()
# build a curve where you want to split the face
F.iso_curve(0, 0.5)
tt=F.iso_curve(0, 0.5)
# make a BRep from a curve
split_edge = make_edge(tt.Line())
# use that to split
split_srf = splitter(F, split_edge)
