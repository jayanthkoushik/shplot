from __future__ import annotations

import sys
from typing import Optional

if sys.version_info < (3, 9):
    from typing_extensions import Callable, Dict, Literal  # type: ignore
else:
    from typing import Callable, Dict, Literal

from ._interface import ColorProfile, FontProfile, PlotScaleProfile, PlottingProfile

__all__ = [
    "SH_BUILTIN_PROFILES",
    "ShPaperProfile",
    "ShBookProfile",
    "ShWebProfile",
    "ShPresentationProfile",
    "CUD_PALETTE",
    "ShLightCUDProfile",
    "BSLightCUDProfile",
    "BSDarkCUDProfile",
    "ShScaleProfile",
    "ShPaperScaleProfile",
    "ShBookScaleProfile",
    "ShWebScaleProfile",
    "ShPresentationScaleProfile",
    "ShFontsetupFontProfile",
    "ShPGFRcFontsFontProfile",
]

############################################################
# COLOR PROFILES

CUD_PALETTE = [
    "#000000",
    "#e69f00",
    "#56b4e9",
    "#009e73",
    "#f0e442",
    "#0072b2",
    "#d55e00",
    "#cc79a7",
]
"""Color Universal Design (CUD) palette.

See <https://jfly.uni-koeln.de/color/>."""


class ShLightCUDProfile(ColorProfile):
    """Black on white color profile with CUD palette."""

    def __init__(self):
        super().__init__(
            palette=CUD_PALETTE, fg="#000000", bg="#ffffff", fg_secondary="#a9a9a9"
        )


class BSLightCUDProfile(ColorProfile):
    """Bootstrap light theme color profile with CUD palette."""

    def __init__(self):
        super().__init__(
            palette=CUD_PALETTE, fg="#212529", bg="#ffffff", fg_secondary="#adb5bd"
        )


class BSDarkCUDProfile(ColorProfile):
    """Bootstrap dark theme color profile with CUD palette."""

    def __init__(self):
        palette = ["#adb5bd"] + CUD_PALETTE[1:]
        super().__init__(
            palette=palette, fg="#adb5bd", bg="#212529", fg_secondary="#495057"
        )


############################################################
# SCALE PROFILES


class ShScaleProfile(PlotScaleProfile):
    """Builder for scale profiles.

    Args:
        fs/fs_*: Font sizes (in points) for different elements.
        marker_size: Default marker size (in points).
        line_width: Default line width (in points).
        full_width_in: Default figure width (in inches).
    """

    def __init__(
        self,
        fs: float,
        fs_small: float,
        fs_smaller: float,
        fs_large: float,
        marker_size: float,
        line_width: float,
        full_width_in: float,
    ):
        super().__init__(
            font_size=fs,
            axes_title_size=fs,
            axes_label_size=fs_small,
            xtick_label_size=fs_smaller,
            ytick_label_size=fs_smaller,
            legend_font_size=fs_smaller,
            legend_title_size=fs_small,
            figure_title_size=fs_large,
            figure_label_size=fs,
            marker_size=marker_size,
            line_width=line_width,
            full_width_in=full_width_in,
            legend_marker_scale=2.0,
            constrained_layout=True,
            constrained_layout_hspace=0.1,
            constrained_layout_wspace=0.02,
        )


class ShPaperScaleProfile(ShScaleProfile):
    r"""Scale profile for a 10pt document.

    Font sizes correspond to relative LaTeX font sizes for 10pt documents:

    - \normalsize: 10pt
    - \small: 9pt
    - \footnotesize: 8pt
    - \large: 12pt
    """

    def __init__(self):
        super().__init__(
            fs=10.0,  # normalsize
            fs_small=9.0,  # small
            fs_smaller=8.0,  # footnotesize
            fs_large=12.0,  # large
            marker_size=2.0,
            line_width=1.5,
            full_width_in=6.5,
        )


class ShBookScaleProfile(ShScaleProfile):
    r"""Scale profile for a 12pt document.

    Font sizes correspond to relative LaTeX font sizes for 12pt documents:

    - \normalsize: 12pt
    - \small: 10.95pt
    - \footnotesize: 10pt
    - \large: 14.4pt
    """

    def __init__(self):
        super().__init__(
            fs=12.0,  # normalsize
            fs_small=10.95,  # small
            fs_smaller=10.0,  # footnotesize
            fs_large=14.4,  # large
            marker_size=3.0,
            line_width=2.0,
            full_width_in=6.0,
        )


