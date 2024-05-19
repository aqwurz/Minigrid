from __future__ import annotations

import numpy as np

TILE_PIXELS = 32

# Map of color names to RGB values
COLORS = {
    "red": np.array([255, 0, 0]),
    "green": np.array([0, 255, 0]),
    "blue": np.array([0, 0, 255]),
    "purple": np.array([112, 39, 195]),
    "yellow": np.array([255, 255, 0]),
    "grey": np.array([100, 100, 100]),
    "white": np.array([255, 255, 255]),
    "ice": np.array([200, 200, 255]),
    "brown": np.array([100, 100, 0]),
    "lightgrey": np.array([200, 200, 200]),
    "lightgreen": np.array([237, 248, 177]),
    "offwhite": np.array([220, 220, 255]),
    "greyice": np.array([200, 200, 220]),
    "lightbrown": np.array([180, 180, 0]),
    "softgreen": np.array([127, 205, 187]),
    "softblue": np.array([44, 127, 184])
}

COLOR_NAMES = sorted(list(COLORS.keys()))

# Used to map colors to integers
COLOR_TO_IDX = {"red": 0,
                "green": 1,
                "blue": 2,
                "purple": 3,
                "yellow": 4,
                "grey": 5,
                "white": 6,
                "ice": 7,
                "brown": 8,
                "lightgrey": 9,
                "lightgreen": 10,
                "offwhite": 11,
                "greyice": 12,
                "lightbrown": 13,
                "softgreen": 14,
                "softblue": 15,
                }

IDX_TO_COLOR = dict(zip(COLOR_TO_IDX.values(), COLOR_TO_IDX.keys()))

# Map of object type to integers
OBJECT_TO_IDX = {
    "unseen": 0,
    "empty": 1,
    "wall": 2,
    "floor": 3,
    "door": 4,
    "key": 5,
    "ball": 6,
    "box": 7,
    "goal": 8,
    "lava": 9,
    "agent": 10,
    "grass": 11,
    "snow": 12,
    "water": 13,
    "ice": 14,
    "mud": 15,
    "soil": 16,
    "hill": 17,
    "powdersnow": 18,
    "slope": 19,
    "slopedice": 20
}

IDX_TO_OBJECT = dict(zip(OBJECT_TO_IDX.values(), OBJECT_TO_IDX.keys()))

# Map of state names to integers
STATE_TO_IDX = {
    "open": 0,
    "closed": 1,
    "locked": 2,
}

# Map of agent direction indices to vectors
DIR_TO_VEC = [
    # Pointing right (positive X)
    np.array((1, 0)),
    # Down (positive Y)
    np.array((0, 1)),
    # Pointing left (negative X)
    np.array((-1, 0)),
    # Up (negative Y)
    np.array((0, -1)),
]
