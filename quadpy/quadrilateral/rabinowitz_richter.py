# -*- coding: utf-8 -*-
#
from .helpers import _symm_r_0, _symm_s, _symm_s_t, _z

from ..helpers import untangle


class RabinowitzRichter(object):
    """
    Philip Rabinowitz and Nira Richter,
    Perfectly Symmetric Two-Dimensional Integration Formulas with Minimal
    Numbers of Points,
    Mathematics of Computation, Vol. 23, No. 108 (Oct., 1969), pp. 765-779,
    <https://doi.org/10.2307/2004962>.
    """

    def __init__(self, index):
        self.name = "RabinowitzRichter({})".format(index)
        if index == 1:
            self.degree = 9
            data = [
                (0.0716134247098111, _symm_r_0(0.9845398119422523)),
                (0.4540903525515453, _symm_r_0(0.4888863428423724)),
                (0.0427846154667780, _symm_s(0.9395672874215217)),
                (0.2157558036359328, _symm_s_t(0.8367103250239890, 0.5073767736746132)),
            ]
        elif index == 2:
            self.degree = 11
            data = [
                (0.3653795255859022, _z()),
                (0.2442720577517539, _symm_r_0(0.7697990683966493)),
                (0.0277561655642043, _symm_r_0(1.044402915409813)),
                (0.3089930361337136, _symm_s(0.4134919534491139)),
                (0.0342651038512293, _symm_s(0.9357870124405403)),
                (0.1466843776513117, _symm_s_t(0.5756535958404649, 0.8830255085256902)),
            ]
        elif index == 3:
            self.degree = 11
            data = [
                (0.0176679598882646, _symm_r_0(0.8989737240828844)),
                (0.2322248008989674, _symm_r_0(0.7632367891419969)),
                (0.0715516745178401, _symm_s(0.8949648832822285)),
                (0.2192868905662522, _symm_s(0.6322452037101431)),
                (0.2965842326220580, _symm_s(0.2797353125538562)),
                (0.0813422207533089, _symm_s_t(0.9602661668053869, 0.4347413023856830)),
            ]
        elif index == 4:
            self.degree = 13
            data = [
                (0.2995235559387052, _z()),
                (0.0331100668669073, _symm_r_0(0.9909890363004588)),
                (0.1802214941550577, _symm_r_0(0.6283940712305196)),
                (0.0391672789603492, _symm_s(0.9194861553393097)),
                (0.1387748348777338, _symm_s(0.6973201917871096)),
                (0.2268881207335663, _symm_s(0.3805687186904865)),
                (0.0365739576550950, _symm_s_t(0.9708504361720127, 0.6390348393207334)),
                (0.1169047000557597, _symm_s_t(0.8623637916722844, 0.3162277660168378)),
            ]
        elif index == 5:
            self.degree = 15
            data = [
                (-0.40980941939297e-5, _symm_r_0(1.315797935069747)),
                (0.0414134647558384, _symm_r_0(0.9796158388578564)),
                (0.1837583771750436, _symm_r_0(0.6375456844500517)),
                (0.0280217865486269, _symm_s(0.9346799288936658)),
                (0.0948146979601645, _symm_s(0.7662665721615083)),
                (0.1688054053337613, _symm_s(0.5138362475917853)),
                (0.1898474000367674, _symm_s(0.2211895845055072)),
                (0.0331477474104121, _symm_s_t(0.9769495664551867, 0.6375975639376926)),
                (0.1135237357315838, _symm_s_t(0.8607803779721935, 0.3368688874716777)),
            ]
        else:
            assert index == 6
            self.degree = 15
            data = [
                (0.0301245207981210, _symm_r_0(0.9915377816777667)),
                (0.0871146840209092, _symm_r_0(0.8020163879230440)),
                (0.1250080294351494, _symm_r_0(0.5648674875232742)),
                (0.0267651407861666, _symm_s(0.9354392392539896)),
                (0.0959651863624437, _symm_s(0.7624563338825799)),
                (0.1750832998343375, _symm_s(0.2156164241427213)),
                (0.0283136372033274, _symm_s_t(0.9769662659711761, 0.6684480048977932)),
                (0.0866414716025093, _symm_s_t(0.8937128379503403, 0.3735205277617582)),
                (0.1150144605755996, _symm_s_t(0.6122485619312083, 0.4078983303613935)),
            ]

        self.points, self.weights = untangle(data)
        return
