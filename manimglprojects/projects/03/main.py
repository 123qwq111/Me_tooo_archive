from manimlib import*
class Notice(VGroup):
    def __init__(self, m_text1, m_text2, **kwargs):

        super().__init__(**kwargs)
        self.line1 = Text(m_text1, font = 'simsun')
        self.line2 = Text(m_text2, font = 'simsun')
        if self.line1.get_height() < 0.5:
            self.line1.scale(1.25)
        if self.line2.get_height() < 0.5:
            self.line2.scale(1.25)
        self.line2.next_to(self.line1, DOWN)
        self.add(self.line1, self.line2)
        self.scale(0.5)
        self.shift(np.array([5.8,2.9,0]))#copy from yuezhengchuixing(github)
class Caption(VGroup):
    def __init__(self, m_text1, **kwargs):

        super().__init__(**kwargs)
        self.cn = Text(m_text1,font ="KaiTi",font_size=36)
        self.add(self.cn)
        self.move_to(BOTTOM+UP*0.5)
class chapter(VGroup):
    def __init__(self, m_text1, **kwargs):

        super().__init__(**kwargs)
        self.cn = Text(m_text1,font ="simsun",font_size=36,color=YELLOW_A)
        self.add(self.cn)
        self.move_to(TOP+LEFT*4.5+DOWN*0.5)
