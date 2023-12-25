from manimlib import*
#define function
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
#part one
class start(Scene):
    def construct(self):
        notice1=Notice("　孔　子","请勿模仿")
        notice2=Notice("视频前言","请听介绍")
        notice3=Notice("中学知识","请　回忆")
#main
        author=Text("-论语",font="msyh")
        quote=Text("学而不思则罔，思而不学则殆",font="simsun",color=YELLOW)
        author.next_to(quote.get_corner(DR), DL)
        que_1=TexText(r"已知$x,y,z \in (0,+ \infty )$,且$x+y+z=1$\\求$\frac{1}{x}+\frac{9}{y}+\frac{25}{z}$的最小值",font_size=36,color=YELLOW)
        ans_1=VGroup(
            TexText("由柯西不等式可知","$(x+y+z)$",r"$(\frac{1}{x}+\frac{9}{y}+\frac{25}{z}) \geqslant 81$",font_size=36,color=BLUE),
            Tex(r"\frac{1}{x}+\frac{9}{y}+\frac{25}{z} \geqslant 81",font_size=36,color=BLUE),
        ).arrange(DOWN)
        pro_1=VGroup(
            Tex("(a^2+b^2)(c^2+d^2)","=","(ac+bd)^2","+","(ad-bc)^2",color=BLUE,font_size=36),
            Tex("(a^2+b^2)(c^2+d^2)","-","(ac+bd)^2","=","(ad-bc)^2",r"\geqslant","0",color=YELLOW,font_size=36),
            Tex("(a^2+b^2)(c^2+d^2)",r"\geqslant","(ac+bd)^2",font_size=36),
        ).arrange(DOWN,buff=LARGE_BUFF)
        pro_2=VGroup(Tex(r"\overrightarrow{v_1}","^2",r"\overrightarrow{v_2}","^2","=","(",r"\overrightarrow{v_1}",r"\cdot",r"\overrightarrow{v_2}",")","^2","+","(","\overrightarrow{v_1}",r"\times","\overrightarrow{v_2}",")","^2"),).arrange(DOWN,buff=LARGE_BUFF)
        pro_3=VGroup(
            TexText("基本不等式:","$2$","$a_i$","$b_i$",r"$ \leqslant $","$a_i^2$","$+$","$b_i^2$",font_size=36),
            TexText("令:",r"$a_i=\frac{a_i}{\sqrt{\sum_{i=1}^{n}a_i^2}}$",r"$b_i=\frac{b_i}{\sqrt{\sum_{i=1}^{n}b_i^2}}$",font_size=36),
            TexText("取有限和:",r"$(\sum_{i=1}^{n}a_ib_i)^2 \leqslant (\sum_{i=1}^{n}a_i^2)(\sum_{i=1}^{n}b_i^2)$",font_size=36),
        ).arrange(DOWN,buff=LARGE_BUFF)
#caption
        cap1=Caption("在中学中我们可能会见到这类问题")
        cap2=Caption("解法便是运用柯西不等式")
        cap3=Caption("关于柯西不等式，我们有很多证法")
        cap4=Caption("但要挑出最直观的话")
        cap5=Caption("恐怕会是运用基本不等式证明")
        cap6=Caption("可能，从证明中我们看不到任何直观的地方")
        cap7=Caption("别担心，直观的的地方在基本不等式的证明")
        cap8=Caption("从代数上这只不过是实数域中完全平方式恒非负")
        cap9=Caption("但从平面几何上呢，立体几何上的拓展呢")
        cap10=Caption("一键三联，让我们开始吧")
#location
        que_1.move_to([0,2,0])
        ans_1.next_to(que_1,DOWN)
#time
        self.wait(2)
        self.play(Write(quote),Write(notice1),runtime=2)
        self.play(Write(author))
        self.wait(1.5)
        self.play(FadeOut(quote),FadeOut(author))
        self.wait()
        self.add(cap1)
        self.play(ReplacementTransform(notice1,notice3))
        self.play(Write(que_1))
        self.wait(2)
        self.remove(cap1)
        self.add(cap2)
        self.wait(1.5)
        self.play(Write(ans_1))
        self.wait(2)
        self.remove(cap2)
        self.play(ReplacementTransform(notice3,notice2),FadeOut(que_1),FadeOut(ans_1))
        self.add(cap3)
        self.wait(1.5)
        self.play(FadeIn(pro_1))
        self.wait(1.3)
        self.play(FadeOut(pro_1),FadeIn(pro_2))
        self.wait(1.3)
        self.remove(cap3)
        self.add(cap4)
        self.wait(1.3)
        self.remove(cap4)
        self.add(cap5)
        self.wait(1.5)
        self.play(FadeOut(pro_2),FadeIn(pro_3))
        self.remove(cap5)
        self.add(cap6)
        self.wait(3.5)
        self.remove(cap6)
        self.add(cap7)
        self.wait(3.5)
        self.remove(cap7)
        self.add(cap8)
        self.wait(4.5)
        self.remove(cap8)
        self.add(cap9)
        self.wait(3.5)
        self.remove(cap9)
        self.add(cap10)
        self.play(FadeOut(notice2),FadeOut(pro_3))
        self.remove(cap10)
        self.wait(2)
