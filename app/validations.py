import math


def validate_address(lat:float,long:float):
    res = True
    if not math.isfinite(lat) or abs(lat) > 90:
        res = False
    if not math.isfinite(lat) and abs(long) > 180:
        res = False
    
    return res
