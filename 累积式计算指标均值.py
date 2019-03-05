# -*- coding: utf-8 -*-
# @Time     : 2019/3/5 17:47
# @Author   : Junee
# @FileName: 先绘制月份表.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import csv
import sys

PATH = sys.path[0]
in_data = []
with open(PATH + '/5km_2.csv','r') as infile:
    reader = csv.reader(infile)
    for each in reader:
        in_data.append(each)
# print(in_data)

time_info = {}
rate_info = {}
price_info = {}
star_info = {}
data = []
# 201707-201812
with open(PATH + '/jiudian_rate.csv','r') as infile:
    reader = csv.reader(infile)
    for each in reader:
        time_info[each[0]] = each[4]
        rate_info[each[0]] = each[2]
        price_info[each[0]] = each[1]
        star_info[each[0]] = each[3]
        if each[4] not in data:
            data.append(each[4])

data.sort()

res = []
for each in in_data:
    temp = {}
    for each_date in data:
        temp[ each_date ] = []
    for each_id in each[1:]:
        each_id = each_id.strip()
        if each_id in time_info.keys():
            temp[time_info[each_id]].append(each_id)
        else:
            pass
    res.append(temp)



# print(res)
# 评分均值
# i = 0
# for dict_ in res:
#     for key,value in dict_.items():
#         sum_ = 0
#         count = 0
#         for each_id_ in value:
#             sum_ += float(rate_info[each_id_])
#             count += 1
#         if count != 0:
#             mean = sum_ / count
#             if mean == 0:
#                 dict_[key] = [0,0,0]
#             else:
#                 dict_[key] = [sum_,mean,count] # 均值+数量
#         else:
#             dict_[key] = [0,0,0]
#     i += 1
# res_list = []
# for dict_ in res:
#     temp = [ ]
#     for value in dict_.values():
#         temp.append(value)
#     res_list.append(temp)
#
# # print(res_list)
# # 修改成累积式
# for each_data in res_list:
#     sum_sum = 0
#     count_sum = 0
#     for i in range(len(each_data)):
#         if each_data[i][0] == 0:
#             if sum_sum == 0:
#                 each_data[i] = 0
#             else:
#                 each_data[i] = sum_sum/count_sum
#         else:
#             sum_sum += each_data[i][0]
#             count_sum += each_data[i][2]
#             each_data[i] = sum_sum/count_sum

    # 永远不会累计成功的代码，笑哭
    # for i in range(len(each_data)):
    #     if each_data[i][0] == 0:
    #         if sum_sum == 0:
    #             each_data[i] = ''
    #         else:
    #             each_data[i] = sum_sum / count_sum
    #             print('累计成功1')
    #     else:
    #         if sum_sum == 0:  ——>问题出在这里，这里的if第一次进去之后，没有累计该点的sum，
#         导致sum_sum 一直是零，笑哭，应该加上sum_sum += each_data[i][1]，然后你就会发现，
#         这个二级条件下面做的事情是一样的，所以此处不需要二级条件了，见正确代码部分
    #            each_data[i] = each_data[i][1]
    #         else:
    #             sum_sum += each_data[i][0]
    #             count_sum += each_data[i][2]
    #             each_data[i] = sum_sum/count_sum
    #             print('累计成功2')

#价格均值
i = 0
for dict_ in res:
    for key,value in dict_.items():
        sum_ = 0
        count = 0
        for each_id_ in value:
            sum_ += float(star_info[each_id_])
            count += 1
        if count != 0:
            mean = sum_ / count
            if mean == 0:
                dict_[key] = [0,0,0]
            else:
                dict_[key] = [sum_,mean,count] # 均值+数量
        else:
            dict_[key] = [0,0,0]
    i += 1
res_list = []
for dict_ in res:
    temp = [ ]
    for value in dict_.values():
        temp.append(value)
    res_list.append(temp)

# print(res_list)
# 修改成累积式
for each_data in res_list:
    sum_sum = 0
    count_sum = 0
    for i in range(len(each_data)):
        if each_data[i][0] == 0:
            if sum_sum == 0:
                each_data[i] = 0
            else:
                each_data[i] = sum_sum/count_sum
        else:
            sum_sum += each_data[i][0]
            count_sum += each_data[i][2]
            each_data[i] = sum_sum/count_sum
with open(PATH + '/5km_mean_star.csv','w',newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(data)
    for each in res_list:
        writer.writerow(each)


# 项目思考，一开始的思路比较乱，又要匹配时间，又要匹配id，后来模型化之后，
# 现将id按照时间分块，再在每一个块下面求均值