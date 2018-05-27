#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : tags_outputer.py

import xlwt;

class TagsOutputer(object):
    def output_tags(self, tags):
	workBook = xlwt.Workbook();
	workSheet = workBook.add_sheet("tags");

	workSheet.write(0, 0, "tagName");
	workSheet.write(0, 1, "blogNumber");
	i = 1;
	for tag in tags:
	    workSheet.write(i, 0, tag["tagName"]);
	    workSheet.write(i, 1, tag["blogNumber"]);
	    i = i + 1;
	workBook.save("tags.xls");
	
		 