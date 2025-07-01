import random

def run_simulation(params):
    collision_prob = 0.1 + 0.01 * params.get('vehicle_num', 1)
    result = {
        'arrived': random.random() > 0.2,
        'collision': random.random() < collision_prob,
        'emergency_brake': random.choice([True, False]),
        'score': random.uniform(0, 1) - (0.5 if random.random() < collision_prob else 0),
    }
    return result
