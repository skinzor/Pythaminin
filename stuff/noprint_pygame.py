from io import StringIO
from contextlib import redirect_stdout

with redirect_stdout(StringIO()):
    import pygame
