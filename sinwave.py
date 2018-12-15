import math
import argparse
import json
import tensorflow as tf
import sys

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--max_steps', type=int, default=300,
                      help='Number of steps to run trainer')
  parser.add_argument('--sinfreq', type=float, default=1.0)
  parser.add_argument('--sinscale', type=float, default=1.0)
  parser.add_argument('--sinfreq2', type=float, default=1.0)
  parser.add_argument('--sinscale2', type=float, default=1.0)
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

def main(_):
  for i in range(0, 100):
    print( \
      json.dumps({ \
        'step': i, \
        'sqrstep': math.sqrt(i), \
        'sinwave': FLAGS.sinscale * math.sin(i * FLAGS.sinfreq), \
        'sinwave2': FLAGS.sinscale2 * math.sin(i * FLAGS.sinfreq2) \
        }))
