import os
import sys
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from random import choice
from models import setup_db, Question, Category, db


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)

    pagenation = 10

    cors = CORS(app, resources={r"*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access_Controll_Allow_Headers',
                             'Content_type,Authorization')
        response.headers.add('Access_Controll_Allow_Methods',
                             'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/categories')
    def categories():

        categories = db.session.query(Category).all()
        formated_categories = [category.format() for category in categories]
        return jsonify({
            'success': True,
            'categories': formated_categories,
            'total_categories': len(formated_categories),
        })

    @app.route('/questions')
    def questions():
        page = request.args.get('page', 1, int)
        start = (page-1)*10
        end = start+10

        questions = db.session.query(Question).all()
        formated_questions = [question.format() for question in questions]
        categories = db.session.query(Category).all()
        formated_categories = [category.format() for category in categories]

        return jsonify({
            'questions': formated_questions[start:end],
            'total_questions': len(formated_questions),
            'total_categories': len(formated_categories),
            'categories': formated_categories,
            'current_category': [],
            'success': True,
        })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            db.session.delete(question)
            db.session.commit()
        except:
            db.session.rollback()
            abort(422)
        return jsonify({
            'success': True,
            'message': 'question deleted',
        })

    @app.route('/questions', methods=['POST'])
    def creation():
        try:
            body = request.get_json()
            question = body.get('question', None)
            answer = body.get('answer', None)
            category = body.get('category', None)
            difficulty = body.get('difficulty', None)
            if (not question or not answer or not category or not difficulty):
                abort(422)
            new_question = Question(question=question,
                                    answer=answer, category=category,
                                    difficulty=difficulty)
            db.session.add(new_question)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(422)
        finally:
            db.session.close()

        return jsonify({
            'success': True,
            'message': 'new question added'
        })

    @app.route('/find', methods=['POST'])
    def find():
        page = request.args.get('page', 1, int)
        start = (page-1)*pagenation
        end = start+pagenation
        try:
            body = request.get_json()
            key = body.get('searchTerm')
        except:
            abort(422)

        categories = db.session.query(Category).all()
        formated_categories = [category.format() for category in categories]

        questions = db.session.query(Question).filter(
            Question.question.ilike('%'+key+'%')).all()
        formated_questions = [question.format() for question in questions]

        return jsonify({
            'questions': formated_questions[start:end],
            'categories': formated_categories,
            'total_questions': len(formated_questions),
            'total_categories': len(formated_categories),
            'success': True,

        })

    @app.route('/categories/<int:category>/questions')
    def questions_category(category):
        page = request.args.get('page', 1, int)
        start = (page-1)*pagenation
        end = start+pagenation
        try:
            category = Category.query.get(category).format()
            questions = db.session.query(Question).filter(
                Question.category == category['type']).all()
            formated_questions = [question.format() for question in questions]
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(422)
        finally:
            db.session.close()

        return jsonify({
            'questions': formated_questions[start:end],
            'total_questions': len(formated_questions),
            'current_category': category,
            'success': True
        })

    @app.route('/quizzes', methods=['POST'])
    def quiz():
        search_data = request.get_json()

        if not search_data:
            abort(422)
        category = search_data['quiz_category']['type']
        previous_questions = search_data["previous_questions"]
        print(previous_questions)
        print(category)
        if category == 'click':
            
            if not previous_questions:
                questions = db.session.query(Question).all()
                if not questions:
                    abort(404)
                formated_questions = [question.format()
                                      for question in questions]
                rand_question = choice(formated_questions)
                total_questions = len(formated_questions)
            else:
                questions = db.session.query(Question).filter(
                    Question.id != previous_questions[-1]).all()
                if not questions:
                    abort(404)
                formated_questions = [question.format()
                                      for question in questions]
                rand_question = choice(formated_questions)
                total_questions = len(formated_questions)

        else:
            if not previous_questions:
                questions = db.session.query(Question).filter(
                    Question.category == category).all()
                if not questions:
                    abort(404)
                formated_questions = [question.format()
                                      for question in questions]
                rand_question = choice(formated_questions)
                total_questions = len(formated_questions)
            else:
                questions = db.session.query(Question).filter(
                    Question.category == category).filter(
                        Question.id != previous_questions[-1]).all()
                if not questions:
                    abort(404)
                formated_questions = [question.format()
                                      for question in questions]
                rand_question = choice(formated_questions)
                total_questions = len(formated_questions)
            if total_questions == 0:
                rand_question = None
        return jsonify({
            'question': rand_question,
            'current_category': category,
            'previous_question': previous_questions,
            'success': True,
            'total_questions': total_questions
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found "
        }), 404



    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422
    return app
