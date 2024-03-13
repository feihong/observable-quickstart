import csv
import sys

data = {
  "Seattle": [69, 108, 178, 207, 253, 268, 312, 281, 221, 142, 72, 52],
  "Chicago": [135, 136, 187, 215, 281, 311, 318, 283, 226, 193, 113, 106],
  "San Francisco": [165, 182, 251, 281, 314, 330, 300, 272, 267, 243, 189, 156]
}

writer = csv.writer(sys.stdout)
writer.writerow(list(data.keys()))

for row in zip(*data.values()):
  writer.writerow(row)
