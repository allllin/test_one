import requests

url = "http://123.56.138.96:3012/api/ainews-user/company-group/delete"
params = {"id": 17225}
hedader = {
    "Content-Type": "application/json;charset=UTF-8",
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTgxLCJpYXQiOjE2MzcyMzkwNTR9.8iB7WqtfXKel63zrfsezZdmXt6kQjLpznaUvsQgKSis"
}
print(requests.get(url, params=params, headers=hedader).json())
