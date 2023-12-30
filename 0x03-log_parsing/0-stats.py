#!/usr/bin/env python3
"""
This module contains a function
that reads stdin line by line
and computes metrics
"""
import re
import sys

regex_pattern = r'''
    \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}          # IP Address
    \ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]    # Date and Time
    \ "GET \/projects\/260 HTTP\/1\.1"         # HTTP Request
    \ \d{1,3}                                  # Status Code
    \ \b(?:[1-9][0-9]{0,2}|1000|102[0-4])\b   # File size
'''

pattern = re.compile(regex_pattern, re.VERBOSE)


def input_checker():
  line_count = 0
  status_code = {}
  total_size = 0

  for line in sys.stdin:
    line = line.strip()  #remove newline character
    match = re.match(pattern, line)  #check for match

    if not match:
      continue  # Move to the next line if there's no match

    line_count += 1  # increase line count variable to perform print at 10counts
    arguments = line.strip().split()
    total_size += int(arguments[4])
    code = arguments[3]

    if code in status_code:
      status_code[code] += 1
    else:
      status_code[code] = 1

    if line_count == 10:
      print(f"File size: {total_size}")
      for status, count in status_code.items():
        print(f"{status}: {count}")
      line_count = 0  # reset line count after 10th line
  return
