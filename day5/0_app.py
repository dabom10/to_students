from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return "Hello, World!"

@app.route("/dabom")
def dabom():
    return "<h1>이거는 테스트용!!</h1>"

# Define another route with a simple HTML template
@app.route("/hello/<name>")
def hello(name):
    # 브라우저 주소창에 입력한 내용이 name 변수에 들어왔는지 확인
    print(f"URL에서 받은 데이터: {name}")
    return render_template("index.html", name=name)

# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
