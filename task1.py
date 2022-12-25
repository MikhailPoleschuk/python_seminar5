string = 'Я люблю Джавуабв абви Питон'
print(''.join([f'{item} ' for item in string.split() if item.find('абв') == -1]))