"""
main.py
Entry Point für das Digital Fashion Generator CLI.
"""
import argparse
import logging.config
import sys
from config import Config
from fashion_generator.core import FashionDesignEngine
from utils.exporters import Exporter
from colorama import Fore, Style

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Digital Fashion Generator - CLI")
    parser.add_argument('--style', type=str, help='Designstil')
    parser.add_argument('--category', type=str, help='Kategorie (z.B. dress, shirt)')
    parser.add_argument('--size', type=str, help='Größe')
    parser.add_argument('--color', type=str, help='Farbe')
    parser.add_argument('--export', type=str, choices=['json', 'csv', 'png', 'svg'], help='Exportformat')
    parser.add_argument('--batch', action='store_true', help='Batch-Verarbeitung aktivieren')
    parser.add_argument('--config', type=str, help='Pfad zur Konfigurationsdatei')
    parser.add_argument('--output', type=str, help='Exportverzeichnis')
    args = parser.parse_args()

    try:
        config = Config(args.config) if args.config else Config()
        engine = FashionDesignEngine(config)
        if args.batch:
            logger.info("Starte Batch-Verarbeitung...")
            # Batch-Logik hier
        else:
            logger.info("Starte Einzelverarbeitung...")
            design = engine.generate(
                style=args.style or config.get('fashion_defaults')['style'],
                category=args.category or config.get('fashion_defaults')['category'],
                size=args.size or config.get('fashion_defaults')['size'],
                color=args.color or config.get('fashion_defaults')['color']
            )
            exporter = Exporter(args.export or config.get('fashion_defaults')['export_format'])
            exporter.export(design, args.output)
            print(Fore.GREEN + "Design erfolgreich generiert und exportiert!" + Style.RESET_ALL)
    except Exception as e:
        logger.error(f"Fehler: {e}")
        print(Fore.RED + f"Fehler: {e}" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    main()
