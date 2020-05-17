# TODO give all weights in terms in scientific notation to avoid round-off error
import math

from ..helpers import article, pm, untangle
from ._helpers import S2Scheme

_source = article(
    authors=["Zhongxuan Luo", "Zhaoliang Meng"],
    title="Cubature formulas over the n-sphere",
    journal="Journal of Computational and Applied Mathematics",
    year="2007",
    volume="202",
    pages="511-522",
    url="https://doi.org/10.1016/j.cam.2006.03.004",
)


def luo_meng_1():
    data = [
        (0.26179938779915, pm([0.22985042169050, 0.39811260850906])),
        (0.26179938779915, pm([0.45970084338098, 0])),
        (0.19501407677793, pm([0.33703975180642, 0.82163211980611])),
        (0.19768500492079, pm([0.81932059025905, 0.34262064294548])),
    ]
    points, weights = untangle(data)
    weights /= math.pi
    return S2Scheme("Luo-Meng 1", weights, points, 7, _source, 3.820e-14)


def luo_meng_2():
    data = [
        (0.34906585039887, [[0, 0]]),
        (0.20125271332781, pm([0.22802635567696, 0.55050432045386])),
        (0.20125271332781, pm([0.55050432045386, 0.22802635567697])),
        (0.11661039976673, pm([0.27959387377058, 0.87565760433418])),
        (0.11891162535334, pm([0.73930517186176, 0.54623880962155])),
        (0.12020849804409, pm([0.91921106078980, 0])),
    ]
    points, weights = untangle(data)
    weights /= math.pi
    return S2Scheme("Luo-Meng 2", weights, points, 9, _source, 6.934e-14)


def luo_meng_3():
    data = [
        (0.10908307824965, pm([0.12847091799048, 0.31015623258278])),
        (0.10908307824965, pm([0.31015623258288, 0.12847091799023])),
        (0.13948043950767, pm([0.21825250754568, 0.67258147681156])),
        (0.13968230996014, pm([0.57180635899884, 0.41597774917474])),
        (0.13980620186210, pm([0.70710678118655, 0])),
        (0.07075156570176, pm([0.23655119019746, 0.91177950680902])),
        (0.07284300646890, pm([0.65590282776745, 0.67608417756031])),
        (0.07457158432863, pm([0.90808090973540, 0.25037451147207])),
    ]
    points, weights = untangle(data)
    weights /= math.pi
    return S2Scheme("Luo-Meng 3", weights, points, 11, _source, 3.859e-13)


def luo_meng_4():
    data = [
        (0.19634954084936, [[0, 0]]),
        (0.10330948998241, pm([0.46080422984078, 0])),
        (0.10330948998241, pm([0.14239633810068, 0.43825086552643])),
        (0.10330948998241, pm([0.37279845302107, 0.27085393049437])),
        (0.10130196428837, pm([0.19820177383648, 0.74246157638449])),
        (0.10163159176824, pm([0.54237877749285, 0.54438809436341])),
        (0.10195288141571, pm([0.74209383687325, 0.19957422888241])),
        (0.04772103677723, pm([0.20435671727372, 0.93255046651235])),
        (0.04919131994151, pm([0.58135727768706, 0.75725541012764])),
        (0.05064404906285, pm([0.85428875985589, 0.42614874782308])),
        (0.05118841995037, pm([0.95467902484934, 0])),
    ]
    points, weights = untangle(data)
    weights /= math.pi
    return S2Scheme("Luo-Meng 4", weights, points, 13, _source, 1.572e-13)


