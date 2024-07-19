#!/usr/bin/python3
"""
Log Parsing:
    Reads stdin line by line and computes metrics.
"""
import sys
import re
import signal

# initialise accumulator, status counts and line counts
total_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


# define a log_stats function that logs the stats to stdout
def log_stats():
    """
    Logs statistics to the stdout
    """
    sys.stdout.write(f'File size: {total_size}\n')
    for key in sorted(status_counts.keys()):
        if status_counts[key] > 0:
            sys.stdout.write(f'{key}: {status_counts[key]}\n')


# signal handler for keyboard interrupt
def signal_handler(sig, frame):
    """
    Handles keyboard interruption CTRL+C and logs statistics to the stdout
    before exiting with success
    """
    log_stats()
    sys.exit(0)


# define a regex to match the desired status code and file size inputs
regex = r'^\S+ ?- ?\[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'

# test input
try:
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # check if input matches the regex pattern
        if not re.match(regex, line):
            continue

        # extract status code and file size from regex expression
        status_code = int(re.match(regex, line).group(1))
        file_size = int(re.match(regex, line).group(2))

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
    """
    Logs the stats to the stdout and graciously exits when program is
    interrupted by the user
    """
    signal.signal(signal.SIGINT, signal_handler)
finally:
    # print final status codes if script ends normally
    log_stats()
