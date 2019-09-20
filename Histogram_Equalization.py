from PGM import PGMImage

from typing import List

def equalize_histogram(img_name: str, visualize_results: bool):
    p = PGMImage(img_name)

    histogram = p.get_histogram(normed=True)

    L = p.quantization  # Number of distinct grey levels

    # Calculate histogram transformer
    T_r = [0] * L

    for i in range(len(histogram)):
        if i == 0:
            T_r[i] = L * histogram[i]
        else:
            T_r[i] = ((T_r[i - 1] / L) + histogram[i]) * L

    # Discretize T_r by taking the ceil
    T_r = [min(int(t_r + 1), 255) for t_r in T_r]

    # Transform the image according to T_r
    p2 = PGMImage(img_name)

    for i in range(len(p2.pixels)):
        p2.pixels[i] = b"".join(bytes([T_r[b]]) for b in p2.pixels[i])

    p2.save(f"equalized-{p2.name}")

    if visualize_results:
        p.show_histogram(title=f"Histogram of {p.name} before equalization")
        p2.show_histogram(title=f"Histogram of {p2.name} after equalization")


if __name__ == "__main__":
    for img in ("images/boat.pgm", "images/f_16.pgm"):
        equalize_histogram(img, visualize_results=True)
