import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def dict_to_Pie(data_dict, type_array):
    data_show =[]
    data_type_show = []
    originkeys = data_dict.keys()
    for key in type_array:
        if key in originkeys:
            data_show.append(data_dict[key])
            data_type_show.append(key)
        else:
            continue

    plt.pie(data_show,explode=None,labels=data_type_show)
    fig, ax = plt.subplots(figsize = (6,3), subplot_kw=dict(aspect = "equal"))

    wedges, textss = plt.pie(data_show,wedgeprops=dict(width = 0.5),startangle= -40)

    bbox_pros = dict(boxstyle = "square,pad = 0.3", fc = 'w',ec = "k",lw = 0.72)
    kw =dict(arrowprops = dict(arrowstyle = "-"),bbox = bbox_pros, zorder = 0,va ="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2-p.theta1)/2.+p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        plt.annotate(data_type_show[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),horizontalalignment=horizontalalignment, **kw)

    plt.title("Pie graph")
    plt.show()

data = {'1':123,'2':2345,'3':2342,'4':444,'5':555}
type_show =['1','3','5']

dict_to_Pie(data,type_show)