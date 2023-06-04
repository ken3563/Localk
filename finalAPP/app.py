from flask import Flask , render_template, request, flash
import redis

app = Flask(__name__)
app.secret_key = "manbearpig_MUD888"

# Connect to Redis
r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    db=0,
    decode_responses=True
)



@app.route("/hello")
def index():
    flash("what's your name?")
    count = r.get('test')
    if count is None:
        count = 0

    # Render the home page with the current counter value.
    return render_template('index.html', count=count)


@app.route("/greet", methods=["POST", "GET"])
def greet():


    if "YES" in request.form:
     in_Yes = r.incrby('YES', 1) 
     yyy = str("YES" in request.form)
     Message_Y = request.form['name_input']
     r.rpush (yyy , Message_Y )
     flash("Hi " + str(request.form['name_input']) + ", great to see you!")
     return render_template("index.html", in_Yes=in_Yes)
    elif "NO" in request.form:
     in_Noo = r.incrby('NO', 1)
     nnn =str("NO" in request.form)
     Message_N = (request.form['name_input'])
     r.rpush ( nnn,  Message_N)
     flash("Hi " + str(request.form['name_input']) + ", great to see you!")
     return render_template("index.html", in_Noo=in_Noo)

    

    


     



    
     
  
    # Atomically add one to the counter in Redis.
    # If the key doesn't exist, Redis will create it with
    # an initial value of 1.s
    


 

  
