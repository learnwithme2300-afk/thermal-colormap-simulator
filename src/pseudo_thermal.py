import argparse
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Pseudo-thermal colormap simulator")
    parser.add_argument("--image", required=True, help="Input image path")
    parser.add_argument("--out", default="outputs", help="Output folder")
    parser.add_argument("--maps", default="inferno,plasma,magma", help="Comma-separated matplotlib colormaps")
    args = parser.parse_args()

    img_path = Path(args.image)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    bgr = cv2.imread(str(img_path))
    if bgr is None:
        raise ValueError("Failed to read image.")
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

    # Normalize intensity to [0,1]
    norm = cv2.normalize(gray.astype(np.float32), None, 0.0, 1.0, cv2.NORM_MINMAX)

    maps = [m.strip() for m in args.maps.split(",") if m.strip()]
    for cmap_name in maps:
        cmap = plt.get_cmap(cmap_name)
        rgba = cmap(norm)
        rgb = (rgba[:, :, :3] * 255).astype(np.uint8)
        bgr_out = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

        out_path = out_dir / f"pseudo_thermal_{cmap_name}.jpg"
        cv2.imwrite(str(out_path), bgr_out)
        print(f"Saved: {out_path}")

    # Save a sample scale bar
    scale = np.linspace(0, 1, 256).reshape(1, -1)
    fig = plt.figure(figsize=(7, 1.2))
    ax = fig.add_subplot(111)
    ax.imshow(scale, aspect="auto", cmap=plt.get_cmap(maps[0] if maps else "inferno"))
    ax.set_axis_off()
    fig.tight_layout()

    scale_path = out_dir / "scale_bar_example.png"
    fig.savefig(scale_path, dpi=200, bbox_inches="tight", pad_inches=0)
    print(f"Saved: {scale_path}")

if __name__ == "__main__":
    main()
