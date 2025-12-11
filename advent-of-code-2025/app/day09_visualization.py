from advent import parse, ints, plt
from matplotlib.patches import Polygon

vertices = parse(9, ints)
fig, ax = plt.subplots(figsize=(8, 6))

polygon = Polygon(
    vertices, fill=True, facecolor='lightblue', edgecolor='darkblue', linewidth=1, alpha=0.7
)

ax.add_patch(polygon)

x_coords, y_coords = zip(*vertices)
ax.plot(
    x_coords + (x_coords[0],),
    y_coords + (y_coords[0],),
    'ro-',
    markersize=1,
    linewidth=1,
    label='Vertices',
)

ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_xlabel('X coordinate', fontsize=12)
ax.set_ylabel('Y coordinate', fontsize=12)
ax.set_title('Rectilinear Polygon Visualization', fontsize=14, fontweight='bold')
ax.legend()

margin = 0.5
all_x = [v[0] for v in vertices]
all_y = [v[1] for v in vertices]
ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
ax.set_ylim(min(all_y) - margin, max(all_y) + margin)

plt.tight_layout()
plt.show()
