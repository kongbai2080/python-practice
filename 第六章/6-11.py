cities = {'guangzhou':{'country':'China','population':'10000000',
	'fact':'wuyang'},
	'huizhou':{'country':'China','population':'2000000',
	'fact':'sushi'},
	'dongguan':{'country':'China','population':'5000000',
	'fact':'saohuang'},
	}
for name,informations in cities.items():
	print(name + ":\t")
	for key,value in informations.items():
		print(key + ":" + value)
	print('\n')
