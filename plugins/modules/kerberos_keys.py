#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: kerberos_keys
short_description: Manage Kerberos
description:
    - Manage Kerberos
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
    comment:
        description:
            - "The description for Kerberos key. May contain 0 to 1024 characters. Can include UTF-8."
        type: str
    tags:
        description:
            - "The tags for the Kerberos key in JSON format."
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: Get Kerberos key information by principal
      infoblox.bloxone.kerberos_keys_info:
        filters:
          principal: "{{ principal }}"

    - name: Get Kerberos key information by tag filter
      infoblox.bloxone.kerberos_keys_info:
        tag_filters:
          location: "site-1"
"""

RETURN = r"""
id:
    description:
        - ID of the Kerberos object
    type: str
    returned: Always
item:
    description:
        - Kerberos object
    type: complex
    returned: Always
    contains:
        algorithm:
            description:
                - "Encryption algorithm of the key in accordance with RFC 3961."
            type: str
            returned: Always
        comment:
            description:
                - "The description for Kerberos key. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        domain:
            description:
                - "Kerberos realm of the principal."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        principal:
            description:
                - "Kerberos principal associated with key."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the Kerberos key in JSON format."
            type: dict
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
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from keys import KerberosKey, KerberosApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class KerberosModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(KerberosModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = KerberosKey.from_dict(self._payload_params)
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
                resp = KerberosApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"name=='{self.params['name']}'"
            resp = KerberosApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Kerberos: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = KerberosApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None
        resp = KerberosApi(self.client).update(id=self.existing.id, body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        KerberosApi(self.client).delete(self.existing.id)

    def run_command(self):
        result = dict(changed=False, object={}, id=None)

        # based on the state that is passed in, we will execute the appropriate
        # functions
        try:
            self.existing = self.find()
            item = {}
            if self.params["state"] == "present" and self.existing is None:
                item = self.create()
                result["changed"] = True
                result["msg"] = "Kerberos created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Kerberos updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Kerberos deleted"

            if self.check_mode:
                # if in check mode, do not update the result or the diff, just return the changed state
                self.exit_json(**result)

            result["diff"] = dict(
                before=self.existing.model_dump(by_alias=True, exclude_none=True) if self.existing is not None else {},
                after=item,
            )
            result["object"] = item
            result["id"] = self.existing.id if self.existing is not None else item["id"] if (item and "id" in item) else None
        except ApiException as e:
            self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        self.exit_json(**result)


def main():
    module_args = dict(
        id=dict(type="str", required=False),
        state=dict(type="str", required=False, choices=["present", "absent"], default="present"),
        comment=dict(type="str"),
        tags=dict(type="dict"),

    )

    module = KerberosModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    module.run_command()


if __name__ == "__main__":
    main()
