#字典

alien_0 = {'color':'green','points':5}

#取值
points = alien_0['points']
print(points) #5

#添加键-值对

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)

#删除字典中的键-值对
del alien_0['color']
print(alien_0)
