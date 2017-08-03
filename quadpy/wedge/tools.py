# -*- coding: utf-8 -*-
#
import numpy

from . import felippa
from .. import helpers


def integrate(f, wedge, scheme, sumfun=helpers.kahan_sum):
    x = _transform(scheme.points.T, wedge)
    det = _get_detJ(scheme.points.T, wedge)
    return sumfun(scheme.weights * f(x) * abs(det), axis=-1)


def _transform(xi, wedge):
    mo = numpy.multiply.outer
    return (
        + mo(0.5 * (1.0-xi[0]-xi[1]) * (1.0-xi[2]), wedge[0])
        + mo(0.5 * xi[0] * (1.0-xi[2]), wedge[1])
        + mo(0.5 * xi[1] * (1.0-xi[2]), wedge[2])
        + mo(0.5 * (1.0-xi[0]-xi[1]) * (1.0+xi[2]), wedge[3])
        + mo(0.5 * xi[0] * (1.0+xi[2]), wedge[4])
        + mo(0.5 * xi[1] * (1.0+xi[2]), wedge[5])
        ).T


def _get_detJ(xi, wedge):
    mo = numpy.multiply.outer
    J0 = (
        - mo(0.5*(1.0 - xi[2]), wedge[0])
        + mo(0.5*(1.0 - xi[2]), wedge[2])
        - mo(0.5*(1.0 + xi[2]), wedge[3])
        + mo(0.5*(1.0 + xi[2]), wedge[5])
        ).T
    J1 = (
        - mo(0.5*(1.0 - xi[2]), wedge[0])
        + mo(0.5*(1.0 - xi[2]), wedge[1])
        - mo(0.5*(1.0 + xi[2]), wedge[3])
        + mo(0.5*(1.0 + xi[2]), wedge[4])
        ).T
    J2 = (
        - mo(0.5 * (1.0-xi[0]-xi[1]), wedge[0])
        - mo(0.5 * xi[0], wedge[1])
        - mo(0.5 * xi[1], wedge[2])
        + mo(0.5 * (1.0-xi[0]-xi[1]), wedge[3])
        + mo(0.5 * xi[0], wedge[4])
        + mo(0.5 * xi[1], wedge[5])
        ).T
    det = (
        + J0[0]*J1[1]*J2[2] + J1[0]*J2[1]*J0[2] + J2[0]*J0[1]*J1[2]
        - J0[2]*J1[1]*J2[0] - J1[2]*J2[1]*J0[0] - J2[2]*J0[1]*J1[0]
        )
    return det


def show(
        scheme,
        wedge=numpy.array([
            [0, 0, 0], [1, 0, 0], [0, 1, 0],
            [0, 0, 1], [1, 0, 1], [0, 1, 1],
            ], dtype=float),
        backend='mpl'
        ):
    edges = numpy.array([
        [wedge[0], wedge[1]],
        [wedge[1], wedge[2]],
        [wedge[0], wedge[2]],
        #
        [wedge[3], wedge[4]],
        [wedge[4], wedge[5]],
        [wedge[5], wedge[3]],
        #
        [wedge[0], wedge[3]],
        [wedge[1], wedge[4]],
        [wedge[2], wedge[5]],
        ])
    edges = numpy.moveaxis(edges, 1, 2)

    helpers.backend_to_function[backend](
            _transform(scheme.points.T, wedge).T,
            scheme.weights,
            integrate(lambda x: numpy.ones(1), wedge, felippa.Felippa(1)),
            edges
            )
    return