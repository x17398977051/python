fruits = ['椰果', '蓝莓', '苹果', '菠萝']
# 复制列表(深复制) 同时省略开始索引和终止索引[:]
fruits_copy = fruits[:]

fruits.append('桔子')

print(f'源数组:\t{fruits}')
print(f'复制数组:\t{fruits_copy}')
