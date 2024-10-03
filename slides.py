from manim import *
from manim_slides import ManimSlidesMagic, Slide

template = TexTemplate()
template.add_to_preamble(r"\usepackage{physics}")
config["background_color"] = WHITE
Text.set_default(color=BLACK, font_size=24)
Tex.set_default(color=BLACK, font_size=28)
MathTex.set_default(color=BLACK, font_size=28)


# %%
# %%manim_slides -v WARNING --progress_bar display -q m Intro --manim-slides controls=true data_uri=true
class Intro(Slide):

    def construct(self):

        title = Text(
            "CMB and energy conservation limits\n on nanohertz GWs\n", font_size=48
        )
        authors = Text("Dave Wright, Tom Giblin, Jeff Hazboun")
        osu_logo = ImageMobject("./figs/osu-logo.png").scale(0.10)
        nanograv_logo = ImageMobject("./figs/nanograv_logo.png").scale(0.25)
        hazgrav_logo = ImageMobject(
            "./figs/hazgrav-logo-binary-and-text-transparent.png"
        ).scale(0.40)
        logos = (
            Group(hazgrav_logo, osu_logo, nanograv_logo)
            .scale(0.9)
            .arrange(RIGHT, aligned_edge=DOWN)
            .to_corner(DL)
        )

        self.play(FadeIn(VGroup(title, authors).arrange(DOWN)), FadeIn(logos))
        self.add_to_canvas(logos=logos)

        self.next_slide()
        citation_map = ImageMobject("./figs/new_physics_paperscape.png")
        self.wipe(self.mobjects_without_canvas, citation_map)

        self.next_slide()
        motivations = []
        motivations.append(
            Text(
                "The 15yr New Physics analysis has > 500 citations",
                color=WHITE,
            ).shift(UP)
        )
        self.play(FadeIn(motivations[0]))

        self.next_slide()
        motivations.append(
            Text(
                "Most of these papers only check for consistency with the 15yr data",
                color=WHITE,
            ).next_to(motivations[0], DOWN)
        )

        self.play(FadeIn(motivations[1], shift=0.3 * UP))

        self.next_slide()

        motivations.append(
            Text(
                "Turns out, a whole zoo of models are consistent",
                color=WHITE,
            ).next_to(motivations[1], DOWN)
        )

        self.play(FadeIn(motivations[2], shift=0.3 * UP))
        self.next_slide()

        motivations.append(
            Text(
                "How can we filter through this large model space in a Hubble time?",
                color=WHITE,
            ).next_to(motivations[2], DOWN)
        )
        self.play(FadeIn(motivations[3], Underline(motivations[3]), shift=0.3 * UP))


