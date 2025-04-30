# Final Case Study – Flood Risk Management for the IJssel River - EPA141

This repository contains all files and code used to conduct the final project for the course "Model-Based Decision Making" in the EPA Master's Programme. The project involves analyzing flood risk management strategies for the IJssel River region using robust decision-making under uncertainty.


## 🎯 Project Objectives

- Develop and evaluate policy strategies (e.g., dike heightening, Room for the River, Early Warning Systems)
- Apply techniques such as RDM, scenario discovery, and multi-objective optimization
- Provide actionable advice to the Delta Programme and critically reflect on model use in policy

## 🧱 Project Structure

| File/Module | Description |
|-------------|-------------|
| `dike_model_function.py` | Core simulation model: breach, water routing, damage calculations |
| `dike_model_optimization.py` | Optimization routines for exploring robust policy solutions |
| `problem_formulation.py` | Defines various XLRM setups: objectives, levers, uncertainties |
| `funs_generate_network.py` | Builds the dike network structure and loads fragility/loss data |
| `funs_dikes.py` | Tools for dike behavior, interpolation, breach logic |
| `funs_economy.py` | Damage, investment, evacuation cost calculations |
| `funs_hydrostat.py` | Functions for hydraulic processes and flood translation |
| `Problem Formulations.ipynb` | Notebook to prototype and validate problem formulations |

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

Results should be interpreted in conjunction with political, economic, and environmental context provided in the project reflection.
