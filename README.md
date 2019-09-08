# BCGDV Intern Submission - Python Solution

Another React.js solution can be seen at [BCGDV Intern Submission - React.js Solution](https://github.com/szymonyang/BCGDV_Intern_submission_React)

### A Simple GET and POST Python Client

---

Implement `GET` method with Python `Requests` library. `r.json()` decode JSON object and return a dictionary. The dictionary contains a key and expire time.

```Python
api_url_base = "https://interns.bcgdvsydney.com"
r = requests.get(api_url_base + "/api/v1/key")
content = r.json()
print(content)
# {'key': 'd593e905-e534-4f2f-9073-6495fd4b1003', 'expires': '2019-08-07 07:09:35.802400'}
```

Implement `POST` method.  Message body should be encoded into JSON object before submission. Otherwise, submission will not be accepted.

```Python
key = content.get("key")
contact = {"name": "Jianwen (Simon) Yang", "email": "jianwen.yeung@gmail.com"}
payload = {"apiKey": key}
r = requests.post(api_url_base + "/api/v1/submit", params=payload, data=json.dumps(contact))