# %%
# %%manim_slides -v WARNING --progress_bar display -q l RuleOfThumb --manim-slides controls=true data_uri=true
class RuleOfThumb(Slide):

    def construct(self):
        osu_logo = ImageMobject("./figs/osu-logo.png").scale(0.10)
        nanograv_logo = ImageMobject("./figs/nanograv_logo.png").scale(0.25)
        hazgrav_logo = ImageMobject(
            "./figs/hazgrav-logo-binary-and-text-transparent.png"
        ).scale(0.40)
        logos = (
            Group(hazgrav_logo, osu_logo, nanograv_logo)
            .scale(0.9)
            .arrange(RIGHT, aligned_edge=DOWN)
            .to_corner(DL)
        )

        self.add(logos)
        self.add_to_canvas(logos=logos)

        methods_to_present = Text("Two methods to discuss today:")

        number_1 = Text("1.")
        rot = Text("Rule of thumb")

        rot_group = VGroup(number_1, rot).arrange(RIGHT)

        number_2 = Text("2.")
        neff = Text("CMB Bounds")

        neff_group = VGroup(number_2, neff).arrange(RIGHT)

        methods_group = VGroup(methods_to_present, rot_group, neff_group).arrange(DOWN)

        self.play(FadeIn(methods_group))
        self.next_slide()

        rot_new = rot.copy()
        rot_new.scale(1.5)
        rot_new.to_edge(UL)
        self.play(
            FadeOut(methods_group[0], methods_group[-1], number_1),
            Transform(rot, rot_new),
        )

        self.add_to_canvas(rot_title=rot_new)

        self.next_slide()
        rot_cite_goal = (
            Paragraph(
                "• Originally derived by Tom Giblin and Eric Thrane [1410.4779]\n",
                "• A heuristic for the max amplitude of a cosmological background",
                alignment="left",
            )
            .next_to(rot, DOWN, buff=1)
            .to_edge(LEFT)
        )

        self.play(FadeIn(rot_cite_goal))

        self.next_slide()
        rot_form = Text("• This rule of thumb takes a very simple form")
        rot_eq = MathTex(
            r"\Omega_\textrm{GW,0}(",
            "k_{*}",
            r") \approx 4.7 \times 10^{-8} ",
            r"\alpha",
            r"^2",
            r"\beta",
            r"\omega",
            r"^{2}",
        )
        self.play(
            FadeIn(rot_form.next_to(rot_cite_goal, DOWN).to_edge(LEFT)),
            FadeIn(rot_eq.scale(1.5).shift(0.5 * DOWN)),
        )

        rot_eq_exp = MathTex(
            r"\Omega_\textrm{GW,0}(",
            r"\text{characteristic scale}",
            r") &\approx 4.7 \times 10^{-8}\\ ",
            r"&\text{fraction of closure density}",
            r"^2\\",
            r"&\text{how quadrupolar}\\",
            r"&\text{source's equation of state}",
            r"^{2}",
        )
        self.next_slide()
        self.play(
            ReplacementTransform(
                rot_eq, rot_eq_exp.scale(1.5).shift(1 * DOWN, 0.5 * RIGHT)
            )
        )

        self.next_slide()
        self.wipe(self.mobjects_without_canvas)

        kg = MathTex(
            r"\ddot{h}_{ij}",
            r"+ 3H \dot{h}_{ij}",
            r"- \frac{1}{a^2} \nabla^2 h_{ij} = (16 \pi G) \Pi_{ij}^{TT}",
        )
        ani = Tex(
            r"where $\Pi_{ij}^{TT}$ is the TT projection ",
            r"of the anisotropic stress tensor ",
        )
        self.play(FadeIn(VGroup(kg, ani).arrange(DOWN).to_edge(UP)))

        assumptions = (
            Tex(r"Assumptions").align_to(ani, DOWN).shift(0.25 * DOWN).to_edge(LEFT)
        )
        uline = Underline(assumptions, color=BLACK, buff=0.1)
        gaussian = MathTex(
            r"\tilde{T}_{ij}(\vec{k}) \approx \tilde{T}(\vec{k}) = A \exp{\frac{-\qty(\abs{\vec{k}} - k^{*})^{2}}{2 \sigma^{2}}}",
            tex_template=template,
        )

        assumptions_group = VGroup(gaussian).align_to(uline, UL)

        self.next_slide()
        self.play(FadeIn(assumptions, uline))

        self.next_slide()

        iso = MathTex(
            r"\tilde{p}_{s}\qty(\vec{k}) &= \frac{1}{3}\tilde{T}^{i}_{\ i}\qty(\tilde{k}) \approx \tilde{T}\qty(\vec{k})\\",
            r"\tilde{\rho_{s}}\qty(\vec{k}) &= \alpha \tilde{\rho}\qty(\vec{k}) = \frac{\tilde{T}\qty(\vec{k})}{",
            r"\omega",
            r"}",
            tex_template=template,
        )
        assumptions_group += VGroup(iso)
        beta = MathTex(
            r"\beta",
            r"\equiv \frac{\abs{\Pi^{TT}}^2}{\abs{T}^2}",
            tex_template=template,
        )
        assumptions_group += VGroup(beta)
        assumptions_group.arrange(DOWN, aligned_edge=LEFT).align_to(uline, UL)

        self.next_slide()
        self.play(FadeIn(assumptions_group))

        self.next_slide()

        rot_steps = (
            Tex(r"How to derive the rule of thumb")
            .next_to(assumptions, DOWN)
            .to_edge(RIGHT)
        )
        rot_steps_underline = Underline(rot_steps, color=BLACK, buff=0.1)

        estimate = (
            Tex(r"Estimate the maximum perturbation")
            .next_to(rot_steps_underline, DOWN)
            .to_edge(RIGHT)
        )

        max_h = MathTex(
            r"&\dot{\tilde{h}} \approx \dot{\tilde{h}}_{ij} \approx \frac{16 \pi G}{k}\Pi^{TT}",
            tex_template=template,
        ).next_to(estimate, DOWN, aligned_edge=RIGHT)

        self.next_slide()

        self.play(FadeIn(rot_steps), FadeIn(rot_steps_underline))
        self.next_slide()

        self.play(FadeIn(estimate), FadeIn(max_h))

        self.next_slide()

        psd_text = Tex(r"Write down the PSD in terms of the perturbations").next_to(
            max_h, DOWN, aligned_edge=RIGHT
        )
        psd = MathTex(
            r"\Omega_{\textrm{GW}} \qty(k) = \frac{1}{\rho} \frac{k^3}{32 \pi G} \frac{1}{V} \sum_{i,j} \int \dd{\Omega} \abs{\dot{\tilde{h}}^{TT}_{ij}}^2",
            tex_template=template,
        ).next_to(psd_text, DOWN, aligned_edge=RIGHT)

        self.play(
            FadeIn(psd_text),
            FadeIn(psd),
        )

        self.next_slide()

        rot_final_text = Tex(r"Evaluate the PSD (today) at $k^*$").next_to(
            psd, DOWN, aligned_edge=RIGHT
        )
        rot_final = MathTex(
            r"\Omega_\textrm{GW,0}\qty(k_{*}) \approx 4.7 \times 10^{-8} ",
            r"\alpha^2\beta\omega^2",
            tex_template=template,
        ).next_to(rot_final_text, DOWN, aligned_edge=RIGHT)

        self.play(
            FadeIn(rot_final_text),
            FadeIn(rot_final),
        )
        self.next_slide


