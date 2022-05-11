def scrape_movie_cast(movie_cast_url):
	m_url = movie_cast_url[:37]
	file_name = m_url[-10:-1] + '_cast' '.json'
	#checking if file exists or not
	value = os.path.exists('cast_cache/' + file_name)
	#if file exists
	if value == True:
		json_data = open('cast_cache/' + str(file_name)).read()
		data = json.loads(json_data)
		return data
	#if file dose not exists
	else:#create file
		url = movie_cast_url
		# sec = random.randint(1,3)
		raw = requests.get(url)
		soup = bs4.BeautifulSoup(raw.text, 'html.parser')
		json_data = raw.text
		# time.sleep(sec)
		#Writing data to json file
		table_data= soup.find('table' , class_ = 'cast_list')
		actors = table_data.findAll('td', class_ = "")
		cast_list = []
		for actor in actors:
			actor_dict = {}
			imdb_id = actor.find('a').get('href')[6:15]
			name = actor.getText().strip()
			actor_dict['imdb_id'] = str(imdb_id)
			actor_dict['name'] = str(name)
			cast_list.append(actor_dict.copy())
		json_data = cast_list[:]
		with open('cast_cache/' + str(file_name),'w+') as file:
			json.dump(json_data,file)
	return cast_list
print()