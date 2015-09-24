#!/usr/bin/python

a = [
  (1140, 545, 37),
  (1730, 976, 61),
  (780, 360, 23),
  (2850, 953, 226),
  (1500, 164, 40),
  (1710, 1093, 180),
  (400, 262, 77),
  (1000, 43, 40),
  (700, 64, 51),
  (600, 18, 14),
  (600, 16, 16)
]

def reduction(total, new):
  return ((total * 1.0) - new) / total

for (orig,sts,us) in a:
  sts_reduction = reduction(orig, sts)
  us_reduction = reduction(orig, us)
  factor = sts * 1.0 / us
  print "%f %f %f" % (sts_reduction, us_reduction, factor)
