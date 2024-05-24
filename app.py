from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, Python!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

