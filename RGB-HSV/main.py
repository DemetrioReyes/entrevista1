import numpy as np

def rgb_to_hsv(rgb):
    rgb = rgb / 255.0
    demo_max = np.max(rgb, axis=-1)
    demo_min = np.min(rgb, axis=-1)
    delta = demo_max - demo_min

    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    
    th = np.zeros_like(demo_max)
    th[demo_max == r] = 60 * (g - b)[demo_max == r] / (delta[demo_max == r] + 1e-10)
    th[demo_max == g] = 60 * (b - r)[demo_max == g] / (delta[demo_max == g] + 1e-10) + 120
    th[demo_max == b] = 60 * (r - g)[demo_max == b] / (delta[demo_max == b] + 1e-10) + 240
    th = np.mod(th, 360)

    ts = delta / (demo_max + 1e-10)
    tv = demo_max

    return np.stack([th, ts, tv], axis=-1)

def hsv_to_rgb(hsv):
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    
    c = v * s
    x = c * (1 - np.abs(np.mod(h / 60.0, 2) - 1))
    m = v - c

    q  = np.zeros_like(h)
    rgb = np.stack([
        np.select([h < 60, h < 120, h < 180, h < 240, h < 300, h < 360],
                  [c + m, x + m, m, m, x + m, c + m], default=q),
        np.select([h < 60, h < 120, h < 180, h < 240, h < 300, h < 360],
                  [x + m, c + m, c + m, x + m, m, m], default=q),
        np.select([h < 60, h < 120, h < 180, h < 240, h < 300, h < 360],
                  [m, m, x + m, c + m, c + m, x + m], default=q)
    ], axis=-1)
    
    return (rgb * 255.0).astype(int)


rgb_input = np.array([180, 53, 89])
hsv = rgb_to_hsv(rgb_input)
rgb_output = hsv_to_rgb(hsv)
print('RGB to HSV', hsv)
print('RGB', rgb_output)