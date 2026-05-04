# from flask import Flask, render_template, request, redirect, session
# import sqlite3
# import joblib
# import numpy as np
# import os
# from sklearn.ensemble import RandomForestClassifier

# app = Flask(__name__)
# app.secret_key = "secret123"

# # ---------- AUTO MODEL CREATE ----------
# if not os.path.exists("model.pkl"):
#     print("Creating model...")

#     # Dummy training data (for demo)
#     X = np.array([[20,70],[40,90],[60,110],[30,80]])
#     y = np.array([0,1,1,0])

#     model = RandomForestClassifier()
#     model.fit(X, y)

#     joblib.dump(model, "model.pkl")

# # Load model
# model = joblib.load("model.pkl")

# # ---------- DATABASE ----------
# conn = sqlite3.connect("database.db", check_same_thread=False)
# c = conn.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
# c.execute("CREATE TABLE IF NOT EXISTS history(username TEXT, age INT, heart INT, result INT)")
# c.execute("CREATE TABLE IF NOT EXISTS booking(name TEXT, doctor TEXT, date TEXT, time TEXT, status TEXT)")
# conn.commit()

# # ---------- HOME ----------
# @app.route("/")
# def home():
#     return render_template("index.html")

# # ---------- REGISTER ----------
# @app.route("/register", methods=["GET","POST"])
# def register():
#     if request.method == "POST":
#         c.execute("INSERT INTO users VALUES(?,?)",
#                   (request.form["username"], request.form["password"]))
#         conn.commit()
#         return redirect("/login")
#     return render_template("register.html")

# # ---------- LOGIN ----------
# @app.route("/login", methods=["GET","POST"])
# def login():
#     if request.method == "POST":
#         user = c.execute("SELECT * FROM users WHERE username=? AND password=?",
#                          (request.form["username"], request.form["password"])).fetchone()
#         if user:
#             session["user"] = request.form["username"]
#             return redirect("/dashboard")
#     return render_template("login.html")

# # ---------- DASHBOARD ----------
# @app.route("/dashboard")
# def dashboard():
#     data = c.execute("SELECT * FROM history WHERE username=?", (session["user"],)).fetchall()
#     bookings = c.execute("SELECT * FROM booking WHERE name=?", (session["user"],)).fetchall()
#     return render_template("dashboard.html", data=data, bookings=bookings)

# # ---------- PREDICT ----------
# @app.route("/predict", methods=["GET","POST"])
# def predict():
#     result = None
#     if request.method == "POST":
#         age = int(request.form["age"])
#         heart = int(request.form["heart"])

#         pred = model.predict(np.array([[age, heart]]))
#         result = pred[0]

#         c.execute("INSERT INTO history VALUES(?,?,?,?)",
#                   (session["user"], age, heart, int(result)))
#         conn.commit()

#     return render_template("predict.html", result=result)

# # ---------- BOOKING ----------
# @app.route("/booking", methods=["GET","POST"])
# def booking():
#     msg = ""
#     if request.method == "POST":
#         c.execute("INSERT INTO booking VALUES(?,?,?,?,?)",
#                   (session["user"],
#                    request.form["doctor"],
#                    request.form["date"],
#                    request.form["time"],
#                    "Pending"))
#         conn.commit()
#         msg = "Appointment Requested ✅"
#     return render_template("booking.html", msg=msg)

# # ---------- CHATBOT ----------
# @app.route("/chatbot", methods=["GET","POST"])
# def chatbot():
#     reply = ""
#     if request.method == "POST":
#         q = request.form["q"].lower()

#         if "diet" in q:
#             reply = "Eat healthy fruits & low salt diet"
#         elif "exercise" in q:
#             reply = "Do walking daily"
#         else:
#             reply = "Ask about heart health"

#     return render_template("chatbot.html", reply=reply)

# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/")

# app.run(debug=True, port=5001)



# from flask import Flask, render_template, request, redirect, session
# import sqlite3
# import os
# import joblib
# import numpy as np
# from sklearn.ensemble import RandomForestClassifier

# app = Flask(__name__)
# app.secret_key = "secret123"

# # --------- MODEL (Dummy) ----------
# if not os.path.exists("model.pkl"):
#     X = np.array([[20,70],[40,90],[60,110],[30,80]])
#     y = np.array([0,1,1,0])
#     model = RandomForestClassifier()
#     model.fit(X, y)
#     joblib.dump(model, "model.pkl")

# model = joblib.load("model.pkl")

# # --------- DATABASE ----------
# conn = sqlite3.connect("database.db", check_same_thread=False)
# c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
# c.execute("CREATE TABLE IF NOT EXISTS history(username TEXT, age INT, heart INT, result INT)")
# c.execute("CREATE TABLE IF NOT EXISTS booking(name TEXT, doctor TEXT, date TEXT, time TEXT, status TEXT)")
# conn.commit()

# # --------- LOGIN (Landing Page) ----------
# @app.route("/", methods=["GET","POST"])
# @app.route("/login", methods=["GET","POST"])
# def login():
#     msg = ""
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         user = c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
#         if user:
#             session["user"] = username
#             return redirect("/dashboard")
#         else:
#             msg = "Invalid Username or Password ❌"
#     return render_template("login.html", msg=msg)

# # --------- REGISTER ----------
# @app.route("/register", methods=["GET","POST"])
# def register():
#     msg = ""
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         # Check existing user
#         exist = c.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
#         if exist:
#             msg = "Username already exists ❌"
#         else:
#             c.execute("INSERT INTO users VALUES(?,?)", (username, password))
#             conn.commit()
#             msg = "Registration Successful ✅"
#             return redirect("/login")
#     return render_template("register.html", msg=msg)

