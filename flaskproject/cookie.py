from flask import  Flask, render_template, request,make_response

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("setcookie.html")

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
    if request.method=='POST':
        user=request.form('sahil')
        resp=make_response(render_template('readcookie.html'))
        resp.setcookie('UserID',user)
        return resp
@app.route('/getcookie')
def getcookie():
    name=request.cookies.get("UserID")
    return'<h1>Welcome'+name+'</h1>'

if __name__=='__main__':
    app.run(debug=True)
    