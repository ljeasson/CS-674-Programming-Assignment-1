from PGM import PGMImage

from typing import List


def transformer_of(p: PGMImage) -> List[int]:
    """ Calculate a transformer for histogram equalization.
    
    The transformer is a list, indexed by intensity values, whose
    values represent the output intensity required for an equalized
    histogram, given an input histogram.

    :param p image to equalize the histogram of
    """

    histogram = p.get_histogram(normed=True)
    L = p.quantization  # Number of distinct grey levels

    # Calculate histogram transformer
    T_r = [0] * (L + 1)  # len([0, L]) = L + 1

    for i in range(len(histogram)):
        if i == 0:
            T_r[i] = L * histogram[i]
        else:
            T_r[i] = ((T_r[i - 1] / L) + histogram[i]) * L

    # Discretize T_r by taking the ceil
    return [min(int(t_r + 1), 255) for t_r in T_r]


def equalize_histogram(img_name: str, visualize_results: bool):
    p = PGMImage(img_name)

    T_r = transformer_of(p)

    p2 = PGMImage(img_name)

    # Transform the image according to T_r
    for i in range(len(p2.pixels)):
        p2.pixels[i] = b"".join(bytes([T_r[b]]) for b in p2.pixels[i])

    p2.save(f"equalized-{p2.name}")

    if visualize_results:
        p.show_histogram(title=f"Histogram of {p.name} before equalization")
        p2.show_histogram(title=f"Histogram of {p2.name} after equalization")


if __name__ == "__main__":
    for img in ("images/boat.pgm", "images/f_16.pgm"):
        equalize_histogram(img, visualize_results=True)
