# shplot.profiles.builtin module


### shplot.profiles.builtin.SH_BUILTIN_PROFILES(_ = {'book': <class 'shplot.profiles.builtin.ShBookProfile'>, 'paper': <class 'shplot.profiles.builtin.ShPaperProfile'>, 'presentation': <class 'shplot.profiles.builtin.ShPresentationProfile'>, 'web_dark': <function <lambda>>, 'web_light': <function <lambda>>}_ )
Built-in plotting profiles with set values for different contexts.


### _class_ shplot.profiles.builtin.ShPaperProfile(font='default', \*\*rc_extra)
Profile for generating figures for a paper (10pt).


* **Parameters**


    * **font** – Name of the font to use–see `ShFontsetupFontProfile`.
    * **\*\*rc_extra** – `rcParams` overrides.



### _class_ shplot.profiles.builtin.ShBookProfile(font='default', \*\*rc_extra)
Profile for generating figures for a book (12pt).


* **Parameters**


    * **font** – Name of the font to use–see `ShFontsetupFontProfile`.
    * **\*\*rc_extra** – `rcParams` overrides.



### _class_ shplot.profiles.builtin.ShWebProfile(theme, font_family='sans-serif', sans_serif_font=None, serif_font=None, monospace_font=None, cursive_font=None, fantasy_font=None, math_font=None, \*\*rc_extra)
Profile for generating figures for the web.


* **Parameters**


    * **theme** – Color theme–‘light’ will generate figures on a light background,
    and ‘dark’ will generate figures on a dark background.
    * **font_family** – Default font family.
    * **sans_serif_font** – Optional override for the default sans-serif font.
    * **serif_font** – Optional override for the default serif font.
    * **monospace_font** – Optional override for the default monospace font.
    * **cursive_font** – Optional override for the default cursive font.
    * **fantasy_font** – Optional override for the default fantasy font.
    * **math_font** – Optional override for the default math font.
    * **\*\*rc_extra** – `rcParams` overrides.



### _class_ shplot.profiles.builtin.ShPresentationProfile(font_family='sans-serif', base_font='default', serif_font=None, sans_serif_font=None, monospace_font=None, dpi=200.0, \*\*rc_extra)
Profile for generating figures for presentations.


* **Parameters**


    * **font_family** – Default font family.
    * **\*_font** – See `ShPGFRcFontsFontProfile`.
    * **dpi** – See `ShPresentationScaleProfile`.
    * **\*\*rc_extra** – `rcParams` overrides.



### shplot.profiles.builtin.CUD_PALETTE(_ = ['#000000', '#e69f00', '#56b4e9', '#009e73', '#f0e442', '#0072b2', '#d55e00', '#cc79a7']_ )
Color Universal Design (CUD) palette.

See <[https://jfly.uni-koeln.de/color/](https://jfly.uni-koeln.de/color/)>.


### _class_ shplot.profiles.builtin.ShLightCUDProfile()
Black on white color profile with CUD palette.


### _class_ shplot.profiles.builtin.BSLightCUDProfile()
Bootstrap light theme color profile with CUD palette.


### _class_ shplot.profiles.builtin.BSDarkCUDProfile()
Bootstrap dark theme color profile with CUD palette.


### _class_ shplot.profiles.builtin.ShScaleProfile(fs, fs_small, fs_smaller, fs_large, marker_size, line_width, full_width_in)
Builder for scale profiles.


* **Parameters**


    * **fs/fs_\*** – Font sizes (in points) for different elements.
    * **marker_size** – Default marker size (in points).
    * **line_width** – Default line width (in points).
    * **full_width_in** – Default figure width (in inches).



### _class_ shplot.profiles.builtin.ShPaperScaleProfile()
Scale profile for a 10pt document.

Font sizes correspond to relative LaTeX font sizes for 10pt documents:


* normalsize: 10pt
* small: 9pt
* footnotesize: 8pt
* large: 12pt


### _class_ shplot.profiles.builtin.ShBookScaleProfile()
Scale profile for a 12pt document.

Font sizes correspond to relative LaTeX font sizes for 12pt documents:


* normalsize: 12pt
* small: 10.95pt
* footnotesize: 10pt
* large: 14.4pt


### _class_ shplot.profiles.builtin.ShWebScaleProfile()
Scale profile for display on the web.

Sizes are for a 16px font size at 96dpi (CSS reference px).


### _class_ shplot.profiles.builtin.ShPresentationScaleProfile(dpi)
Scale profile for presentations.

Sizes are based on a 48px font size, and will be scaled based on dpi.


* **Parameters**

    **dpi** – Scale for converting pixel sizes to points.



### _class_ shplot.profiles.builtin.ShFontsetupFontProfile(font='default')
LaTeX font profile using the `fontsetup` package.

See <[https://www.ctan.org/pkg/fontsetup](https://www.ctan.org/pkg/fontsetup)> for details on the package.
This profile simply sets the latex preamble to load the package with the
given font.


* **Parameters**

    **font** – One of the fonts supported by `fontsetup`. This value is
    passed as the sole argument to the package.



### _class_ shplot.profiles.builtin.ShPGFRcFontsFontProfile(family='serif', base_font='default', serif=None, sans_serif=None, monospace=None)
LaTeX font profile combining `fontsetup` with system fonts.

This profile loads the `fontsetup` package with the given font as in
`ShFontsetupFontProfile`, but also sets the `pgf.rcfonts` rcParam to
`True`, so that `matplotlib` will insert `fontspec` commands into the
LaTeX preamble to set `serif/sans-serif/monospace` fonts.


* **Parameters**


    * **family** – Default font family.
    * **base_font** – One of the fonts supported by `fontsetup`. This value is
    passed as the sole argument to the package.
    * **serif/sans_serif/monospace** – Overrides for serif/sans-serif/monospace
    families. If `None`, values from `rcParams` (`font.serif` etc.)
    will be used.
