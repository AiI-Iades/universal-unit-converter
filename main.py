import argparse
from fractions import Fraction

def convert_unit(value, from_unit, to_unit):
    # Conversion factors (example: length, mass, etc.)
    conversion = {
        'm': {'m': 1, 'km': 1e-3, 'cm': 1e2, 'mm': 1e3},
        'kg': {'kg': 1, 'g': 1e3, 't': 1e-3},
        's': {'s': 1, 'ms': 1e3, 'ns': 1e6},
        # Add more units here
    }
    
    if from_unit not in conversion or to_unit not in conversion[from_unit]:
        raise ValueError(f'Unsupported unit: {from_unit} or {to_unit}')
    
    factor = conversion[from_unit][to_unit]
    return value * factor

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Universal Unit Converter')
    parser.add_argument('value', type=float, help='Value to convert')
    parser.add_argument('--from-unit', required=True, help='Source unit')
    parser.add_argument('--to-unit', required=True, help='Target unit')
    args = parser.parse_args()

    try:
        result = convert_unit(args.value, args.from_unit, args.to_unit)
        print(f'{args.value} {args.from_unit} = {result:.6f} {args.to_unit}')
    except ValueError as e:
        print(f'Error: {e}')