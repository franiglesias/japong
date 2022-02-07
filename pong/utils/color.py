def inc_byte(byte, pct):
    """increments byte by percentage"""
    if byte == 0:
        return (pct * 255) / 100

    byte += byte * pct / 100

    return min(byte, 255)


def dec_byte(byte, pct):
    """decrements byte by percentage"""
    byte -= byte * pct / 100

    return max(byte, 0)


def darken(color, pct):
    """darks a color by percentage"""
    return dec_byte(color[0], pct), dec_byte(color[1], pct), dec_byte(color[2], pct)


def lighten(color, pct):
    """lights a color by percentage"""
    return inc_byte(color[0], pct), inc_byte(color[1], pct), inc_byte(color[2], pct)
