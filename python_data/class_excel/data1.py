#!/usr/bin/env python
# -*- coding: utf-8 -*-
values = [3139486695, 3139486696, 3139486697, 3139486698, 3139486699, 3139486700, 3139486701, 3139486702]
key = ["QuestionId"]
# data = {
#     list2:[x.__dict__ for x in list1]
# }
# print(data)
result = []
for v in values:
    item = { "QuestionId": v, "AnswerDuration":10,"Options":"C"}
    result.append(item)

res = {"Answers": result}

print(res)