# %%
# %%manim_slides -v WARNING --progress_bar display -q m Neff --manim-slides controls=true data_uri=true
class Neff(Slide):

    def construct(self):
        osu_logo = ImageMobject("./figs/osu-logo.png").scale(0.10)
        nanograv_logo = ImageMobject("./figs/nanograv_logo.png").scale(0.25)
        hazgrav_logo = ImageMobject(
            "./figs/hazgrav-logo-binary-and-text-transparent.png"
        ).scale(0.40)
        logos = (
            Group(hazgrav_logo, osu_logo, nanograv_logo)
            .scale(0.9)
            .arrange(RIGHT, aligned_edge=DOWN)
            .to_corner(DL)
        )

        self.add(logos)
        self.add_to_canvas(logos=logos)

        methods_to_present = Text("Two methods to discuss today:")

        number_1 = Text("1.", color=GREY)
        rot = Text("Rule of thumb", color=GREY)

        rot_group = VGroup(number_1, rot).arrange(RIGHT)

        number_2 = Text("2.")
        neff = Text("CMB Bounds")

        neff_group = VGroup(number_2, neff).arrange(RIGHT)

        methods_group = VGroup(methods_to_present, rot_group, neff_group).arrange(DOWN)

        self.play(FadeIn(methods_group))
        self.next_slide()

        neff_new = neff.copy()
        neff_new.scale(1.5)
        neff_new.to_edge(UL)
        self.play(
            FadeOut(methods_group[0], methods_group[1], number_2),
            Transform(neff, neff_new),
        )

        self.add_to_canvas(neff_title=neff_new)

        self.next_slide()
        text_0 = Tex(
            r"• Specifically, bounds on the effective number of neutrino species $N_{\textrm{eff}}$"
        )
        text_1 = Tex(r"• The Standard Model predicts $N_{\textrm{eff}} = 3.046$")
        text_2 = Tex(
            r"• GWs in the early universe add to $N_{\textrm{eff}}$ giving a deviation\\ \noindent from the SM value $\Delta N_{\textrm{eff}} > 0$ "
        )
        text_3 = Tex(r"• $\Delta N_{\textrm{eff}}$ is constrained by CMB measurements ")

        text_4 = Tex(
            r"$\int{ \dd{\ln{f}}\ h^2 \Omega_\textrm{GW,0}\qty(f)} < 5.6 \times 10^{-6} \Delta N_{\textrm{eff}}$",
            tex_template=template,
        )

        text_group = (
            VGroup(text_0, text_1, text_2, text_3)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(neff_new, DOWN)
            .to_edge(LEFT)
        )


        pspec = ImageMobject("./figs/neff_power_spectrum.png")
        pspec_cap = Tex(r"Fig. 1 of [1912.00995]").scale(0.8)
        pspec_group = Group(pspec, pspec_cap).arrange(DOWN, buff=0.1).to_edge(RIGHT)
        text_4.next_to(pspec_group, LEFT)
        self.play(FadeIn(text_1, text_2, text_3, pspec_group))
        self.next_slide()

        self.play(
            FadeIn(text_4), FadeIn(SurroundingRectangle(text_4, BLACK))
        )
        self.next_slide()


