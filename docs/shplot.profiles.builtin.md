# shplot.profiles.builtin module


### shplot.profiles.builtin.SH_BUILTIN_PROFILES(_: Dict[str, Callable[[...], [PlottingProfile](shplot.profiles.md#shplot.profiles.PlottingProfile)]]_ _ = {'book': <function make_builtin_profile_builder.<locals>.profile_builder>, 'paper': <function make_builtin_profile_builder.<locals>.profile_builder>, 'presentation': <function make_builtin_profile_builder.<locals>.profile_builder>, 'web_dark': <function make_builtin_profile_builder.<locals>.profile_builder>, 'web_light': <function make_builtin_profile_builder.<locals>.profile_builder>}_ )
Built-in plotting profiles with set values for different contexts.


### _class_ shplot.profiles.builtin.ShPaperProfile(fontname='default', \*\*rc_extra)
Bases: `_ShFontsetupProfile`

Profile for generating figures for a paper (10pt).


* **Parameters**


    * **fontname** (*ShFontsetupFontProfile.FontType*) – Name of the font to use–see `ShFontsetupFontProfile`.
    * **\*\*rc_extra** – `rcParams` overrides.



### _class_ shplot.profiles.builtin.ShBookProfile(fontname='default', \*\*rc_extra)
Bases: `_ShFontsetupProfile`

Profile for generating figures for a book (12pt).


* **Parameters**


    * **fontname** (*ShFontsetupFontProfile.FontType*) – Name of the font to use–see `ShFontsetupFontProfile`.
    * **\*\*rc_extra** – `rcParams` overrides.