#part two
class main1(Scene):
    def construct(self):
        notice1=Notice("奇妙操作","请　思考")
        #notice2=Notice("　定　理","请　理解")
#main
        text1=VGroup(
            Tex("ab",r"\leqslant",r"\frac{1}{2}a^2","+",r"\frac{1}{2}b^2"),
            Tex("ab",r"\leqslant",r"\int_{0}^{a}x dx","+",r"\int_{0}^{b}x dx")
        ).arrange(DOWN,LARGE_BUFF)
        axes=Axes(x_range=(0,5),y_range=(0,5),width=4,height=4,color=GREY)
        linear_graph=axes.get_graph(
            lambda x:x,
            color=BLUE
        )
        linear_label=axes.get_graph_label(linear_graph,"y=x")
        left=Polygon(axes.c2p(0,0,0),axes.c2p(0,2,0),axes.c2p(3,2,0),axes.c2p(3,0,0),fill_opacity=0.5,fill_color=YELLOW)
        right1=Polygon(axes.c2p(0,0,0),axes.c2p(0,2,0),axes.c2p(2,2,0),fill_opacity=0.5,fill_color=BLUE)
        right2=Polygon(axes.c2p(0,0,0),axes.c2p(3,0,0),axes.c2p(3,3,0),fill_opacity=0.5,fill_color=BLUE)
#caption
        cap1=Caption("回到基本不等式")
        cap2=Caption("可以将右边改写成积分形式")
        cap3=Caption("这样便很容易得到了其几何意义")
        cap4=Caption("其中左边表示坐标轴与x=a,y=b围成的面积(黄色)")
        cap5=Caption("右边分别表示坐标轴、y=x与x=a,y=b围成的面积(蓝色和绿色)")
        cap6=Caption("在坐标轴上结论，不等式显然成立")
        cap7=Caption("之所以说这是最直观的做法")
        cap8=Caption("其一在于我们可以借助几何意义理解多组元的情况")
        cap9=Caption("这里的多组元指a、b、c等(包含角标时)")
        cap10=Caption("其二在于我们可以同样借助几何意义理解分割线是曲线的情况")
        cap11=Caption("例如柯西不等式的推广赫尔德不等式")
#time
        self.play(Write(notice1))
        self.add(cap1)
        self.wait(2)
        self.play(Write(text1[0]))
        self.wait(2)
        self.remove(cap1)
        self.add(cap2)
        self.wait(2)
        self.play(TransformFromCopy(text1[0],text1[1]))
        self.wait(2)
        self.remove(cap2)
        self.add(cap3)
        self.play(FadeOut(text1[0]))
        self.play(text1[1].animate.shift(UP*3.5+LEFT*4).scale(0.75))
        self.wait(2)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(linear_graph),Write(linear_label))

        self.remove(cap3)
        self.add(cap4)
        self.wait(1.5)
        self.play(FadeIn(left))
        self.wait(2)
        self.remove(cap4)
        self.add(cap5)
        self.wait(1.5)
        self.play(FadeIn(right1),FadeIn(right2))
        self.wait(2.5)
        self.remove(cap5)
        self.add(cap6)
        self.wait(2.5)
        a=VGroup(axes,linear_graph,linear_label,right1,right2,left)
        self.play(FadeOut(a))
        self.play(text1[1].animate.shift(DOWN*3.5+RIGHT*4).scale(1.25))
        self.remove(cap6)
        self.add(cap7)
        self.wait(3.5)
        self.remove(cap7)
        self.add(cap8)
        self.wait(4.5)
        self.remove(cap8)
        self.add(cap9)
        self.wait(4.5)
        self.remove(cap9)
        self.add(cap10)
        self.wait(4.5)
        self.remove(cap10)
        self.add(cap11)
        self.wait(4.5)
        self.play(FadeOut(text1[1]),FadeOut(notice1))
        self.remove(cap11)
        self.wait(2)
