#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_host
short_description: Manages DNS Hosts
description:
    - Manages DNS Hosts.
    - A DNS Host object associates a DNS Config Profile with an on-prem host.
    - This resource represents an existing backend object that cannot be created or deleted through API calls. Instead, it can only be updated.
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - ID of the object
        type: str
        required: false
    state:
        description:
            - Indicate desired state of the object
        type: str
        required: false
        choices:
            - present
            - absent
        default: present
    absolute_name:
        description:
            - "The fully qualified domain name (FQDN) of the DNS host."
        type: str
        required: false
    associated_server:
        description:
            - "Host associated server configuration."
        type: dict
    inheritance_sources:
        description:
            - "Optional. Inheritance configuration."
        type: dict
        suboptions:
            kerberos_keys:
                description:
                    - "Optional. Field config for I(kerberos_keys) field from I(Host) object."
                type: dict
                suboptions:
                    action:
                        description:
                            - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                        type: str
    kerberos_keys:
        description:
            - "Optional. I(kerberos_keys) contains a list of keys for GSS-TSIG signed dynamic updates."
            - "Defaults to empty."
        type: list
        elements: dict
        suboptions:
            key:
                description:
                    - "The resource identifier."
                type: str
    server:
        description:
            - "The resource identifier."
        type: str
    tags:
        description:
            - "Host tagging specifics."
        type: dict

extends_documentation_fragment:
    - infoblox.universal_ddi.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: Retrieve Infra Host Information (required as parent)
      infoblox.universal_ddi.infra_host_info:
        filters:
          display_name: "test_infra_host"

    - name: Create a DNS Server (required as parent)
      infoblox.universal_ddi.dns_server:
        name: "example_server"
        state: present

    - name: Update DNS Host
      infoblox.universal_ddi.dns_host:
        id: "{{ infra_host.id }}"
        absolute_name: "example_server_name"
        server: "{{ server.id }}"
        state: present

    - name: "Dissociate DNS Host"
      infoblox.universal_ddi.dns_host:
        id: "{{ infra_host_info.legacy_id }}"
        state: "absent"

    - name: Delete the DNS Server
      infoblox.universal_ddi.dns_server:
        name: "example_server_name"
        state: "absent"
"""

RETURN = r"""
id:
    description:
        - ID of the Host object
    type: str
    returned: Always
item:
    description:
        - Host object
    type: complex
    returned: Always
    contains:
        absolute_name:
            description:
                - "Host FQDN."
            type: str
            returned: Always
        address:
            description:
                - "Host's primary IP Address."
            type: str
            returned: Always
        anycast_addresses:
            description:
                - "Anycast address configured to the host. Order is not significant."
            type: list
            returned: Always
        associated_server:
            description:
                - "Host associated server configuration."
            type: dict
            returned: Always
            contains:
                id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                name:
                    description:
                        - "DNS server name."
                    type: str
                    returned: Always
        comment:
            description:
                - "Host description."
            type: str
            returned: Always
        current_version:
            description:
                - "Host current version."
            type: str
            returned: Always
        dfp:
            description:
                - "Below I(dfp) field is deprecated and not supported anymore. The indication whether or not BloxOne DDI DNS and BloxOne TD DFP are both active on the host will be migrated into the new I(dfp_service) field."
            type: bool
            returned: Always
        dfp_service:
            description:
                - "DFP service indicates whether or not BloxOne DDI DNS and BloxOne TD DFP are both active on the host. If so, BloxOne DDI DNS will augment recursive queries and forward them to BloxOne TD DFP. Allowed values:"
                - "* I(unavailable): BloxOne TD DFP application is not available,"
                - "* I(enabled): BloxOne TD DFP application is available and enabled,"
                - "* I(disabled): BloxOne TD DFP application is available but disabled."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_sources:
            description:
                - "Optional. Inheritance configuration."
            type: dict
            returned: Always
            contains:
                kerberos_keys:
                    description:
                        - "Optional. Field config for I(kerberos_keys) field from I(Host) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                algorithm:
                                    description:
                                        - "Encryption algorithm of the key in accordance with RFC 3961."
                                    type: str
                                    returned: Always
                                domain:
                                    description:
                                        - "Kerberos realm of the principal."
                                    type: str
                                    returned: Always
                                key:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                principal:
                                    description:
                                        - "Kerberos principal associated with key."
                                    type: str
                                    returned: Always
                                uploaded_at:
                                    description:
                                        - "Upload time for the key."
                                    type: str
                                    returned: Always
                                version:
                                    description:
                                        - "The version number (KVNO) of the key."
                                    type: int
                                    returned: Always
        kerberos_keys:
            description:
                - "Optional. I(kerberos_keys) contains a list of keys for GSS-TSIG signed dynamic updates."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                algorithm:
                    description:
                        - "Encryption algorithm of the key in accordance with RFC 3961."
                    type: str
                    returned: Always
                domain:
                    description:
                        - "Kerberos realm of the principal."
                    type: str
                    returned: Always
                key:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                principal:
                    description:
                        - "Kerberos principal associated with key."
                    type: str
                    returned: Always
                uploaded_at:
                    description:
                        - "Upload time for the key."
                    type: str
                    returned: Always
                version:
                    description:
                        - "The version number (KVNO) of the key."
                    type: int
                    returned: Always
        name:
            description:
                - "Host display name."
            type: str
            returned: Always
        ophid:
            description:
                - "On-Prem Host ID."
            type: str
            returned: Always
        protocol_absolute_name:
            description:
                - "Host FQDN in punycode."
            type: str
            returned: Always
        provider_id:
            description:
                - "External provider identifier."
            type: str
            returned: Always
        server:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        site_id:
            description:
                - "Host site ID."
            type: str
            returned: Always
        tags:
            description:
                - "Host tagging specifics."
            type: dict
            returned: Always
        type:
            description:
                - "Defines the type of host. Allowed values:"
                - "* I(bloxone_ddi): host type is BloxOne DDI,"
                - "* I(microsoft_azure): host type is Microsoft Azure,"
                - "* I(amazon_web_service): host type is Amazon Web Services,"
                - "* I(microsoft_active_directory): host type is Microsoft Active Directory,"
                - "* I(google_cloud_platform): host type is Google Cloud Platform."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.universal_ddi.plugins.module_utils.modules import UniversalDDIAnsibleModule

