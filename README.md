# Thermal Colormap Simulator

This project simulates a thermal-like image by converting grayscale intensity values into color maps.

## What it does
- reads an input image
- converts it to grayscale
- normalizes intensity
- applies pseudo-thermal colormaps such as inferno, plasma, and magma
- saves the outputs

## Important note
This is a visualization simulation only.
It is **not** a real thermal camera measurement system.

## Technologies
- Python
- OpenCV
- NumPy
- Matplotlib

## Run
```bash
python src/pseudo_thermal.py --image data/sample.jpg --out outputs
