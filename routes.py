import json
from flask import render_template, redirect, url_for, session, request, flash
from app import app, load_init
from forms.pizza_form import LoginForm, CreateAccountForm, PizzaForm

def is_logged_in():
    return "login" in session

def load_users():
    with open("data/users.json") as f:
        return json.load(f)

def save_users(users):
    with open("data/users.json", "w") as f:
        json.dump(users, f, indent=2)

def load_orders():
    with open("data/pizzaorders.json") as f:
        return json.load(f)

def save_orders(orders):
    with open("data/pizzaorders.json", "w") as f:
        json.dump(orders, f, indent=2)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = load_users()
        user = next((u for u in users if u["email"] == form.email.data and u["password"] == form.password.data), None)
        if user:
            session["login"] = user["email"]
            session["role"] = user["role"]
            return redirect(url_for("index"))
        else:
            flash("Invalid email or password. Please try again.", "error")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    session.pop("login", None)
    session.pop("role", None)
    return redirect(url_for("login"))


@app.route("/create", methods=["GET", "POST"])
def create():
    form = CreateAccountForm()
    if form.validate_on_submit():
        users = load_users()
        new_user = {
            "id": len(users) + 1,
            "email": form.email.data,
            "password": form.password.data,
            "role": form.role.data
        }
        users.append(new_user)
        save_users(users)
        flash("Account created! Please login.", "success")
        return redirect(url_for("login"))
    return render_template("create.html", form=form)


@app.route("/")
def index():
    if not is_logged_in():
        return redirect(url_for("login"))
    orders = load_orders()
    orders.sort(key=lambda x: x["order_date"], reverse=True)
    return render_template("index.html", orders=orders)


@app.route("/pizza", methods=["GET", "POST", "PUT", "DELETE"])
def pizza():
    if not is_logged_in():
        return redirect(url_for("login"))

    if request.method == "DELETE":
        order_id = request.args.get("id", type=int)
        orders = load_orders()
        orders = [o for o in orders if o["id"] != order_id]
        save_orders(orders)
        return "", 204

    init = load_init()
    form = PizzaForm()
    form.type.choices = [(t, t) for t in init["type"]]
    form.crust.choices = [(c, c) for c in init["crust"]]
    form.size.choices = [(s, s) for s in init["size"]]
    if form.validate_on_submit():
        orders = load_orders()
        new_order = {
            "id": max([o["id"] for o in orders], default=0) + 1,
            "type": form.type.data,
            "crust": form.crust.data,
            "size": form.size.data,
            "quantity": form.quantity.data,
            "price_per": form.price_per.data,
            "order_date": form.order_date.data.strftime("%Y/%m/%d")
        }
        orders.append(new_order)
        save_orders(orders)
        flash("Pizza order added!", "success")
        return redirect(url_for("index"))
    return render_template("pizza.html", form=form)


@app.route("/confirm", methods=["GET"])
def confirm():
    if not is_logged_in():
        return redirect(url_for("login"))
    order_id = request.args.get("id", type=int)
    orders = load_orders()
    order = next((o for o in orders if o["id"] == order_id), None)
    return render_template("confirm.html", order=order)