from flask.cli import FlaskGroup

from project import app, db, Todo


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Todo(title="test", description="naber"))
    db.session.commit()

@cli.command("seed_db")
def seed_db_multi():
    db.session.add(Todo(title="test", description="naber"))
    db.session.add(Todo(title="test1", description="naber"))
    db.session.add(Todo(title="test2", description="naber"))
    db.session.commit()

if __name__ == "__main__":
    cli()
