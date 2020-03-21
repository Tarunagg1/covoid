from flask import Flask , render_template,request
app = Flask(__name__)
import pickle

file = open('model.pkl', 'rb') 
clf = pickle.load(file) 
file.close()


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method =="POST":
        mydict = request.form
        fever = int(mydict['fever'])
        bodypain = int(mydict['bodypain'])
        age = int(mydict['age'])
        nose = int(mydict['nose'])
        breath = int(mydict['breath'])
      #code for infrence
        inputfe = [fever, bodypain, age, nose, breath]
        infprob = clf.predict_proba([inputfe])[0][1]
        return render_template('show.html',inf=infprob)
    # return 'Hello, World!'+ str(infprob)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

