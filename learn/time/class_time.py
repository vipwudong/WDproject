import  time

# print(time.asctime())
# print(time.time())
# #1607228839.720567
# #1607228870.176897
# print(time.localtime())
#
# print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))
#获取两天前现在的时间

now_time = time.time()
before = now_time - 60*60*24*2
print(time.localtime(before))
print(time.strftime("%Y-%m-%d %H:%m:%S", time.localtime(before)))