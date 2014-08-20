import tweepy, operator, time

#Create txt file to store results
text_file = open("results.txt", "w")

#First parameter is Consumer Key, second is Consumer Secret 
auth = tweepy.OAuthHandler('', '')		# EMPTY
auth.set_access_token('', '')			# EMPTY    
api = tweepy.API(auth)

#Specify target user
target = api.get_user("EssexBladesSU")
text_file.write("***********\nTarget account name: %s\nTarget has %i followers\n***********\n" % (target.screen_name, target.followers_count))

#Save the target's list of followers
followers = api.followers_ids(id=target.screen_name)

#Create followers of followers dictionary
foff = {}
for i in range(len(followers)):
	time.sleep(5.1)				# avoids request limit violations
	foff[followers[i]] = api.get_user(id=followers[i]).followers_count
	if i % 10 == 0:	print "%i of %i followers analysed for 'most followed' analysis" % (i, len(followers)+1)	# keep track of analysis progress

#Find most followed
mostid = max(foff.iteritems(), key=operator.itemgetter(1))[0]
mostfollowed = api.get_user(id=mostid)
text_file.write("\n***********\n%s is the most followed user that follows the target \n%s has %i followers\n***********\n" % (mostfollowed.screen_name, mostfollowed.screen_name, max(foff.values())))

#Create activity dictionary
active = {}
for i in range(len(followers)):
	time.sleep(5.1)				# avoids request limit violations
	try:	# skip users with protected tweets
		temp = api.user_timeline(id=followers[i])
	except tweepy.error.TweepError: pass
	if len(temp) == 20:
		active[followers[i]] = temp[19].created_at
	if i % 10 == 0:	print "%i of %i followers analysed for 'most active' analysis" % (i, len(followers)+1)	# keep track of analysis progress

#Find most active
activeid = max(active.iteritems(), key=operator.itemgetter(1))[0]
mostactive = api.get_user(id=activeid)
text_file.write("\n***********\n%s is the most active user that follows the target \n(Measured as: 20 most recent tweets in the shortest time among users with at least 20 tweets) \n%s's 20th most recent tweet was published on: %s\n***********" % (mostactive.screen_name, mostactive.screen_name, max(active.values())))

text_file.close()

### The created txt file includes all the answers for the first-degree part of the questions
### I did not do the second-degree part due to the rate restrictions
### However, it would be relatively easy to implement by simply running the same code on the initially extracted list of followers' followers