# # --------- DASHBOARD (Protected) ----------
# @app.route("/dashboard")
# def dashboard():
#     if "user" not in session:
#         return redirect("/login")
#     return render_template("dashboard.html", user=session["user"])

# # --------- LOGOUT ----------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/login")

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)



# COMMENT OUT BROKEN MODEL LOAD - Replace with this:
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)








# TEMPORARY FAKE MODEL (for testing)
# from flask import Flask, render_template, request, redirect, session
# import pandas as pd
# import numpy as np
# import sqlite3
# import joblib
# import os
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline

# app = Flask(__name__)
# app.secret_key = "secret123"

# # ---------------- DATABASE SETUP ----------------
# def init_db():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
    
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT,
#         password TEXT
#     )
#     """)
    
#     conn.commit()
#     conn.close()

# init_db()

# # ---------------- MODEL TRAINING ----------------
# def train_model():
#     print("Training model...")

#     df = pd.read_csv("arrhythmia_dataset.csv")

#     # Assume last column is target
#     X = df.iloc[:, :-1]
#     y = df.iloc[:, -1]

#     # Handle missing values
#     pipeline = Pipeline([
#         ("imputer", SimpleImputer(strategy="mean")),
#         ("model", LogisticRegression(max_iter=1000))
#     ])

#     pipeline.fit(X, y)

#     joblib.dump(pipeline, "best_model.pkl")
#     print("Model saved as best_model.pkl")

# # Train only if model not exists
# if not os.path.exists("best_model.pkl"):
#     train_model()

# # Load model
# model = joblib.load("best_model.pkl")

# # Load dataset for sampling
# df = pd.read_csv("arrhythmia_dataset.csv")
# X = df.iloc[:, :-1]

# # ---------------- ROUTES ----------------

# @app.route("/")
# def home():
#     return render_template("index.html")

# # ---------- REGISTER ----------
# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()

#         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

#         conn.commit()
#         conn.close()

#         return redirect("/login")

#     return render_template("register.html")

# # ---------- LOGIN ----------
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()

#         cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#         user = cursor.fetchone()

#         conn.close()

#         if user:
#             session["user"] = username
#             return redirect("/")
#         else:
#             return "Invalid Login"

#     return render_template("login.html")

# # ---------- LOGOUT ----------
# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect("/")

# # ---------- PREDICTION ----------
# @app.route("/predict", methods=["GET", "POST"])
# def predict():
#     result = ""

#     if "user" not in session:
#         return redirect("/login")

#     if request.method == "POST":
#         try:
#             # Take random sample (no 187 inputs issue)
#             sample = X.sample(1).values

#             # Replace NaN safely
#             sample = np.nan_to_num(sample)

#             prediction = model.predict(sample)

#             if prediction[0] == 1:
#                 result = "⚠️ Arrhythmia Detected"
#             else:
#                 result = "✅ Normal"

#         except Exception as e:
#             result = "Error: " + str(e)

#     return render_template("predict.html", result=result)

# # ---------------- MAIN ----------------
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, session
import pandas as pd
import numpy as np
import sqlite3
import joblib
import os
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        doctor TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- MODEL ----------------
def train_model():
    df = pd.read_csv("arrhythmia_dataset.csv")

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("model", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X, y)
    joblib.dump(pipeline, "best_model.pkl")

if not os.path.exists("best_model.pkl"):
    train_model()

model = joblib.load("best_model.pkl")

df = pd.read_csv("arrhythmia_dataset.csv")
X = df.iloc[:, :-1]

# ---------------- ROUTES ----------------
@app.route("/dashboard")
def dashboard():
    df = pd.read_csv("arrhythmia_dataset.csv")
    table = df.head(10).to_html(classes="table table-striped", index=False)
    return render_template("dashboard.html", table=table)
@app.route("/")
def home():
    return render_template("index.html")

# -------- REGISTER --------
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO users(username,password) VALUES(?,?)",(u,p))
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

# -------- LOGIN --------
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?",(u,p))
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = u
            return redirect("/")
        else:
            return "Invalid login"

    return render_template("login.html")

# -------- DOCTOR PAGE --------
@app.route("/doctors", methods=["GET","POST"])
def doctors():
    msg = ""

    if request.method == "POST":
        name = request.form["name"]
        doctor = request.form["doctor"]
        date = request.form["date"]

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO appointments(name,doctor,date) VALUES(?,?,?)",(name,doctor,date))
        conn.commit()
        conn.close()

        msg = "✅ Appointment Booked Successfully"

    return render_template("doctors.html", msg=msg)

# -------- PREDICTION --------
@app.route("/predict", methods=["GET","POST"])
def predict():
    result = ""

    if request.method == "POST":
        try:
            values = [float(request.form.get(f"f{i}")) for i in range(1,6)]
            sample = np.array(values).reshape(1,-1)

            # pad remaining features
            if sample.shape[1] < X.shape[1]:
                extra = np.zeros((1, X.shape[1] - sample.shape[1]))
                sample = np.concatenate([sample, extra], axis=1)

            pred = model.predict(sample)

            result = "⚠️ Arrhythmia Detected" if pred[0]==1 else "✅ Normal"

        except:
            result = "Error in input"

    return render_template("predict.html", result=result)

# -------- LOGOUT --------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)