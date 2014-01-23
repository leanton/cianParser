import re

def testTransportation(transportation):
	if type(transportation) is str:
		time = re.search(u'\d+', transportation)
		auto = re.search(u'авто', transportation)
		foot = re.search(u'пешком', transportation)
		if time and auto:
			time = int(time)
			d = {}
			d['auto'] = time
			return d
		elif time and foot:
			time = int(time)
			d = {}
			d['foot'] = time
			return d
		else:
			return "error"




"3мин. на автомобиле"	