import  yaml
yaml_data = yaml.safe_load(open("data3"))
print(yaml_data)
print(yaml_data['me'])
print(yaml_data['me']['power'])