from behave import given, when, then


@given('there is an empty ServiceRegistry')
def step_impl_0(context):
    context.page = context.client.get('/services', follow_redirects=True).json
    assert context.page['status']


@when('I add a service "{service}" with version "{version}"')
def step_impl_1(context, service, version):
    context.page = context.client.put(
        '/services',
        follow_redirects=True,
        data={
            'service': service,
            'version': version
        },
    ).json
    assert context.page['status']
    assert context.page['item']['service'] == service
    assert context.page['item']['version'] == version


@then('I should be notified with a change "{change}"')
def step_impl_2(context, change):
    assert context.page['item']['change'] == change


@when(u'I search for a service "{service}" with version "{version}"')
def step_impl_3(context, service, version):
    context.page = context.client.get(
        '/services/?service={s}&version={v}'.format(s=service, v=version),
        follow_redirects=True
    ).json
    assert context.page['status']


@then(u'I should find count "{count}" instances of service')
def step_impl_4(context, count):
    assert len(context.page['items']) == int(count)


@then(u'the service "{service}" should have the correct type')
def step_impl_5(context, service):
    # non specified
    pass


@then(u'the service "{service}" should have the correct version "{version}"')
def step_impl_6(context, service, version):
    for item in context.page['items']:
        assert item['version'] == version


@then(u'I should find count "{count}" services')
def step_impl_7(context, count):
    assert len(context.page['items']) == int(count)


@when(u'I search for a service "{service}" without version')
def step_impl_8(context, service):
    context.page = context.client.get(
        '/services/?service={s}'.format(s=service),
        follow_redirects=True
    ).json
    assert context.page['status']


@when(u'I update a service')
def step_impl_9(context):
    context.page = context.client.get(
        '/services/',
        follow_redirects=True
    ).json
    assert context.page['status']

    sid = str(context.page['items'][0]['id'])
    context.page = context.client.put(
        '/services/' + sid,
        follow_redirects=True,
        data=context.page['items'][0],
    ).json
    assert context.page['status']
    assert context.page['item']['change'] == 'changed'


@when(u'I remove a service')
def step_impl_10(context):
    context.page = context.client.get(
        '/services/',
        follow_redirects=True
    ).json
    assert context.page['status']

    sid = str(context.page['items'][0]['id'])
    context.page = context.client.delete(
        '/services/' + sid,
        follow_redirects=True,
        data=context.page['items'][0],
    ).json
    assert context.page['status']


@then(u'the service should be removed')
def step_impl_11(context):
    assert context.page['item']['change'] == 'removed'
