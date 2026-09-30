import numpy as np
import matplotlib.pyplot as plt

# Grid
volume_range = np.linspace(df['Volume'].min(), df['Volume'].max(), 10)
weight_range = np.linspace(df['Weight'].min(), df['Weight'].max(), 10)

volume_grid, weight_grid = np.meshgrid(volume_range, weight_range)

co2_pred = (
    model.intercept_
    + model.coef_[0] * volume_grid
    + model.coef_[1] * weight_grid
)

# 3D graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    df['Volume'],
    df['Weight'],
    df['CO2']
)

ax.plot_surface(
    volume_grid,
    weight_grid,
    co2_pred,
    alpha=0.5
)

# Labels
ax.set_xlabel('Volume - Xondamir')
ax.set_ylabel('Weight')
ax.set_zlabel('CO2')

plt.show()
