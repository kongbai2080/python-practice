rivers = {'nile':'egypt',
	'changjiang':'china',
	'huanghe':'china',
	}
for r,c in rivers.items():
	print("The " + r.title() + " runs through " + c.title())

for r in rivers.keys():
	print(r)

for c in rivers.values():
	print(c)