### _class_ shplot.profiles.builtin.ShWebProfile(theme, font_family='sans-serif', sans_serif_font=None, serif_font=None, monospace_font=None, cursive_font=None, fantasy_font=None, math_font=None, \*\*rc_extra)
Bases: [`PlottingProfile`](shplot.profiles.md#shplot.profiles.PlottingProfile)

Profile for generating figures for the web.


* **Parameters**


    * **theme** (*Literal**[**'light'**, **'dark'**]*) – Color theme–‘light’ will generate figures on a light
    background, and ‘dark’ will generate figures on a dark
    background.
    * **font_family** (*Literal**[**'serif'**, **'sans-serif'**, **'monospace'**, **'fantasy'**, **'cursive'**]*) – Default font family.
    * **sans_serif_font** (*Optional**[**str**]*) – Optional override for default sans-serif font.
    * **serif_font** (*Optional**[**str**]*) – Optional override for default serif font.
    * **monospace_font** (*Optional**[**str**]*) – Optional override for default monospace font.
    * **cursive_font** (*Optional**[**str**]*) – Optional override for default cursive font.
    * **fantasy_font** (*Optional**[**str**]*) – Optional override for default fantasy font.
    * **math_font** (*Optional**[**Literal**[**'dejavusans'**, **'dejavuserif'**, **'cm'**, **'stix'**, **'stixsans'**]**]*) – Optional override for default math font.
    * **\*\*rc_extra** – `rcParams` overrides.



### _class_ shplot.profiles.builtin.ShPresentationProfile(font_family='sans-serif', base_font='default', serif_font=None, sans_serif_font=None, monospace_font=None, dpi=200.0, \*\*rc_extra)
Bases: [`PlottingProfile`](shplot.profiles.md#shplot.profiles.PlottingProfile)

Profile for generating figures for presentations.


* **Parameters**


    * **font_family** (*Literal**[**'serif'**, **'sans-serif'**, **'monospace'**]*) – Default font family.
    * **base_font** (*ShFontsetupFontProfile.FontType*) – See `ShPGFRcFontsFontProfile`.
    * **serif_font** (*Optional**[**str**]*) – See `ShPGFRcFontsFontProfile`.
    * **sans_serif_font** (*Optional**[**str**]*) – See `ShPGFRcFontsFontProfile`.
    * **monospace_font** (*Optional**[**str**]*) – See `ShPGFRcFontsFontProfile`.
    * **dpi** (*Union**[**float**, **str**]*) – See `ShPresentationScaleProfile`.
    * **\*\*rc_extra** – `rcParams` overrides.



### shplot.profiles.builtin.CUD_PALETTE(_ = ['#000000', '#e69f00', '#56b4e9', '#009e73', '#f0e442', '#0072b2', '#d55e00', '#cc79a7']_ )
Color Universal Design (CUD) palette.

See <[https://jfly.uni-koeln.de/color/](https://jfly.uni-koeln.de/color/)>.


### _class_ shplot.profiles.builtin.ShLightCUDProfile()
Bases: [`ColorProfile`](shplot.profiles.md#shplot.profiles.ColorProfile)

Black on white color profile with CUD palette.


### _class_ shplot.profiles.builtin.BSLightCUDProfile()
Bases: [`ColorProfile`](shplot.profiles.md#shplot.profiles.ColorProfile)

Bootstrap light theme color profile with CUD palette.


### _class_ shplot.profiles.builtin.BSDarkCUDProfile()
Bases: [`ColorProfile`](shplot.profiles.md#shplot.profiles.ColorProfile)

Bootstrap dark theme color profile with CUD palette.


### _class_ shplot.profiles.builtin.ShScaleProfile(fs, fs_small, fs_smaller, fs_large, marker_size, line_width, full_width_in)
Bases: [`PlotScaleProfile`](shplot.profiles.md#shplot.profiles.PlotScaleProfile)

Builder for scale profiles.


* **Parameters**


    * **fs** (*float*) – Base font size (in points).
    * **fs_small** (*float*) – Small font size (in points).
    * **fs_smaller** (*float*) – Smaller font size (in points).
    * **fs_large** (*float*) – Large font size (in points).
    * **marker_size** (*float*) – Default marker size (in points).
    * **line_width** (*float*) – Default line width (in points).
    * **full_width_in** (*float*) – Default figure width (in inches).



### _class_ shplot.profiles.builtin.ShPaperScaleProfile()
Bases: [`ShScaleProfile`](#shplot.profiles.builtin.ShScaleProfile)

Scale profile for a 10pt document.

Font sizes correspond to relative LaTeX font sizes for 10pt
documents:


* normalsize: 10pt
* small: 9pt
* footnotesize: 8pt
* large: 12pt


### _class_ shplot.profiles.builtin.ShBookScaleProfile()
Bases: [`ShScaleProfile`](#shplot.profiles.builtin.ShScaleProfile)

Scale profile for a 12pt document.

Font sizes correspond to relative LaTeX font sizes for 12pt
documents:


* normalsize: 12pt
* small: 10.95pt
* footnotesize: 10pt
* large: 14.4pt


### _class_ shplot.profiles.builtin.ShWebScaleProfile()
Bases: `_ShWebScaleProfile`

Scale profile for display on the web.

Sizes are for a 16px font size at 96dpi (CSS reference px).


### _class_ shplot.profiles.builtin.ShPresentationScaleProfile(dpi)
Bases: `_ShWebScaleProfile`

Scale profile for presentations.

Sizes are based on a 48px font size, and will be scaled based on
dpi.


* **Parameters**

    **dpi** (*float*) – Scale for converting pixel sizes to points.



### _class_ shplot.profiles.builtin.ShFontsetupFontProfile(font='default')
Bases: [`FontProfile`](shplot.profiles.md#shplot.profiles.FontProfile)

LaTeX font profile using the `fontsetup` package.

See <[https://www.ctan.org/pkg/fontsetup](https://www.ctan.org/pkg/fontsetup)> for details on the package.
This profile simply sets the latex preamble to load the package with
the given font.


* **Parameters**

    **font** (*FontType*) – One of the fonts supported by `fontsetup`. This value is
    passed as the sole argument to the package.



#### FontType()
alias of `Literal`[‘default’, ‘olddefault’, ‘cambria’, ‘concrete’, ‘ebgaramond’, ‘erewhon’, ‘euler’, ‘fira’, ‘gfsartemisia’, ‘gfsdidotclassic’, ‘gfsdidot’, ‘kekris’, ‘libertinus’, ‘lucida’, ‘minion’, ‘msgaramond’, ‘neoeuler’, ‘oldstandard’, ‘palatino’, ‘stixtwo’, ‘talos’, ‘times’, ‘xcharter’]


### _class_ shplot.profiles.builtin.ShPGFRcFontsFontProfile(family='serif', base_font='default', serif=None, sans_serif=None, monospace=None)
Bases: [`FontProfile`](shplot.profiles.md#shplot.profiles.FontProfile)

LaTeX font profile combining `fontsetup` with system fonts.

This profile loads the `fontsetup` package with the given font as in
`ShFontsetupFontProfile`, but also sets the `pgf.rcfonts` rcParam to
`True`, so that `matplotlib` will insert `fontspec` commands into
the LaTeX preamble to set `serif/sans-serif/monospace` fonts.


* **Parameters**


    * **family** (*List**[**str**]*) – Default font family.
    * **base_font** (*ShFontsetupFontProfile.FontType*) – One of the fonts supported by `fontsetup`. This value
    is passed as the sole argument to the package.
    * **serif** (*List**[**str**]*) – Override for serif font. If `None`, `font.serif` from
    `rcParams` will be used.
    * **sans_serif** (*List**[**str**]*) – Override for sans-serif font. If `None`,
    `font.sans-serif` from `rcParams` will be used.
    * **monospace** (*List**[**str**]*) – Override for monospace font. If `None`,
    `font.monospace` from `rcParams` will be used.
