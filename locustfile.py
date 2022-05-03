from locust import HttpUser, task


class LoadTesting(HttpUser):

    @task
    def vinted_search(self):
        self.client.get("/api/v1/vinted/items", params={"search_text": "string","per_page": 2})

    @task
    def vc_search(self):
        self.client.get("/api/v1/vestiaire/items", params={"search_text": "string", "per_page": 2})

    @task
    def all_search(self):
        self.client.get("/api/v1/all_markets/items", params={"search_text": "string", "per_page": 2, "marketplaces": ["VINTED", "VC"]})
