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


@when(u'I remove a service')
def step_impl(context):
    context.services = get(URL).json()['result']
    context.service_id = 1
    data = {
        'service_id': context.service_id
    }
    context.response = delete(URL, data=data)


@then(u'the service should be removed')
def step_impl(context):
    services = get(URL).json()['result']
    assert len(services) == len(context.services) - 1, "Service not removed"

    for service in services:
        assert service['id'] != context.service_id, "Wrong service removed"


@then(u'I should be notified with a change "{change}"')
def step_impl(context, change):
    assert context.response.json()['result'] == change, context.response.text
