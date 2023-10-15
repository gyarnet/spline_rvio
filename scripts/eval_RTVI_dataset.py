import subprocess
import os
dataset_dir = "/home/gyarnet/slam/data/RTVI/"
for f_basename in os.listdir(dataset_dir):
    f_basename_rm_ext = f_basename.split(".")[0]
    ext = f_basename.split(".")[1]
    if ext != "bag":
        continue
    # print(f_basename_rm_ext)
    # result = subprocess.run(["roslaunch","spline_vio","RTVI.launch", "bag:=" + dataset_dir + f_basename, "results:=" + "/tmp/" + f_basename_rm_ext + ".txt"],
    #                          stdout=subprocess.PIPE,
    #                          encoding='utf-8')
    # print(result.stdout)
    subprocess.run(["evo_traj","tum",""])