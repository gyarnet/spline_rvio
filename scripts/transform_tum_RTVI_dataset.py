import os
dataset_dir = "/home/gyarnet/slam/data/RTVI/"
for f_basename in os.listdir(dataset_dir):
    f_basename_rm_ext = f_basename.split(".")[0]
    new_fname = dataset_dir + f_basename_rm_ext + "_tum_gt.txt"
    ext = f_basename.split(".")[1]
    if ext != "csv":
        continue
    fp = open(dataset_dir + f_basename)
    lines = fp.readlines()
    for line in lines:
        tokens = line.split(',')

    fp.close()