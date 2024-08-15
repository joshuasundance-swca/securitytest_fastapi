# securitytest_fastapi
api key in header fastapi server/client

- `keys.py`
  - has `correct_key` and `incorrect_key` variables
  - used by `server.py` and `client.py`
- `server.py`
  - fastapi app ran with `uvicorn app:app --port 8081`
  - has a `/protected-endpoint` endpoint that requires a correct api key in the header
  - uses `keys.correct_key` to check the api key
- `client.py`
  - sends requests using correct and incorrect api key to `http://localhost:8081/protected-endpoint`
  - prints results

to use an api key in header for auth, use env vars or something instead of hardcoding :P
