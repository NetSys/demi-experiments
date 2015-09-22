#!/usr/bin/python

from extract_runtime_stats import *

# long runs:
experiments = [
  ("raft-45", "akka-raft-fuzz-long_2015_09_02_12_18_50_DDMin_STSSchedNoPeek"),
  ("raft-46", "akka-raft-fuzz-long_2015_09_02_12_36_41_DDMin_STSSchedNoPeek"),
  ("raft-56", "akka-raft-fuzz-long_2015_09_02_12_48_32_DDMin_STSSchedNoPeek"),
  ("raft-58-init", "akka-raft-fuzz-long_2015_09_02_13_25_20_DDMin_STSSchedNoPeek"),
  ("raft-58-log-match", "akka-raft-fuzz-long_2015_08_30_20_59_21_DDMin_STSSchedNoPeek"),
  ("raft-42", "akka-raft-fuzz-long_2015_08_30_21_57_21_DDMin_STSSchedNoPeek"),
  ("raft-66", "akka-raft-fuzz-long_2015_08_12_23_55_04_DDMin_STSSchedNoPeek"),
  ("spark-2294", "spark-fuzz_2015_09_22_10_35_51_DDMin_STSSchedNoPeek"),
  ("spark-2294-blocks", "spark-fuzz_2015_09_21_17_53_01_DDMin_STSSchedNoPeek")
]

NUM_NODES = 4

print("--- minimization ---")
for k,v in experiments:
  print(k)
  lst = parse("%s/minimization_stats.json" %v)
  init = lst[0]
  print("Initial: %d (%d)" %
      (get_deliveries(init), get_externals(init) + NUM_NODES))
  prov = lst[1]
  print("Provenance: %d (%d)" %
      (get_deliveries(prov), get_externals(prov) + NUM_NODES))
  # After both DDMin and IntMin
  sts = lst[3]
  print("STSSched: %d (%d)" %
      (get_deliveries(sts), get_externals(sts) + NUM_NODES))
  dpor = lst[-1]
  print("Wildcard DPOR: %d (%d)" %
      (get_deliveries(dpor), get_externals(dpor) + NUM_NODES))


print
print("--- runtime ---")
for k,v in experiments:
  print(k)
  lst = parse("%s/minimization_stats.json" %v)
  print("STSSched:")
  # 0 and 1 are fenceposts for provenance
  # 2 and 3 are DDMin and IntMin
  stssched_slice = lst[2:4]
  print_runtime_stats(stssched_slice)
  print("Wildcard DPOR:")
  dpor_slice = lst[4:]
  print_runtime_stats(dpor_slice)
