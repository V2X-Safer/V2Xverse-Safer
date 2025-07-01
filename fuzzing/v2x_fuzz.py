import logging
import random
import os
from V2Xverse.common.random import set_random_seeds
from .seed import load_seeds, mutate_seed
from .operator import Operator
from .metrics import run_simulation
from .report import FuzzReport

FUZZ_ROUNDS = 10
RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')

def save_result(round_idx, params, result):
    import yaml
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, f'result_{round_idx}.yaml')
    with open(out_path, 'w') as f:
        yaml.safe_dump({'params': params, 'result': result}, f)
    logging.info(f'Result saved: {out_path}')

def main():
    set_random_seeds()
    logging.basicConfig(level=logging.INFO)
    report = FuzzReport()
    operator = Operator()
    seeds = load_seeds()
    for i in range(FUZZ_ROUNDS):
        if seeds:
            seed = random.choice(seeds)
            params = mutate_seed(seed, operator)
        else:
            params = {}
            params.update(operator.random_weather())
            params.update(operator.random_traffic())
            params.update(operator.random_rsu())
        logging.info(f'Fuzz round {i+1}: params={params}')
        result = run_simulation(params)
        logging.info(f'Fuzz round {i+1}: result={result}')
        save_result(i+1, params, result)
        report.add(params, result)
    report_path = os.path.join(RESULTS_DIR, 'fuzz_report.yaml')
    report.save(report_path)
    logging.info(f'Fuzz summary: {report.summary()}')
    logging.info(f'Report saved: {report_path}')

if __name__ == '__main__':
    main()
