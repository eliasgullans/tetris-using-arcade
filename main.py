"""
Example "Arcade" library code.

This example shows the drawing primitives and how they are used.
It does not assume the programmer knows how to define functions or classes
yet.

API documentation for the draw commands can be found here:
https://api.arcade.academy/en/latest/quick_index.html

A video explaining this example can be found here:
https://vimeo.com/167158158

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.drawing_primitives
"""

# Import the Arcade library. If this fails, then try following the instructions
# for how to install arcade:
# https://api.arcade.academy/en/latest/install/index.html
import arcade

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Tetris v0.1")

# Set the background color to white
# For a list of named colors see
# https://api.arcade.academy/en/latest/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.
arcade.set_background_color(arcade.color.GRAY)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Draw a filled in rectangle
# arcade.draw_text("draw_filled_rect", 363, 3, arcade.color.BLACK, 10)
arcade.draw_rectangle_filled(100, 100, 15, 15, arcade.color.BLUSH)

# Finish the render.
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()


#def drawTetriminos():
