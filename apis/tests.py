from rest_framework.test import APITestCase


class BasicTest(APITestCase):
    def test_add_get_drinks(self):
        data = {
            "name": "tea",
            "description": "milk drink"}

        # post / add drink
        self.client.post("/drinks/", data)

        # get api to fetch the drinks
        response = self.client.get("/drinks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["name"], "tea")
        self.assertEqual(response.json()[0]["description"], "milk drink")