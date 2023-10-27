from flask import Flask, render_template, request, redirect, make_response 
from markupsafe import Markup 
  
  
app = Flask(__name__)  
  
comments = []  # Initialize an empty list for storing comments  
  
@app.route('/', methods=['GET', 'POST'])  
def home():  
    if request.method == 'POST':  
        comment = request.form.get('comment')  
        comments.append(Markup(comment))  # treat the comment as HTML    
        return redirect('/')    
    resp = make_response(render_template('home.html', comments='<br>'.join(comments)))    
    resp.set_cookie('FortuneCookie', 'YourFutureIsCrunchy')      
    return resp     
  
if __name__ == "__main__":  
    app.run(host='0.0.0.0', port=5000, debug=True)  
