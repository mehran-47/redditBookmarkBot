#!/usr/bin/env python3
import praw, json, sys

if __name__ == '__main__':
	class SavedLinkProcessor(praw.Reddit):
		def __init__(self, authentiCationDictionary):
			super(praw.Reddit, self).__init__()
			redditbot = praw.Reddit(**authentiCationDictionary)
			self.redditor = redditbot.redditor(authentiCationDictionary['username'])

		def processNtalk(self, limit=None):
			self.savedLinksGen = self.redditor.saved(**{'limit':limit})
			print([x.permalink for x in self.savedLinksGen])

	if sys.argv[1:]:
		with open(sys.argv[1]) as f: auth = json.loads(f.read())
		'''
		redditbot = praw.Reddit(**auth)
		print(redditbot.user.me())
		savedLinks = [x for x in redditbot.redditor('prometheus_47').saved(**{'limit':5})]
		print(savedLinks)
		print(len(savedLinks))
		print('http://www.reddit.com'+savedLinks[0].permalink)
		#savedLinks[0].unsave()
		#print(savedLinks[0].unsave)
		
		#print(dir(savedLinks[0]))
		#prometheus = praw.models.Redditor(redditbot, name='prometheus_47')
		#print(prometheus.saved(**{'sort':"new", 'time':"all", 'limit':10}))
		#submissions = [asub for asub in redditbot.get('/user/'+auth['username']+'/saved')]
		#print(submissions[-1].permalink)
		'''
		sp = SavedLinkProcessor(auth)
		print(dir(sp.redditor))