length = int(input())
width = int(input())
height = int(input())
percent = int(input())
volume_tank = length * width * height
volume_liters = volume_tank / 1000
occupied_space = volume_liters * (percent / 100)
liters_required = volume_liters - occupied_space
print(liters_required)
