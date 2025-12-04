
from flask import Flask, request, jsonify, render_template, send_from_directory
import os, json
from expense import Expense
from datetime import date

app = Flask(__name__, template_folder='templates', static_folder='static')

EXPENSE_FILE = 'expenses.csv'
BUDGET_FILE = 'budgets.json'
GROUP_FILE = 'groups.json'

def ensure_files():
    if not os.path.exists(EXPENSE_FILE):
        open(EXPENSE_FILE, 'w').close()
    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, 'w') as f:
            json.dump({}, f)
    if not os.path.exists(GROUP_FILE):
        with open(GROUP_FILE, 'w') as f:
            json.dump({}, f)

def load_expenses():
    items = []
    if not os.path.exists(EXPENSE_FILE):
        return items
    with open(EXPENSE_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            name, amt, cat, month, group = parts
            items.append(Expense(name, float(amt), cat, month, group))
    return items

def save_expense_obj(exp):
    with open(EXPENSE_FILE, 'a') as f:
        f.write(f"{exp.name},{exp.amount},{exp.category},{exp.month},{exp.group}\n")

def load_json(path):
    with open(path,'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path,'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    ensure_files()
    return render_template('index.html')

@app.route('/api/expenses', methods=['GET','POST'])
def api_expenses():
    ensure_files()
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        amount = float(data.get('amount',0))
        category = data.get('category')
        month = data.get('month') or date.today().strftime('%Y-%m')
        group = data.get('group','')
        exp = Expense(name, amount, category, month, group)
        save_expense_obj(exp)
        return jsonify({'status':'ok'}), 201
    else:
        exps = load_expenses()
        result = [{'name':e.name,'amount':e.amount,'category':e.category,'month':e.month,'group':e.group} for e in exps]
        return jsonify(result)

@app.route('/api/budgets', methods=['GET','POST'])
def api_budgets():
    ensure_files()
    if request.method == 'POST':
        data = request.json
        month = data.get('month')
        category = data.get('category')
        limit = float(data.get('limit',0))
        budgets = load_json(BUDGET_FILE)
        if month not in budgets:
            budgets[month] = {}
        budgets[month][category] = limit
        save_json(BUDGET_FILE, budgets)
        return jsonify({'status':'ok'}), 201
    else:
        return jsonify(load_json(BUDGET_FILE))

@app.route('/api/reports/total')
def api_total():
    user_month = request.args.get('month')
    exps = load_expenses()
    total = sum(e.amount for e in exps if e.month == user_month)
    return jsonify({'month': user_month, 'total': total})

@app.route('/api/reports/compare')
def api_compare():
    user_month = request.args.get('month')
    exps = load_expenses()
    budgets = load_json(BUDGET_FILE)
    cats = {}
    for e in exps:
        if e.month == user_month:
            cats[e.category] = cats.get(e.category,0) + e.amount
    out = []
    for cat, spent in cats.items():
        budget = budgets.get(user_month, {}).get(cat)
        status = 'No Budget'
        if budget is not None:
            if spent > budget:
                status = 'Exceeded'
            elif spent >= 0.9*budget:
                status = '10% Left'
            else:
                status = 'OK'
        out.append({'category':cat,'spent':spent,'budget':budget,'status':status})
    return jsonify(out)

@app.route('/api/group/summary')
def api_group():
    group = request.args.get('group')
    exps = load_expenses()
    members = {}
    total = 0
    for e in exps:
        if e.group == group:
            members[e.name] = members.get(e.name,0) + e.amount
            total += e.amount
    if not members:
        return jsonify({'error':'no group data'}), 404
    share = total / len(members)
    settle = {u: round(share - amt,2) for u,amt in members.items()}
    return jsonify({'group':group,'total':total,'share':share,'settlement':settle})

if __name__ == '__main__':
    ensure_files()
    app.run(host='0.0.0.0', port=5000, debug=True)
