#!/usr/bin/python3
""""""
import sys
import re
import signal

# initialise accumulator, status counts and line counts
total_size: int = 0
status_counts: 'dict[int, int]' = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count: int = 0


# define a log_stats function that logs the stats to stdout
def log_stats():
    """"""
    sys.stdout.write(f'File size: {total_size}\n')
    for key in sorted(status_counts):
        sys.stdout.write(f'{key}: {status_counts[key]}\n')


# signal handler for keyboard interrupt
def signal_handler(sig, frame):
    log_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# define a regex to match the desired status code and file size inputs
# <status_code>: <file_size>
regex = r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'

# test input
# print('Enter log data:')
try:
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # check if input matches the regex pattern
        if not re.match(regex, line):
            continue

        # extract status code and file size from regex expression
        status_code = int(re.match(regex, line).group(1))
        # check output
        # print(f'{status_code}')
        file_size = int(re.match(regex, line).group(2))
        # check output
        # print(f'{file_size}')

        # update the total file size
        total_size += file_size

        # update the count for the status code
        if status_code in status_counts.keys():
            status_counts[status_code] += 1

        # increase line count till we reach 10
        line_count += 1

        # check if 10 lines are reached and log the stats to stdout
        if line_count == 10:
            log_stats()
            line_count = 0


except KeyboardInterrupt:
    """"""
    signal.signal(signal.SIGINT, signal_handler)

# print final status codes if script ends normally
log_stats()
