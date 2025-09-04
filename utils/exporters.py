"""
exporters.py
Exportfunktionen für Fashion Designs.
"""
import json
import csv
from fashion_generator.models import FashionItem

class Exporter:
    """Exportiert FashionItem in verschiedene Formate."""
    def __init__(self, fmt: str = "json"):
        self.fmt = fmt

    def export(self, item: FashionItem, path: str = None):
        if self.fmt == "json":
            with open(path or "design.json", "w") as f:
                json.dump(item.serialize(), f, indent=2)
        elif self.fmt == "csv":
            with open(path or "design.csv", "w", newline='') as f:
                writer = csv.DictWriter(f, fieldnames=item.serialize().keys())
                writer.writeheader()
                writer.writerow(item.serialize())
        elif self.fmt in ["png", "svg"]:
            # Dummy: Bildexport via Renderer
            from fashion_generator.rendering import Renderer
            renderer = Renderer()
            renderer.export(item, path or f"design.{self.fmt}", fmt=self.fmt)
        else:
            raise ValueError(f"Unbekanntes Exportformat: {self.fmt}")
