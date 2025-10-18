from manim import *
import numpy as np

class ModularPeriodicity(Scene):
    def construct(self):
        # 场景1：引入斐波那契数列
        self.scene1_fibonacci_intro()
        self.clear()
        
        # 场景2：模运算引入
        self.scene2_mod_operation()
        self.clear()
        
        # 场景3：Pisano周期概念
        self.scene3_pisano_period()
        self.clear()
        
        # 场景4：推广到新数列
        self.scene4_new_sequence()
        self.clear()
        
        # 场景5：计算模75的周期
        self.scene5_mod75_calculation()
        self.clear()
        
        # 场景6：验证新数列模75的周期
        self.scene6_verification()
        self.clear()
        
        # 场景7：周期性可视化
        self.scene7_visualization()
        self.clear()
        
        # 场景8：数学原理解释
        self.scene8_math_explanation()
        self.clear()
        
        # 场景9：总结与拓展
        self.scene9_conclusion()

    def scene1_fibonacci_intro(self):
        """场景1：引入斐波那契数列"""
        # 标题
        title = Text("探索数列的模周期", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 斐波那契数列
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
        
        # 逐项显示斐波那契数列
        for i, item in enumerate(fib_text):
            self.play(Write(item), run_time=0.5)
            if i == 1:
                explanation = Text("从第三项开始，每一项等于前两项之和", 
                                 font_size=24, color=YELLOW)
                explanation.next_to(fib_text, RIGHT, buff=1)
                self.play(Write(explanation))
        
        self.wait(2)
        
        # 显示递推关系
        recurrence = MathTex("F_n = F_{n-1} + F_{n-2}")
        recurrence.next_to(fib_text, DOWN, buff=0.5)
        self.play(Write(recurrence))
        
        self.wait(3)

    def scene2_mod_operation(self):
        """场景2：模运算的引入"""
        title = Text("模运算下的周期性", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 斐波那契数列
        fib_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        fib_group = VGroup()
        
        for i, num in enumerate(fib_nums):
            text = MathTex(f"{num}")
            fib_group.add(text)
        
        fib_group.arrange(RIGHT, buff=0.3)
        fib_group.shift(UP * 2)
        
        # 模2标记
        mod_label = MathTex("\\text{mod } 2", font_size=36)
        mod_label.next_to(fib_group, DOWN, buff=0.3)
        
        # 余数序列
        remainders = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        rem_group = VGroup()
        
        for rem in remainders:
            text = MathTex(f"{rem}")
            rem_group.add(text)
        
        rem_group.arrange(RIGHT, buff=0.3)
        rem_group.next_to(mod_label, DOWN, buff=0.5)
        
        # 显示原始数列
        self.play(Write(fib_group))
        self.play(Write(mod_label))
        
        # 逐项计算余数
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
        
        # 高亮周期模式
        pattern_box1 = SurroundingRectangle(VGroup(rem_group[0], rem_group[1], rem_group[2]))
        pattern_box2 = SurroundingRectangle(VGroup(rem_group[3], rem_group[4], rem_group[5]))
        pattern_text = Text("周期模式: 0, 1, 1", font_size=24, color=GREEN)
        pattern_text.next_to(rem_group, DOWN, buff=0.8)
        
        self.play(Create(pattern_box1))
        self.play(Write(pattern_text))
        self.play(ReplacementTransform(pattern_box1.copy(), pattern_box2))
        
        self.wait(2)
        
        # 显示周期长度
        period_text = MathTex("\\pi(2) = 3", font_size=36, color=RED)
        period_text.next_to(pattern_text, DOWN, buff=0.5)
        self.play(Write(period_text))
        
        self.wait(3)

    def scene3_pisano_period(self):
        """场景3：Pisano周期概念"""
        title = Text("Pisano周期", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Pisano周期示例
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
        
        # 解释文本
        explanation1 = Text("斐波那契数列模n的周期", font_size=24)
        explanation1.next_to(examples, RIGHT, buff=1)
        
        explanation2 = Text("由意大利数学家Pisano发现", font_size=20, color=GRAY)
        explanation2.next_to(explanation1, DOWN, buff=0.3)
        
        self.play(Write(explanation1))
        self.play(Write(explanation2))
        
        self.wait(3)

    def scene4_new_sequence(self):
        """场景4：推广到新数列"""
        title = Text("推广到新数列", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 新数列定义
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
        
        # 显示新数列
        for item in new_seq_text:
            self.play(Write(item), run_time=0.5)
        
        self.wait(1)
        
        # 显示递推关系
        recurrence = MathTex("a_n = a_{n-1} + a_{n-2}")
        recurrence.next_to(new_seq_text, DOWN, buff=0.5)
        self.play(Write(recurrence))
        
        self.wait(2)
        
        # 对比斐波那契数列
        fib_seq_text = VGroup(
            MathTex("F_0 = 0"),
            MathTex("F_1 = 1"),
            MathTex("F_n = F_{n-1} + F_{n-2}")
        )
        fib_seq_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        fib_seq_text.shift(RIGHT * 3 + UP * 0.5)
        
        comparison_text = Text("相同递推关系", font_size=24, color=YELLOW)
        comparison_text.move_to(UP * 2)
        
        self.play(Write(comparison_text))
        for item in fib_seq_text:
            self.play(Write(item), run_time=0.5)
        
        self.wait(2)
        
        # 关键结论
        conclusion = Text("相同递推关系的数列，模n的周期相同！", 
                         font_size=28, color=GREEN)
        conclusion.shift(DOWN * 2)
        self.play(Write(conclusion))
        
        self.wait(3)

    def scene5_mod75_calculation(self):
        """场景5：计算模75的周期"""
        title = Text("计算模75的周期", font_size=48, color=BLUE)
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
        
        # 逐步显示计算过程
        for i, step in enumerate(steps):
            self.play(Write(step), run_time=1.5)
            if i < len(steps) - 1:
                self.wait(1)
        
        self.wait(2)
        
        # 最终结果强调
        result_box = SurroundingRectangle(steps[-1], color=YELLOW, buff=0.2)
        result_text = Text("周期长度为200", font_size=32, color=RED)
        result_text.next_to(steps, DOWN, buff=0.8)
        
        self.play(Create(result_box))
        self.play(Write(result_text))
        
        self.wait(3)

    def scene6_verification(self):
        """场景6：验证新数列模75的周期"""
        title = Text("验证新数列模75的周期", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 计算前几项模75
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
        
        # 解释部分匹配但不是完整周期
        explanation1 = Text("a₈的余数回到了1，但下一项不是3", 
                           font_size=20, color=YELLOW)
        explanation1.next_to(calculations[5], RIGHT, buff=0.5)
        
        explanation2 = Text("这不是周期的开始", 
                           font_size=20, color=YELLOW)
        explanation2.next_to(calculations[6], RIGHT, buff=0.5)
        
        self.play(Write(explanation1))
        self.play(Write(explanation2))
        
        self.wait(2)
        
        # 显示完整周期
        full_period = VGroup(
            MathTex("a_{200} \\equiv 1 \\pmod{75}"),
            MathTex("a_{201} \\equiv 3 \\pmod{75}")
        )
        full_period.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        full_period.shift(DOWN * 1.5)
        
        period_text = Text("完整周期在200项后开始重复", 
                          font_size=24, color=GREEN)
        period_text.next_to(full_period, UP, buff=0.3)
        
        self.play(Write(period_text))
        for item in full_period:
            self.play(Write(item), run_time=1)
        
        self.wait(3)

    def scene7_visualization(self):
        """场景7：周期性可视化"""
        title = Text("周期性可视化", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建模75的圆
        circle = Circle(radius=2.5, color=WHITE)
        center = circle.get_center()
        
        # 添加刻度
        ticks = VGroup()
        numbers = VGroup()
        for i in range(12):  # 只显示12个主要刻度
            angle = i * TAU / 12
            start_point = circle.point_at_angle(angle)
            end_point = start_point + (circle.point_at_angle(angle) - center) * 0.1
            tick = Line(start_point, end_point, color=WHITE, stroke_width=2)
            ticks.add(tick)
            
            # 数字标签
            number = Integer(i * 6)  # 0, 6, 12, ..., 66
            number.scale(0.5)
            number.move_to(circle.point_at_angle(angle) * 1.15)
            numbers.add(number)
        
        self.play(Create(circle))
        self.play(Create(ticks), Write(numbers))
        
        # 生成新数列模75的值（简化版本）
        def generate_sequence_mod(n_terms):
            a, b = 1, 3  # 初始值
            sequence = [a % 75, b % 75]
            for _ in range(n_terms - 2):
                a, b = b, (a + b) % 75
                sequence.append(b)
            return sequence
        
        mod_sequence = generate_sequence_mod(50)  # 生成前50项
        
        # 创建移动的点
        dot = Dot(color=RED, radius=0.08)
        
        # 轨迹
        trajectory = VGroup()
        
        # 动画：点在圆上移动
        self.play(FadeIn(dot))
        
        for i, mod_val in enumerate(mod_sequence[:25]):  # 只显示前25步
            angle = mod_val * TAU / 75
            target_pos = circle.point_at_angle(-angle)  # 负号使0在顶部
            
            # 添加轨迹点
            traj_dot = Dot(target_pos, color=YELLOW, radius=0.03, fill_opacity=0.5)
            trajectory.add(traj_dot)
            
            self.play(
                dot.animate.move_to(target_pos),
                FadeIn(traj_dot),
                run_time=0.3
            )
            
            # 显示当前步数和余数
            if i % 5 == 0:  # 每5步显示一次信息
                info_text = Text(f"步数: {i}, 余数: {mod_val}", font_size=18)
                info_text.to_edge(DOWN)
                self.play(Write(info_text), run_time=0.1)
                self.play(FadeOut(info_text), run_time=0.1)
        
        # 显示周期性解释
        explanation = Text("点在模75的圆上移动，最终会形成循环", 
                          font_size=24, color=YELLOW)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        
        self.wait(3)

    def scene8_math_explanation(self):
        """场景8：数学原理解释"""
        title = Text("数学原理：为什么会有周期性？", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 状态概念
        state_concept = Text("状态 = (aₖ, aₖ₊₁)", font_size=36, color=YELLOW)
        state_concept.shift(UP * 2)
        self.play(Write(state_concept))
        
        # 状态数量计算
        state_calc = VGroup(
            MathTex("\\text{模75的余数: } 0, 1, 2, \\dots, 74"),
            MathTex("\\text{可能的余数对: } 75 \\times 75 = 5625"),
            MathTex("\\text{状态总数: } 5625")
        )
        
        state_calc.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        state_calc.shift(UP * 0.5)
        
        for item in state_calc:
            self.play(Write(item), run_time=1.2)
        
        self.wait(2)
        
        # 鸽巢原理
        pigeonhole = VGroup(
            Text("鸽巢原理", font_size=32, color=RED),
            MathTex("\\text{有限状态} \\Rightarrow \\text{必然重复}"),
            MathTex("\\text{状态重复} \\Rightarrow \\text{序列重复}")
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
        """场景9：总结与拓展"""
        title = Text("总结与拓展", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 关键点总结
        key_points = VGroup(
            Text("• 相同递推关系的数列，模n的周期相同", font_size=24),
            Text("• 周期长度可以通过质因数分解计算", font_size=24),
            Text("• 周期性源于有限状态必然重复", font_size=24),
            Text("• 适用于任何线性递推数列", font_size=24)
        )
        
        key_points.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        key_points.shift(UP * 1)
        
        for point in key_points:
            self.play(Write(point), run_time=1)
        
        self.wait(2)
        
        # 数学之美
        beauty_text = Text("数学中充满了这样的规律和联系", 
                          font_size=32, color=GREEN)
        beauty_text.shift(DOWN * 0.5)
        
        exploration_text = Text("等待着我们去发现和探索！", 
                               font_size=28, color=YELLOW)
        exploration_text.shift(DOWN * 1.5)
        
        self.play(Write(beauty_text))
        self.wait(1)
        self.play(Write(exploration_text))
        
        self.wait(4)
