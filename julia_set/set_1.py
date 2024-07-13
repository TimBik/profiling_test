"""Julia set generator without optional PIL-based image drawing"""
import time

from time_wrapper import timefn

# площадь исследуемой комплексной плоскости
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193


def calculate_z_serial_purepython(max_iter, zs, cs):
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
    return output


@timefn
def calc_pure_python(desired_width: int, max_iterations: int) -> None:
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
    for y_coord in y:
        for x_coord in x:
            zs.append(complex(x_coord, y_coord))
            cs.append(complex(c_real, c_imag))
    print("Length of x: ", len(x))
    print("Total elements: ", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")
    # Сумма для сетки 1000 на 1000 за 300 итераций
    # проверка, что код работает как ожидалось
    assert sum(output) == 33219980


if __name__ == "__main__":
    # вычисляем множество Жюлиа на чистом Python
    # с разумными для ноутбука параметрами
    calc_pure_python(desired_width=1000, max_iterations=300)
