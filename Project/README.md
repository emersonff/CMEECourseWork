# My CMEE Final Project Repository

This is an index of code of my final project submitted in partial fulfilment of the requirements for the degree of Master of Science/Research at Imperial College London.

To download the skeleton data(JSON files), please visit: https://drive.google.com/file/d/1Pa8huQ8Lz_dXCWxJYm5ClphJN_ctQkqI/view?usp=sharing


The main running sequence is as follows:
* [DataExtraction.py](Code/DataExtraction.py): Read metadata from csv file. Merge calibrated data.
* [MDataPlot.R](Code/MDataPlot.R): Visually inspect image labels
* [TestDGenerate.py](Code/TestDGenerate.py): Generate test dataset
* [GetSeq.py](Code/GetSeq.py): Get first image of every image sequence
* [CompareClassifier.py](Code/CompareClassifier.py): Compare the performance as classifier with CNN + MLP classifier
* [Clustering.py](Code/Clustering.py): Spectral clustering of different human poses



There are other utilities in [utils](Code/utils). [Cali_time.R](Code/Cali_time.R),[Final.R](Code/Final.R),[glm.R](Code/glm.R), [json_plot.R](Code/json_plot.R) are for data analysis.