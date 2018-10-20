# print("hello flask prog")

from flask import Flask
# Install the flask
app =Flask(__name__)
# __name__ special type of varible used in the python / its an argument passed to the flask/

# creating a route
@app.route('/')
def index():
    return 'hello'
# new route
@app.route('/about')
def about():
    return 'about page'
# new route eg
@app.route('/example')
def example():
    return 'example page'
# new route eg new
@app.route('/example_new')
def example_new():
    return 'example_new page'

# if stmnt
if(__name__=='__main__'):
    app.run(debug=True)