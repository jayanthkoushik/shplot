# shplot

shplot is a Python library wrapper for managing Matplotlib configuration
through profiles, and provides a number of built-in profiles suitable
for different use cases.

## Installation

shplot is available on PyPI, and can be installed with `pip`:

```sh
pip install shplot
```

## Usage

Common use cases are shown here. For in-depth documentation, refer to
the doc files inside `docs/`, or visit the project website at <https://jkoushik.me/shplot>.
`demos/` contains illustrations of the different built-in profiles.

### Create a plot and use it in a context

<!-- cSpell: disable -->

```pycon
>>> from shplot import ShPlot
>>> plot = ShPlot(builtin_profile_name="paper")
>>> with plot.context(nrows=2, ncols=2) as (fig, axs):
...     # `axs` is a 2x2 array.
...     pass
>>> with plot.context(mosaic="AAB\nC.B") as (fig, axs):
...     # `axs` is a dictionary.
...     pass

```

<!-- cSpell: enable -->

### Update Matplotlib settings using a profile

```pycon
>>> from shplot.profiles import ColorProfile
>>> profile = ColorProfile(fg="yellow", bg="black")
>>> profile.config()  # will update `matplotlib.rcParams`

```

### Use a built-in profile with overrides

```pycon
>>> from shplot import ShPlot
>>> from shplot.profiles.builtin import ShPaperProfile
>>> profile = ShPaperProfile(fontname="fira", **{"axes.grid": True})
>>> profile.config()

```

### Create a plot using command line arguments

**`main.py`**

```python
from shplot import ShPlot

plot = ShPlot.parse_from_cmdline()
with plot.context() as (fig, ax):
    ...
```

```
$ python main.py -h
usage: main.py [-h] [--file str] [--shprofile str] [--profile-args key=val,...] [--width
  float] [--aspect float[;float]]

options:
  -h/--help                   show this help message and exit
  --file str                  Plot save file (extension will be added if not provided).
                              (optional)
  --shprofile str             Name of a built-in profile.
                              ({paper/book/web_light/web_dark/presentation} optional)
  --profile-args key=val,...  Arguments for the builtin-profile. Refer to the individual
                              profiles for details. (optional)
  --width float               Plot width, in inches (if greater than 1), or as a fraction of
                              the configured plot width (if less than or equal to 1).
                              (optional)
  --aspect float[;float]      Plot aspect ratio, width/height. When provided as a command
                              line argument, can be passed as a single number or a ratio in
                              the form `<WIDTH>;<HEIGHT>`. (optional)
```
