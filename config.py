"""
config.py
Zentrale Konfigurationsverwaltung für das Digital Fashion Generator Projekt.
"""
from typing import Any, Dict
import json
import os

class Config:
    """Lädt und verwaltet Konfigurationen für verschiedene Umgebungen."""
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self.load()

    def load(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                self.config = json.load(f)
        else:
            self.config = self.default_config()

    def default_config(self) -> Dict[str, Any]:
        return {
            "fashion_defaults": {
                "style": "avant-garde",
                "category": "dress",
                "size": "M",
                "color": "iridescent",
                "export_format": "png"
            },
            "ml_model": {
                "pattern_recognition": True,
                "trend_analysis": True
            }
        }

    def get(self, key: str, default=None):
        return self.config.get(key, default)
