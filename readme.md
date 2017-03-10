# Bokeh - Image with HoverTool
Functions to plot numpy arrays and single channel images with a Bokeh HoverTool to inspect pixel data.

See examples and function docstring for tips on how to use and modify to taste.

## Usage
Copy and paste the functions to taste. Alternately, you can check this project out into your overall project directory. If your project is already a git repository, you can use
```
git submodule add git@github.com:alexwhittemore/bokeh_im_hovertool.git
```
to clone the repo as a submodule. Then, inside your project,
```python
import bokeh_im_hovertool.image_with_hovertool as im_ht
im_ht.plot_with_hovertool(yourdata)
```


## Examples
![Rendered numpy array](/example_screenshots/random_t.png?raw=true "Rendered numpy array")
![Test image from file](/example_screenshots/image.png?raw=true "Image loaded from file with PIL")