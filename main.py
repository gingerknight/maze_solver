# Maze Solver
from gui_graphics import Window


def main():
    # Create a window with specified dimensions
    window = Window(800, 600)

    # Start the event loop to keep the window open
    window.wait_for_close()


if __name__ == "__main__":
    main()
# This is the main entry point for the Maze Solver application.
# It initializes the window and starts the event loop.
# The window will remain open until the user closes it.
