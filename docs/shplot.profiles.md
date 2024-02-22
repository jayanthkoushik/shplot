# shplot.profiles package


### _class_ shplot.profiles.ProfileBase(\*\*args)
Base class for profiles.

Profile classes are thin wrappers around subsets of `matplotlib` parameters.
Once instantiated, they can be used to generate a dictionary which can be
used to update `matplotlib.rcParams`.

Profile classes have a dataclass-like interface. All attributes are exposed
as properties, and can be set either at initialization (as keyword arguments)
or later. Unless specified otherwise, attributes directly correspond to
`matplotlib` parameters with the same name.

### Examples

```python
>>> from shplot.profiles import ColorProfile
>>> profile = ColorProfile(fg_secondary="gray")
>>> profile.rc()
{'grid.color': 'gray', 'legend.edgecolor': 'gray'}
```

```python
>>> profile.grid_alpha = 0.5
>>> profile.rc()
{'grid.color': 'gray', 'legend.edgecolor': 'gray', 'grid.alpha': 0.5}
```


#### rc()
Return profile configuration as a `dict` of matplotlib `rcParams`.

Unset attributes are not included in the returned dictionary so that
different profiles can be combined together.


#### config(reload_mpl=True)
Update `matplotlib.rcParams` with profile configuration.


* **Parameters**

    **reload_mpl** – Whether to reload `matplotlib` and `pyplot` modules
    before applying the configuration. Reloading is necessary for
    fonts to be updated.


### Examples

```python
>>> import matplotlib as mpl
>>> print(mpl.rcParams["grid.color"])
#b0b0b0
>>> color_prof = ColorProfile(fg_secondary="gray")
>>> color_prof.config()
>>> print(mpl.rcParams["grid.color"])
gray
```


#### context(reload_mpl=True)
Context manager for `config` method.


* **Parameters**

    **reload_mpl** – Whether to first reload `matplotlib` and `pyplot` modules.


### Examples

```python
>>> mpl.rcParams["grid.color"] = 'black'
>>> print(mpl.rcParams["grid.color"])
black
>>> color_prof = ColorProfile(fg_secondary="red")
>>> with color_prof.context():
...     print(mpl.rcParams["grid.color"])
red
>>> print(mpl.rcParams["grid.color"])
black
```


### _class_ shplot.profiles.ColorProfile(\*\*args)
Wrapper for color-related matplotlib params.


#### palette()
`axes.prop_cycle` colors.


* **Type**

    List[str]



#### fg()
Primary foreground color, used for text, axes lines, ticks, etc.


* **Type**

    str



#### fg_secondary()
Secondary foreground color, used for grid lines and legend frame.


* **Type**

    str



#### bg()
Axes and figure face color.


* **Type**

    str



#### grid_alpha()

* **Type**

    float



#### legend_frame_alpha()

* **Type**

    float



#### transparent()
Whether to save figures with transparent background.


* **Type**

    bool



### _class_ shplot.profiles.FontProfile(\*\*args)
Wrapper for font-related matplotlib params.


#### family()

* **Type**

    List[str]



#### style()

* **Type**

    typing_extensions.Literal[normal, italic, oblique]



#### variant()

* **Type**

    typing_extensions.Literal[normal, small-caps]



#### weight()

* **Type**

    typing_extensions.Literal[normal, bold, bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800, 900]



#### stretch()

* **Type**

    typing_extensions.Literal[ultra-condensed, extra-condensed, condensed, semi-condensed, normal, semi-expanded, expanded, extra-expanded, ultra-expanded, wider, narrower]



#### serif()

* **Type**

    List[str]



#### sans_serif()

* **Type**

    List[str]



#### monospace()

* **Type**

    List[str]



#### cursive()

* **Type**

    List[str]



#### fantasy()

* **Type**

    List[str]



#### text_usetex()

* **Type**

    bool



#### latex_preamble()

* **Type**

    List[str]



#### math_fontset()

* **Type**

    typing_extensions.Literal[dejavusans, dejavuserif, cm, stix, stixsans, custom]



#### custom_math_rm()

* **Type**

    str



#### custom_math_sf()

* **Type**

    str



#### custom_math_tt()

* **Type**

    str



#### custom_math_it()

* **Type**

    str



#### custom_math_bf()

* **Type**

    str



#### custom_math_cal()

* **Type**

    str



#### math_fallback()

* **Type**

    typing_extensions.Literal[cm, stix, stixsans, None]



#### math_default()

* **Type**

    typing_extensions.Literal[rm, cal, it, tt, sf, bf, default, bb, frak, scr, regular]



#### pgf_rcfonts()

* **Type**

    bool



#### set_pgf_preamble()
Whether to set `pgf.preamble` using `latex_preamble`.


* **Type**

    bool



### _class_ shplot.profiles.PlotScaleProfile(\*\*args)
Wrapper for plot scale-related matplotlib params.


#### font_size()

* **Type**

    float



#### axes_title_size()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile.FloatOrStr](#shplot.profiles.PlotScaleProfile.FloatOrStr)



#### axes_label_size()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile.FloatOrStr](#shplot.profiles.PlotScaleProfile.FloatOrStr)



#### xtick_label_size()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile.FloatOrStr](#shplot.profiles.PlotScaleProfile.FloatOrStr)



#### ytick_label_size()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile.FloatOrStr](#shplot.profiles.PlotScaleProfile.FloatOrStr)



#### legend_font_size()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile.FloatOrStr](#shplot.profiles.PlotScaleProfile.FloatOrStr)



#### legend_title_size()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile.FloatOrStr](#shplot.profiles.PlotScaleProfile.FloatOrStr)



#### figure_title_size()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile.FloatOrStr](#shplot.profiles.PlotScaleProfile.FloatOrStr)