# %%
# %%manim_slides -v WARNING --progress_bar display -q m Methods --manim-slides controls=true data_uri=true
class Methods(Slide):

    def construct(self):
        osu_logo = ImageMobject("./figs/osu-logo.png").scale(0.10)
        nanograv_logo = ImageMobject("./figs/nanograv_logo.png").scale(0.25)
        hazgrav_logo = ImageMobject(
            "./figs/hazgrav-logo-binary-and-text-transparent.png"
        ).scale(0.40)
        logos = (
            Group(hazgrav_logo, osu_logo, nanograv_logo)
            .scale(0.9)
            .arrange(RIGHT, aligned_edge=DOWN)
            .to_corner(DL)
        )

        self.add(logos)
        self.add_to_canvas(logos=logos)

        methods = Text("Methods").to_edge(UL).scale(1.5)

        self.play(FadeIn(methods))
        self.next_slide()

        text_0 = Tex(
            r"• We choose two representative models from the 15yr New Physics analysis:",
        )
        fopt = VGroup(Tex(r"• First order phase transitions (FOPT)"))
        fopt_source = VGroup(Tex(r"\ sourced by sound waves"))
        fopt += fopt_source
        fopt.arrange(RIGHT, buff=0.1)

        sigw = VGroup(Tex(r"• Scalar induced gravitational waves (SIGW)"))
        sigw_source = VGroup(
            Tex(r" from a delta function peak in the scalar power spectrum")
        )
        sigw += sigw_source
        sigw.arrange(RIGHT, buff=0.1)

        text_1 = Tex(
            r"• For each model, we orthogonally sample from the prior and 68\% CI"
        )
        text_2 = VGroup(
            Tex(
                r"• We find the peak and integrated energy of $\Omega_{\textrm{GW,0}}\qty(f)$,",
                tex_template=template,
            )
        )

        text_25 = VGroup(
            Tex(r" then apply the rule of thumb and $N_{\textrm{eff}}$ bounds")
        )
        text_2 += text_25
        text_2.arrange(RIGHT, buff=0.1)

        text_group = (
            VGroup(text_0, fopt, sigw, text_1, text_2)
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(methods, DOWN)
            .to_edge(LEFT)
        )
        fopt.shift(RIGHT * 0.5)
        sigw.shift(RIGHT * 0.5)

        self.play(FadeIn(text_group))

        self.next_slide()
        code = """# Instead of this
result = []
for sample in samples:
    result.append(func(sample))

# Do this
result = jax.vmap(func)(samples)
"""
        rendered_code = Code(
            code=code,
            language="Python",
            font_size=18,
            insert_line_no=False,
            style="dracula",
        ).next_to(text_group, DOWN, aligned_edge=LEFT)
        jax_logo = SVGMobject("./figs/jax-logo.svg").next_to(
            rendered_code, RIGHT, aligned_edge=UP
        )
        self.play(FadeIn(rendered_code), FadeIn(jax_logo))


