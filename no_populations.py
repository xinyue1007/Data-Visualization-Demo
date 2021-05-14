import pygal_maps_world.maps

#在世界地图上呈现数字数据
wm = pygal_maps_world.maps.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca':3412600, 'us':309349000, 'mx':113423000})

wm.render_to_file('na_populations.svg')