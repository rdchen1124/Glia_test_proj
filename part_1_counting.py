urls = ["http://www.google.com/a.txt","http://www.google.com.tw/a.txt","http://www.google.com/download/c.jpg","http://www.google.co.jp/a.txt","http://www.google.com/b.txt","https://facebook.com/movie/b.txt","http://yahoo.com/123/000/c.jpg","http://gliacloud.com/haha.png"]
file_names = [ url.split("/")[-1] for url in urls]
file_dict = {}
for file in file_names:
	if file not in file_dict:
		file_dict[file]=1
	else:
		file_dict[file]+=1
sort_file = [[key, file_dict[key]] for key in sorted(file_dict, key=file_dict.get, reverse=True)]
for i in sort_file[:3]:
	print(i[0]+" "+str(i[1]))
# print(sort_file[:3])
