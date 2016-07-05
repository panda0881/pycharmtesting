import csv

my_file_path = 'C:/User/user/PycharmProjects/pycharmtesting/csv_testing.csvNew'

# myfile = open(myfilepath, 'a', newline='') # 使用append模式打开文件
# mywriter = csv.writer(myfile)
# mywriter.writerow((3, 'wang', 25)) # 加入一行
# mywriter.writerow((4, 'zhou', 38))
# mywriter.writerows([[5, 'zhao', 16],[6, 'qian', 28]]) # 加入多行
# myfile.close()

field_names = ['Related_layer', 'Username', 'link']
my_file = open('Instagram_data.csv', 'w')
my_writer = csv.writer(my_file)
my_writer.writerow(field_names)
my_writer.writerow(['5', 'haha', 'www.testoi.com'])
my_file.close()
