# Final Case Study – Flood Risk Management for the IJssel River - EPA141

This repository contains all files and code used to conduct the final project for the course "Model-Based Decision Making" in the EPA Master's Programme. The project involves analyzing flood risk management strategies for the IJssel River region using robust decision-making under uncertainty.


## 🎯 Project Objectives

- Develop and evaluate policy strategies (e.g., dike heightening, Room for the River, Early Warning Systems)
- Apply techniques such as RDM, scenario discovery, and multi-objective optimization
- Provide actionable advice to the Delta Programme and critically reflect on model use in policy

## 🧱 Project Structure

| Path | File/Module | Description                                                      |
|------|-------------|------------------------------------------------------------------|
| `model_scripts/` | `dike_model_function.py` | Core simulation: breach logic, routing, and damage computations  |
|  | `dike_model_optimization.py` | Optimization routines for robust strategy evaluation             |
|  | `dike_model_simulation.py` | Experimental setups and batch simulations                        |
|  | `problem_formulation.py` | Defines XLRM configurations: objectives, levers, uncertainties   |
|  | `funs_generate_network.py` | Builds dike network; loads fragility and loss data               |
|  | `funs_dikes.py` | Dike behavior models: breach mechanics, interpolation tools      |
|  | `funs_economy.py` | Economic calculations: investment, damage, evacuation costs      |
|  | `funs_hydrostat.py` | Simulates hydraulic processes and flood translation              |
|  | `GSA.ipynb` | Global Sensitivity Analysis                                      |
|  | `PRIM_*.ipynb` | Scenario discovery for different actor perspectives              |
|  | `DimStack_*.ipynb` | Visualization of trade-offs across levers and uncertainiteis     |
|  | `Experimental runs .ipynb` | Logs and setups for batch experiments                            |
|  | `__init__.py` | Marks module directory for imports                               |
| `data/` | Various subfolders & `.xlsx` files | Input data for fragility, hydrology, losses, rating curves, etc. |
| `experimental data/` | `.tar.gz` archives | Compressed files containing model outputs from exploratory runs  |
| `images/` | `rfr_IJssel.PNG`, `rfr_wlreduction.PNG` | Visualizations constructed from scripts                          |
| `report/` | — | Project write-up and documentation (not shown)                   |
| — | `EPAcourse_presentation.pptx` | Final assignment presentation slides                             |
| — | `requirements.txt` | Python dependencies for environment setup                        |


## 📦 Dependencies

Install required packages with:

```bash
pip install -r requirements.txt
```

Required libraries include:
- `ema_workbench`
- `networkx`
- `pandas`
- `numpy`
- `openpyxl`

## 👥 Team Members

- Ada Precup — 5240719  
- Akmal Umar — 6128971  
- Muhammad Haidar Ramadhani — 6122221  
- Dell'Orto Alessandro — 6129161  

## 📌 Notes

This model is developed for exploratory analysis only and is not calibrated for real-world prediction. It supports strategy comparison and stakeholder reflection under uncertainty.

Results should be interpreted in conjunction with political, economic, and environmental context provided in the project reflection and report.
