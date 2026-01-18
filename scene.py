from manim import *
import numpy as np

class SineWave(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 2*np.pi, np.pi/2], y_range=[-1.5, 1.5, 1])
        curve = ax.plot(lambda x: np.sin(x))
        self.play(Create(ax), Create(curve))
        self.wait()
