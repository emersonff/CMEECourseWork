# Mini project: Identify What Mathematical Model Best Fits an Empirical Bacteria Growth Data
The objective of this project is to fit previously collected microbial growth data to 4 published level one models(Logistic, Gompertz, Baranyi, Buchanan) using NLLS method and then statistically determine which model(s) best fits the growth data mainly using model selection approaches including AIC, BIC, AICc, and RSS.

## Data Preparation:
* [DataPrep.py](Code/DataPrep.py): is used to remove repeated and irrational data points. Additionally, it generates a new .csv file including IDs and the natural logarithm of population size for future convenience.

## Model Fittings and Plotting
* [Fitting.R](Code/Fitting.R): performs NLLS fitting for all models to each sub-dataset. Then it calculates AIC, RSS, BIC, AICc and saves the results for plottting.

* [PLotting.R](Code/Plottin.R): saves all fittings for report.

## Work Flows
```
sh run_MiniProject.sh 
```