#part three
class main2(Scene):
    def construct(self):
        notice1=Notice("类比操作","请　欣赏")
#main
        text1=VGroup(
            Tex("abc",r"\leqslant",r"\frac{1}{3}a^3","+",r"\frac{1}{3}b^3","+",r"\frac{1}{3}c^3"),
            Tex("abc",r"\leqslant",r"\int_{0}^{a^2}x dx","+",r"\int_{0}^{b^2}x dx","+",r"\int_{0}^{c^2}x dx")
        ).arrange(DOWN,LARGE_BUFF)
        text2=VGroup(
            Tex(r"(\sum_{i=1}^{n}a_ib_ic_i)^3",r"\leqslant",r"\sum_{i=1}^{n}a_i^3",r"\sum_{i=1}^{n}b_i^3",r"\sum_{i=1}^{n}c_i^3"),
            Tex(r"(\sum_{j=1}^{n} \prod_{i=1}^{n} a_{ij})^n",r"\leqslant",r"\prod_{i=1}^{n} \sum_{j=1}^{n} a_{ij}^n")
        )
        axes=ThreeDAxes(x_range=[0,5],y_range=[0,5],z_range=[0,5],width=4,height=4,Color=GREY)
        cuboid=VGroup(
            Polygon(axes.c2p(0,0,0),axes.c2p(3,0,0),axes.c2p(3,0,1),axes.c2p(0,0,1),fill_opacity=0.5,fill_color=YELLOW),
            Polygon(axes.c2p(0,0,0),axes.c2p(0,2,0),axes.c2p(0,2,1),axes.c2p(0,0,1),fill_opacity=0.5,fill_color=YELLOW),
            Polygon(axes.c2p(0,0,0),axes.c2p(0,2,0),axes.c2p(3,2,0),axes.c2p(3,0,0),fill_opacity=0.5,fill_color=YELLOW),
            Polygon(axes.c2p(3,0,0),axes.c2p(3,2,0),axes.c2p(3,2,1),axes.c2p(3,0,1),fill_opacity=0.5,fill_color=YELLOW),
            Polygon(axes.c2p(0,0,1),axes.c2p(0,2,1),axes.c2p(3,2,1),axes.c2p(3,0,1),fill_opacity=0.5,fill_color=YELLOW),
            Polygon(axes.c2p(0,2,0),axes.c2p(3,2,0),axes.c2p(3,2,1),axes.c2p(0,2,1),fill_opacity=0.5,fill_color=YELLOW),
        )
        pyramida=VGroup(
            Polygon(axes.c2p(0,0,0),axes.c2p(3,0,0),axes.c2p(3,0,1),axes.c2p(0,0,1),fill_opacity=0.5,fill_color=RED),
            Polygon(axes.c2p(0,0,0),axes.c2p(3,0,0),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=RED),
            Polygon(axes.c2p(0,0,1),axes.c2p(3,0,1),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=RED),
            Polygon(axes.c2p(3,0,0),axes.c2p(3,0,1),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=RED),
            Polygon(axes.c2p(0,0,0),axes.c2p(0,0,1),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=RED)
        )
        pyramidb=VGroup(
            Polygon(axes.c2p(0,0,0),axes.c2p(0,2,0),axes.c2p(0,2,1),axes.c2p(0,0,1),fill_opacity=0.5,fill_color=BLUE),
            Polygon(axes.c2p(0,0,0),axes.c2p(0,2,0),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=BLUE),
            Polygon(axes.c2p(0,0,0),axes.c2p(0,0,1),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=BLUE),
            Polygon(axes.c2p(0,2,1),axes.c2p(0,0,1),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=BLUE),
            Polygon(axes.c2p(0,2,1),axes.c2p(0,2,0),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=BLUE)
        )
        pyramidc=VGroup(
            Polygon(axes.c2p(0,0,0),axes.c2p(0,2,0),axes.c2p(3,2,0),axes.c2p(3,0,0),fill_opacity=0.5,fill_color=GREEN),
            Polygon(axes.c2p(0,0,0),axes.c2p(0,2,0),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=GREEN),
            Polygon(axes.c2p(0,0,0),axes.c2p(3,0,0),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=GREEN),
            Polygon(axes.c2p(3,2,0),axes.c2p(3,0,0),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=GREEN),
            Polygon(axes.c2p(3,2,0),axes.c2p(0,2,0),axes.c2p(3,2,1),fill_opacity=0.5,fill_color=GREEN)
        )
