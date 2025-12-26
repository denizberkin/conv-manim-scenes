from manim import *


class ConvolutionFormula(Scene):
    def construct(self):
        # Note: double backslashes are required in Python strings for LaTeX commands
        formula = MathTex("(f * g)(t) = \\int_{-\\infty}^{\\infty} f(\\tau)g(t - \\tau) d\\tau")
        formula.scale(1.5)
        self.play(Write(formula), run_time=2)
        self.wait(1)
