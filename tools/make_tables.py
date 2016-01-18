#!/usr/bin/python

from extract_runtime_stats import *

# long runs:
experiments = [
  ("raft-45", "akka-raft-fuzz-long_2016_01_03_20_36_00_DDMin_STSSchedNoPeek"), # "akka-raft-fuzz-long_2015_09_02_12_18_50_DDMin_STSSchedNoPeek"
  ("raft-46", "akka-raft-fuzz-long_2016_01_05_17_18_39_DDMin_STSSchedNoPeek"), # "akka-raft-fuzz-long_2015_09_02_12_36_41_DDMin_STSSchedNoPeek"
  ("raft-56", "akka-raft-fuzz-long_2016_01_10_13_47_46_DDMin_STSSchedNoPeek"), # "akka-raft-fuzz-long_2015_09_02_12_48_32_DDMin_STSSchedNoPeek"
  ("raft-58-init", "akka-raft-fuzz-long_2015_09_02_13_25_20_DDMin_STSSchedNoPeek"),
  ("raft-58-log-match", "akka-raft-fuzz-long_2015_08_30_20_59_21_DDMin_STSSchedNoPeek"),
  ("raft-42", "akka-raft-fuzz-long_2015_08_30_21_57_21_DDMin_STSSchedNoPeek"),
  ("raft-66", "akka-raft-fuzz-long_2015_08_12_23_55_04_DDMin_STSSchedNoPeek"),
  ("spark-2294", "spark-fuzz_2015_09_22_10_35_51_DDMin_STSSchedNoPeek"),
  ("spark-2294-blocks", "spark-fuzz_2015_09_21_17_53_01_DDMin_STSSchedNoPeek"),
  ("spark-3150", "spark-fuzz_2015_09_22_12_36_30_DDMin_STSSchedNoPeek"),
  ("spark-9256", "spark-fuzz_2015_09_15_20_44_06_DDMin_STSSchedNoPeek")
]

# Optimal runs:
#  ("raft-45-opt", "akka-raft-interactive_2016_01_03_15_13_24"), # 4 nodes
#  ("raft-46-opt", "akka-raft-interactive_2016_01_05_17_02_39"), # 3 nodes
#  ("raft-56-opt", "akka-raft-interactive_2016_01_09_18_05_42"), # 4 nodes
#  ("raft-58-init-opt", "akka-raft-interactive_2016_01_12_18_42_05"), # 4 nodes, 3 sends
#  ("raft-58-opt", "akka-raft-interactive_2016_01_18_13_21_55"), # 2 nodes [3 node cluster]
#  ("raft-42-opt", "akka-raft-interactive_2016_01_17_21_21_00"), # 4 nodes
#  ("raft-66-opt", "akka-raft-interactive_2016_01_17_21_51_48"), # 4 nodes

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
