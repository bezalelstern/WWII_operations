import graphene
from flask import Flask
from flask_graphql import GraphQLView

from db.database import init_db, db_session, URL
from types_1.query import Query

schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Flask

#with app.app_context():
 #   init_db()

app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql',
                                               schema=schema,
                                               graphiql=True))
@app.teardown_appcontext
def shutdown_server(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host='0.0.0',
            port=5001)