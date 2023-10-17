from pickle import TRUE
from flask import Flask, request, render_template_string, make_response
from markupsafe import Markup 
  
app = Flask(__name__)      
  
comments = []      
  
@app.route('/')      
def home():    
    comment_form = '''    
    <form action="/" method="post">    
        <textarea name="comment"></textarea>    
        <input type="submit" value="Post Comment">    
    </form>    
    '''    
    resp = make_response(render_template_string('''    
    <h1>Welcome Deepak's & Graeme's lame a** demo of XSS!</h1>    
    {}     
    <hr>    
    <h2>Comments</h2>    
    {}    
    '''.format(comment_form, '<br>'.join(comments))))    
    resp.set_cookie('session_token', 'faketoken12345WoWyayayayayya')    
    return resp   
  
@app.route('/', methods=['POST'])    
def post_comment():    
    comment = request.form.get('comment')    
    comments.append(Markup(comment))  # treat the comment as HTML  
    return '', 302, {'Location': '/'}    
  
if __name__ == "__main__":      
    app.run(host='0.0.0.0', port=5000, debug=TRUE)   
