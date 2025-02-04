#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_host_info
short_description: Retrieve DNS Host
description:
    - Retrieves information about existing DNS Hosts
    - A DNS Host object associates DNS configuration with hosts.
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - ID of the object
        type: str
        required: false
    filters:
        description:
            - Filter dict to filter objects
        type: dict
        required: false
    filter_query:
        description:
            - Filter query to filter objects
        type: str
        required: false
    inherit:
        description:
            - Return inheritance information
        type: str
        required: false
        choices:
            - full
            - partial
            - none
        default: full
    tag_filters:
        description:
            - Filter dict to filter objects by tags
        type: dict
        required: false
    tag_filter_query:
        description:
            - Filter query to filter objects by tags
        type: str
        required: false

extends_documentation_fragment:
    - infoblox.universal_ddi.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: Get DNS Host information by ID
      infoblox.universal_ddi.dns_host_info:
        id: "{{ dns_host_id }}"

    - name: Get DNS Host information by filters (e.g. absolute_name)
      infoblox.universal_ddi.dns_host_info:
        filters:
          absolute_name: "example_host"

    - name: Get DNS Host information by raw filter query
      infoblox.universal_ddi.dns_host_info:
        filter_query: "absolute_name=='example_host'"
"""

RETURN = r"""
id:
    description:
        - ID of the Host object
    type: str
    returned: Always
objects:
    description:
        - Host object
    type: list
    elements: dict
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
    from dns_config import HostApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by UniversalDDIAnsibleModule


class DnsHostInfoModule(UniversalDDIAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(DnsHostInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = HostApi(self.client).read(self.params["id"], inherit="full")
            return [resp.result]
        except NotFoundException as e:
            return None

    def find(self):
        if self.params["id"] is not None:
            return self.find_by_id()

        filter_str = None
        if self.params["filters"] is not None:
            filter_str = " and ".join([f"{k}=='{v}'" for k, v in self.params["filters"].items()])
        elif self.params["filter_query"] is not None:
            filter_str = self.params["filter_query"]

        tag_filter_str = None
        if self.params["tag_filters"] is not None:
            tag_filter_str = " and ".join([f"{k}=='{v}'" for k, v in self.params["tag_filters"].items()])
        elif self.params["tag_filter_query"] is not None:
            tag_filter_str = self.params["tag_filter_query"]

        all_results = []
        offset = 0

        while True:
            try:
                resp = HostApi(self.client).list(
                    offset=offset, limit=self._limit, filter=filter_str, tfilter=tag_filter_str
                )
                all_results.extend(resp.results)

                if len(resp.results) < self._limit:
                    break
                offset += self._limit

            except ApiException as e:
                self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        return all_results

    def run_command(self):
        result = dict(objects=[])

        if self.check_mode:
            self.exit_json(**result)

        find_results = self.find()

        all_results = []
        for r in find_results:
            all_results.append(r.model_dump(by_alias=True, exclude_none=True))

        result["objects"] = all_results
        self.exit_json(**result)


def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        id=dict(type="str", required=False),
        filters=dict(type="dict", required=False),
        filter_query=dict(type="str", required=False),
        inherit=dict(type="str", required=False, choices=["full", "partial", "none"], default="full"),
        tag_filters=dict(type="dict", required=False),
        tag_filter_query=dict(type="str", required=False),
    )

    module = DnsHostInfoModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[
            ["id", "filters", "filter_query"],
            ["id", "tag_filters", "tag_filter_query"],
        ],
    )
    module.run_command()


if __name__ == "__main__":
    main()
