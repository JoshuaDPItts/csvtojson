import csv
import json
import sys


args = sys.argv
input_file = args[1]
input_file_fh = open(input_file, 'r')
#assume headers TODO: fix later for both:
headers = input_file_fh.readline().strip().split(',')

reader = csv.DictReader(input_file_fh, fieldnames=headers)

out = json.dumps([row for row in reader])

print out