class vedio(Scene):
    def construct(self):
        # make objects
        notice0=Notice("沃茨基·硕德", "请勿模仿")
        quote=Text("优雅的结论往往伴随着巧妙的方法。",font ="simsun",t2c={"优雅":BLUE,"巧妙":GREEN})

        notice1=Notice("视频前言","请听介绍")
        equality_pic_1=SVGMobject("ell.svg")
        equality_pic_2=SVGMobject("sin.svg")
        equality=Tex("=",color = YELLOW,size=1.5)
        equality_l=Tex(r"\frac{x^2}2+\frac{y^2}1=1",color = BLUE)
        equality_r=Tex(r"y=\sin x,x\in[0.2\pi]",color = GREEN)
        equality_discription=Text("在长度上",font ="simsun",t2c={"长度":RED})
        #position
        author=Text("-Walski Schölder", color = YELLOW, font = "Times New Roman")
        author.next_to(quote.get_corner(DOWN + RIGHT), DOWN + LEFT)

        equality_pic_1.shift(LEFT*2.5)
        equality_pic_2.shift(RIGHT*2.5)
        equality_discription.shift(DOWN*1.5)
        equality_r.shift(RIGHT*2.5)
        equality_l.shift(LEFT*2.5)
        #showing objects
        self.wait(2)
        self.play(Write(quote), runtime = 2)
        self.play(Write(author), Write(notice0))
        self.wait(2)
        self.play(FadeOut(quote), FadeOut(author),ReplacementTransform(notice0,notice1))
        self.wait(1)
        self.play(FadeIn(equality_l),shift=LEFT)
        self.play(FadeIn(equality_r),shift=RIGHT)
        self.play(Write(equality),Write(equality_discription))
        self.wait(-2+4)#本期视频将会带大解决一个简单的长度问题
        self.play(Transform(equality_l,equality_pic_1),Transform(equality_r,equality_pic_2))
        self.wait(-1+4)#作为赠品，大家还能了解到一种巧妙的几何方法
        self.play(FadeOut(equality_l),FadeOut(equality_r),FadeOut(equality),FadeOut(equality_discription))
        self.wait(1.2)

        # make objects
        pi_normal=SVGMobject("PiCreatures_well.svg",stroke_color=WHITE)
        pi_thinking=SVGMobject("PiCreatures_confused.svg",stroke_color=WHITE)
        bubble_thinking=SVGMobject("Bubbles_thought.svg")
        thinking=Text("弧微分计算长度 \n 就可以得到了",font="kaiti",t2c={"弧微分":RED},font_size=16)
        discribe_ell=Text("参数方程的弧微分",font="kaiti",t2c={"参数方程":GREEN},font_size=16)
        integrate_ell=r"x &= \sqrt{2}\sin{\theta},y=\cos{\theta}\\"
        integrate_ell+=r"C &= \int\sqrt{(dx)^2+(dy)^2}\\"
        integrate_ell+=r"C &= \int_{0}^{2\pi}\sqrt{1+\cos^2\theta}d{\theta}\\"
        integrate_sin=r"C &= \int_{0}^{2\pi}\sqrt{(dx)^2+(dy)^2}\\"
        integrate_sin+=r"C &= \int_{0}^{2\pi}\sqrt{1+\cos^2x}dx\\"
        integrated_ell=Tex(integrate_ell)
        integrated_sin=Tex(integrate_sin)
        doubt=Text("???",font_size=16)
        plot_ell=SVGMobject("ell.svg")
        plot_sin=SVGMobject("sin.svg")
        #position
        pi_normal.move_to([-4,0,0])
        pi_thinking.move_to([-4,0,0])
        bubble_thinking.next_to(pi_normal,UR*0.5)
        thinking.move_to([-2.1,2.5,0])
        doubt.move_to([-2,2.5,0])
        discribe_ell.move_to([3,3,0])
        integrated_ell.move_to([3,2,0])
        integrated_sin.move_to([3,-1,0])
        integrated_ell.scale(0.5)
        integrated_sin.scale(0.5)
        plot_ell.move_to([2,2,0])
        plot_sin.move_to([2,-2,0])
        #showing objects
        self.play(FadeIn(pi_normal))
        self.play(Transform(pi_normal,pi_thinking),FadeIn(bubble_thinking))#可能有观众会问
        self.play(FadeIn(thinking))#这个等式用弧微分推起来很容易呀
        self.wait(3.7-3)
        self.play(Write(discribe_ell),Write(integrated_ell),Write(integrated_sin),runtime=2)
        self.wait(5.1-2)#嗯，确实如此
        self.play(FadeOut(discribe_ell),Transform(integrated_ell,plot_ell),Transform(integrated_sin,plot_sin))
        self.play(ReplacementTransform(thinking,doubt))
        self.wait(5.2-2)#但稍微想象一下就可以发现，从几何直观到积分的过程是单向的
        self.play(FadeOut(integrated_ell),FadeOut(integrated_sin),FadeOut(pi_normal),FadeOut(doubt),FadeOut(bubble_thinking))
        self.wait(3.5)#严格证明几何直观的现象也需要积分，不过要证明的东西是显然的
        self.play(Uncreate(notice1))
        self.wait(4.5-2)#一键三连，我们开始吧
        #make objects
        notice2=Notice("几何直观","请听介绍")
        notice3=Notice("严格考虑","请  思考")
        notice4=Notice("  结  语","请  期待")

        obj=ImageMobject("obj.png",fill_opacity=0)
        obj_ell=ImageMobject("obj_ell.png",fill_opacity=0)
        side=ImageMobject("side.png",fill_opacity=0)
        layer=ImageMobject("layer.png",fill_opacity=0)
        thinking2=Text("magic!",font_size=32,color=RED)
        #position
        obj.move_to([2,0,0]).scale(0.5)
        pi_normal.move_to([-4,0,0])
        pi_thinking.move_to([-4,0,0])
        bubble_thinking.next_to(pi_normal,UR*0.5)
        thinking2.move_to([-2.1,2.5,0])
        obj_ell.move_to([3,2,0]).scale(0.5)
        side.move_to([3,-2,0]).scale(0.5)
        layer.move_to([3,-2,0]).scale(0.5)
        #showing objects
        self.wait(2)
        self.play(Write(notice2))
        self.play(FadeIn(obj))
        self.wait(5-2)#首先我们要引入一个几何图形，它的特点是侧面是圆、底面是正方形
        self.play(FadeInFromPoint(obj_ell,[2,0,0]))
        self.wait(4-1)#首先很容易看出其中的一个椭圆
        self.play(FadeInFromPoint(side,[2,0,0]))
        self.play(FadeTransform(side,layer))
        self.wait(3-2)#正弦曲线在柱面上，展开之后就是正弦曲线了,于是就证明了
        self.play(FadeIn(pi_normal))
        self.play(FadeIn(thinking2),Transform(pi_normal,pi_thinking),FadeIn(bubble_thinking))
        self.wait(4-2)#相当神奇，但这两个坐标系描述同一曲线长度相等吗
        self.play(ReplacementTransform(notice2,notice3))
        self.wait(2)#事实上，这是显然的。这是弧微分的思路，所以一定程度上反直觉
        self.play(FadeOut(pi_normal),FadeOut(bubble_thinking),FadeOut(thinking2),FadeOut(obj),FadeOut(obj_ell),FadeOut(side),FadeOut(layer))
        self.play(ReplacementTransform(notice3,notice4))
        self.wait(4-1)#本期视频，我们通过坐标系的转化解决了一个简单的几何问题，下期视频，我们将进一步讨论坐标系的特点
        self.play(Uncreate(notice4))
        self.wait(2)