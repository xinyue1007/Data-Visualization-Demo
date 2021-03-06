import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个RandWalk实例，并将其包含的点都绘制出来
#rw =RandomWalk()
#rw.fill_walk()
#plt.scatter(rw.x_values,rw.y_values,s=15)
#splt.show()

#模拟多次随机漫步
#只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    #plt.plot(rw.x_values, rw.y_values,linewidth=5)

    #突出起点与终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴这种方法不可用，不生效
    #current_axes = plt.axes()
    #current_axes.get_xaxis().set_visible(False)
    #current_axes.get_yaxis().set_visible(False)
    #隐藏坐标轴这种方法可用，生效
    plt.axis('off')
    # 隐藏坐标轴这种方法可用，生效，与off有些许区别
    #current_axes = plt.gca()
    #current_axes.axes.get_yaxis().set_visible(False)
    #current_axes.axes.get_xaxis().set_visible(False)


    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break