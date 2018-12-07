import tweepy 
from textblob import TextBlob
consumer_key = "OlXJYelDKuz7Zr9BX6xYbAAgq" 
consumer_secret = "XcF9uDM1ne2BgeFyCX1pvIWzUBtDAL9d8t9QuxbySvZg1qSuEd"
access_key = "2202669843-LQCwOPE7Idoc7aDLajrWy5r3hGQ62PpfAE94mtk"
access_secret = "UCQLivdu341a4bKj9EdWUM8ItOjwxX21fNdcxgplibta1"
cn=0
cp=0
cnu=0
def sent(se):
	global cp,cn,cnu
	if se>0:
		cp+=1
		return " Positive "
	elif se==0:
		cnu+=1
		return " Neutral "
	else:
		cn+=1
		return " Negetive "

username="FIFAcom"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_key, access_secret) 
api = tweepy.API(auth) 
number_of_tweets=10
tweets = api.user_timeline(screen_name=username) 
tmp=[]  
tweets_for_csv = [tweet.text for tweet in tweets] 
for j in tweets_for_csv: 
	tmp.append(j)  
for i in tmp:
	ti=TextBlob(i)
	se=ti.sentiment.polarity
	print i," :::: Review ",sent(se) 
print "\nPositive : ",cp,"\nNegetive : ",cn,"\nNeutral :",cnu

