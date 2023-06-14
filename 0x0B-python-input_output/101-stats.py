#!/usr/bin/python3
"""Log parsing"""


import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

    """Extract relevant information from the line"""
    parts = line.split()
    file_size = int(parts[-1])
    status_code = parts[-2]


    total_file_size += file_size

    if status_code in status_codes:
        status_codes[status_code] += 1

    if line_count % 10 == 0:
        print("Total file size: {}".format(total_file_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print("{}: {}".format(code, status_codes[code]))


except KeyboardInterrupt:
    """Handle keyboard interruption (CTRL + C)"""
    print("Total file size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
