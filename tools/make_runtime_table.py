#!/usr/bin/python

from extract_runtime_stats import *

# long runs:
experiments = {
  "raft-42": "akka-raft-fuzz-long_2015_08_30_21_57_21_DDMin_STSSchedNoPeek",
}

for k,v in experiments.iteritems():
  print(k)
  lst = parse("%s/minimization_stats.json" %v)
  print("STSSched:")
  stssched_slice = lst[0:2]
  print_stats(stsschedSlice)
  print("Wildcard DPOR:")
  dpor_slice = lst[2:]
  print_stats(dpor_slice)