try:
    from dns_config import Host, HostApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by UniversalDDIAnsibleModule


class DnsHostModule(UniversalDDIAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(DnsHostModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "portal_url", "portal_key", "api_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = Host.from_dict(self._payload_params)
        self._existing = None

    @property
    def existing(self):
        return self._existing

    @existing.setter
    def existing(self, value):
        self._existing = value

    @property
    def payload_params(self):
        return self._payload_params

    @property
    def payload(self):
        return self._payload

    def payload_changed(self):
        if self.existing is None:
            # if existing is None, then it is a create operation
            return True

        return self.is_changed(self.existing.model_dump(by_alias=True, exclude_none=True), self.payload_params)

    def find(self):
        if self.params["id"] is not None:
            try:
                # Attempt to read the host using the provided ID,If the ID is not found
                # and the state is "absent", return None, If the state is not "absent", raise the exception.
                resp = HostApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException:

                if self.params["state"] == "absent":
                    return None
                raise

        return None

    def update(self):
        if self.check_mode:
            return None

        resp = HostApi(self.client).update(id=self.existing.id, body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        update_body = self.payload
        # set the server to empty string to unassociate the host
        setattr(update_body, "server", "")

        resp = HostApi(self.client).update(id=self.existing.id, body=update_body)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def run_command(self):
        result = dict(changed=False, object={}, id=None)

        # based on the state that is passed in, we will execute the appropriate
        # functions
        try:
            self.existing = self.find()
            item = {}
            if self.params["state"] == "present" and self.existing is None:
                self.fail_json("Host does not exist, and creation is not allowed")
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Host updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Host unassociated from the server"

            if self.check_mode:
                # if in check mode, do not update the result or the diff, just return the changed state
                self.exit_json(**result)

            result["diff"] = dict(
                before=self.existing.model_dump(by_alias=True, exclude_none=True) if self.existing is not None else {},
                after=item,
            )
            result["object"] = item
            result["id"] = (
                self.existing.id if self.existing is not None else item["id"] if (item and "id" in item) else None
            )
        except ApiException as e:
            self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        self.exit_json(**result)


def main():
    module_args = dict(
        id=dict(type="str", required=False),
        state=dict(type="str", required=False, choices=["present", "absent"], default="present"),
        absolute_name=dict(type="str"),
        associated_server=dict(type="dict", options=dict()),
        inheritance_sources=dict(
            type="dict",
            options=dict(
                kerberos_keys=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                    no_log=True,
                ),
            ),
        ),
        kerberos_keys=dict(
            type="list",
            elements="dict",
            options=dict(
                key=dict(type="str", no_log=True),
            ),
            no_log=True,
        ),
        server=dict(type="str"),
        tags=dict(type="dict"),
    )

    module = DnsHostModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["id", "server"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
