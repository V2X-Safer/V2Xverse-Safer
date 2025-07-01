import os
import glob
import yaml
import random

SEED_DIR = os.path.join(os.path.dirname(__file__), '../seeds')

def load_seeds(seed_dir=SEED_DIR):
    seeds = []
    for s in glob.glob(os.path.join(seed_dir, '*.yaml')):
        try:
            with open(s, 'r') as f:
                seeds.append(yaml.safe_load(f))
        except Exception:
            continue
    return seeds

def mutate_seed(seed, operator):
    mutated = dict(seed) if isinstance(seed, dict) else {}
    mutated.update(operator.random_weather())
    mutated.update(operator.random_traffic())
    mutated.update(operator.random_rsu())
    return mutated
