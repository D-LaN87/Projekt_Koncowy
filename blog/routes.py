from flask import render_template, request, flash, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)


@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
    return edit_or_entry_form()


@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    return edit_or_entry_form(entry)


def edit_or_entry_form(entry=None):
    form = EntryForm(obj=entry)
    errors = None

    if request.method == 'POST':
        if form.validate_on_submit():
            if entry is None:
                entry = Entry()
                db.session.add(entry)

            form.populate_obj(entry)
            db.session.commit()

            if entry.id:
                flash('Wpis został zapisany pomyślnie!', 'success')
            else:
                flash('Nowy wpis został dodany!', 'success')

            return redirect(url_for('index'))
        else:
            errors = form.errors

    return render_template("entry_form.html", form=form, errors=errors)
