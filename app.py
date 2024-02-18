from flask import Flask, redirect, request, render_template

from contacts_model import Contact

Contact.load_db()

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/contacts')


@app.route('/contacts')
def contacts():
    search = request.args.get('q')

    if search:
        contacts_set = Contact.search(search)
    else:
        contacts_set = Contact.all()

    return render_template('contacts/show_all.html', contacts=contacts_set)


@app.route("/contacts/<contact_id>")
def contacts_view(contact_id=0):
    contact = Contact.find(contact_id)
    return render_template("contacts/show.html", contact=contact)


@app.route("/contacts/new", methods=['GET'])
def contacts_new_get():
    return render_template("contacts/new.html", contact=Contact())


@app.route("/contacts/new", methods=['POST'])
def contacts_new():
    c = Contact(None, request.form['first_name'], request.form['last_name'], request.form['phone'],
                request.form['email'])

    if c.save():
        return redirect("/contacts")
    else:
        return render_template("contacts/new.html", contact=c)


@app.route("/contacts/<contact_id>/edit", methods=["GET"])
def contacts_edit_get(contact_id=0):
    contact = Contact.find(contact_id)
    return render_template("contacts/edit.html", contact=contact)


@app.route("/contacts/<contact_id>/edit", methods=["POST"])
def contacts_edit_post(contact_id=0):
    c = Contact.find(contact_id)

    c.update(request.form['first_name'], request.form['last_name'], request.form['phone'], request.form['email'])

    if c.save():
        return redirect("/contacts/" + str(contact_id))
    else:
        return render_template("contacts/edit.html", contact=c)


@app.route("/contacts/<contact_id>/delete", methods=["POST"])
def contacts_delete(contact_id=0):
    contact = Contact.find(contact_id)
    contact.delete()
    return redirect("/contacts")


if __name__ == '__main__':
    app.run()