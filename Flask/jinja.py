from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

"""
{{ }} print output in html
{%....%} conditions ,for loops
{#....#} for comments

"""
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the jinja course</H1></html>"

@app.route("/index",methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit',methods=["GET", "POST"])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        #password = request.form['password']
        return f"Hello may name is {username} and this is  my password  !"

    return render_template('form.html')

# ## variable rule
# @app.route('/success/<int:score>')
# def success(score):
#     return f"Your score is " + str(score)
#     #return f"Your score is {score}" 

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL" 
    return render_template('result.html',results=res)


@app.route('/successres/<int:score>')
def successres(score):

    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL" 

    exp={"score":score,"res": res}
             
    return render_template('result1.html',results=exp)

# if condition
@app.route('/successif/<int:score>')
def successif(score): 
    return render_template('result2.html',results=score)


@app.route('/fail/<int:score>')
def fail(score):
   
    return render_template('result.html',results=score)



if __name__=="__main__":
    app.run(debug=True)