#cap
        cap1=Caption("首先来解释第一个拓展")
        cap2=Caption("也就是在x-y-z坐标系中的情况")
        cap3=Caption("类比一下，这个不等式积分后得到的应该是体积")
        cap4=Caption("也就不难想到下面的积分式")
        cap5=Caption("同样可以用图像来表示")
        cap6=Caption("左边为长方体体积")
        cap7=Caption("右边为三个四棱锥的体积")
        cap8=Caption("不等式也显然成立了")
        cap9=Caption("以此类推，在套用柯西不等式的证法")
        cap10=Caption("便可以得到柯西不等式的一个推广")
        cap11=Caption("我们得到了高次，但代价是多元")
        cap12=Caption("那么，有没有办法可以双元高次呢")
        cap13=Caption("答案是肯定的")
#time   
        self.wait(2)
        self.play(Write(notice1))
        self.add(cap1)
        self.wait(3.5)
        self.remove(cap1)
        self.add(cap2)
        self.wait(3.5)
        self.remove(cap2)
        self.add(cap3)
        self.wait()
        self.play(Write(text1[0]))
        self.wait(1.5)
        self.remove(cap3)
        self.add(cap4)
        self.wait(2.5)
        self.play(TransformFromCopy(text1[0],text1[1]))
        self.wait()
        self.play(FadeOut(text1[0]),text1[1].animate.shift(UP*3.5+LEFT*4).scale(0.5))
        self.wait(1.5)
        self.remove(cap4)
        self.add(cap5)
        self.play(ShowCreation(axes))
        self.wait(2.5)
        self.remove(cap5)
        self.add(cap6)
        self.wait(1.5)
        self.play(FadeIn(cuboid))
        self.wait(1.5)
        self.play(FadeOut(cuboid))
        self.wait()
        self.remove(cap6)
        self.add(cap7)
        self.wait(1.5)
        self.play(ShowCreationThenFadeOut(pyramida),runtime=2.5)
        self.play(ShowCreationThenFadeOut(pyramidb),runtime=2.5)
        self.play(ShowCreationThenFadeOut(pyramidc),runtime=2.5)
        self.wait(1.5)
        self.play(FadeIn(cuboid))
        self.wait(2)
        self.play(FadeIn(pyramida),FadeIn(pyramidb),FadeIn(pyramidc))
        self.remove(cap7)
        self.add(cap8)
        self.wait(5)
        a=VGroup(pyramida,pyramidb,pyramidc,cuboid,axes)
        self.play(FadeOut(a))
        self.play(text1[1].animate.shift(DOWN*3+RIGHT*4).scale(2))
        self.play(FadeOut(text1[1]))
        self.wait(1.5)
        self.remove(cap8)
        self.add(cap9)
        self.wait(1.5)
        self.play(Write(text2[0]))
        self.wait()
        self.play(FadeOut(text2[0]))
        self.remove(cap9)
        self.add(cap10)
        self.wait(1.5)
        self.play(Write(text2[1]))
        self.wait(2)
        self.play(FadeOut(text2[1]))
        self.wait()
        self.remove(cap10)
        self.add(cap11)
        self.wait(3.5)
        self.remove(cap11)
        self.add(cap12)
        self.wait(3.5)
        self.remove(cap12)
        self.add(cap13)
        self.wait(3.5)
        self.play(FadeOut(notice1))
        self.remove(cap13)
        self.wait(2)
#part four
class main3(Scene):
    def construct(self):
        notice1=Notice("奇妙操作","请　思考")
        notice2=Notice("　定　理","请　理解")
