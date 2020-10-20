
import json
import matplotlib.pyplot as plt
import os

""" plt.plot([10,9,8], [1, 2, 3])
plt.ylabel('Rank')
plt.xlabel('Time')
plt.show()
         """


         

directory = "./europe/"
ranklists = []
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(filename, "r")
        ranklist = json.load(f)

    else:
        continue