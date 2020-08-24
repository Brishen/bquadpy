import ndim
import numpy
import pytest
from helpers import check_degree, find_best_scheme
from matplotlib import pyplot as plt

import quadpy


@pytest.mark.parametrize("scheme", quadpy.s3.schemes.values())
def test_scheme(scheme):
    scheme = scheme()

    assert scheme.points.dtype == numpy.float64, scheme.name
    assert scheme.weights.dtype == numpy.float64, scheme.name

    print(scheme)

    degree, err = check_degree(
        lambda poly: scheme.integrate(poly, [0.0, 0.0, 0.0], 1.0),
        ndim.nball.integrate_monomial,
        3,
        scheme.degree + 1,
        tol=scheme.test_tolerance,
    )
    assert (
        degree >= scheme.degree
    ), "{} -- observed: {}, expected: {} (max err: {:.3e})".format(
        scheme.name, degree, scheme.degree, err
    )


@pytest.mark.parametrize("scheme", [quadpy.s3.schemes["hammer_stroud_11_3"]()])
def test_show(scheme, backend="mpl"):
    scheme.show(backend=backend)
    plt.close()


def test_get_good_scheme():
    degree = 0
    while True:
        best = find_best_scheme(
            quadpy.s3.schemes.values(),
            degree,
            lambda pts: numpy.all((pts[0] ** 2 + pts[1] ** 2 + pts[2] ** 2 <= 1)),
            lambda keys: len(
                keys - set(["zero3", "symm_r00", "symm_rr0", "symm_rrr", "symm_rrs"])
            )
            == 0,
        )
        if best is None:
            break

        # print(degree, best.name)
        b = quadpy.s3.get_good_scheme(degree)
        assert best.name == b.name, f"{best.name} != {b.name}"
        degree += 1

    # assert degree == 12


if __name__ == "__main__":
    test_get_good_scheme()
