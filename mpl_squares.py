import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_values,squares,linewidth=5)
#设置曲线的宽度
#plt.plot(squares, linewidth=5)
#plt.plot(squares)
#设置图表标题，并给出坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
#设置图标x,y轴标题
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize=14)

#设置度标记大小
plt.tick_params(axis='both',labelsize=14)

plt.show()