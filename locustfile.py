from locust import HttpUser, task


class LoadTesting(HttpUser):
    @task
    def hello_world(self):
        self.client.post("/api/v1/hello", json={})

    @task
    def vinted_search(self):
        self.client.post("/api/v1/vinted/search", json={"search_text": "string","per_page": 2})
