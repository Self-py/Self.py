def my_mp3_playlist(file_path):
	fid = open(file_path, "r")
	lines = fid.readlines()
	fid.close()
	song_lengths, artist_count = {}, {}
	length = len(lines)
	for line in lines:
		line_list = line.split(';')
		song_lengths[line_list[0]] = line_list[2]
		if line_list[1] in artist_count.keys():
			artist_count[line_list[1]] = artist_count[line_list[1]] + 1
		else:
			artist_count[line_list[1]] = 1
	return max(song_lengths, key=song_lengths.get), length, max(artist_count, key=artist_count.get)