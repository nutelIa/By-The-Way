# from yelp.client import Client
# from yelp.oauth1_authenticator import Oauth1Authenticator


def get_search_params(lat, lon):
	params = {}
	params["term"] = "restaurant"
	params["ll"] = "{}, {}".format(str(lat), str(lon))
	params["radius filter"] = "8046.72"
	params["limit"] = "15"
	return params

def get_results(params):

	session = rauth.Oauth1Session(
	    consumer_key="YsB6W_am8jmyO-fcwf_1yw",
	    consumer_secret="J_RrmSf7Ky1j3FxfwF2h2u2gYng",
	    token="7ExwVC7C275qeQR8YgF9oSV2VPgyCxGO",
	    token_secret="8TPFCM4arIUM5ONyN92AT4bTegs"
	)
	request = session.get("http://api.yelp.com/v2/search")
	data = request.json()
	session.close()
	print(data)
	return data