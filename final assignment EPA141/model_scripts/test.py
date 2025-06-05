import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

from ema_workbench import (
    Model,
    Policy,
    ema_logging,
    SequentialEvaluator,
    MultiprocessingEvaluator,
    Scenario,
)
from dike_model_function import DikeNetwork
from problem_formulation import get_model_for_problem_formulation, sum_over, sum_over_time

ema_logging.log_to_stderr(ema_logging.INFO)

if __name__ == "__main__":
    # choose problem formulation number, between 0-5
    dike_model, planning_steps = get_model_for_problem_formulation(3)
    print("model loaded")

    # print uncertainty names
    print("Uncertainties defined in model:")
    for u in dike_model.uncertainties:
        print("-", u.name)

    # ✅ create a reference scenario for all uncertainties (fully compatible with old versions)
    reference_dict = {}
    for u in dike_model.uncertainties:
        if hasattr(u, "categories"):
            reference_dict[u.name] = u.categories[0]
        elif hasattr(u, "lower_bound") and hasattr(u, "upper_bound"):
            reference_dict[u.name] = (u.lower_bound + u.upper_bound) / 2

    reference = Scenario("reference")
    reference.parameters = reference_dict
    print("Reference scenario created.")

    # run baseline experiments (optional)
    with MultiprocessingEvaluator(dike_model) as evaluator:
        experiments, outcomes = evaluator.perform_experiments(scenarios=50, policies=4)
    print("results loaded")

    # build epsilon values for optimization
    epsilons = []
    for name, values in outcomes.items():
        values = np.asarray(values)
        min_val, max_val = values.min(), values.max()
        range_val = max_val - min_val

        if range_val < 1e-5:
            epsilon = 1e-5  # avoid zero epsilon
        else:
            epsilon = range_val * 0.2

        epsilons.append(epsilon)

    print("epsilons loaded")

    # perform optimization using fixed reference scenario
    with MultiprocessingEvaluator(dike_model) as evaluator:
        results, convergence = evaluator.optimize(
            nfe=20,
            searchover="levers",
            epsilons=epsilons,
            reference=reference  # ✅ fixes the KeyError
        )

    print("results optimized")