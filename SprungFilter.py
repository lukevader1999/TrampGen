from Sprung import Sprung
from typing import List as ls
import json

class SprungFilter:
    def __init__(self, 
                max_rotationen=None,
                max_schrauben=None,
                start=None, 
                ende=None, 
                position=None, 
                exclude_starts=None, 
                exclude_endes=None,
                exclude_codes=None,
                filter_json_path="filter.json",
                costum_functions: list[callable[[Sprung], bool]] = None):

        self.max_rotationen = max_rotationen
        self.max_schrauben = max_schrauben
        self.start = start if start is None or isinstance(start, list) else [start]
        self.ende = ende if ende is None or isinstance(ende, list) else [ende]
        self.position = position if position is None or isinstance(position, list) else [position]
        self.exclude_starts = exclude_starts or []
        self.exclude_endes = exclude_endes or []
        self.exclude_codes = set(exclude_codes) if exclude_codes else set()
        self.costum_functions = costum_functions

        # Filter-JSON laden und Codes ergänzen
        if filter_json_path:
            try:
                with open(filter_json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    self.exclude_codes.update(data.keys())
                elif isinstance(data, list):
                    self.exclude_codes.update(data)
            except Exception:
                pass

    def match(self, sprung):
        if self.max_rotationen is not None and sprung.rotationen > self.max_rotationen:
            return False
        if self.max_schrauben is not None and sprung.schrauben > self.max_schrauben:
            return False
        if self.start is not None and sprung.start not in self.start:
            return False
        if self.ende is not None and sprung.ende not in self.ende:
            return False
        if self.position is not None and sprung.position not in self.position:
            return False
        if sprung.start in self.exclude_starts:
            return False
        if sprung.ende in self.exclude_endes:
            return False
        if hasattr(sprung, 'code') and sprung.code in self.exclude_codes:
            return False
        if self.costum_functions:
            if any(func(sprung) is False for func in self.costum_functions):
                return False
        return True

    def filter(self, sprung_liste: ls[Sprung]) -> ls[Sprung]:
        return [sprung for sprung in sprung_liste if self.match(sprung)]
