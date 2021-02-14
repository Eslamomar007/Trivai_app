# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 

GET '/qeusintions'
- Fetches a dictionary of categories,current category, number total quesitons and list of qeustions in which the keys are the ids and the value is the corresponding string of the questions
- Request Arguments: None
- Returns: An list of objects with a single key, questions, that contains a object of id: question_string key:value pairs. 

{
        'questions': formated_questions,
        'total_questions': len(formated_questions),
        'total_categories': len(formated_categories),
        'categories': formated_categories,
        'current_category':None,
        'success': True,
    }


3. Create an endpoint to handle GET requests for all available categories. 

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An list of objects with a single key, categories, that contains a object of id: category_string key:value pairs. 
[{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "His  tory",
'5' : "Entertainment",
'6' : "Sports"},
'success': True,]



4. Create an endpoint to DELETE question using a question ID. 

DELETE '/questions/<int:question_id>'
- Fetches  success boolean and messege detect the state of response,
- Request Arguments: question id 
- Returns: after deleting return object with key='success' and value=True and if failed value will be False or will raise error.
{
        'success':True,
        'messege':'question deleted',
} 


5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 5


POST '/questions'
- Fetches : dictionary about the state of the creation request.
- body: required{
        question: question,
        answer: answer,
        difficulty: difficulty,
        category: category
}
- Request Arguments: json body contain question,answer, category and difficulty score.
- Returns: success creation will return a object with succession messege
{
        'success':True,
        'messege':'question deleted',
} 




6. Create a GET endpoint to get questions based on category. 

GET '/categories/<int:category>/questions'
- Fetches :  Fetches a dictionary of current category, number total quesitons and list of qeustions in which the keys are the ids and the value is the corresponding string of the questions.

- Request Arguments: id of the category.
- Returns: this post request return a dictionary of objects
{
      'questions': formated_questions,
      'total_questions': formated_questions,
      'current_category': category,
      'success':True
    }


7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 

POST '/find'
- Fetches :  Fetches a dictionary of current category, number total quesitons and list of qeustions in which the keys are the ids and the value is the corresponding string of the questions which match the search term posted as json
- body:
{'searchTerm':'search term'}
- Request Arguments: json body with search term.
- Returns: this post request return a dictionary of objects with matchs question.
{
      'questions': formated_questions,
      'total_questions': formated_questions,
      'current_category': category,
      'success':True
      }



8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.


POST '/categories/<int:category>/questions'
- Fetches :  Fetches a dictionary of current category, number total quesitons and list of qeustions in which the keys are the ids and the value is the corresponding string of the questions which match the category and previous question if provided posted as json.

- body:
{'previous_question':'previous question',
'quiz_category':'category'
}
- Request Arguments: json body with search term.
- Returns: this post request return a dictionary of objects with random question.
{
            'question': rand_question,
            'current_category': category,
            'previous_question': previous_questions,
            'success':True,
            'total_questions': total_questions
    }




9. Create error handlers for all expected errors including 400, 404, 422 and 500. 
in error cases you will find error handlerwithch will clarify the reason of this error.


REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...
```
Done



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
Done 