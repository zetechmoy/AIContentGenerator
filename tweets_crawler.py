import tweepy, time

def getTweets(api, screen_name, limit=200):
	new_tweets = api.user_timeline(screen_name = screen_name, count=limit, tweet_mode="extended")
	tweets = [tweet.full_text for tweet in new_tweets]
	return tweets

def normalize(tweets):
	for i in range(0, len(tweets)):
		if tweets[i].startswith("RT "):
			tweets[i] = tweets[i][3:]
			spl = tweets[i].split(": ")
			spl.pop(0)
			tweets[i] = ": ".join(spl)

		if "http" in tweets[i]:
			tweets[i] = tweets[i][:tweets[i].index("http")]

		if "=&gt;" in tweets[i]:
			tweets[i] = tweets[i].replace(" =&gt; ", "")

	return tweets

#tweets = ['RT @Korben: RD 974 entre Dijon et Beaune : les conducteurs doivent changer de vitesse toutes les 45 secondes ! - France 3 Bourgogne-Franche…', "14 comparaisons de célébrités qui ont le même âge, mais vous ne l'auriez jamais soupçonné #âge #célébrités #actualité #technologie #retweet =&gt; https://t.co/eIX51hNdu5", 'Guide de Noël : Les 10 meilleures BD de l’année qui méritent toute votre attention ... #noël #guide #attention #actualité #technologie #retweet =&gt; https://t.co/shUtO2ddwg', 'RT @JournalDuGeek: [Bon Plan] La PlayStation 4 à 185 euros + 30 euros remboursés en Superpoints  chez Rakuten ! https://t.co/9KalqvJvUT htt…', '# Levée de fonds : Foodvisor lève 1 million d’euros #levée #fonds #actualité #technologie #retweet =&gt; https://t.co/SbmLYHnqy9']


auth = tweepy.OAuthHandler("WRHgIe6KHjnrF8TNVIwbpAjw1", "IcvizAhCEcPpWh2UT5sDNL0wkT6dJZnJIzEUAT12a9IwVTHa2L")
auth.set_access_token("1010869406187118595-qphR2rb5jTeMGbeTQEMvxBsKUvGB6d", "89KGyj6q2RDPubwnnad4n7Gd0yCeTfrjpPo3ekhIy3YBw")

api = tweepy.API(auth)

screen_names = ["StartupActusFr", "Laure_Tubiana", "StartupStud_io", "sintreg_helene", "creativ_group_", "Startup365_fr", "LeVillagebyCA", "agreenstartup", "SIVAL_ANGERS", "SamsysFr", "will_agri", "pampaas_ag", "Farm_Connexion", "AgriStartSumm"]
screen_names = ["OrangeFabFr", "Digitaly_FR", "wiseed", "radenkovic_fr", "Bpifrance", "PEPITE_centre", "bymaddyness"]
tweets = []
for screen_name in screen_names:
	print("Getting tweets from "+screen_name)
	tweets = tweets = getTweets(api, screen_name)
	time.sleep(10)

tweets = normalize(tweets)

file = open("output_tweet.data", "a")
file.seek(0)
file.truncate(0)
for tweet in tweets:
	file.write(tweet+'\n')
file.close()
