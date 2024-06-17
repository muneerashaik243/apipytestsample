import requests


class TestPytestMultiEnvDemo:

    def test_validate_fact_about_cat(self, target_env):
        host = target_env["host"]
        get_api = target_env["getCatFacts"]
        response_exptd = target_env["factResponse"]
        # send request
        response = requests.get(host+get_api)
        jsondata = response.json()
        facts_resp_actual = jsondata.get('data')
        # assert
        assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)
        assert facts_resp_actual[0] == response_exptd,"Fact Returned is not as Expected"


    def test_validate_cat_breed(self, target_env):
        host = target_env["host"]
        get_api = target_env["getCatBreed"]
        response_exptd = target_env["breedResponse"]
        # send request
        response = requests.get(host+get_api)
        jsondata = response.json()
        breed_resp_actual = jsondata.get('data')
        # assert
        assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)
        assert breed_resp_actual[0] == response_exptd,"Breed Returned is not as Expected"


    def test_validate_random_fact(self, target_env):
        host = target_env["host"]
        get_api = target_env["getRandomFact"]
        response_exptd = target_env["factResponse"]
        # send request
        response = requests.get(host+get_api)
        jsondata = response.json()
        # assert
        assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)
        assert isinstance(jsondata.get('fact'),str),"Random Fact is empty"
        assert jsondata.get('length') > 0, "'jsondata' is empty"
