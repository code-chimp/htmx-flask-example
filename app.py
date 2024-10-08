from flask import Flask, render_template

from blueprints.contacts import contacts_bp
from contact_service import ContactService

ContactService.load_db()

app = Flask(__name__)
app.register_blueprint(contacts_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