#main
        text1=VGroup(
            Tex("ab",r"\leqslant",r"\int_{o}^{a} f(x) dx + \int_{o}^{b} f^{-1}(x) dx"),
            Tex(r"f(x)=x^{p-1}(p \geqslant 0)"),
            Tex(r"f^{-1}(x)=x^{\frac{1}{p-1}}"),
            Tex("ab",r"\leqslant",r"\int_{o}^{a} x^{p-1} dx + \int_{o}^{b} x^{\frac{1}{p-1}} dx"),
            Tex(r"q=\frac{p}{p-1}"),
            Tex(r"\frac{1}{p}","+",r"\frac{1}{q}","=","1"),
            Tex("ab",r"\leqslant",r"\frac{a^p}{p}+\frac{a^q}{q}")
        )
        text2=VGroup(
            TexText("令:",r"$a_i=\frac{a_i}{(\sum_{i=1}^{n}a_i^p)^{\frac{1}{p}}}$",r"$b_i=\frac{b_i}{(\sum_{i=1}^{n}b_i^q)^{\frac{1}{q}}}$"),
            TexText("取有限和:",r"$\sum_{i=1}^{n}a_ib_i \leqslant (\sum_{i=1}^{n}a_i^p)^{\frac{1}{p}}(\sum_{i=1}^{n}b_i^q)^{\frac{1}{q}}$"),
        ).arrange(DOWN,LARGE_BUFF)
        plane=Axes(x_range=[-2,2],y_range=[0,4],width=4,height=4)
        parabola=plane.get_graph(
            lambda x:x**2,
            color=BLUE,
            x_range=[-2,2]
        )
        axes=Axes(x_range=[0,5],y_range=[0,5],width=4,height=4)
        func=axes.get_graph(
            lambda x:x**2,
            color=BLUE,
            x_range=[0,2]
        )
        left=Polygon(axes.c2p(0,0,0),axes.c2p(0,1,0),axes.c2p(2,1,0),axes.c2p(2,0,0),fill_opacity=0.5,fill_color=BLUE)
#cap
        cap1=Caption("双元至多要在x-y坐标系中考虑")
        cap2=Caption("那么高次代表什么呢？")
        cap3=Caption("从前面的例子可以发现高次受维度的影响")
        cap4=Caption("除此之外，实际上还受曲线次数影响")
        cap5=Caption("想要理解也很简单")
        cap6=Caption("例如抛物线在一维中可以被压缩为直线")
        cap7=Caption("因此只要考虑二维高次曲线的情况即可")
        cap8=Caption("不等式左边还是ab")
        cap9=Caption("右边的两个被积函数互为反函数")
        cap10=Caption("由此可以得到不等式的离散形式")
        cap11=Caption("总结一下得到推广赫尔德不等式")
        cap12=Caption("这样问题就解决了")
#location
        text1[0].shift(UP*0.5)
        text1[1].next_to(text1[0],DL)
        text1[2].next_to(text1[0],DR)
        text1[4].next_to(text1[3],DL)
        text1[5].next_to(text1[3],DR)
        text1[6].shift(DOWN*2)
#time
        self.wait(2)
        self.add(cap1)
        self.play(Write(notice1))
        self.wait(3.5)
        self.remove(cap1)
        self.add(cap2)
        self.wait(3.5)
        self.remove(cap2)
        self.add(cap3)
        self.wait(3.5)
        self.remove(cap3)
        self.add(cap4)
        self.wait(3.5)
        self.remove(cap4)
        self.add(cap5)
        self.wait(3.5)
        self.remove(cap5)
        self.add(cap6)
        self.wait()
        self.play(ShowCreation(plane),ShowCreation(parabola))
        self.play(Rotating(plane,-PI/2,X_AXIS),Rotating(parabola,-PI/2,X_AXIS))
        self.play(FadeOut(plane),FadeOut(parabola))
        self.wait(1.5)
        self.remove(cap6)
        self.add(cap7)
        self.wait(1.5)
        self.play(ShowCreation(axes),ShowCreation(func))
        self.wait()
        self.remove(cap7)
        self.add(cap8)
        self.wait(1.5)
        self.play(ShowCreationThenDestruction(left),runtime=2)
        self.play(FadeOut(axes),FadeOut(func))
        self.wait()
        self.remove(cap8)
        self.add(cap9)
        self.wait(1.5)
        self.play(Write(text1[0]))
        self.wait()
        self.play(Write(text1[1]),Write(text1[2]))
        self.wait(3.5)
        a=VGroup(text1[1],text1[0],text1[2])
        self.play(FadeTransform(a,text1[3]))
        self.wait(1.5)
        self.remove(cap9)
        self.add(cap10)
        self.wait(1.5)
        self.play(Write(text1[4]),Write(text1[5]))
        self.wait(3.5)
        b=VGroup(text1[3],text1[4],text1[5])
        self.play(FadeTransform(b,text1[6]))
        self.wait(2.5)
        self.play(FadeOut(text1[6]))
        self.remove(cap10)
        self.add(cap11)
        self.wait()
        self.play(Write(text2),ReplacementTransform(notice1,notice2))
        self.wait(2)
        self.remove(cap11)
        self.add(cap12)
        self.wait(2)
        self.play(FadeOut(notice2),FadeOut(text2))
        self.remove(cap12)
        self.wait(2)
