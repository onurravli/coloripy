# coloripy

A small tool to generate monochromatic color palettes with Python.

## Installation

```bash
git clone https://github.com/onurravli/coloripy.git
cd coloripy
pip install -r requirements.txt
```

## Usage

You can generate a monochromatic color palette by running the following command:

```bash
python main.py -s <start_color> -e <end_color> -q <quantity>
```

### Arguments

- `-s, --start_color`: The starting color of the palette in hexadecimal format.
- `-e --end_color`: The ending color of the palette in hexadecimal format.
- `-q, --quantity`: The number of colors in the palette. (Default: 10)

## Example

To generate a color palette with 10 colors between `#ff0000` and `#00ff00`, run the following command:

```bash
python main.py -s "#ff0000" -e "#00ff00" -q 10
```

This will output an array of colors in hexadecimal format:

```python
['#ff0000', '#e31c00', '#c73800', '#aa5500', '#8e7100', '#718e00', '#55aa00', '#38c700', '#1ce300', '#00ff00']
```

## License

This project is licensed under the MIT License.
