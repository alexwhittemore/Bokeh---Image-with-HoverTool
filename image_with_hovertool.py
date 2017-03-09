import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, BoxSelectTool
from bokeh.models.sources import ColumnDataSource
import bokeh

def val_to_color(val_range, val, color_pallete):
    """
    range: [low, high]
    val: value to map in range
    color_pallette: array of colors
    """
    length = len(color_pallete)
    index = int(round(np.interp(val, val_range, [0, length-1])))
    return color_pallete[index]

def plot_with_hovertool(array_to_plot, colors=None, plot_as_circles=False, zero_index=False, flip_vert=True):
    """ Plots a numpy array as an image, with HoverTool.

    array_to_plot: numpy array
    colors: array of hex color strings
    plot_as_circles: True to plot circle glyphs instead
    zero_index: True to index the image at 0 instead of 1.
    flip_vert: True will take input matrix y=0 as the TOP row,
        as one often does rendering an image.

    Bokeh supports plotting arrays as images out of the box, however
    there's no support for adding a HoverTool over these, if, say, you'd
    like to view pixel values, or additional data represented by a pixel
    This fuction will plot an arbitrary array with a HoverTool displaying
    coordinates and value.

    This should also give you a good starting point to customize additional
    data display.
    """

    if colors is None:
        #color_pallete = bokeh.palettes.gray(256)
        color_pallete = bokeh.palettes.inferno(256)
    else:
        color_pallete = colors

    (dims_y, dims_x) = array_to_plot.shape

    # Get the x-indicies of the array
    x_index_vec = np.arange(0, dims_x, 1)
    y_index_vec = np.arange(0, dims_y, 1)
    if flip_vert:
        y_index_vec = np.flipud(y_index_vec)

    if not zero_index:
        x_index_vec = x_index_vec+1
        y_index_vec = y_index_vec+1

    # Make arrays of index coordinates
    xx, yy = np.meshgrid(x_index_vec, y_index_vec)

    # Calculate the range of highest value to lowest of the data to plot:
    val_range = [np.amin(array_to_plot), np.amax(array_to_plot)]

    # We've got a scalar function above to map a value to a color, make a vector
    # version of that for our specific values array
    color_mapper = np.vectorize(lambda val:\
                                val_to_color(val_range, val, color_pallete))

    # Then make an array the same size as the values array, but of
    # corresponding colors
    color_array = color_mapper(array_to_plot)

    # Reshape the matricies into (x*y)-long lists for the dictionary
    x,y = array_to_plot.shape
    x_coords = np.reshape(xx, [1, x*y])[0]
    y_coords = np.reshape(yy, [1, x*y])[0]
    values = np.reshape(array_to_plot, [1, x*y])[0]
    colors = np.reshape(color_array, [1, x*y])[0]

    source = ColumnDataSource(
        data=dict(
            x_coord=x_coords,
            y_coord=y_coords,
            value=values,
            color=colors,
        )
    )

    output_file("toolbar.html")
    TOOLS = [BoxSelectTool(), HoverTool()]

    p = figure(plot_width=600, plot_height=600, title=None, tools=TOOLS)

    if plot_as_circles:
        p.circle("x_coord", "y_coord", radius=.5, color="color", source=source, line_color="black")
    else:
        p.rect("x_coord", "y_coord", width=1, height=1, color="color", source=source)

    p.select_one(HoverTool).tooltips = [
        ("X", "@x_coord"),
        ("Y", "@y_coord"),
        ("Value", "@value"),
    ]


    show(p)
