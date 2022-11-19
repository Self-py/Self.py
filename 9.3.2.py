def my_mp4_playlist(file_path, new_song):
	fid = open(file_path, "r")
	lines = fid.readlines()
	fid.close()
	if len(lines) >= 3:
		lines[2] = new_song + lines[2][lines[2].find(';'):]
	else:
		for n in range(2 - len(lines)):
			lines.append("\n")
		lines.append(new_song + ";")
	text = ''
	for i in range(len(lines)):
		text = text + lines[i]
	print(text)