import seaborn as sns
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
# plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# sns.set(font='SimHei')  # 解决Seaborn中文显示问题

sns.set(style="darkgrid", color_codes=True)
iris = sns.load_dataset('iris',data_home='seaborn-data',cache=True)
print(iris.head())
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

fig = sns.pairplot(iris,
kind = 'scatter', #散点图
diag_kind = 'hist', #直方图
hue = 'species', #按照某一字段分类
palette = 'husl', #设置颜色样式
markers = ['o', 's', 'D'], #设置点样式
height = 2 #图标大小
)

fig.savefig("scatter.jpg", dpi = 400)
plt.show()


