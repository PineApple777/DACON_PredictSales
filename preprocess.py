# -*- coding: utf-8 -*-

import os
import sys

import csv

path_list = ['datas\\train\\train.csv',
			'datas\\test\\test.csv',
			'datas\\submission.csv']

def get_data(filename, encoding='utf-8'):
	f = open(filename, 'r', encoding=encoding)
	rdr = csv.reader(f)
	data_list = []
	for line in rdr:
		data_list.append({line[0]: line[1:]})
	data_name = data_list.pop(0)	
	return data_list, data_name

if __name__ == "__main__":
	for path in path_list:
		data_list, data_name = get_data(path)
		print("FILENAME : %s" % path)

		id = list(data_name.keys())[0]
		names = list(data_name.values())[0]
		print("[%s]" % id, end=' ')
		for name in names:
			print("%-10s " % name, end='|')
		print("")

		for data in data_list:
			did = list(data.keys())[0]
			infos = list(data.values())[0]
			print("[%s]" % did, end=' ')
			for info in infos:
				print("%-10s " % info, end='|')
			print("")