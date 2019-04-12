# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TopicRegenerateKeyRequest(Model):
    """Topic regenerate share access key request.

    All required parameters must be populated in order to send to Azure.

    :param key_name: Required. Key name to regenerate key1 or key2
    :type key_name: str
    """

    _validation = {
        'key_name': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(self, *, key_name: str, **kwargs) -> None:
        super(TopicRegenerateKeyRequest, self).__init__(**kwargs)
        self.key_name = key_name