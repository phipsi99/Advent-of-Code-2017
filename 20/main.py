from pathlib import Path
import re

import numpy as np
from tqdm import tqdm

def do_main(debug_mode=False):
    with open(Path("20/input.txt")) as file:
        lines = [line.rstrip().replace(" ", "") for line in file if line.strip()]

    if debug_mode:
        with open(Path("20/test.txt")) as file:
            lines = [line.rstrip().replace(" ", "") for line in file if line.strip()]

    point_sum = 0
    particles = []

    positions = np.empty((len(lines), 3), dtype=float)
    velocities = np.empty((len(lines), 3), dtype=float)
    accelerations = np.empty((len(lines), 3), dtype=float)
    for line_index, line in enumerate(lines):
        positions[line_index] = re.findall(r"p=<(-?\d+,-?\d+,-?\d+)>", line)[0].split(",")
        velocities[line_index] = re.findall(r"v=<(-?\d+,-?\d+,-?\d+)>", line)[0].split(",")
        accelerations[line_index] = re.findall(r"a=<(-?\d+,-?\d+,-?\d+)>", line)[0].split(",")

    closest_to_0 = None
    old_closest_to_0 = (np.abs(positions).sum(axis=1)).argmin()
    while old_closest_to_0 != closest_to_0:
        old_closest_to_0 = closest_to_0
        for i in range(100):
            velocities += accelerations
            positions += velocities
        closest_to_0 = (np.abs(positions).sum(axis=1)).argmin()
    print(int((np.abs(positions).sum(axis=1)).argmin()))


    positions = np.empty((len(lines), 3), dtype=float)
    velocities = np.empty((len(lines), 3), dtype=float)
    accelerations = np.empty((len(lines), 3), dtype=float)
    for line_index, line in enumerate(lines):
        positions[line_index] = re.findall(r"p=<(-?\d+,-?\d+,-?\d+)>", line)[0].split(",")
        velocities[line_index] = re.findall(r"v=<(-?\d+,-?\d+,-?\d+)>", line)[0].split(",")
        accelerations[line_index] = re.findall(r"a=<(-?\d+,-?\d+,-?\d+)>", line)[0].split(",")

    for i in tqdm(range(10000)):
        velocities += accelerations
        positions += velocities
        unique_rows, inverse_indices, counts = np.unique(positions, axis=0, return_counts=True, return_inverse=True)
        is_unique = counts[inverse_indices] == 1
        positions = positions[is_unique]
        velocities = velocities[is_unique]
        accelerations = accelerations[is_unique]
    print(len(positions))


if __name__ == "__main__":
    do_main(False)
