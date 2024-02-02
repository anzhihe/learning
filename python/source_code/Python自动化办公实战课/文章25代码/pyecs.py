import requests
import json
from pyecharts.charts import Map
from pyecharts import options as opts

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
data = requests.get(url)
alldata = json.loads(data.json()['data'])

chinadata = []
for province in alldata['areaTree'][0]['children']:
    provincedata = (
        province['name'],
        province['total']['nowConfirm']
    )
    chinadata.append(provincedata)

map_chart = Map()
map_chart.add(
        "全国确诊病例分布图",
        tuple(chinadata),
        "china",
        is_map_symbol_show=False
    )

map_chart.set_global_opts(
    title_opts=opts.TitleOpts(
        title=f"全国疫情地图( {alldata['lastUpdateTime']} )"),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            pieces=[
                {"min": 1, "max": 9, "label": "1-9人", "color": "#FFE6BE"},
                {"min": 10, "max": 99, "label": "10-99人", "color": "#FFB769"},
                {"min": 100, "max": 499, "label": "100-499人", "color": "#FF8F66"},
                {"min": 500, "max": 999, "label": "500-999人", "color": "#ED514E"},
                {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CA0D11"},
                {"min": 10000, "max": 100000, "label": "10000人以上", "color": "#A52A2A"}
            ]))

map_chart.render('covid19_map.html')


