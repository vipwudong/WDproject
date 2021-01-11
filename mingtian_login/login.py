dic = {"_api_app_type":11,"_api_app_version":9000000,"_api_device":2,"_api_key":"i4TSNuSOuVqfnjgIPhbM44AbRL7ivofR","_api_format":2}
dic1 = sorted(dic.items(),key=lambda item:item[0])
a  = (str(dic1))
url = "/v1/user.login"
print(type(dic1))

e  = ["_api_app_type=11,_api_app_version=9000000,_api_device=2,_api_key=i4TSNuSOuVqfnjgIPhbM44AbRL7ivofR,_api_format=2"]

b = str(list)
print(b.replace(",","&"))