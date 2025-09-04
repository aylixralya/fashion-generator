"""
validators.py
Validierung für Eingabeparameter und Design Constraints.
"""
def validate_parameter_range(param: str, value, valid_range):
    if value not in valid_range:
        raise ValueError(f"Ungültiger Wert für {param}: {value}")

def check_design_constraints(item):
    # Dummy-Constraint: Größe muss M oder L sein
    if item.size not in ['M', 'L']:
        raise ValueError("Design Constraint verletzt: Größe muss M oder L sein.")
