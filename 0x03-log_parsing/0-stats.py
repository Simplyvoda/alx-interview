#!/usr/bin/env python3
"""
This module contains a function
that reads stdin line by line
and computes metrics
"""
import re
import sys

fmt = (r'\s*(?P<ip>\S+)\s*',
       r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
       r'\s*"(?P<request>[^"]*)"\s*', r'\s*(?P<status_code>\S+)',
       r'\s*(?P<file_size>\d+)')
pattern = '{}\\-{}{}{}{}\\s*'.format(fmt[0], fmt[1], fmt[2], fmt[3], fmt[4])


def main():
  line_count = 0
  status_code = {}
  total_size = 0

  try:
    for line in sys.stdin:
      line = line.strip()  # remove newline character
      match = re.fullmatch(pattern, line)  # check for match
      if not match:
        continue  # Move to the next line if there's no match

      line_count += 1  # increase line count to perform print at 10counts
      arguments = line.strip().split(" ")
      total_size += int(arguments[-1])
      code = arguments[-2]

      if code in status_code:
        status_code[code] += 1
      else:
        status_code[code] = 1

      if line_count == 10:
        print(f"File size: {total_size}")
        for status in sorted(status_code.keys()):
          print(f"{status}: {status_code[status]}")
        line_count = 0  # reset line count after 10th line

  except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for status in sorted(status_code.keys()):
      print(f"{status}: {status_code[status]}")
    sys.exit()


if __name__ == '__main__':
  main()
