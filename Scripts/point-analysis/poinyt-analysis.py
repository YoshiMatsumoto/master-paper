
class FirstAnalysis(object):
    import numpy
    import numba

    @numba.jit
    def np_within_circle(pt_x, pt_y, pt_center_x, pt_center_y, radius):
        if (pt_x - pt_center_x) ** 2 + (pt_y - pt_center_y) ** 2 < radius ** 2:
            return 1
        else:
            return 0