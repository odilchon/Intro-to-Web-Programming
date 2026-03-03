from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Task
from app.forms import TaskForm

main = Blueprint("main", __name__)


@main.route("/")
def index():
    tasks = Task.query.order_by(Task.id.desc()).all()
    return render_template("index.html", tasks=tasks)


@main.route("/add", methods=["GET", "POST"])
def add_task():
    form = TaskForm()

    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data
        )
        db.session.add(task)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("add_task.html", form=form, page_title="Add New Task", button_text="Add Task")


@main.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.completed = form.completed.data
        db.session.commit()
        flash("Task updated successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("add_task.html", form=form, page_title="Edit Task", button_text="Update Task")


@main.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!", "info")
    return redirect(url_for("main.index"))


@main.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash("Task status updated!", "success")
    return redirect(url_for("main.index"))


@main.route("/search")
def search():
    query = request.args.get("q", "")
    tasks = Task.query.filter(Task.title.ilike(f"%{query}%")).all()
    return render_template("index.html", tasks=tasks, query=query)