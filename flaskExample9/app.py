# Import libraries
from flask import Flask,request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id' : 1, 'date' : '2023-06-01', 'amount' :100},
    {'id' : 2, 'date' : '2023-06-02', 'amount' :-200},
    {'id' : 3, 'date' : '2023-06-03', 'amount' : 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route("/add", methods = ["GET","POST"])
def add_transaction():
    if request.method == 'GET':
        return render_template("form.html")
    if request.method == 'POST':
       # request.form(data)
        transaction = {
            'id' : len(transactions)+1 ,
            'date' : request.form['date'] ,
            'amount' : float(request.form['amount'])
        }
        transactions.append(transaction)

        return redirect(url_for("get_transactions"))

# Update operation
@app.route("/edit/<int:transaction_id>", methods = ["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template("edit.html", transaction = transaction)

    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        return redirect(url_for("get_transactions"))           

    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
        
    return redirect(url_for("get_transactions"))

#search operations
@app.route("/search", methods = {"GET", "POST"})
def search_transactions():
    if request.method == "POST":
        min_value = request.form.get('min_amount')
        max_value = request.form.get('max_amount')

        min1 = float(min_value)
        max1 = float(max_value)

        new_list = []
        for transaction in transactions:
            if (transaction['amount'] >= min1):
                if (transaction['amount'] <= max1) :
                    new_list.append(transaction)
                    print(transaction)
        
        return render_template("transactions.html", transactions = new_list)
    
    if request.method == "GET":
        return render_template("search.html")

#total balance
@app.route("/balance")
def total_balance():
    sum = 0
    for transaction in transactions:
        sum = transaction['amount'] + sum

    print("Sum of all transaction", sum)
    total = {"Total " : sum}
    return render_template("transactions.html", total_balance = total, transactions = transactions)



# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True) 
