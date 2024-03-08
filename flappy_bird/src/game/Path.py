from pathlib import Path

class Root():
    def __init__(self):
        self.ROOT = Path(__file__).parent.parent.parent
        self.DATA = self.ROOT / "data"
        self.ASSETS = self.DATA / "assets"
        self.FONT = self.DATA / "font"
        self.JSON = self.DATA / "json"
        self.SOUND = self.DATA / "sound"