from PIL import ImageDraw, Image
from time_wrapper import timefn

# площадь исследуемой комплексной плоскости
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193
desired_width = 5000
img = Image.new('RGB', (desired_width, desired_width))


def calculate_z_serial_purepython(max_iter, zs, cs, pil_coord):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < max_iter:
            z = z * z + c
            n += 1
        output[i] = n
        img.putpixel(xy=pil_coord[i], value=(min(n, 256), min(n, 256), min(n, 256)))
    return output


@timefn
def draw_pure_python(desired_width: int, max_iterations: int):
    """Create a list of complex coordinates (zs) and
    complex parameters (cs), build Julia set"""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    y_coord = y2
    while y_coord > y1:
        y.append(y_coord)
        y_coord += y_step
    x_coord = x1
    while x_coord < x2:
        x.append(x_coord)
        x_coord += x_step
    # формируем список координат и начальные условия для
    # каждой клетки.
    # обратите внимание, что начальное условие - это
    # константа, которую легко убрать, мы используем ее для
    # моделирования реального сценария
    zs = []
    cs = []
    pil_coord = []
    for i, y_coord in enumerate(y):
        for j, x_coord in enumerate(x):
            zs.append(complex(x_coord, y_coord))
            cs.append(complex(c_real, c_imag))
            pil_coord.append((i, j))
    output = calculate_z_serial_purepython(max_iterations, zs, cs, pil_coord)


if __name__ == "__main__":
    # рисуем множество Жюлиа на чистом Python
    # с разумными для ноутбука параметрами
    draw_pure_python(desired_width=desired_width, max_iterations=300)
    name = f"sets/julia_set_{desired_width}.png"
    img.save(name)
