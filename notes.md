Experiments:

akka-raft-fuzz_2015_04_19_15_35_23*:
  - Original two-leader bug, reported
    [here](https://github.com/ktoso/akka-raft/issues/47). Before we had
    support for message shrinking.

akka-raft-fuzz_2015_05_17_17_14_33*:
  - Joint consensus bug, reported
    [here](https://github.com/ktoso/akka-raft/issues/49). Found as a result of
    message shrinking (before we made sure Starts were also removed).

akka-raft-fuzz_2015_05_18_17_09_51*:
  - Long run of a new two-leader bug, after support for message shrinking. MCS
    is inflated; would be interesting to see if we can make it the same length
    as short run (below) by reordering or allowing not previously seen
    messages.

akka-raft-fuzz_2015_05_19_17_49_06*:
  - Short run of a new two-leader bug, after support for message shrinking.
    Should be pretty close to minimal.
