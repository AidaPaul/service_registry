from services.apps.service.models import Service



def before_feature(context, feature):
	context.fixtures = ['services.json']
