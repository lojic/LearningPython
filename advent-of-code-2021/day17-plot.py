# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day17/day17-plot.rkt
from advent import *

x_min, x_max, y_min, y_max = 206, 250, -105, -57

def plot_trajectory(dx, dy):
    points = shoot(dx, dy)
    print(points)
    plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], 'k-', linewidth=4)
    plt.plot([ x for (x,y) in points ], [ y for (x,y) in points ], '.:', label=f'({dx}, {dy})')
    plt.legend()
    plt.show()

def shoot(dx, dy):
    x, y, results = 0, 0, []
    while x <= x_max and y >= y_min:
        results.append((x, y))
        if dx > 0:   dx -= 1
        dy -= 1
        x  += dx
        y  += dy
    return results

if __name__ == '__main__':
    plot_trajectory(22,12)