#### figure_label_size()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile.FloatOrStr](#shplot.profiles.PlotScaleProfile.FloatOrStr)



#### marker_size()

* **Type**

    float



#### line_width()

* **Type**

    float



#### full_width_in()
Default figure width in inches.


* **Type**

    float



#### default_aspect_wh()
Default figure aspect ratio (width/height).


* **Type**

    float



#### legend_marker_scale()

* **Type**

    float



#### subplot_left()

* **Type**

    float



#### subplot_right()

* **Type**

    float



#### subplot_bottom()

* **Type**

    float



#### subplot_top()

* **Type**

    float



#### subplot_hspace()

* **Type**

    float



#### subplot_wspace()

* **Type**

    float



#### autolayout()

* **Type**

    bool



#### constrained_layout()

* **Type**

    bool



#### constrained_layout_hspace()

* **Type**

    float



#### constrained_layout_wspace()

* **Type**

    float



#### _class_ FloatOrStr()
Float or string type.


### _class_ shplot.profiles.AxesProfile(\*\*args)
Wrapper for axes-related matplotlib params.


#### grid_axes()
Which axes to draw grid lines on.


* **Type**

    Set[typing_extensions.Literal[x, y]]



#### grid_lines()
Which grid lines to draw.


* **Type**

    Set[typing_extensions.Literal[major, minor]]



#### spines()
Which sides to draw spines on.


* **Type**

    Set[typing_extensions.Literal[left, right, bottom, top]]



#### xtick_major_lines()
Where to draw major x-axis tick lines.


* **Type**

    Set[typing_extensions.Literal[bottom, top]]



#### xtick_minor_lines()
Where to draw minor x-axis tick lines.


* **Type**

    Set[typing_extensions.Literal[bottom, top]]



#### xtick_labels()
Where to draw x-axis tick labels.


* **Type**

    Set[typing_extensions.Literal[bottom, top]]



#### xtick_direction()
Direction of x-axis ticks.


* **Type**

    typing_extensions.Literal[in, out, inout]



#### xtick_alignment()
Alignment of x-axis tick labels.


* **Type**

    typing_extensions.Literal[left, center, right]



#### xlabel_position()
Position of x-axis label.


* **Type**

    typing_extensions.Literal[left, center, right]



#### ytick_major_lines()
Where to draw major y-axis tick lines.


* **Type**

    Set[typing_extensions.Literal[left, right]]



#### ytick_minor_lines()
Where to draw minor y-axis tick lines.


* **Type**

    Set[typing_extensions.Literal[left, right]]



#### ytick_labels()
Where to draw y-axis tick labels.


* **Type**

    Set[typing_extensions.Literal[left, right]]



#### ytick_direction()
Direction of y-axis ticks.


* **Type**

    typing_extensions.Literal[in, out, inout]



#### ytick_alignment()
Alignment of y-axis tick labels.


* **Type**

    typing_extensions.Literal[bottom, center, top, baseline, center_baseline]



#### ylabel_position()
Position of y-axis label.


* **Type**

    typing_extensions.Literal[bottom, center, top]



### _class_ shplot.profiles.PlottingProfile(\*\*kwargs)
Wrapper for color, font, scale, and axes profiles.

All arguments for initialization are optional, and must be passed as keyword
arguments. Arguments other than `color`, `font`, `scale`, and `axes` are used to
update `matplotlib.rcParams` directly, and will override any values set by
the profile.


#### color()

* **Type**

    [shplot.profiles._interface.ColorProfile](#shplot.profiles.ColorProfile)



#### font()

* **Type**

    [shplot.profiles._interface.FontProfile](#shplot.profiles.FontProfile)



#### scale()

* **Type**

    [shplot.profiles._interface.PlotScaleProfile](#shplot.profiles.PlotScaleProfile)



#### axes()

* **Type**

    [shplot.profiles._interface.AxesProfile](#shplot.profiles.AxesProfile)


### Examples

```python
>>> from shplot.profiles import PlottingProfile, ColorProfile
>>> color_profile = ColorProfile(fg_secondary="gray")
>>> rc_extra = {"backend": "Agg", "legend.edgecolor": "darkgray"}
>>> profile = PlottingProfile(color=color_profile, **rc_extra)
>>> profile.rc()
{'grid.color': 'gray', 'legend.edgecolor': 'darkgray', 'backend': 'Agg'}
```

## Submodules


* [shplot.profiles.builtin module](shplot.profiles.builtin.md)


    * [`SH_BUILTIN_PROFILES`](shplot.profiles.builtin.md#shplot.profiles.builtin.SH_BUILTIN_PROFILES)
    * [`ShPaperProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShPaperProfile)
    * [`ShBookProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShBookProfile)
    * [`ShWebProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShWebProfile)
    * [`ShPresentationProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShPresentationProfile)
    * [`CUD_PALETTE`](shplot.profiles.builtin.md#shplot.profiles.builtin.CUD_PALETTE)
    * [`ShLightCUDProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShLightCUDProfile)
    * [`BSLightCUDProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.BSLightCUDProfile)
    * [`BSDarkCUDProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.BSDarkCUDProfile)
    * [`ShScaleProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShScaleProfile)
    * [`ShPaperScaleProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShPaperScaleProfile)
    * [`ShBookScaleProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShBookScaleProfile)
    * [`ShWebScaleProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShWebScaleProfile)
    * [`ShPresentationScaleProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShPresentationScaleProfile)
    * [`ShFontsetupFontProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShFontsetupFontProfile)
    * [`ShPGFRcFontsFontProfile`](shplot.profiles.builtin.md#shplot.profiles.builtin.ShPGFRcFontsFontProfile)
