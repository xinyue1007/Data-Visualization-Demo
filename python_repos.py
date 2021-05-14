import requests

import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code:",r.status_code)

#将API响应存储在一个变量中
respone_dict = r.json()

print("Total repositories:",respone_dict['total_count'])

#探索有关仓库的信息
repo_dicts = respone_dict['items']
print("Repositories returned:", len(repo_dicts))
#处理结果
print(respone_dict.keys())

#研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
   print('\nName:', repo_dict['name'])
   print('Owner:', repo_dict['owner']['login'])
   print('Stars:', repo_dict['stargazers_count'])
   print('Repository:', repo_dict['html_url'])
   print('Description:', repo_dict['description'])

#for key in sorted(repo_dict.keys()):
#    print(key)


#names,stars = [],[]
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

#可视化
my_style = LCS()

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.major_label_font_size = 18

#较长的项目名缩短为15个字符
my_config.truncate_label = 15
#以隐藏图表中的水平线
my_config.show_y_guides = False
#设置了自定义宽度
my_config.width = 1000

#chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

#chart.add('',stars)
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')