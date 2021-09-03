import random
lst = [{'1': '2'}, {'3':'4'}, {'5': '6'}]
obj = lst[random.randint(0, 2)].get('1')
print(obj)