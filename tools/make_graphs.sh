#!/bin/bash

# Must be invoked from the top-level STS2 directory.

for F in akka-raft-fuzz-long_2015_09_02_12_18_50_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_09_02_12_36_41_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_09_02_12_48_32_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_09_02_13_25_20_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_08_30_20_59_21_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_08_30_21_57_21_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_08_12_23_55_04_DDMin_STSSchedNoPeek \
  spark-fuzz_2015_09_22_10_35_51_DDMin_STSSchedNoPeek \
  spark-fuzz_2015_09_21_17_53_01_DDMin_STSSchedNoPeek \
  spark-fuzz_2015_09_22_12_36_30_DDMin_STSSchedNoPeek \
  spark-fuzz_2015_09_15_20_44_06_DDMin_STSSchedNoPeek; do

  echo "Making $F"
  ./interposition/src/main/python/minimization_stats/generate_graph.py experiments/$F/minimization_stats.json
done

for F in akka-raft-fuzz-long_2015_09_02_12_18_50_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_09_02_12_36_41_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_09_02_12_48_32_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_09_02_13_25_20_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_08_30_20_59_21_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_08_30_21_57_21_DDMin_STSSchedNoPeek \
  akka-raft-fuzz-long_2015_08_12_23_55_04_DDMin_STSSchedNoPeek \
  spark-fuzz_2015_09_22_10_35_51_DDMin_STSSchedNoPeek \
  spark-fuzz_2015_09_21_17_53_01_DDMin_STSSchedNoPeek \
  spark-fuzz_2015_09_22_12_36_30_DDMin_STSSchedNoPeek \
  spark-fuzz_2015_09_15_20_44_06_DDMin_STSSchedNoPeek; do

  open experiments/$F/minimization_stats.pdf
done
