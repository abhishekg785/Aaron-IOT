# watson api
# to handle the user sentiment
import json
from watson_developer_cloud import ToneAnalyzerV3
from config import WATSON_API


class WatsonAPI:

	def __init__(self):
		print 'inside the Watson Api cons'
		self.tone_analyzer = ToneAnalyzerV3(
    		username = WATSON_API.TONE_ANALYZER_USERNAME,
    		password = WATSON_API.TONE_ANALYZER_PASSWORD,
    		version='2016-05-19 ')

	def tone_analyzer_api(self, query_text):
		print json.dumps(self.tone_analyzer.tone(text = query_text), indent=2)

	def natural_language_api(self):
		pass