# %%
# %%manim_slides -v WARNING --progress_bar display -q m Results --manim-slides controls=true data_uri=true
class Results(Slide):

    def construct(self):
        osu_logo = ImageMobject("./figs/osu-logo.png").scale(0.10)
        nanograv_logo = ImageMobject("./figs/nanograv_logo.png").scale(0.25)
        hazgrav_logo = ImageMobject(
            "./figs/hazgrav-logo-binary-and-text-transparent.png"
        ).scale(0.40)
        logos = (
            Group(hazgrav_logo, osu_logo, nanograv_logo)
            .scale(0.9)
            .arrange(RIGHT, aligned_edge=DOWN)
            .to_corner(DL)
        )

        self.add(logos)
        self.add_to_canvas(logos=logos)

        results = Text("Results").to_edge(UL).scale(1.5)

        self.play(FadeIn(results))
        self.next_slide()

        scenarios = (
            Text("We have to choose values for our rule of thumb parameters")
            .scale(0.8)
            .next_to(results, DOWN, aligned_edge=LEFT)
        )

        rot_scenarios = (
            MathTable(
                [
                    [
                        r"\text{scenario}",
                        r"\alpha",
                        r"\beta",
                        r"\omega",
                        r"\Omega_{\mathrm{GW, 0}}(k^*)",
                    ],
                    [
                        r"\text{optimistic}",
                        r"1",
                        r"0.1",
                        r"1 / 3",
                        r"4.97 \times 10^{-10}",
                    ],
                    [
                        r"\text{realistic}",
                        r"0.1",
                        r"0.03",
                        r"1 / 3",
                        r"1.49 \times 10^{-12}",
                    ],
                    [
                        r"\text{pessimistic}",
                        r"0.02",
                        r"0.005",
                        r"1 / 3",
                        r"9.93 \times 10^{-15}",
                    ],
                ],
                include_outer_lines=True,
                line_config={"color": BLACK},
                v_buff=0.5,
                h_buff=0.5,
            )
            .scale(0.5)
            .to_corner(UR)
        )
        self.play(FadeIn(scenarios), FadeIn(rot_scenarios))
        self.next_slide()

        rot_fopt_caption = (
            Text(r"The FOPT results")
            .scale(0.8)
            .next_to(scenarios, DOWN, aligned_edge=LEFT)
        )
        rot_underline = Underline(rot_fopt_caption, color=BLACK)

        rot_fopt = (
            ImageMobject("./figs/pt-sound-peak-omega-hist.png")
            .scale(0.5)
            .next_to(rot_fopt_caption, DOWN, buff=1)
            .shift(RIGHT * 3)
        )
        neff_fopt = (
            ImageMobject("./figs/pt-sound-int-omega-hist.png")
            .scale(0.5)
            .next_to(rot_fopt, RIGHT, aligned_edge=DOWN, buff=1)
        )
        self.play(
            FadeIn(rot_fopt_caption, rot_underline), FadeIn(rot_fopt), FadeIn(neff_fopt)
        )

        self.next_slide()
        rot_sigw_caption = (
            Text(r"The SIGW results")
            .scale(0.8)
            .next_to(scenarios, DOWN, aligned_edge=LEFT)
        )
        rot_underline = Underline(rot_sigw_caption, color=BLACK)
        rot_sigw = (
            ImageMobject("./figs/sigw-delta-peak-omega-hist.png")
            .scale(0.5)
            .next_to(rot_sigw_caption, DOWN, buff=1)
            .shift(RIGHT * 3)
        )
        neff_sigw = (
            ImageMobject("./figs/sigw-delta-int-omega-hist.png")
            .scale(0.5)
            .next_to(rot_sigw, RIGHT, aligned_edge=DOWN, buff=1)
        )

        self.play(
            Transform(rot_fopt_caption, rot_sigw_caption),
            Transform(rot_underline, rot_underline),
            FadeOut(rot_fopt),
            FadeIn(rot_sigw),
            FadeOut(neff_fopt),
            FadeIn(neff_sigw),
        )


