# Maze Solver
from gui_graphics import Window, Line, Point, CATPPUCCIN


def main():
    # Create a window with specified dimensions
    window = Window(800, 600)

    # Draw some lines on the window
    line1 = Line(Point(100, 100), Point(200, 200))
    line2 = Line(Point(200, 100), Point(100, 200))
    line3 = Line(Point(300, 100), Point(400, 200))
    line4 = Line(Point(400, 100), Point(300, 200))
    window.draw_line(line1, CATPPUCCIN["path"])
    window.draw_line(line2, CATPPUCCIN["wall"])
    window.draw_line(line3, CATPPUCCIN["highlight"])
    window.draw_line(line4, CATPPUCCIN["start"])

    # Start the event loop to keep the window open
    window.wait_for_close()


if __name__ == "__main__":
    main()
# This is the main entry point for the Maze Solver application.
# It initializes the window and starts the event loop.
# The window will remain open until the user closes it.
