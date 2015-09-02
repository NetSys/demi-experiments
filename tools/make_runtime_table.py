#!/usr/bin/python

from extract_runtime_stats import *

# long runs:
experiments = [
  ("raft-45": "akka-raft-fuzz-long_2015_09_02_12_18_50_DDMin_STSSchedNoPeek"),
  ("raft-46": "akka-raft-fuzz-long_2015_09_02_12_36_41_DDMin_STSSchedNoPeek"),
  ("raft-56": "akka-raft-fuzz-long_2015_09_02_12_48_32_DDMin_STSSchedNoPeek"),
  ("raft-58-init": "akka-raft-fuzz-long_2015_09_02_13_25_20_DDMin_STSSchedNoPeek"),
  ("raft-58-log-match": "akka-raft-fuzz-long_2015_08_30_20_59_21_DDMin_STSSchedNoPeek"),
  ("raft-42": "akka-raft-fuzz-long_2015_08_30_21_57_21_DDMin_STSSchedNoPeek"),
  ("raft-66": "akka-raft-fuzz-long_2015_08_12_23_55_04_DDMin_STSSchedNoPeek")
]

for k,v in experiments.iteritems():
  print(k)
  lst = parse("%s/minimization_stats.json" %v)
  print("STSSched:")
  stssched_slice = lst[0:2]
  print_stats(stssched_slice)
  print("Wildcard DPOR:")
  dpor_slice = lst[2:]
  print_stats(dpor_slice)