# %%
# %%manim_slides -v WARNING --progress_bar display -q m Final --manim-slides controls=true data_uri=true
class Final(Slide):

    def construct(self):
        osu_logo = ImageMobject("./figs/osu-logo.png").scale(0.10)
        nanograv_logo = ImageMobject("./figs/nanograv_logo.png").scale(0.25)
        hazgrav_logo = ImageMobject(
            "./figs/hazgrav-logo-binary-and-text-transparent.png"
        ).scale(0.40)
        logos = (
            Group(hazgrav_logo, osu_logo, nanograv_logo)
            .scale(0.9)
            .arrange(RIGHT, aligned_edge=DOWN)
            .to_corner(DL)
        )

        self.add(logos)
        self.add_to_canvas(logos=logos)

        final = Text("Takeaways and future plans").scale(1.5).to_edge(UL)

        self.play(FadeIn(final))

        text_0 = Text(
            "• The rule of thumb and CMB measurements provide fast methods to explore new physics models \n without a full Bayesian analysis",
            t2w={"without": BOLD}, line_spacing=1
        ).scale(0.8).next_to(final, DOWN, aligned_edge=LEFT)

        caveat = Text(
            "• The rule of thumb is not a hard bound. If models exceed the rule of thumb, you need to first check \n if you are violating the assumptions",
            t2w={"not": BOLD}, line_spacing=1
        ).scale(0.8).next_to(text_0, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(text_0, caveat))

        self.next_slide()
        future_plan = Text("• I plan to incorporate the methods and utilities from this work into PTArcade").scale(0.8).next_to(caveat, DOWN, aligned_edge=LEFT)
        future_plan_2 = Text("• We will have quick and efficient methods to assess the feasibility of new physics models").scale(0.8).next_to(future_plan, DOWN, aligned_edge=LEFT)
        qr = ImageMobject("./figs/github_qr.png").to_corner(DR)
        self.play(FadeIn(future_plan), FadeIn(future_plan_2), FadeIn(qr))


