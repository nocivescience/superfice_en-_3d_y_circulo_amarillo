from manim import *
class LaplacianScene(ThreeDScene):
    CONFIG={
        'plane_config':{
            'x_range':[-10,10,2],
            'y_range':[-10,10,2],
            'z_range':[-10,10,2]
        }
    }
    def construct(self):
        axes=self.get_axes()
        self.set_camera_orientation(phi=70*DEGREES, theta=130*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.02)
        self.play(Create(axes))
        self.wait()
    def get_axes(self):
        return ThreeDAxes(**self.CONFIG['plane_config'])