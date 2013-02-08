import sys, png, array, math, json, time

with open('sensors.json', 'r') as f:
	sensor_info = json.load(f)
with open('data.json', 'r') as f:
	sensor_data = json.load(f)

width = 112
height = 77

data = [[],[],[],[]]
for k in sensor_info.keys():
	x = int((sensor_info[k]['x']/800.0) * 112)
	y = int((sensor_info[k]['y']/550.0) * 77)
	temp = sensor_data[k]
	floor = sensor_info[k]['level']
	data[floor - 1].append([x, y, temp, floor])

def createHeatmap(sensor_data):
	p = 2
	data = []
	for f in range(len(sensor_data)):
		floor = []
		for i in range(height):
			pixel_row = []
			for j in range(width):
				# add pixel value here
				numerator = 0
				denominator = 0
				on_sensor = False
				for sensor in sensor_data[f]:
					distance = math.sqrt((j - sensor[0])**2 + (i - sensor[1])**2)**p

					if distance:
						numerator += float(sensor[2]) / distance
						denominator += 1 / distance
					else:
						numerator = 0
						denominator = 1
						temp = sensor[2]
						on_sensor = True
				if not on_sensor:
					temp = numerator / denominator
				pixel_row += temp2rgb(temp)
			floor.append(tuple(pixel_row))
		data.append(floor)
	return data


def temp2rgb(temp):

	min_temp = 18.0
	max_temp = 28.0
	min_hue = 0
	max_hue = 240

	if (temp < min_temp):
		temp = min_temp
	elif (temp > max_temp):
		temp = max_temp

	temp_percent = (temp - min_temp)/ (max_temp - min_temp)
	hue = max_hue - (min_hue + temp_percent * max_hue)
	
	h = math.floor(hue/60.0);

	if (h == 0 ):
		r = 1
		g = hue/60.0
		b = 0
	elif (h == 1):
		r = 1 - (hue - 60)/60.0
		g = 1
		b = 0
	elif (h == 2):
		r = 0
		g = 1
		b = (hue - 120)/60.0
	elif (h == 3):
		r = 0
		g = 1 - (hue - 180)/60.0
		b = 1
	elif (h == 4):
		r = 0
		g = 0
		b = 1

	return [round(r* 255), round(g * 255), round(b * 255)]



sensors = [
	[(35, 50, 18.0), (110, 50, 18.0), (35, 190, 18.0), (110, 190, 28.0)],
	[(35, 50, 27.7), (110, 50, 24.0), (35, 190, 18.0), (110, 190, 24.0)],
	[(35, 50, 26.1), (110, 50, 22.2), (35, 190, 21.0), (110, 190, 23.2)],
	[(20, 20, 18.0), (50, 50, 26.0), (500, 500, 23.0), (200, 300, 28.0)]
]

floor_data = createHeatmap(data)


for floor in range(len(data)):
	floor_no = str(floor + 1)
	f = open('floor' + floor_no + '.png', 'wb')
	w = png.Writer(width, height)
	w.write(f, floor_data[floor])
	f.close()
time.sleep(5)