class _ShWebScaleProfile(ShScaleProfile):
    def __init__(
        self, fs_px: float, ms_px: float, lw_px: float, fw_px: float, dpi: float
    ):
        pt_per_px = 72.0 / dpi
        fs = fs_px * pt_per_px
        super().__init__(
            fs=fs,  # medium
            fs_small=fs * 0.8125,  # small
            fs_smaller=fs * 0.625,  # x-small
            fs_large=fs * 1.125,  # large
            marker_size=ms_px * pt_per_px,
            line_width=lw_px * pt_per_px,
            full_width_in=fw_px / dpi,
        )


class ShWebScaleProfile(_ShWebScaleProfile):
    """Scale profile for display on the web.

    Sizes are for a 16px font size at 96dpi (CSS reference px).
    """

    def __init__(self):
        # CSS reference px is based on 96dpi.
        super().__init__(fs_px=16.0, ms_px=3.0, lw_px=2.0, fw_px=675.0, dpi=96.0)


class ShPresentationScaleProfile(_ShWebScaleProfile):
    """Scale profile for presentations.

    Sizes are based on a 48px font size, and will be scaled based on dpi.

    Args:
        dpi: Scale for converting pixel sizes to points.
    """

    def __init__(self, dpi: float):
        super().__init__(fs_px=48.0, ms_px=9.0, lw_px=6.0, fw_px=1600.0, dpi=dpi)


############################################################
# FONT PROFILES


class ShFontsetupFontProfile(FontProfile):
    """LaTeX font profile using the `fontsetup` package.

    See <https://www.ctan.org/pkg/fontsetup> for details on the package.
    This profile simply sets the latex preamble to load the package with the
    given font.

    Args:
        font: One of the fonts supported by `fontsetup`. This value is
            passed as the sole argument to the package.
    """

    FontType = Literal[
        "default",
        "olddefault",
        "cambria",
        "concrete",
        "ebgaramond",
        "erewhon",
        "euler",
        "fira",
        "gfsartemisia",
        "gfsdidotclassic",
        "gfsdidot",
        "kekris",
        "libertinus",
        "lucida",
        "minion",
        "msgaramond",
        "neoeuler",
        "oldstandard",
        "palatino",
        "stixtwo",
        "talos",
        "times",
        "xcharter",
    ]

    def __init__(self, font: FontType = "default"):
        super().__init__(
            family=["serif"],
            latex_preamble=[r"\usepackage[%s]{fontsetup}" % font],
            pgf_rcfonts=False,
        )


class ShPGFRcFontsFontProfile(FontProfile):
    """LaTeX font profile combining `fontsetup` with system fonts.

    This profile loads the `fontsetup` package with the given font as in
    `ShFontsetupFontProfile`, but also sets the `pgf.rcfonts` rcParam to
    `True`, so that `matplotlib` will insert `fontspec` commands into the
    LaTeX preamble to set `serif/sans-serif/monospace` fonts.

    Args:
        family: Default font family.
        base_font: One of the fonts supported by `fontsetup`. This value is
            passed as the sole argument to the package.
        serif/sans_serif/monospace: Overrides for serif/sans-serif/monospace
            families. If `None`, values from `rcParams` (`font.serif` etc.)
            will be used.
    """

    def __init__(
        self,
        family: Literal["serif", "sans-serif", "monospace"] = "serif",
        base_font: ShFontsetupFontProfile.FontType = "default",
        serif: Optional[str] = None,
        sans_serif: Optional[str] = None,
        monospace: Optional[str] = None,
    ):
        super().__init__(
            family=[family],
            latex_preamble=[r"\usepackage[%s]{fontsetup}" % base_font],
            pgf_rcfonts=True,
        )
        if serif is not None:
            self.serif = [serif]
        if sans_serif is not None:
            self.sans_serif = [sans_serif]
        if monospace is not None:
            self.monospace = [monospace]


############################################################
# FULL PROFILES


sh_rc_overrides = {
    "axes.grid": True,
    "axes.grid.axis": "y",
    "axes.axisbelow": True,  # draw grid lines below all plot elements
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "ytick.left": False,
    "figure.titleweight": "bold",
    "pdf.fonttype": 42,
}


class _ShFontsetupProfile(PlottingProfile):
    def __init__(self, font: ShFontsetupFontProfile.FontType, **kwargs):
        super().__init__(
            font=ShFontsetupFontProfile(font),
            **{"backend": "pgf", "savefig.format": "pdf", **sh_rc_overrides, **kwargs},
        )


