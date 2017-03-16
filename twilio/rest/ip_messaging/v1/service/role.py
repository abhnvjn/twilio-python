# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class RoleList(ListResource):

    def __init__(self, version, service_sid):
        """
        Initialize the RoleList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid

        :returns: twilio.rest.ip_messaging.v1.service.role.RoleList
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleList
        """
        super(RoleList, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
        }
        self._uri = '/Services/{service_sid}/Roles'.format(**self._solution)

    def create(self, friendly_name, type, permission):
        """
        Create a new RoleInstance

        :param unicode friendly_name: The friendly_name
        :param role.role_type type: The type
        :param unicode permission: The permission

        :returns: Newly created RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Type': type,
            'Permission': permission,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams RoleInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v1.service.role.RoleInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists RoleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v1.service.role.RoleInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of RoleInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RolePage
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return RolePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a RoleContext

        :param sid: The sid

        :returns: twilio.rest.ip_messaging.v1.service.role.RoleContext
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleContext
        """
        return RoleContext(
            self._version,
            service_sid=self._solution['service_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a RoleContext

        :param sid: The sid

        :returns: twilio.rest.ip_messaging.v1.service.role.RoleContext
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleContext
        """
        return RoleContext(
            self._version,
            service_sid=self._solution['service_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.RoleList>'


class RolePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RolePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid

        :returns: twilio.rest.ip_messaging.v1.service.role.RolePage
        :rtype: twilio.rest.ip_messaging.v1.service.role.RolePage
        """
        super(RolePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RoleInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        """
        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.RolePage>'


class RoleContext(InstanceContext):

    def __init__(self, version, service_sid, sid):
        """
        Initialize the RoleContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid

        :returns: twilio.rest.ip_messaging.v1.service.role.RoleContext
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleContext
        """
        super(RoleContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Roles/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a RoleInstance

        :returns: Fetched RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the RoleInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, permission):
        """
        Update the RoleInstance

        :param unicode permission: The permission

        :returns: Updated RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        """
        data = values.of({
            'Permission': permission,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.RoleContext {}>'.format(context)


class RoleInstance(InstanceResource):

    class RoleType(object):
        CHANNEL = "channel"
        DEPLOYMENT = "deployment"

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the RoleInstance

        :returns: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        """
        super(RoleInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'friendly_name': payload['friendly_name'],
            'type': payload['type'],
            'permissions': payload['permissions'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: RoleContext for this RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleContext
        """
        if self._context is None:
            self._context = RoleContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def type(self):
        """
        :returns: The type
        :rtype: role.role_type
        """
        return self._properties['type']

    @property
    def permissions(self):
        """
        :returns: The permissions
        :rtype: unicode
        """
        return self._properties['permissions']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a RoleInstance

        :returns: Fetched RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the RoleInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, permission):
        """
        Update the RoleInstance

        :param unicode permission: The permission

        :returns: Updated RoleInstance
        :rtype: twilio.rest.ip_messaging.v1.service.role.RoleInstance
        """
        return self._proxy.update(
            permission,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.RoleInstance {}>'.format(context)
