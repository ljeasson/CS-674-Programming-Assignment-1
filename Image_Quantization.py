from PGM import PGMImage


def adjust_quantization_and_save(img_name: str, quantization: int):
    p = PGMImage(img_name)
    print(f"Adjusting quantization of {img_name} to {quantization}")
    p.quantization = quantization

    for i in range(p.rows):
        # Normalize, quantize, and cast to byte string
        p.pixels[i] = b"".join(
            [bytes([int((int(px) / 256) * quantization)]) for px in p.pixels[i]]
        )

    p.save(f"images/quantized-{quantization}-{p.name}")


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/peppers.pgm"):
        for q in (128, 32, 8, 2):
            adjust_quantization_and_save(img, q)