class ShPaperProfile(_ShFontsetupProfile):
    """Profile for generating figures for a paper (10pt).

    Args:
        font: Name of the font to use--see `ShFontsetupFontProfile`.
        **rc_extra: `rcParams` overrides.
    """

    def __init__(self, font: ShFontsetupFontProfile.FontType = "default", **rc_extra):
        super().__init__(
            font, color=ShLightCUDProfile(), scale=ShPaperScaleProfile(), **rc_extra
        )


class ShBookProfile(_ShFontsetupProfile):
    """Profile for generating figures for a book (12pt).

    Args:
        font: Name of the font to use--see `ShFontsetupFontProfile`.
        **rc_extra: `rcParams` overrides.
    """

    def __init__(self, font: ShFontsetupFontProfile.FontType = "default", **rc_extra):
        super().__init__(
            font, color=ShLightCUDProfile(), scale=ShBookScaleProfile(), **rc_extra
        )


class ShWebProfile(PlottingProfile):
    """Profile for generating figures for the web.

    Args:
        theme: Color theme--'light' will generate figures on a light background,
            and 'dark' will generate figures on a dark background.
        font_family: Default font family.
        sans_serif_font: Optional override for the default sans-serif font.
        serif_font: Optional override for the default serif font.
        monospace_font: Optional override for the default monospace font.
        cursive_font: Optional override for the default cursive font.
        fantasy_font: Optional override for the default fantasy font.
        math_font: Optional override for the default math font.
        **rc_extra: `rcParams` overrides.
    """

    def __init__(
        self,
        theme: Literal["light", "dark"],
        font_family: Literal[
            "serif", "sans-serif", "monospace", "fantasy", "cursive"
        ] = "sans-serif",
        sans_serif_font: Optional[str] = None,
        serif_font: Optional[str] = None,
        monospace_font: Optional[str] = None,
        cursive_font: Optional[str] = None,
        fantasy_font: Optional[str] = None,
        math_font: Optional[
            Literal["dejavusans", "dejavuserif", "cm", "stix", "stixsans"]
        ] = None,
        **rc_extra,
    ):
        if theme == "light":
            color_profile: ColorProfile = BSLightCUDProfile()
        elif theme == "dark":
            color_profile = BSDarkCUDProfile()
        else:
            raise ValueError(f"invalid value for theme: {theme!r}")

        font_profile = FontProfile(family=[font_family])
        if sans_serif_font is not None:
            font_profile.sans_serif = [sans_serif_font]
        if serif_font is not None:
            font_profile.serif = [serif_font]
        if monospace_font is not None:
            font_profile.monospace = [monospace_font]
        if cursive_font is not None:
            font_profile.cursive = [cursive_font]
        if fantasy_font is not None:
            font_profile.fantasy = [fantasy_font]
        if math_font is not None:
            font_profile.math_fontset = math_font

        super().__init__(
            color=color_profile,
            font=font_profile,
            scale=ShWebScaleProfile(),
            **{
                "backend": "svg",
                "svg.fonttype": "path",
                "savefig.format": "svg",
                **sh_rc_overrides,
                **rc_extra,
            },
        )


class ShPresentationProfile(PlottingProfile):
    """Profile for generating figures for presentations.

    Args:
        font_family: Default font family.
        *_font: See `ShPGFRcFontsFontProfile`.
        dpi: See `ShPresentationScaleProfile`.
        **rc_extra: `rcParams` overrides.
    """

    def __init__(
        self,
        font_family: Literal["serif", "sans-serif", "monospace"] = "sans-serif",
        base_font: ShFontsetupFontProfile.FontType = "default",
        serif_font: Optional[str] = None,
        sans_serif_font: Optional[str] = None,
        monospace_font: Optional[str] = None,
        dpi: float = 200.0,
        **rc_extra,
    ):
        super().__init__(
            color=ShLightCUDProfile(),
            font=ShPGFRcFontsFontProfile(
                font_family, base_font, serif_font, sans_serif_font, monospace_font
            ),
            scale=ShPresentationScaleProfile(dpi),
            **{
                "backend": "pgf",
                "savefig.format": "png",
                "figure.dpi": dpi,
                **sh_rc_overrides,
                **rc_extra,
            },
        )


SH_BUILTIN_PROFILES: Dict[str, Callable[..., PlottingProfile]] = {
    "paper": ShPaperProfile,
    "book": ShBookProfile,
    "web_light": lambda **kwargs: ShWebProfile(theme="light", **kwargs),
    "web_dark": lambda **kwargs: ShWebProfile(theme="dark", **kwargs),
    "presentation": ShPresentationProfile,
}
"""Built-in plotting profiles with set values for different contexts."""
