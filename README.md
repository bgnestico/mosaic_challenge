# QA Challenge for Mosaic

## API Coding Challenge:
### Create a RESTful API that allows users to manage a collection of books.

***The API should have the following endpoints:***

- GET /books: Retrieve a list of all books
- GET /books/{id}: Retrieve details of a specific book
- POST /books: Create a new book
- PUT /books/{id}: Update details of a specific book
- DELETE /books/{id}: Delete a specific book

***The book object should have the following properties:***

- id: unique identifier for the book
- title: title of the book
- author: author of the book
- publication_date: publication date of the book


### Steps:

1. cd into project root: `cd Mosaic_challenge/api`
2. install dependencies: `pip install -r requirements.txt`
3. execute flask command to run the API: `FLASK_APP=app.py flask run`
4. from a new terminal window, execute tests using pytest: `pytest tests/test_api.py`
5. check the test output data saved to the flat file @ `data/books.json`

***NOTE:*** 
- The lines 32 and 71 have been commented out to enable data visualization in step 5. 
- Uncommenting these lines will delete all test created data to avoid leaving unnecessary data in the flat file and clear it for test re-execution.


## Cypress Coding Problem: 
### Write a Cypress test case that verifies the login functionality.

### Steps:

1. cd into project root: `cd Mosaic_challenge/cypress`
2. install dependencies: `npm install`
3. execute test: `npx cypress run`
