from manim import *
import numpy as np

class Vectors3D(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            z_range=[-10, 10, 1],
            tips=False,
            axis_config={"include_ticks": False},
        )

        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)

        # Coordinates -> scene points (requires ThreeDAxes)
        origin = ax.coords_to_point(0, 0, 0)
        p1 = ax.coords_to_point(-8, 1, 4)
        p2 = ax.coords_to_point(3, -2, 4)

        dot1 = Dot3D(p1)
        dot2 = Dot3D(p2)

        # Start with lines
        # l1 = Line3D(origin, p1)
        # l2 = Line3D(origin, p2)
        # l3 = Line3D(p1, p2)

        # Target arrows
        v1 = Arrow3D(origin, p1).set_color(GREEN)
        v2 = Arrow3D(origin, p2).set_color(GREEN)
        v3 = Arrow3D(p1, p2).set_color(RED)

        self.add(ax)
        self.begin_ambient_camera_rotation(rate=0.15, about="theta")

        self.play(FadeIn(dot1), FadeIn(dot2), run_time=1.5)
        self.play(GrowFromPoint(v1,origin), GrowFromPoint(v2,origin), run_time=3)

        # Replace line with arrow cleanly
        # self.play(ReplacementTransform(l1, v1), run_time=0.8)
        # self.play(ReplacementTransform(l2, v2), run_time=0.8)
        self.wait(.7)
        self.stop_ambient_camera_rotation()
        self.play(GrowFromPoint(v3,p2), run_time=2)


        self.wait(3)