def luo_meng_5():
    data = [
        (0.05464091129997, pm([0.26349922998554, 0])),
        (0.05464091129997, pm([0.08142573996847, 0.25060265974957])),
        (0.05464091129997, pm([0.21317535496663, 0.15488096150859])),
        (0.08535187281584, pm([0.14865659379572, 0.55489701326339])),
        (0.08536560703414, pm([0.40617004422892, 0.40624545951758])),
        (0.08537932359881, pm([0.55488321130685, 0.14870810340184])),
        (0.07254080017264, pm([0.18047783326862, 0.79838479036808])),
        (0.07303155482639, pm([0.50739130020565, 0.64229634147179])),
        (0.07360272502709, pm([0.73617733529664, 0.35781762503817])),
        (0.07384344684536, pm([0.81852948743000, 0])),
        (0.03255139877430, pm([0.17885299875228, 0.94793447064359])),
        (0.03364947668306, pm([0.51771758964946, 0.81396354535359])),
        (0.03485759424523, pm([0.79062758601644, 0.55269899224337])),
        (0.03554380854735, pm([0.94452004763159, 0.19608680582601])),
    ]
    points, weights = untangle(data)
    weights /= math.pi
    return S2Scheme("Luo-Meng 5", weights, points, 15, _source, 3.339e-10)


# TODO find mistake
# def luo_meng_6():
#     data = [
#         (0.12566370614359, [[0, 0]]),
#         (0.05840846471928, pm([0.09675812994165, 0.36110625670843])),
#         (0.05840846471928, pm([0.26434812694957, 0.26434812676097])),
#         (0.05840846471928, pm([0.36110625674316, 0.09675812981205])),
#         (0.06992018223251, pm([0.14347639334166, 0.62914552544285])),
#         (0.06996062112205, pm([0.40212812179518, 0.50468063296759])),
#         (0.07001072267677, pm([0.58130075071609, 0.28017673859189])),
#         (0.07003290482486, pm([0.64529804558133, 0])),
#         (0.05451221994169, pm([0.16359877475730, 0.83450130452851])),
#         (0.05497050073244, pm([0.46782321680688, 0.71013972158889])),
#         (0.05555796700074, pm([0.70405774447146, 0.47692733074510])),
#         (0.05593580988433, pm([0.83361584135279, 0.16805241863048])),
#         (0.02373604417773, pm([0.15912091676987, 0.95790205017621])),
#         (0.02450554997213, pm([0.46530163489622, 0.85228527644703])),
#         (0.02542637441947, pm([0.72779904913934, 0.64280972920247])),
#         (0.02606318434828, pm([0.90714987061331, 0.34637395417630])),
#         (0.02628242756629, pm([0.97102821992230, 0])),
#     ]
#     points, weights = untangle(data)
#     weights /= math.pi
#     return S2Scheme("Luo-Meng 6", weights, points, 17, _source)


# TODO find error
# def luo_meng_7():
#     data = [
#         (0.62831853071796, [[0, 0]]),
#         (0.15739501981117, pm([0.22313923447538, 0.83276696021106])),
#         (0.15739501981117, pm([0.60962772574453, 0.60962772573512])),
#         (0.15739501981117, pm([0.83276696021278, 0.22313923446896])),
#         (0.04163923078518, pm([0.35648911914249, 1.56350584123606])),
#         (0.04166872260747, pm([0.99921385294824, 1.25427536200095])),
#         (0.04170520866795, pm([1.44454064039602, 0.69637442937729])),
#         (0.04172134401374, pm([1.60363181798263, 0])),
#         (0.00248954249688, pm([0.45703259734803, 2.34995743719975])),
#         (0.00252313408619, pm([1.31014474018574, 2.00367150787068])),
#         (0.00256386275246, pm([1.97776433468844, 1.34893550183970])),
#         (0.00258875098551, pm([2.34618078213053, 0.47604042816812])),
#         (1.709615741554363e-5, pm([0.45304937170440, 3.27851194591105])),
#         (2.053886363962915e-5, pm([1.44579291938731, 2.97717603559694])),
#         (2.222665327035189e-5, pm([2.39757845514132, 2.28155908626652])),
#         (2.292272152266965e-5, pm([3.06875713971016, 1.23960636097153])),
#         (2.312500019706606e-5, pm([3.30966679783376, 0])),
#     ]
#     points, weights = untangle(data)
#     weights /= math.pi
#     return S2Scheme("Luo-Meng 6", weights, points, 17, _source)
