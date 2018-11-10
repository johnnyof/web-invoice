from flask import render_template, g, flash, redirect, url_for
from faktura import app, db
from faktura.forms import CustomerRegistration, ItemRegistration, SettingsForm
from faktura.models import Customer, Inventory

invoices = [
    {
        'id': '1',
        'customer': 'dfkdpfw wekwefok',
        'date': '23.08.2018',
        'deadline': '05.09.2018',
        'sum': '9500'

    },
    {
        'id': '2',
        'customer': 'Jane Doe',
        'date': '22.08.2018',
        'deadline': '04.09.2018',
        'sum': '3499'

    }


]
inventorys = [
    {

        'id': '1',
        'name': '2" bolt',
        'in_stock': '33'

    },
    {

        'id': '2',
        'name': 'Slangeklemme',
        'in_stock': '366'

    }


]
customers = [
    {

        'id': '1',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'phone_number': '57455666',
        'email': 'jane@doe.com'

    },
    {

        'id': '2',
        'first_name': 'Joe',
        'last_name': 'Doe',
        'phone_number': '47855462',
        'email': 'Joe@doe.com'
    }


]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/settings")
def settings():
    form = SettingsForm()
    return render_template('settings.html', form=form)


@app.route("/inventory")
def dispInventory():
    inventory = Inventory.query.all()
    return render_template('inventory.html', inventorys=inventory)


@app.route("/customers")
def dispCustomers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)


@app.route("/invoices")
def dispInvoices():
    return render_template('invoices.html', invoices=invoices)


@app.route("/invoice/<string:id>/")
def invoice(id):
    return render_template('invoice.html', id=id)


@app.route("/inventory/<string:id>/")
def inventory(id):
    return render_template('inventory.html', id=id)


@app.route("/customer/<string:id>/")
def customer(id):
    customer = Customer.query.filter_by(id=id).first()
    return render_template('customer.html', customer=customer)


@app.route("/customer/new", methods=['GET', 'POST'])
def newCustomer():
    form = CustomerRegistration()
    if form.validate_on_submit():
        newCustomer = Customer(first_name=form.first_name.data, last_name=form.last_name.data,
                               email=form.email.data, phone_number=form.phone_number.data)
        db.session.add(newCustomer)
        db.session.commit()
        flash(f'Customer created for {form.first_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('newCustomer.html', form=form)


@app.route("/inventory/new", methods=['GET', 'POST'])
def newItem():
    form = ItemRegistration()
    if form.validate_on_submit():
        newInventory = Inventory(
            name=form.name.data, inStock=form.inStock.data)
        db.session.add(newInventory)
        db.session.commit()
        flash(f'Item added to inventory {form.name.data}.')
        return redirect(url_for('newItem'))

    return render_template('newItem.html', form=form)


@app.route("/invoice/new", methods=['GET', 'POST'])
def newInvoice():
    form = InvoiceRegistration()
    if form.validate_on_submit():
        newInvoice = Invoice(customer_name=form.customer_name)
