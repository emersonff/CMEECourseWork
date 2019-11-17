import os                   # Operating-system interface
import subprocess           # To run other programs
p = subprocess.Popen(["Rscript", "fmr.R"],\
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = p.communicate()

if stderr.decode() == "":
    print("Run was successful.")
    print(stdout.decode())