# %%
# %%manim_slides -v WARNING --progress_bar display -q m BackUp --manim-slides controls=true data_uri=true
class BackUp(Slide):

    def construct(self):
        osu_logo = ImageMobject("./figs/osu-logo.png").scale(0.10)
        nanograv_logo = ImageMobject("./figs/nanograv_logo.png").scale(0.25)
        hazgrav_logo = ImageMobject(
            "./figs/hazgrav-logo-binary-and-text-transparent.png"
        ).scale(0.40)
        logos = (
            Group(hazgrav_logo, osu_logo, nanograv_logo)
            .scale(0.9)
            .arrange(RIGHT, aligned_edge=DOWN)
            .to_corner(DL)
        )

        self.add(logos)
        self.add_to_canvas(logos=logos)

        methods_to_present = Text("Rule of thumb backup slides")

        rot = Text("Rule of thumb")

        self.play(FadeIn(methods_to_present))
        self.next_slide()

        rot.scale(1.5)
        rot.to_edge(UL)
        self.play(
            ReplacementTransform(methods_to_present, rot),
        )

        self.add_to_canvas(rot_title=rot)

        self.next_slide()
        rot_cite_goal = (
            Paragraph(
                "• Originally derived by Tom Giblin and Eric Thrane [1410.4779]\n",
                "• A heuristic for the max amplitude of a cosmological background",
                alignment="left",
            )
            .next_to(rot, DOWN, buff=1)
            .to_edge(LEFT)
        )

        self.play(FadeIn(rot_cite_goal))

        self.next_slide()
        rot_form = Text("• This rule of thumb takes a very simple form")
        rot_eq = MathTex(
            r"\Omega_\textrm{GW,0}(",
            "k_{*}",
            r") \approx 4.7 \times 10^{-8} ",
            r"\alpha",
            r"^2",
            r"\beta",
            r"\omega",
            r"^{2}",
        )
        self.play(
            FadeIn(rot_form.next_to(rot_cite_goal, DOWN).to_edge(LEFT)),
            FadeIn(rot_eq.scale(1.5).shift(0.5 * DOWN)),
        )

        rot_eq_exp = MathTex(
            r"\Omega_\textrm{GW,0}(",
            r"\text{characteristic scale}",
            r") &\approx 4.7 \times 10^{-8}\\ ",
            r"&\text{fraction of closure density}",
            r"^2\\",
            r"&\text{how quadrupolar}\\",
            r"&\text{source's equation of state}",
            r"^{2}",
        )
        self.next_slide()
        self.play(
            ReplacementTransform(
                rot_eq, rot_eq_exp.scale(1.5).shift(1 * DOWN, 0.5 * RIGHT)
            )
        )

        self.next_slide()
        self.remove_from_canvas("rot_title")
        self.wipe(self.mobjects_without_canvas)

        kg = MathTex(
            r"\ddot{h}_{ij}",
            r"+ 3H \dot{h}_{ij}",
            r"- \frac{1}{a^2} \nabla^2 h_{ij} = (16 \pi G) \Pi_{ij}^{TT}",
        )
        ani = Tex(
            r"where $\Pi_{ij}^{TT}$ is the TT projection ",
            r"of the anisotropic stress tensor ",
        )
        self.play(Write(VGroup(kg, ani).arrange(DOWN).to_edge(UP)))

        assumptions = (
            Tex(r"Assumptions").align_to(ani, DOWN).shift(0.25 * DOWN).to_edge(LEFT)
        )
        uline = Underline(assumptions, color=BLACK, buff=0.1)
        gaussian = MathTex(
            r"\tilde{T}_{ij}(\vec{k}) \approx \tilde{T}(\vec{k}) = A \exp{\frac{-\qty(\abs{\vec{k}} - k^{*})^{2}}{2 \sigma^{2}}}",
            tex_template=template,
        )

        assumptions_group = VGroup(gaussian).align_to(uline, UL)

        self.next_slide()
        self.play(FadeIn(assumptions, uline))

        self.next_slide()

        iso = MathTex(
            r"\tilde{p}_{s}\qty(\vec{k}) &= \frac{1}{3}\tilde{T}^{i}_{\ i}\qty(\tilde{k}) \approx \tilde{T}\qty(\vec{k})\\",
            r"\tilde{\rho_{s}}\qty(\vec{k}) &= \frac{\tilde{T}\qty(\vec{k})}{",
            r"\omega",
            r"}",
            tex_template=template,
        )
        assumptions_group += VGroup(iso)
        assumptions_group.arrange(DOWN, aligned_edge=LEFT).align_to(uline, UL)
        self.next_slide()
        self.play(FadeIn(assumptions_group))

        stress_energy_der = [
            MathTex(
                r"\int \dd[3]{k} \abs{A}^{2} \exp{\frac{-\qty(\abs{\vec{k}} - k^{*})^{2}}{\sigma^{2}}}",
                r"=\int \dd[3]{k} \abs{\omega \tilde{\rho}_{s}\qty(\vec{k})}^2",
                tex_template=template,
            ).to_edge(RIGHT),
            MathTex(
                r"4\pi\abs{A}^{2} \int \dd{k} k^2 \exp{\frac{-\qty(k - k^{*})^{2}}{\sigma^{2}}}",
                r"=\int \dd[3]{k} \abs{\omega \tilde{\rho}_{s}\qty(\vec{k})}^2",
                tex_template=template,
            ).to_edge(RIGHT),
            MathTex(
                r"4\pi\abs{A}^{2} \int \dd{k} k^2 \exp{\frac{-\qty(k - k^{*})^{2}}{\sigma^{2}}}",
                r"=\omega^2\int \dd{V} \rho^{2}_{s}\qty(\vec{x})",
                tex_template=template,
            ).to_edge(RIGHT),
            MathTex(
                r"\abs{A}^{2} W\qty(k^*, \sigma)",
                r"=\omega^2\int \dd{V} \rho^{2}_{s}\qty(\vec{x})",
                tex_template=template,
            ).to_edge(RIGHT),
            MathTex(
                r"\abs{A}^{2} W\qty(k^*, \sigma)",
                r"=\omega^2 V \rho^{2}_{s}",
                tex_template=template,
            ).to_edge(RIGHT),
            MathTex(
                r"\abs{A}^{2}",
                r"=\frac{\omega^2 V \rho^{2}_{s}}{ W\qty(k^*, \sigma)}",
                tex_template=template,
            ).to_edge(RIGHT),
            MathTex(
                r"\abs{\tilde{T}}^{2}",
                r"=\frac{\omega^2 V \rho^{2}_{s}}{ W\qty(k^*, \sigma)}\exp{\frac{-\qty(k - k^*)^2}{\sigma^2}",
                tex_template=template,
            ).to_edge(RIGHT),
            MathTex(
                r"\abs{\tilde{T}}^{2}",
                r"=\frac{\omega^2 V \alpha^2 \rho^{2}}{ W\qty(k^*, \sigma)}\exp{\frac{-\qty(k - k^*)^2}{\sigma^2}",
                tex_template=template,
            ).to_edge(RIGHT),
            MathTex(
                r"\abs{\Pi^{TT}}^{2}",
                r"=\frac{ \beta \omega ^2 V \alpha ^2 \rho^{2} } {W\qty(k^*, \sigma)} \exp{\frac{-\qty(k - k^*)^2}{\sigma^2}",
                tex_template=template,
            ).to_edge(RIGHT),
        ]
        self.next_slide()
        self.play(Write(stress_energy_der[0]))

        for i, obj in enumerate(stress_energy_der[1:-1]):
            self.next_slide()
            self.play(ReplacementTransform(stress_energy_der[i], obj))

        self.next_slide()

        beta = MathTex(
            r"\beta",
            r"\equiv \frac{\abs{\Pi^{TT}}^2}{\abs{T}^2}",
            tex_template=template,
        )
        assumptions_group += VGroup(beta)
        assumptions_group.arrange(DOWN, aligned_edge=LEFT).align_to(uline, UL)
        self.play(Write(assumptions_group[-1], run_time=1))

        self.next_slide()
        self.play(ReplacementTransform(stress_energy_der[-2], stress_energy_der[-1]))

        self.next_slide()
        # self.add(index_labels(stress_energy_der[-1][1]))
        self.play(stress_energy_der[-1].animate.align_to(uline, UP))

        self.next_slide()

        max_h = (
            MathTex(
                r"&\text{Estimate the maximum perturbation}\\"
                r"&\tilde{h} \approx \tilde{h}_{ij} \approx \frac{16 \pi G}{k^2}\Pi^{TT}",
                tex_template=template,
            )
            .to_edge(RIGHT)
            .next_to(stress_energy_der[-1], DOWN)
        )

        self.play(
            Indicate(stress_energy_der[-1][1][1:3]),
            Indicate(stress_energy_der[-1][1][5]),
        )

        self.next_slide()

        self.play(FadeIn(max_h))

        excersize = (
            Tex("The rest is left as an exercise to the reader...")
            .to_edge(RIGHT)
            .next_to(max_h, DOWN)
        )

        self.next_slide()

        self.play(FadeIn(excersize))

        self.next_slide()

        rot_new = (
            MathTex(
                r"\Omega_\textrm{GW,0}\qty(k_{*}) \approx 2.3 \times 10^{-4}",
                r"\alpha^2\beta\omega^2",
                r"\frac{k_{*}}{\sigma}",
                r"\qty( \frac{H}{k_{*}})^2",
                tex_template=template,
            )
            .to_edge(RIGHT)
            .next_to(excersize, DOWN)
        )

        self.play(Write(rot_new, run_time=1))
        self.next_slide()

        self.play(Indicate(rot_new[2][0:]), Indicate(rot_new[3][1:5]))
        self.next_slide()

        rot_k_choice = (
            MathTex(
                r"\Omega_\textrm{GW,0}\qty(k_{*}) \approx 2.3 \times 10^{-4}",
                r"\alpha^2\beta\omega^2",
                r"\frac{1}{2}",
                r"\qty( \frac{1}{100})^2",
                tex_template=template,
            )
            .to_edge(RIGHT)
            .next_to(excersize, DOWN)
        )

        self.play(ReplacementTransform(rot_new, rot_k_choice))
        self.next_slide()

        rot_final = MathTex(
            r"\Omega_\textrm{GW,0}\qty(k_{*}) \approx 4.7 \times 10^{-8} ",
            r"\alpha^2\beta\omega^2",
            tex_template=template,
        ).move_to(rot_k_choice.get_edge_center(LEFT), aligned_edge=LEFT)
        self.play(ReplacementTransform(rot_k_choice, rot_final))
        self.play(FadeIn(SurroundingRectangle(rot_final, BLACK)))
