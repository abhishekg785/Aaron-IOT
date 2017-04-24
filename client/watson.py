# watson api
# to handle the user sentiment
import json
from watson_developer_cloud import ToneAnalyzerV3
from config import WATSON_API


class WatsonAPI:

	def __init__(self):
		print 'inside the Watson Api cons'
		try:
			self.tone_analyzer = ToneAnalyzerV3(
	    		username = WATSON_API.TONE_ANALYZER_USERNAME,
	    		password = WATSON_API.TONE_ANALYZER_PASSWORD,
	    		version='2016-05-19 ')
		except:
			print 'Internet connection error'


	def tone_analyzer_api(self, query_text):
		tone_name_arr = []
		tone_id_arr = []
		tone_score_arr = []
		fetched_data = json.dumps(self.tone_analyzer.tone(text = query_text), indent=3)
		fetched_json_data = json.loads(fetched_data)
		fetched_tones_json = fetched_json_data['document_tone']['tone_categories'][0]['tones']
		for tone in fetched_tones_json:
			tone_name = tone['tone_name']
			tone_score = tone['score']
			tone_id = tone['tone_id']
			tone_name_arr.append(tone_name)
			tone_score_arr.append(tone_score)
			tone_id_arr.append(tone_id)
		print tone_name_arr
		# print tone_score_arr
		max_tone_score = max(tone_score_arr)
		predicted_tone_index = tone_score_arr.index(max_tone_score)
		predicted_tone = tone_name_arr[predicted_tone_index]
		print predicted_tone
		return predicted_tone


	def natural_language_api(self):
		pass


	def test_arr():
		pass