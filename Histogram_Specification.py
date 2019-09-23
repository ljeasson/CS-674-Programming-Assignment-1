from PGM import PGMImage
from Histogram_Equalization import transformer_of

from typing import List


def specify_histogram(img_name, specified_img_name, visualize_results=True):
    p1, p2 = PGMImage(img_name), PGMImage(specified_img_name)

    T_r = transformer_of(p1)

    G_z = transformer_of(p2)

    def inverted_histogram(h: List[int]) -> List[int]:
        G_i = [0] * len(h)
        for h_i in h:
            G_i[h_i] = h_i

        # Populate missing values
        last_nonzero_intensity = 0
        for i in range(len(h)):
            if G_i[i] != 0:
                last_nonzero_intensity = G_i[i]
            else:
                G_i[i] = last_nonzero_intensity

        return G_i

    G_inverse_z = inverted_histogram(G_z)

    p3 = PGMImage(img_name)

    for i in range(len(p3.pixels)):
        p3.pixels[i] = b"".join(bytes([G_inverse_z[T_r[b]]]) for b in p3.pixels[i])

    p3.save(f"specified-to-{p2.name}-{p1.name}")

    if visualize_results:
        p1.show_histogram()
        p2.show_histogram()
        p3.show_histogram(title=f"Histogram of {p1.name}, specified to {p2.name}")


if __name__ == "__main__":
    specify_histogram("images/boat.pgm", "images/sf.pgm")
    specify_histogram("images/f_16.pgm", "images/peppers.pgm")
