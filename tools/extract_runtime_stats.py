#!/usr/bin/python

import json
import argparse

def parse(logfile):
  '''Input: logfile.'''
  with open(logfile) as f:
    return json.load(f)

def sum(lst, extractor):
  return reduce(lambda x,y: x + y, map(extractor, lst), 0)

def sum_replays(lst):
  return sum(lst, lambda o: o["total_replays"])

def sum_runtime(lst):
  return sum(lst, lambda o: o["prune_duration_seconds"])

def print_stats():
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--start_index', type=int,
    default=0,
    help='Which index to start summing from')
  parser.add_argument('-e', '--end_index', type=int,
    default=-1,
    help='Which index to end summing from')
  parser.add_argument('path', metavar='path', type=str)

  args = parser.parse_args()

  lst = parse(args.path)
  end_idx = len(lst) if (args.end_index == -1) else args.end_index
  subseq = lst[args.start_index:end_idx]

  print("Runtime: %0.2f, Replays: %d" % (sum_runtime(subseq), sum_replays(subseq)))

if __name__ == "__main__":
  print_stats()
