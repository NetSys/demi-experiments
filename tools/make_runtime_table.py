#!/usr/bin/python

import os

# long runs:
experiments = {
  "raft-42": "akka-raft-fuzz-long_2015_08_30_21_57_21_DDMin_STSSchedNoPeek",
}

for k,v in experiments.iteritems():
  print(k)
  os.system("./tools/extract_runtime_stats.py %s/minimization_stats.json" % v)
