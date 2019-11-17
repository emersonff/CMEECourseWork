# Biological Computing in Python 2

## Numerical Computing in Python
### Practicals
* [LV1.py](Code/LV1.py): A python program uses numerical integration in Python for solving a classical model in biology — the Lotka-Volterra model for a predator-prey system in two-dimensional space. It could take arguments for the four LV model parameters 𝑟, 𝑎, 𝑧 ,𝑒 from the command line. The output which is named as `LV_model.pdf` contains 2 figures describing Consumer-Resource population dynamics ans is saved under `Results` directory. 

### The need for speed: profiling code

#### Profiling within `ipython`  
To profile code under `ipython` environment, simply use the command:
```python
run -p your_python_script
run -p -s cumtime your_python_scripy #allow sorting the report by cumtime
#Additionally, -l limits the number of lines displayed or filters the results by function name, and -T saves the report in a text file
```
* [profileme.py](Code/profileme.py), [profileme2.py](Code/profileme2.py): Two Python program used for demonstrate how to profile python code.

#### Profiling without `ipython`
To profile code under `bash` environment, simply use the command:
```
python3 -m cProfile your_python_script
```
Or,
```
python3 -m cProfile -o profires your_python_script
```

#### Quick profiling with `timeit`
* [timeit.py](Code/timeit.py): A python program demonstrates how to use `timeit` module or `time` module to recording the running time of a specific section of code.

### Practicals
* [LV2.py](Code/LV2.py): Similar to `LV1.py`. It runs the Lotka-Volterra model with prey density dependence r*R*(1 - R/K). The results are saved in `LV2.pdf` under `Results` directory.
* [LV3.py](Code/LV3.py): A discrete-time version of the LV model. 
* [LV4.py](Code/LV4.py): A discrete-time version of the LV model with a random gaussian fluctuation in resource's growth rate at each time-step.
* [run_LV.py](Code/run_LV.py): A python script that runs and profiles 4 LV models metioned above.

### Networks in Python
* [DrawFW.py](Code/DrawFW.py): Generates and plots a random adjacency list of food web with "connectance probability C. The resulted plot is saved in `DrawFW.pdf` under `Results`directory.
* [Nets.R](Code/Nets.R): A R script visualizes the QMEE CDT collaboration network, coloring the the nodes by the type of node (organization type: "University","Hosting Partner", "Non-hosting Partner").
* [Nets.py](COde/Nets.py): A python version of `Nets.R`.
## Regular Expression in Python
* [regexs.py](Code/regexs.py): Some regexes tried during the lecture.
* [re4.py](Code/re4.py): Parsing email addresses using regexes.
* [blackbirds.py](Code/blackbirds.py): Captures the Kingdom, Phylum and Species name for each species and prints it out to screen neatly.

## Using Python to build workflows
* [TestR.py](Code/TestR.py): Runs `TestR.R`
* [using_os.py](Code/using_os.py): Gets files and directories in your home/ that start with either an upper or lower case 'C'
* [run_fmr_R.py](Code/run_fmr_R.py): Runs `fmr.R` to generate the desired result