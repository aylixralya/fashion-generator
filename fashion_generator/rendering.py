"""
rendering.py
3D Visualisierung für Fashion Designs.
"""
import matplotlib.pyplot as plt
import numpy as np
from fashion_generator.models import FashionItem

class Renderer:
    """3D Wireframe und Surface Renderer für FashionItem."""
    def __init__(self):
        pass

    def render(self, item: FashionItem, mode: str = "wireframe"):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Dummy 3D shape
        X, Y = np.meshgrid(np.linspace(-1, 1, 30), np.linspace(-1, 1, 30))
        Z = np.sin(X ** 2 + Y ** 2)
        if mode == "wireframe":
            ax.plot_wireframe(X, Y, Z, color='blue')
        else:
            ax.plot_surface(X, Y, Z, cmap='viridis')
        plt.title(f"{item.style} {item.category} ({item.size})")
        plt.show()

    def export(self, item: FashionItem, path: str, fmt: str = "png"):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(np.linspace(-1, 1, 30), np.linspace(-1, 1, 30))
        Z = np.sin(X ** 2 + Y ** 2)
        ax.plot_wireframe(X, Y, Z, color='blue')
        plt.title(f"{item.style} {item.category} ({item.size})")
        fig.savefig(path, format=fmt)
