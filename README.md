# Document text search engine

## Documentation
* [About](#about)
* [How to run](#how-to-run)
* [Testing](#testing)
* [What can be improved here?](#improvement)
* [License](#license)

## About
A simple search engine for document texts. The data is stored in a database, the search index is in elastic.

### **Database structure:**
* `id` – unique identifier for every doc;
* `rubrics` – array of headings;
* `text` – text of the doc;
* `created_date` – doc creation date.

### **Index structure:**
* `id` – identifier from db;
* `text` – text from db structure.

### **Methods:**
* the service must accept an arbitrary text request as input, search for the document text in the index and return the first 20 documents with all database fields, sorted by creation date;
* delete doc from db and the index by `id` field.

### **Technical requirements:**
* `README` with deploy guide;
* `docs.json` - service docs in openapi format.

### **If u wanna tryhard:**
- [X] functional testing;
- [X] service runs in Docker;
- [X] asynchronous API calls.

## How to run 
If you want to change default config settings, look `docker-compose.yml`, `Docker`, `config/.env`. Default dataset stores in `config posts.csv`, and config in `config/env`. <br>

Clone service.
```shell
git clone https://github.com/lusm554/document-text-search-engine.git
```

Set default config.
```shell 
cp config/env config/.env
```

Run service:
```shell
chmod +x run.sh
./run.sh 
```
The service will start in about 2 minutes (due to importing data from postgres to elasticsearch), so run tests after the server API is ready. You can check this in the docker logs or just `curl localhost` (for the default config).

## Testing
As mentioned above, the service must be ready before testing. <br>
If you changed some config data in `docker-compose.yml` or `Docker` or `config/.env` check out `testing/main.py`. Make sure you have `requests` and `pytest` installed or just `pip install requests pytest`.
```shell
chmod +x testing.sh
./testing.sh
```

## Improvement
My thoughts on what can be improved in this service:
- Use connection pools to reduce request time (at the moment i don't understand how to create global pool object, i don't fully understand how to work with asynchrony in python). Probably [solution](https://dev.to/sethmlarson/the-problem-with-flask-async-views-and-async-globals-pl).
- Probably use nginx for high concurrency.
- Use production server able to communicate with Flask through a WSGI protocol.
- Optimized task queues to manage long-running jobs, like search documents by arbitrary text.
- How find error? Logging.

## License
[MIT](https://github.com/lusm554/document-text-search-engine/blob/main/LICENSE)

