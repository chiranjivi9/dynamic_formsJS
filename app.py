from firebase import firebase
from flask import Flask, render_template, request, url_for
from form import fireput
app = Flask(__name__)


firebase = firebase.FirebaseApplication('https://dynamin-form.firebaseio.com/', None)
app.config['SECRET_KEY'] = 'abc'


@app.route("/", methods=['POST', 'GET'])
#count = 0
def dynamic_form():
    # form = fireput()
    # if form.validate_on_submit():
    #     #global count
    #     #count += 1
    #     putData = {'Name' : form.champs.data}
    #     print(form.champs.data)
    #     #firebase.put('/formEntry', 'Form' + str(count), putData=putData)
    #     return render_template('result.html', form=form)
    return render_template('formdynamic.html')

if __name__=='__main__':
    app.run(debug=True)
