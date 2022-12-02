import os

import http.client
# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# # Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


# @app.after_request
# def after_request(response):
#     """Ensure responses aren't cached"""
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response
    

# # start of API 
# conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

# headers = {
#     'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
#     'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
#     }

# conn.request("GET", "/search/?q=%3CREQUIRED%3E&type=multi&offset=0&limit=10&numberOfTopResults=5", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

# #end of API

@app.route("/")
def index():
  return render_template("index.html")

 
# @app.route("/sentencer")
# @login_required
# def sentencer():
#     """Show portfolio of stocks"""
#     user_id = session["user_id"]
#     transactions_db = db.execute(
#         "SELECT symbol, SUM(shares) AS shares, price FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
#     cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
#     cash = cash_db[0]["cash"]

#     totalstockvalue = 0
#     for row in transactions_db:
#         totalstockvalue += row["shares"]*row["price"]

#     totalcapital = totalstockvalue + cash

#     return render_template("index.html", database=transactions_db, cash=cash, totalstockvalue=totalstockvalue, totalcapital = totalcapital)


