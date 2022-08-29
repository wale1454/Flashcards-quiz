from flask import Flask, render_template, abort, redirect
# from flask import jsonify
import requests

app = Flask(__name__)


@app.route("/quiz/<int:index>")
def welcome(index):
    ty = index

    lk = " https://the-trivia-api.com/api/questions?categories=science&limit=100&difficulty=easy"
    pl = requests.get(lk).json()

    category = pl[index]["category"]
    question = pl[index]["question"]
    options = pl[index]["incorrectAnswers"]
    correctAns = pl[index]["correctAnswer"]

    return render_template('main.html',  index=ty, category = category, options = options,
                            question=question, ty=ty, correctAns = correctAns)


@app.route('/quiz')
def redirr():
    return redirect('/')


@app.route("/")
def homePage():
    return render_template("home.html")


 
@app.errorhandler(404) 
def invalid_route(e): 

    return redirect('/')
    # return jsonify({'errorCode' : 404, 'message' : 'Route not found'})
  
if __name__ == '__main__':
    app.run(debug=True)


# @app.route("/date")
# def curDate():

#     return f"The time now is { datetime.now() }"

# rt = 0
# @app.route("/viewed")
# def viewCount():
#     global rt
#     rt += 1


#     return str(rt)





