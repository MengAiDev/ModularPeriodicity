from manim import *
import numpy as np

class ModularPeriodicity(Scene):
    def construct(self):
        # Scene 1: Introducing Fibonacci sequence
        self.scene1_fibonacci_intro()
        self.clear()
        
        # Scene 2: Introducing modulo operation
        self.scene2_mod_operation()
        self.clear()
        
        # Scene 3: Pisano period concept
        self.scene3_pisano_period()
        self.clear()
        
        # Scene 4: Extending to new sequence
        self.scene4_new_sequence()
        self.clear()
        
        # Scene 5: Calculating modulo 75 period
        self.scene5_mod75_calculation()
        self.clear()
        
        # Scene 6: Verifying period of new sequence modulo 75
        self.scene6_verification()
        self.clear()
        
        # Scene 7: Periodicity visualization
        self.scene7_visualization()
        self.clear()
        
        # Scene 8: Mathematical explanation
        self.scene8_math_explanation()
        self.clear()
        
        # Scene 9: Conclusion and extensions
        self.scene9_conclusion()

    def scene1_fibonacci_intro(self):
        """Scene 1: Introducing Fibonacci sequence"""
        # Title
        title = Text("Exploring Modular Periodicity of Sequences", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Fibonacci sequence
        fib_text = VGroup()
        fib_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        
        for i, val in enumerate(fib_values):
            if i <= 5:
                text = MathTex(f"F_{{{i}}} = {val}")
            else:
                text = MathTex(f"F_{{{i}}} = {val}")
                text.set_opacity(0.7)
            fib_text.add(text)
        
        fib_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        fib_text.next_to(title, DOWN, buff=0.8)
        
        # Display Fibonacci sequence term by term
        for i, item in enumerate(fib_text):
            self.play(Write(item), run_time=0.5)
            if i == 1:
                explanation = Text("Starting from the third term, each term equals the sum of the previous two", 
                                 font_size=24, color=YELLOW)
                explanation.next_to(fib_text, RIGHT, buff=1)
                self.play(Write(explanation))
        
        self.wait(2)
        
        # Show recurrence relation
        recurrence = MathTex("F_n = F_{n-1} + F_{n-2}")
        recurrence.next_to(fib_text, DOWN, buff=0.5)
        self.play(Write(recurrence))
        
        self.wait(3)

    def scene2_mod_operation(self):
        """Scene 2: Introducing modulo operation"""
        title = Text("Periodicity Under Modulo Operation", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Fibonacci sequence
        fib_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        fib_group = VGroup()
        
        for i, num in enumerate(fib_nums):
            text = MathTex(f"{num}")
            fib_group.add(text)
        
        fib_group.arrange(RIGHT, buff=0.3)
        fib_group.shift(UP * 2)
        
        # Mod 2 label
        mod_label = MathTex("\\text{mod } 2", font_size=36)
        mod_label.next_to(fib_group, DOWN, buff=0.3)
        
        # Remainder sequence
        remainders = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        rem_group = VGroup()
        
        for rem in remainders:
            text = MathTex(f"{rem}")
            rem_group.add(text)
        
        rem_group.arrange(RIGHT, buff=0.3)
        rem_group.next_to(mod_label, DOWN, buff=0.5)
        
        # Display original sequence
        self.play(Write(fib_group))
        self.play(Write(mod_label))
        
        # Calculate remainders term by term
        for i, (fib_item, rem_item) in enumerate(zip(fib_group, rem_group)):
            self.play(
                Indicate(fib_item, color=YELLOW),
                run_time=0.5
            )
            self.play(
                TransformFromCopy(fib_item, rem_item),
                run_time=0.5
            )
        
        self.wait(1)
        
        # Highlight periodic pattern
        pattern_box1 = SurroundingRectangle(VGroup(rem_group[0], rem_group[1], rem_group[2]))
        pattern_box2 = SurroundingRectangle(VGroup(rem_group[3], rem_group[4], rem_group[5]))
        pattern_text = Text("Periodic pattern: 0, 1, 1", font_size=24, color=GREEN)
        pattern_text.next_to(rem_group, DOWN, buff=0.8)
        
        self.play(Create(pattern_box1))
        self.play(Write(pattern_text))
        self.play(ReplacementTransform(pattern_box1.copy(), pattern_box2))
        
        self.wait(2)
        
        # Show period length
        period_text = MathTex("\\pi(2) = 3", font_size=36, color=RED)
        period_text.next_to(pattern_text, DOWN, buff=0.5)
        self.play(Write(period_text))
        
        self.wait(3)

    def scene3_pisano_period(self):
        """Scene 3: Pisano period concept"""
        title = Text("Pisano Period", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Pisano period examples
        examples = VGroup(
            MathTex("\\pi(2) = 3"),
            MathTex("\\pi(3) = 8"),
            MathTex("\\pi(4) = 6"),
            MathTex("\\pi(5) = 20"),
            MathTex("\\pi(6) = 24")
        )
        
        examples.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        examples.shift(LEFT * 3)
        
        for example in examples:
            self.play(Write(example), run_time=0.8)
        
        self.wait(2)
        
        # Explanation text
        explanation1 = Text("Period of Fibonacci sequence modulo n", font_size=24)
        explanation1.next_to(examples, RIGHT, buff=1)
        
        explanation2 = Text("Discovered by Italian mathematician Pisano", font_size=20, color=GRAY)
        explanation2.next_to(explanation1, DOWN, buff=0.3)
        
        self.play(Write(explanation1))
        self.play(Write(explanation2))
        
        self.wait(3)

    def scene4_new_sequence(self):
        """Scene 4: Extending to new sequence"""
        title = Text("Extending to New Sequence", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # New sequence definition
        new_seq_text = VGroup()
        new_values = [1, 3, 4, 7, 11, 18, 29, 47, 76]
        
        for i, val in enumerate(new_values):
            if i <= 4:
                text = MathTex(f"a_{{{i}}} = {val}")
            else:
                text = MathTex(f"a_{{{i}}} = {val}")
                text.set_opacity(0.7)
            new_seq_text.add(text)
        
        new_seq_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        new_seq_text.shift(LEFT * 3 + UP * 0.5)
        
        # Display new sequence
        for item in new_seq_text:
            self.play(Write(item), run_time=0.5)
        
        self.wait(1)
        
        # Show recurrence relation
        recurrence = MathTex("a_n = a_{n-1} + a_{n-2}")
        recurrence.next_to(new_seq_text, DOWN, buff=0.5)
        self.play(Write(recurrence))
        
        self.wait(2)
        
        # Compare with Fibonacci sequence
        fib_seq_text = VGroup(
            MathTex("F_0 = 0"),
            MathTex("F_1 = 1"),
            MathTex("F_n = F_{n-1} + F_{n-2}")
        )
        fib_seq_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        fib_seq_text.shift(RIGHT * 3 + UP * 0.5)
        
        comparison_text = Text("Same recurrence relation", font_size=24, color=YELLOW)
        comparison_text.move_to(UP * 2)
        
        self.play(Write(comparison_text))
        for item in fib_seq_text:
            self.play(Write(item), run_time=0.5)
        
        self.wait(2)
        
        # Key conclusion
        conclusion = Text("Sequences with the same recurrence relation have the same period modulo n!", 
                         font_size=28, color=GREEN)
        conclusion.shift(DOWN * 2)
        self.play(Write(conclusion))
        
        self.wait(3)

    def scene5_mod75_calculation(self):
        """Scene 5: Calculating modulo 75 period"""
        title = Text("Calculating Period Modulo 75", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        steps = VGroup(
            MathTex("1.\\ 75 = 3 \\times 5^2"),
            MathTex("2.\\ \\pi(3) = 8"),
            MathTex("3.\\ \\pi(5) = 20"),
            MathTex("4.\\ \\pi(25) = \\pi(5^2) = 20 \\times 5 = 100"),
            MathTex("5.\\ \\pi(75) = \\text{lcm}(\\pi(3), \\pi(25)) = \\text{lcm}(8, 100) = 200")
        )
        
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        steps.shift(UP * 0.5)
        
        # Step-by-step display of calculation process
        for i, step in enumerate(steps):
            self.play(Write(step), run_time=1.5)
            if i < len(steps) - 1:
                self.wait(1)
        
        self.wait(2)
        
        # Emphasize final result
        result_box = SurroundingRectangle(steps[-1], color=YELLOW, buff=0.2)
        result_text = Text("Period length is 200", font_size=32, color=RED)
        result_text.next_to(steps, DOWN, buff=0.8)
        
        self.play(Create(result_box))
        self.play(Write(result_text))
        
        self.wait(3)

    def scene6_verification(self):
        """Scene 6: Verifying period of new sequence modulo 75"""
        title = Text("Verifying Period of New Sequence Modulo 75", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Calculate first few terms modulo 75
        calculations = VGroup(
            MathTex("a_0 = 1 \\equiv 1 \\pmod{75}"),
            MathTex("a_1 = 3 \\equiv 3 \\pmod{75}"),
            MathTex("a_2 = 4 \\equiv 4 \\pmod{75}"),
            MathTex("a_3 = 7 \\equiv 7 \\pmod{75}"),
            MathTex("\\vdots"),
            MathTex("a_8 = 76 \\equiv 1 \\pmod{75}"),
            MathTex("a_9 = 123 \\equiv 48 \\pmod{75}"),
            MathTex("\\vdots")
        )
        
        calculations.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        calculations.scale(0.9)
        calculations.shift(UP * 0.5 + LEFT * 1)
        
        for calc in calculations:
            self.play(Write(calc), run_time=0.8)
        
        self.wait(2)
        
        # Explanation: partial match but not full period
        explanation1 = Text("a₈'s remainder returns to 1, but next term is not 3", 
                           font_size=20, color=YELLOW)
        explanation1.next_to(calculations[5], RIGHT, buff=0.5)
        
        explanation2 = Text("This is not the start of the period", 
                           font_size=20, color=YELLOW)
        explanation2.next_to(calculations[6], RIGHT, buff=0.5)
        
        self.play(Write(explanation1))
        self.play(Write(explanation2))
        
        self.wait(2)
        
        # Show full period
        full_period = VGroup(
            MathTex("a_{200} \\equiv 1 \\pmod{75}"),
            MathTex("a_{201} \\equiv 3 \\pmod{75}")
        )
        full_period.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        full_period.shift(DOWN * 1.5)
        
        period_text = Text("Full period starts repeating after 200 terms", 
                          font_size=24, color=GREEN)
        period_text.next_to(full_period, UP, buff=0.3)
        
        self.play(Write(period_text))
        for item in full_period:
            self.play(Write(item), run_time=1)
        
        self.wait(3)

    def scene7_visualization(self):
        """Scene 7: Periodicity visualization"""
        title = Text("Periodicity Visualization", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create modulo 75 circle
        circle = Circle(radius=2.5, color=WHITE)
        center = circle.get_center()
        
        # Add ticks
        ticks = VGroup()
        numbers = VGroup()
        for i in range(12):  # Only show 12 main ticks
            angle = i * TAU / 12
            start_point = circle.point_at_angle(angle)
            end_point = start_point + (circle.point_at_angle(angle) - center) * 0.1
            tick = Line(start_point, end_point, color=WHITE, stroke_width=2)
            ticks.add(tick)
            
            # Number labels
            number = Integer(i * 6)  # 0, 6, 12, ..., 66
            number.scale(0.5)
            number.move_to(circle.point_at_angle(angle) * 1.15)
            numbers.add(number)
        
        self.play(Create(circle))
        self.play(Create(ticks), Write(numbers))
        
        # Generate new sequence modulo 75 values (simplified version)
        def generate_sequence_mod(n_terms):
            a, b = 1, 3  # Initial values
            sequence = [a % 75, b % 75]
            for _ in range(n_terms - 2):
                a, b = b, (a + b) % 75
                sequence.append(b)
            return sequence
        
        mod_sequence = generate_sequence_mod(50)  # Generate first 50 terms
        
        # Create moving dot
        dot = Dot(color=RED, radius=0.08)
        
        # Trajectory
        trajectory = VGroup()
        
        # Animation: dot moving on circle
        self.play(FadeIn(dot))
        
        for i, mod_val in enumerate(mod_sequence[:25]):  # Only show first 25 steps
            angle = mod_val * TAU / 75
            target_pos = circle.point_at_angle(-angle)  # Negative sign puts 0 at top
            
            # Add trajectory point
            traj_dot = Dot(target_pos, color=YELLOW, radius=0.03, fill_opacity=0.5)
            trajectory.add(traj_dot)
            
            self.play(
                dot.animate.move_to(target_pos),
                FadeIn(traj_dot),
                run_time=0.3
            )
            
            # Display current step and remainder
            if i % 5 == 0:  # Show info every 5 steps
                info_text = Text(f"Step: {i}, Remainder: {mod_val}", font_size=18)
                info_text.to_edge(DOWN)
                self.play(Write(info_text), run_time=0.1)
                self.play(FadeOut(info_text), run_time=0.1)
        
        # Show periodicity explanation
        explanation = Text("Dot moves on modulo 75 circle, eventually forming a cycle", 
                          font_size=24, color=YELLOW)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        
        self.wait(3)

    def scene8_math_explanation(self):
        """Scene 8: Mathematical explanation"""
        title = Text("Mathematical Principle: Why Periodicity?", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # State concept
        state_concept = Text("State = (aₖ, aₖ₊₁)", font_size=36, color=YELLOW)
        state_concept.shift(UP * 2)
        self.play(Write(state_concept))
        
        # State count calculation
        state_calc = VGroup(
            MathTex("\\text{Modulo 75 remainders: } 0, 1, 2, \\dots, 74"),
            MathTex("\\text{Possible remainder pairs: } 75 \\times 75 = 5625"),
            MathTex("\\text{Total states: } 5625")
        )
        
        state_calc.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        state_calc.shift(UP * 0.5)
        
        for item in state_calc:
            self.play(Write(item), run_time=1.2)
        
        self.wait(2)
        
        # Pigeonhole principle
        pigeonhole = VGroup(
            Text("Pigeonhole Principle", font_size=32, color=RED),
            MathTex("\\text{Finite states} \\Rightarrow \\text{Inevitable repetition}"),
            MathTex("\\text{State repetition} \\Rightarrow \\text{Sequence repetition}")
        )
        
        pigeonhole.arrange(DOWN, buff=0.4)
        pigeonhole.shift(DOWN * 1)
        
        self.play(Write(pigeonhole[0]))
        self.wait(1)
        self.play(Write(pigeonhole[1]))
        self.wait(1)
        self.play(Write(pigeonhole[2]))
        
        self.wait(3)

    def scene9_conclusion(self):
        """Scene 9: Conclusion and extensions"""
        title = Text("Conclusion and Extensions", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Key points summary
        key_points = VGroup(
            Text("• Sequences with same recurrence relation have same period modulo n", font_size=24),
            Text("• Period length can be calculated through prime factorization", font_size=24),
            Text("• Periodicity arises from inevitable repetition in finite states", font_size=24),
            Text("• Applies to any linear recurrence sequence", font_size=24)
        )
        
        key_points.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        key_points.shift(UP * 1)
        
        for point in key_points:
            self.play(Write(point), run_time=1)
        
        self.wait(2)
        
        # Beauty of mathematics
        beauty_text = Text("Mathematics is full of such patterns and connections", 
                          font_size=32, color=GREEN)
        beauty_text.shift(DOWN * 0.5)
        
        exploration_text = Text("Waiting for us to discover and explore!", 
                               font_size=28, color=YELLOW)
        exploration_text.shift(DOWN * 1.5)
        
        self.play(Write(beauty_text))
        self.wait(1)
        self.play(Write(exploration_text))
        
        self.wait(4)