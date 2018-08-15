from app import app, db
from app.models import User, Pet

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'app':app, 'User':User, 'Pet':Pet}



if __name__ == '__main__':
    app.run()
