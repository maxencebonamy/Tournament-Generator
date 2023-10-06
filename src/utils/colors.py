LIGHT_COLORS = [
    "EF9A9A",
    "F48FB1",
    "E1BEE7",
    "B388FF",
    "64B5F6",
    "00BCD4",
    "80CBC4",
    "1DE9B6",
    "81C784",
    "00C853",
    "76FF03",
    "FFEB3B",
    "FF9E80",
    "BCAAA4",
    "B0BEC5",
    "9E9D24"
]

DARK_COLORS = [
    "F44336",
    "E91E63",
    "880E4F",
    "9C27B0",
    "4A148C",
    "651FFF",
    "0D47A1",
    "006064",
    "009688",
    "4CAF50",
    "F57F17",
    "FF6F00",
    "BF360C",
    "795548",
    "607D8B"
]

def get_light_color(index: int) -> str:
    if index >= len(LIGHT_COLORS):
        return "FFFFFF"
    return LIGHT_COLORS[index]

def get_dark_color(index: int) -> str:
    if index >= len(DARK_COLORS):
        return "000000"
    return DARK_COLORS[index]