from behave import *
from requests import get, put, delete, post

@given(u'there is an empty ServiceRegistry')
def step_impl(context):
    pass


@when(u'I add a service "{service}" with version "{version}"')
def step_impl(context, service, version):
    data = {
        'service': service,
        'version': version
    }
    context.response = post(URL, data=data)


@when(u'I search for a service "{service}" with version "{version}"')
@when(u'I search for a service "{service}" without version')
def step_impl(context, service, version=None):
    data = {
        'service': service,
        'version': version
    }
    context.response = get(URL, data=data)


@when(u'I update a service')
def step_impl(context):
    data = {
        'service_id': 1,
        'version': '1.3.3.7'
    }
    context.response = put(URL, data=data)
