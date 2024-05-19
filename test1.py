import numpy as np
from ipycanvas import Canvas, hold_canvas

canvas = Canvas(width=400, height=300)
n_rects = 300
x = np.random.randint(0, canvas.width, size=(n_rects))
y = np.random.randint(0, canvas.width, size=(n_rects))
width = np.random.randint(10, 40, size=(n_rects))
height = np.random.randint(10, 40, size=(n_rects))
colors_fill = np.random.randint(0, 255, size=(n_rects, 3))
colors_outline = np.random.randint(0, 255, size=(n_rects, 3))
alphas = np.random.random(n_rects)
with hold_canvas():
    canvas.fill_styled_rects(x, y, width, height, color=colors_fill, alpha=alphas)
    canvas.line_width = 2
    canvas.stroke_styled_rects(x, y, width, height, color=colors_outline, alpha=alphas)
canvas