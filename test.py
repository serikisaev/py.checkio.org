from datetime import datetime, timedelta

# count = 0.25
# print(type(count))
# for i in range(719):
#     count += 0.25
#     print(count)
# current_time = time(16, 00, 25)
# print("{}:{}".format(current_time.hour, current_time.minute))

# from datetime import datetime, timedelta
#
# clock_in_half_hour = dt = datetime.strptime("01/01/01 07:30", "%d/%m/%y %H:%M") + timedelta(minutes=30)
# print('{}:{}'.format(clock_in_half_hour.hour, clock_in_half_hour.minute))
# print(clock_in_half_hour.hour)
# for i in range(12):
#     for j in range(59):
#         print(i, j)
time = "07:01"
count = 0
d = {}
for i in range(721):

    # print(count)
    today = (datetime(2017, 3, 5, 6, 00, 00) + timedelta(minutes=i)).strftime("%H:%M")
    d[today]=count
    count += 0.25
    # print(today.strftime("%H:%M"))  # 2017-04-05-00.18.00
print(d)
if time in d:
    print(d[time])
else:
    print("I don't see the sun!")