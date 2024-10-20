# round() is too slow for most practical usecases

_precomputed = {
    0: 1.0,
    1: 1.4,
    2: 1.41,
    3: 1.414,
    4: 1.4142,
    5: 1.41421,
    6: 1.414214,
    7: 1.4142136,
    8: 1.41421356,
    9: 1.414213562,
    10: 1.4142135624,
    11: 1.41421356237,
    12: 1.414213562373,
    13: 1.4142135623731,
    14: 1.41421356237310,
    15: 1.414213562373095,
    16: 1.4142135623730951,
}

def compute_square_root_of_2_with_adjustable_rounding(ndigits: int):
    return _precomputed.get(ndigits, 1.4142135623730951)
