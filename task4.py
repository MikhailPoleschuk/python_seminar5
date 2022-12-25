# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
file_path = r'task4_string.txt'
with open(file_path, 'w') as f_data:
    f_data.writelines('aqqqqfffqqqqqqqqeeweeeeerrrrdsfsdfffffffsssssv')

with open(file_path, 'r') as f_data:
    str = f_data.readline()

rle_string = ''
count = 1
print(len(str))
for i in range(1, len(str)):
    if str[i] == str[i-1] and i == len(str)-1:
        count += 1 
        rle_string = rle_string + f'{count}{str[i-1]}'
    elif str[i] == str[i-1]:
        count += 1 
    else:
        rle_string = rle_string + f'{count}{str[i-1]}'
        count = 1
    print(f"count= {count} i= {i}")

print(rle_string)


file_path_new = r'task4_RLE_string.txt'

with open(file_path_new, 'w') as f_data:
    f_data.writelines(rle_string)