#part five
class end(Scene):
    def construct(self):
        notice1=Notice("错误思路","请勿尝试")
        notice2=Notice("补充说明","请　思考")
#main
        text1=VGroup(
            Tex(r"(\sum_{j=1}^{n} \prod_{i=1}^{m} a_{ij})^k",r"\leqslant",r"\prod_{i=1}^{m} \sum_{j=1}^{n} a_{ij}^k"),
            TexText(r"$k \leqslant m$,$a_{ij} \geqslant 0$")
        ).arrange(DOWN,LARGE_BUFF)
        text2=VGroup(
            Text("平行四边形旋转过程中转到长方形时面积最大推出柯西不等式。",color=YELLOW,font="simsun",font_size=36),
            Text("平行六面体旋转过程中转到长方体时体积最大推出三元不等式？",color=BLUE,font="simsun",font_size=36),
            Tex(r"条件为：",r"(a_1b_2c_3+a_2b_3c_1+a_3b_1c_2-a_3b_2c_1-a_2b_1c_3-a_1b_3c_2)^2 \\ \leqslant (a_1^2+a_2^2+a_3^2)(b_1^2+b_2^2+b_3^2)(c_1^2+c_2^2+c_3^2)"),
            Text("明显得不出来",color=RED,font_size=80,font="simsun")
        )
        text3=Text("柳暗花明又一村",font_size=100,font="KaiTi",color=YELLOW)
#cap
        cap1=Caption("先前，我们讨论了两个猜想")
        cap2=Caption("现在，我们可以把它们结合起来，得到更强的式子")
        cap3=Caption("需要注意的是条件")
        cap4=Caption("非负是为了避免讨论")
        cap5=Caption("p大于等于1在之前有提到")
        cap6=Caption("是为了避免被积函数单调递减")
        cap7=Caption("此外，将其扩充到复数域也很简单")
        cap8=Caption("只需用复数的模代替即可")
        cap9=Caption("最后，我将介绍一个的思路：体积类比面积")
        cap10=Caption("很遗憾，无法找到体积的拉格朗日恒等式")
        cap11=Caption("同样，长方体切出平行六面体也相当困难")
        cap12=Caption("最后的最后：以一句话结束")        
#location
        text2[0].shift(UP*0.5)
        text2[1].shift(DOWN*0.5)
        text2[3].shift(DOWN*1.5)

#time
        self.wait(2)
        self.add(cap1)
        self.play(Write(notice1))
        self.wait(2.5)
        self.remove(cap1)
        self.add(cap2)
        self.wait(1.5)
        self.play(Write(text1))
        self.wait(2)
        self.remove(cap2)
        self.add(cap3)
        self.wait(3.5)
        self.remove(cap3)
        self.add(cap4)
        self.wait(3.5)
        self.remove(cap4)
        self.add(cap5)
        self.wait(3.5)
        self.remove(cap5)
        self.add(cap6)
        self.wait(3.5)
        self.remove(cap6)
        self.add(cap7)
        self.wait(3.5)
        self.remove(cap7)
        self.add(cap8)
        self.wait(1.5)
        self.play(FadeOut(text1))
        self.remove(cap8)
        self.play(ReplacementTransform(notice1,notice2))
        self.add(cap9)
        self.play(Write(text2[0]))
        self.wait()
        self.play(Write(text2[1]))
        self.wait()
        a=VGroup(text2[0],text2[1])
        self.play(FadeTransform(a,text2[2]))
        self.wait(1.5)
        self.play(Write(text2[3]))
        self.wait(2)
        self.play(FadeOut(text2[2]),FadeOut(text2[3]))
        self.remove(cap9)
        self.add(cap10)
        self.wait(3.5)
        self.remove(cap10)
        self.add(cap11)
        self.wait(3.5)
        self.remove(cap11)
        self.play(FadeOut(notice2))
        self.add(cap12)
        self.play(Write(text3))
        self.wait(3.5)
        self.remove(cap12)
        self.play(FadeOut(text3))
        self.wait(2)
#目录
# 几个柯西不等式证明
# 杨氏不等式            
# 推广其一:高维柯西不等式
# 推广其二:赫尔德不等式
#补充复数域的解决办法，其他方法的局限性：平行四边形中矩形最大，