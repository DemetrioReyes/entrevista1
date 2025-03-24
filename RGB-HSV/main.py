import numpy as np

def rgb_to_hsv(rgb):
    rgb = rgb / 255.0
    max_val = np.max(rgb, axis=-1)
    min_val = np.min(rgb, axis=-1)
    delta = max_val - min_val

    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]

    hue = np.zeros_like(max_val)
    hue = np.where(delta != 0, np.select(
        [max_val == r, max_val == g, max_val == b],
        [(g - b) / delta, (b - r) / delta + 2, (r - g) / delta + 4]
    ) * 60, hue)
    hue = np.mod(hue, 360)

    saturation = np.where(max_val != 0, delta / max_val, 0)
    value = max_val

    return np.stack([hue, saturation, value], axis=-1)

def hsv_to_rgb(hsv):
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    
    c = v * s
    x = c * (1 - np.abs(np.mod(h / 60.0, 2) - 1))
    m = v - c

    idx = (h // 60).astype(int)
    rgb_matrix = np.array([
        [c, x, 0], [x, c, 0], [0, c, x],
        [0, x, c], [x, 0, c], [c, 0, x]
    ])
    
    rgb = rgb_matrix[idx] + m[..., np.newaxis]
    return (rgb * 255.0).astype(int)

rgb_input = np.array([180, 53, 89])
hsv = rgb_to_hsv(rgb_input)
rgb_output = hsv_to_rgb(hsv)
print('RGB to HSV:', hsv)
print('HSV to RGB:', rgb_output)