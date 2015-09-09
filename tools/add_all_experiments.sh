#!/bin/bash

for F in akka-raft-fuzz-long_2015_09_02_12_18_50_DDMin_STSSchedNoPeek akka-raft-fuzz-long_2015_09_02_12_36_41_DDMin_STSSchedNoPeek akka-raft-fuzz-long_2015_09_02_12_48_32_DDMin_STSSchedNoPeek akka-raft-fuzz-long_2015_09_02_13_25_20_DDMin_STSSchedNoPeek akka-raft-fuzz-long_2015_08_30_20_59_21_DDMin_STSSchedNoPeek akka-raft-fuzz-long_2015_08_30_21_57_21_DDMin_STSSchedNoPeek akka-raft-fuzz-long_2015_08_12_23_55_04_DDMin_STSSchedNoPeek; do
  git add $F/*
  git commit -m "Update minimization stats"
done

git push
