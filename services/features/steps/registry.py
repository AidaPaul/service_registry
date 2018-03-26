from django.contrib.auth.models import User

from behave import given, when, then
from services.apps.service.models import Service as ServiceRegistry
from rest_framework.test import APIClient

api_client = APIClient()



@given('there is an empty ServiceRegistry')
def an_empty_service_registry(context):
    pass

@when('I add a service "{service}" with version "{version}"')
def add_a_service(context, service, version):
    context.response = context.test.client.post(context.get_url('apiv1:create'),
        {"service": service, "version": version})


@then('I should be notified with a change "{change}"')
def i_should_be_notified(context, change):
    context.test.assertEqual(context.response.data.get('change'), change)


@when('I search for a service "{service}" with version "{version}"')
def search_for_a_service_with_version(context, service, version):
    context.response = context.test.client.get(
        context.get_url('apiv1:search'), {"service": service, "version": version})


@then('I should find count "{count:d}" instances of service')
def i_should_find_number_of_instances_service(context, count):
    context.test.assertEqual(context.response.data.get('count'), count)


@then('the service "{service}" should have the correct type')
def the_service_should_have_the_correct_type(context, service):
    context.test.assertEqual(context.response.data.get('service'), service)


@then('the service "{service}" should have the correct version "{version}"')
def the_service_should_have_the_correct_version(context, service, version):
    context.test.assertEqual(context.response.data.get('service'), service)
    context.test.assertEqual(context.response.data.get('version'), version)


@when('I search for a non existing service '
      '"{service}" with version "{version}"')
def search_for_a_service_with_version(context, service, version):
    context.response = context.test.client.get(
        context.get_url('apiv1:search'),
        {"service": service, "version": version})


@then('I should find count "{count:d}" services')
def i__should_find_number_of_services(context, count):
    context.test.assertEqual(context.response.data.get('count'), count)


@when('I search for a service "{service}" without version')
def search_for_a_service_without_version(context, service):
    context.response = context.test.client.get(
        context.get_url('apiv1:search'), {"service": service})


@then('I should find count "{count:d}" services')
def i_should_find_number_of_services(context, count):
    context.test.assertEqual(context.response.data.get('count'), count)


@then('the service without version "{service}" should have the correct type')
def the_service_should_have_the_correct_type(context, service):
    context.test.assertEqual(context.response.data.get('service'), service)


@when('I update a service')
def i_update_a_service(context):
    context.response = api_client.put(
        context.get_url('apiv1:update', pk=1),
        {"service": "test", "version": "0.0.4"})


@then('I should be notified with an update change "{change}"')
def should_be_notified_with_an_update_change(context, change):
    context.test.assertEqual(context.response.data.get('change'), change)


@when(u'I remove a service')
def i_remote_a_service(context):
    context.response = api_client.delete(
        context.get_url('apiv1:delete', pk=1))
    context.test.assertEqual(context.response.data.get('change'), 'removed')


@then(u'the service should be removed')
def service_should_be_removed(context):
    context.test.assertEqual(
        ServiceRegistry.objects.filter(pk=1).exists(), False)


@then('I should be notified with a delete change "{change}"')
def should_notified_with_a_delete_change(context, change):
    context.test.assertEqual(context.response.data.get('change'), change)