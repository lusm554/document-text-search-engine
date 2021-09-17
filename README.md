# Document text search engine

## Documentation
* [About](#about)
* [How to run](#how-to-run)
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
Set variables in `config/.env`. Example of dotenv in the same dir - `config/env`. <br>
For example: set `CSV_FILE_URL` to link of the test dataset.

Then run:
```shell
chmod +x run.sh
./run.sh 
```
## License
[MIT](https://github.com/lusm554/document-text-search-engine/blob/main/LICENSE)

