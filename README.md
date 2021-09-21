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
If you want to change default config settings, look `docker-compose.yml`, `Docker`, `config/.env`. <br>

Set defaunt config.
```shell 
cp config/env config/.env
```

Then run:
```shell
chmod +x run.sh
./run.sh 
```

## Testing
So, before testing service should be run. <br>
If you changed some config data (in `docker-compose.yml` or `Docker` or `config/.env`) check out `testing/main.py`.
```shell
chmod +x testing.sh
./testing.sh
```


## Improvement
- Use connection pools to reduce request time (at the moment i don't understand how to create global pool object, i don't fully understand how to work with asynchrony in python). Probably [solution](https://dev.to/sethmlarson/the-problem-with-flask-async-views-and-async-globals-pl)

## License
[MIT](https://github.com/lusm554/document-text-search-engine/blob/main/LICENSE)

