import re


def validate_address(lat:float,long:float):
    pattern = "^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"

    res = True
    if not re.match(pattern,lat):
        res = False
    if not re.match(pattern,long):
        res = False
    
    return res
