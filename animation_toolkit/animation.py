from typing import List

from .keyframe import KeyFrame
from .transform import Transform
from .utils import pairwise, dict_filter

class Animation:
    '''takes in a list of keyframes, and generates a list of interpolated keyframe deltas'''
    def __init__(self, keyframes, length):
        self.keyframes = keyframes
        self.length = length
        self.deltas = self._interpolate()

    def print_deltas(self):
        for delta in self.deltas:
            print(delta)

    def __len__(self) -> int:
        return self.length

    def _interpolate(self) -> List[Transform]:
        deltas = []

        # filter keyframes to within the length
        self.keyframes = dict_filter(self.keyframes, lambda k, v: k <= self.length)
        # add initial keyframe if there isnt one
        self.keyframes[1] = self.keyframes.get(0) or KeyFrame()
        # add a final keyframe if there isnt one on the last frame
        last_keyframe_frame_index = sorted(self.keyframes.keys(), reverse=True)[0]
        if last_keyframe_frame_index != self.length - 1:
            self.keyframes[self.length] = self.keyframes[last_keyframe_frame_index]

        for start, end in pairwise(sorted(self.keyframes.keys())):
            keyframe = self.keyframes[start]
            next_keyframe = self.keyframes[end]
            if next_keyframe.ease == KeyFrame.Ease.INSTANT:
                deltas += [keyframe.transform for _ in range(end - start)]
                deltas.append(next_keyframe.transform)
            if next_keyframe.ease == KeyFrame.Ease.LINEAR:
                deltas += keyframe.transform.lerp(next_keyframe.transform, end - start)
            elif next_keyframe.ease == KeyFrame.Ease.EXPONENTIAL:
                deltas += keyframe.transform.experp(next_keyframe.transform, end - start)

        if len(deltas) < self.length: # pad till the end of the animation
            deltas += [Transform() for _ in range(self.length - len(deltas))]
        return deltas