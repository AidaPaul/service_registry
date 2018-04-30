from service_server import app, init_db


def before_all(context):
    '''
    Starts a flask testing app with in memory database.
    '''
    app.config['PROVIDER'] = 'sqlite'
    app.config['DATABASE'] = ':memory:'
    app.testing = True
    context.db = init_db(app)
    context.client = app.test_client()
