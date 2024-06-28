from unittest import TestCase

import matplotlib as mpl

from shplot.profiles import (
    AxesProfile,
    ColorProfile,
    FontProfile,
    PlotScaleProfile,
    PlottingProfile,
    ProfileBase,
)


class TestProfileBase(TestCase):
    def setUp(self):
        class DummyProfile(ProfileBase):
            def __init__(self, rc_dict):
                super().__init__()
                self.rc_dict = rc_dict

            def _rc(self):
                return self.rc_dict

        self.DummyProfile = DummyProfile
        mpl.rcdefaults()
        self._set_font_size_and_verify()

    def _set_font_size_and_verify(self):
        mpl.rcParams["font.size"] = 10
        self.assertEqual(mpl.rcParams["font.size"], 10)

    def test_profile_base_config_updates_rc_params(self):
        dummy_profile = self.DummyProfile({"font.size": 100})
        dummy_profile.config()
        self.assertEqual(mpl.rcParams["font.size"], 100)

    def test_profile_base_config_updates_rc_params_without_reload(self):
        dummy_profile = self.DummyProfile({"font.size": 100})
        dummy_profile.config(reload_mpl=False)
        self.assertEqual(mpl.rcParams["font.size"], 100)

    def test_profile_base_context_restores_original_rc_params(self):
        dummy_profile = self.DummyProfile({"font.size": 100})
        with dummy_profile.context():
            self.assertEqual(mpl.rcParams["font.size"], 100)

        self.assertEqual(mpl.rcParams["font.size"], 10)


class TestColorProfile(TestCase):
    def test_color_profile_config_is_valid(self):
        profile = ColorProfile(
            palette=["black", "white"],
            fg="red",
            fg_secondary="blue",
            bg="green",
            grid_alpha=0.5,
            legend_frame_alpha=0.5,
            transparent=True,
        )
        with profile.context():
            pass


class TestFontProfile(TestCase):
    def test_font_profile_config_is_valid(self):
        profile = FontProfile(
            family=["x", "y"],
            style="normal",
            variant="normal",
            weight="300",
            stretch="condensed",
            serif=["xserif", "yserif"],
            sans_serif=["xsans", "ysans"],
            monospace=["xmono", "ymono"],
            cursive=["xcursive", "ycursive"],
            fantasy=["xfantasy", "yfantasy"],
            text_usetex=True,
            latex_preamble=[],
            math_fontset="stix",
            custom_math_rm="cxrm",
            custom_math_sf="cxsf",
            custom_math_tt="cxtt",
            custom_math_it="cxit",
            custom_math_bf="cxbf",
            custom_math_cal="cxcal",
            math_fallback="stixsans",
            math_default="sf",
            pgf_rcfonts=True,
            set_pgf_preamble=True,
        )
        with profile.context():
            pass


class TestPlotScaleProfile(TestCase):
    def test_plot_scale_profile_config_is_valid(self):
        profile = PlotScaleProfile(
            font_size=10.0,
            axes_title_size="xx-small",
            axes_label_size="x-small",
            xtick_label_size="small",
            ytick_label_size="medium",
            legend_font_size="large",
            legend_title_size="x-large",
            figure_title_size="xx-large",
            figure_label_size=10.0,
            marker_size=1.0,
            line_width=1.0,
            full_width_in=10.0,
            default_aspect_wh=0.5,
            legend_marker_scale=1.0,
            subplot_left=0.5,
            subplot_right=0.5,
            subplot_bottom=0.5,
            subplot_top=0.5,
            subplot_hspace=0.25,
            subplot_vspace=0.25,
            autolayout=True,
            constrained_layout=True,
            constrained_layout_hspace=0.1,
            constrained_layout_wspace=0.1,
        )
        with profile.context():
            pass


class TestAxesProfile(TestCase):
    def test_axes_scale_profile_config_is_valid(self):
        profile = AxesProfile(
            grid_axes="both",
            grid_lines="major",
            spines={"left", "right", "bottom", "top"},
            axis_below="line",
            xticks_top="major",
            xticks_bottom="major",
            xlabels_top=True,
            xlabels_bottom=True,
            xtick_direction="in",
            xtick_alignment="center",
            xlabel_position="center",
            yticks_left="major",
            yticks_right="major",
            ylabels_left=True,
            ylabels_right=True,
            ytick_direction="in",
            ytick_alignment="center",
            ylabel_position="center",
        )
        with profile.context():
            pass


class TestPlottingProfile(TestCase):
    def test_plotting_profile_config_is_valid(self):
        profile = PlottingProfile(
            color=ColorProfile(),
            font=FontProfile(),
            scale=PlotScaleProfile(),
            axes=AxesProfile(),
        )
        with profile.context():
            pass
