import sys
from collections import defaultdict


def process_logs(lines):
  total_file_size = 0
  status_counts = defaultdict(int)
  line_count = 0

  try:
    for line in lines:
      line_count += 1
      line = line.strip()
      data = line.split()

      # Check if the line matches the expected format
      if len(data) >= 7 and data[3] == '"GET' and data[5].isdigit():
        status_code = int(data[6])
        file_size = int(data[7])

        total_file_size += file_size
        status_counts[status_code] += 1

      # Print statistics after every 10 lines
      if line_count % 10 == 0:
        print_stats(total_file_size, status_counts)

  except KeyboardInterrupt:
    print_stats(total_file_size, status_counts)


def print_stats(total_file_size, status_counts):
  print(f"File size: {total_file_size}")
  for status_code in sorted(status_counts.keys()):
    print(f"{status_code}: {status_counts[status_code]}")


if __name__ == "__main__":
  lines = sys.stdin.readlines()
  process_logs(lines)
