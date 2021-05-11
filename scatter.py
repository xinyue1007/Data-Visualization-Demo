import matplotlib.pyplot as plt

#1 针对相应的x,y坐标绘制一个点
#plt.scatter(2,4)
#2 s表示绘制点的尺寸
#plt.scatter(2,4,s=200)

#3 绘制一系列的坐标点
#x_values = [1,2,3,4,5]
#y_values = [1,4,9,16,25]
#plt.scatter(x_values,y_values,s=100)

#4 自动计算数据，关闭3
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

#plt.scatter(x_values,y_values,s=40)
#删除数据点的轮廓
#plt.scatter(x_values,y_values,edgecolors='none',s=40)
#自定义颜色
#plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)
#plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='none',s=40)

#使用颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)

#设置图表标题，并给出坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
#设置图标x,y轴标题
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置度标记大小
plt.tick_params(axis='both',which='major',labelsize=14)

#4 自动计算数据，关闭3
#设置每个坐标轴的取值范围  为x（0，1100） y（0，1100000）
plt.axis([0,1100,0,1100000])

#显示图表
#plt.show()
#自动保存图表此时需要关闭显示函数，不让保存的图片将为空白
plt.savefig('squares_plot.png',bbox_inches='tight')