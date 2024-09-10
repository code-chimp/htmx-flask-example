from flask import Blueprint, render_template, request, redirect, Response
from typing import Optional, List, Union
from contact import Contact
from contact_service import ContactService

contacts_bp = Blueprint('contacts', __name__)


@contacts_bp.route('/')
def index() -> Response:
    return redirect('/contacts')


@contacts_bp.route('/contacts')
def contacts() -> str:
    search: Optional[str] = request.args.get('q')
    contacts_set: List[Contact] = ContactService.search(search) if search else ContactService.all()
    return render_template('contacts/show_all.html', contacts=contacts_set)


@contacts_bp.route("/contacts/<int:contact_id>")
def contacts_view(contact_id: int = 0) -> str:
    contact: Optional[Contact] = ContactService.find(contact_id)
    return render_template("contacts/show.html", contact=contact)


@contacts_bp.route("/contacts/new", methods=['GET'])
def contacts_new_get() -> str:
    return render_template("contacts/new.html", contact=Contact())


@contacts_bp.route("/contacts/new", methods=['POST'])
def contacts_new() -> Union[str, Response]:
    c: Contact = Contact(None, request.form['first_name'], request.form['last_name'], request.form['phone'],
                         request.form['email'])

    if c.validate():
        if ContactService.email_exists(c):
            c.errors['email'] = 'Email already exists'

    if len(c.errors) == 0 and ContactService.save(c):
        return redirect("/contacts")

    return render_template("contacts/new.html", contact=c)


@contacts_bp.route("/contacts/<int:contact_id>/edit", methods=["GET"])
def contacts_edit_get(contact_id: int = 0) -> str:
    contact: Optional[Contact] = ContactService.find(contact_id)
    return render_template("contacts/edit.html", contact=contact)


@contacts_bp.route("/contacts/<int:contact_id>/edit", methods=["POST"])
def contacts_edit_post(contact_id: int = 0) -> Union[str, Response]:
    c: Optional[Contact] = ContactService.find(contact_id)

    if c:
        c.update(
            request.form['first_name'],
            request.form['last_name'],
            request.form['phone'],
            request.form['email'])

        if c.validate():
            if ContactService.email_exists(c):
                c.errors['email'] = 'Email already exists'

        if len(c.errors) == 0 and ContactService.save(c):
            return redirect(f"/contacts/{contact_id}")

    return render_template("contacts/edit.html", contact=c)


@contacts_bp.route("/contacts/<int:contact_id>/delete", methods=["POST"])
def contacts_delete(contact_id: int = 0) -> Response:
    contact: Optional[Contact] = ContactService.find(contact_id)
    if contact:
        ContactService.delete(contact)
    return redirect("/contacts")
