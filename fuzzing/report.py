import yaml
import os

class FuzzReport:
    def __init__(self):
        self.records = []
    def add(self, params, result):
        self.records.append({'params': params, 'result': result})
    def summary(self):
        total = len(self.records)
        collision = sum(1 for r in self.records if r['result'].get('collision'))
        arrived = sum(1 for r in self.records if r['result'].get('arrived'))
        avg_score = sum(r['result'].get('score', 0) for r in self.records) / total if total else 0
        return {'total': total, 'collision': collision, 'arrived': arrived, 'avg_score': avg_score}
    def save(self, path):
        with open(path, 'w') as f:
            yaml.safe_dump({'summary': self.summary(), 'records': self.records}, f)
