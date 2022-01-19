from typing import List

import numpy as np

from .vec2 import Vec2
from .utils import sigspace

class Transform:
    def __init__(self, pos=Vec2(0, 0), rot=Vec2(0, 0), scale=Vec2(1, 1)):
        self.pos, self.rot, self.scale = pos, rot, scale
    def __repr__(self) -> str:
        return f"Transform({self.pos}, {self.rot}, {self.scale})"

    @classmethod
    def _vec_lin_space(self, start: Vec2, end: Vec2, n: int) -> List[Vec2]:
        return [Vec2(x, y) for x, y in zip(
            np.diff(np.linspace(start.x, end.x, n+1), 1).tolist(), 
            np.diff(np.linspace(start.y, end.y, n+1), 1).tolist())]
    @classmethod
    def _vec_sig_space(self, start: Vec2, end: Vec2, n: int) -> List[Vec2]:
        return [Vec2(x, y) for x, y in zip(
            np.diff(sigspace(start.x, end.x, n+1), 1).tolist(),
            np.diff(sigspace(start.y, end.y, n+1), 1).tolist())]
        

    def lerp(self, target, n) -> List['Transform']:
        positions = Transform._vec_lin_space(self.pos, target.pos, n)
        rotations = Transform._vec_lin_space(self.rot, target.rot, n)
        scales = Transform._vec_lin_space(self.scale, target.scale, n)
        return [Transform(pos, rot, scale) for pos, rot, scale in zip(positions, rotations, scales)]

    def experp(self, target, n) -> List['Transform']:
        positions = Transform._vec_sig_space(self.pos, target.pos, n)
        rotations = Transform._vec_sig_space(self.rot, target.rot, n)
        scales = Transform._vec_sig_space(self.scale, target.scale, n)
        return [Transform(pos, rot, scale) for pos, rot, scale in zip(positions, rotations, scales)]