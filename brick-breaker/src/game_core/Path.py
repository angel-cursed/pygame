from pathlib import Path

class Dir():
    def __init__(self):
        self.ROOT = Path(__file__).parent.parent.parent
        self.DATA = self.ROOT / "data"
        self.SOUND = self.DATA / "sound"