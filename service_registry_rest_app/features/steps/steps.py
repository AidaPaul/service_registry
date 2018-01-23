from behave import *
import requests

BASE_URL = "http://127.0.0.1:8000"
SERVICE_URL = BASE_URL + "/services/"

@given('there is an empty ServiceRegistry')
def step_impl(context):
    context.r = requests.get(SERVICE_URL)
    # assert context.r.json() == []

@when('I add a service "{service}" with version "{version}"')
def step_impl(context, service, version):
    context.r = requests.post(SERVICE_URL, json={"name": str(service), "version": str(version)})


@then('I should be notified with a change "{change}"')
def step_impl(context, change):
    r = context.r
    print (r.status_code)
    print (r.json())

    assert r.status_code == 201

@when('I search for a service "{service}" with version "{version}"')
def step_impl(context, service, version):
    context.r = requests.get(SERVICE_URL+"?name="+str(service)+"&version="+str(version))

@then('I should find count "{count}" instances of service')
def step_impl(context, count):
    r = context.r
    c = r.json()[0].get('count')
    assert count == c
    assert r.status_code == 200

# TODO - add DELETE and update tests


