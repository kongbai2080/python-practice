dic = {'int': 'zhen xing',
	'float': 'fu dian xing',
	'char': 'zi fu xing',
	'unsigned int': 'wu fu hao zhen xing',
	'unsigned char': 'wu fu hao zi fu xing',
	'for': 'xun huan',
	'if': 'tiao jian',
	'lie biao': '2wei zi fu shu zu+zhen xing shu zu+fu dian xing shu zu',
	'yuan zu': 'lei lie biao',
	'zi dian': 'jie gou ti',
	}
print("int: " + dic['int']) 
print("float: "+ dic['float']) 
print("char: " + dic['char']) 
print("unsigned int: " + dic['unsigned int']) 
print("unsigned cahr: " + dic['unsigned char'])
print("\n")

print("int: " + dic['int'] +  
	"\nfloat: "+ dic['float'] +  
	"\nchar: " + dic['char'] +
	"\nunsigned int: " + dic['unsigned int'] +  
	"\nunsigned cahr: " + dic['unsigned char']
	)
print("\n")

for k,v in dic.items():
	print(k + ": " + v)
