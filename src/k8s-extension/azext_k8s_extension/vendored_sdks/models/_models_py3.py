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
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorDefinition(Model):
    """Error definition.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Service specific error code which serves as the
     substatus for the HTTP error code.
    :type code: str
    :param message: Required. Description of the error.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str, message: str, **kwargs) -> None:
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponse(Model):
    """Error response.

    :param error: Error definition.
    :type error: ~azure.mgmt.kubernetesconfiguration.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Resource(Model):
    """The Resource model definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class ProxyResource(Resource):
    """ARM proxy resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ProxyResource, self).__init__(**kwargs)


class ExtensionInstance(ProxyResource):
    """The Extension Instance object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param extension_type: Type of the Extension, of which this resource is an
     instance of.  It must be one of the Extension Types registered with
     Microsoft.KubernetesConfiguration by the Extension publisher.
    :type extension_type: str
    :param auto_upgrade_minor_version: Flag to note if this instance
     participates in auto upgrade of minor version, or not.
    :type auto_upgrade_minor_version: bool
    :param release_train: ReleaseTrain this extension instance participates in
     for auto-upgrade (e.g. Stable, Preview, etc.) - only if
     autoUpgradeMinorVersion is 'true'.
    :type release_train: str
    :param version: Version of the extension for this extension instance, if
     it is 'pinned' to a specific version. autoUpgradeMinorVersion must be
     'false'.
    :type version: str
    :param scope: Scope at which the extension instance is installed.
    :type scope: ~azure.mgmt.kubernetesconfiguration.models.Scope
    :param configuration_settings: Configuration settings, as name-value pairs
     for configuring this instance of the extension.
    :type configuration_settings: dict[str, str]
    :param install_state: Status of installation of this instance of the
     extension. Possible values include: 'Pending', 'Installed', 'Failed'
    :type install_state: str or
     ~azure.mgmt.kubernetesconfiguration.models.InstallStateType
    :param statuses: Status from this instance of the extension.
    :type statuses:
     list[~azure.mgmt.kubernetesconfiguration.models.ExtensionStatus]
    :ivar creation_time: DateLiteral (per ISO8601) noting the time the
     resource was created by the client (user).
    :vartype creation_time: str
    :ivar last_modified_time: DateLiteral (per ISO8601) noting the time the
     resource was modified by the client (user).
    :vartype last_modified_time: str
    :ivar last_status_time: DateLiteral (per ISO8601) noting the time of last
     status from the agent.
    :vartype last_status_time: str
    :ivar error_info: Error information from the Agent - e.g. errors during
     installation.
    :vartype error_info:
     ~azure.mgmt.kubernetesconfiguration.models.ErrorDefinition
    :param identity: The identity of the configuration.
    :type identity:
     ~azure.mgmt.kubernetesconfiguration.models.ConfigurationIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'last_status_time': {'readonly': True},
        'error_info': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'extension_type': {'key': 'properties.extensionType', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'Scope'},
        'configuration_settings': {'key': 'properties.configurationSettings', 'type': '{str}'},
        'install_state': {'key': 'properties.installState', 'type': 'str'},
        'statuses': {'key': 'properties.statuses', 'type': '[ExtensionStatus]'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'str'},
        'last_status_time': {'key': 'properties.lastStatusTime', 'type': 'str'},
        'error_info': {'key': 'properties.errorInfo', 'type': 'ErrorDefinition'},
        'identity': {'key': 'identity', 'type': 'ConfigurationIdentity'},
    }

    def __init__(self, *, extension_type: str=None, auto_upgrade_minor_version: bool=None, release_train: str=None, version: str=None, scope=None, configuration_settings=None, install_state=None, statuses=None, identity=None, **kwargs) -> None:
        super(ExtensionInstance, self).__init__(**kwargs)
        self.extension_type = extension_type
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.release_train = release_train
        self.version = version
        self.scope = scope
        self.configuration_settings = configuration_settings
        self.install_state = install_state
        self.statuses = statuses
        self.creation_time = None
        self.last_modified_time = None
        self.last_status_time = None
        self.error_info = None
        self.identity = identity


class ExtensionInstanceForCreate(ProxyResource):
    """Object to create a new Extension Instance.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param extension_type: Type of the Extension, of which this resource is an
     instance of.  It must be one of the Extension Types registered with
     Microsoft.KubernetesConfiguration by the Extension publisher.
    :type extension_type: str
    :param auto_upgrade_minor_version: Flag to note if this instance
     participates in auto upgrade of minor version, or not.
    :type auto_upgrade_minor_version: bool
    :param release_train: ReleaseTrain this extension instance participates in
     for auto-upgrade (e.g. Stable, Preview, etc.) - only if
     autoUpgradeMinorVersion is 'true'.
    :type release_train: str
    :param version: Version of the extension for this extension instance, if
     it is 'pinned' to a specific version. autoUpgradeMinorVersion must be
     'false'.
    :type version: str
    :param scope: Scope at which the extension instance is installed.
    :type scope: ~azure.mgmt.kubernetesconfiguration.models.Scope
    :param configuration_settings: Configuration settings, as name-value pairs
     for configuring this instance of the extension.
    :type configuration_settings: dict[str, str]
    :param configuration_protected_settings: Configuration settings that are
     sensitive, as name-value pairs for configuring this instance of the
     extension.
    :type configuration_protected_settings: dict[str, str]
    :param identity: The identity of the configuration.
    :type identity:
     ~azure.mgmt.kubernetesconfiguration.models.ConfigurationIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'extension_type': {'key': 'properties.extensionType', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'Scope'},
        'configuration_settings': {'key': 'properties.configurationSettings', 'type': '{str}'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'ConfigurationIdentity'},
    }

    def __init__(self, *, extension_type: str=None, auto_upgrade_minor_version: bool=None, release_train: str=None, version: str=None, scope=None, configuration_settings=None, configuration_protected_settings=None, identity=None, **kwargs) -> None:
        super(ExtensionInstanceForCreate, self).__init__(**kwargs)
        self.extension_type = extension_type
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.release_train = release_train
        self.version = version
        self.scope = scope
        self.configuration_settings = configuration_settings
        self.configuration_protected_settings = configuration_protected_settings
        self.identity = identity


class ExtensionInstanceForList(ProxyResource):
    """The Extension Instance object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param extension_type: Type of the Extension, of which this resource is an
     instance of.  It must be one of the Extension Types registered with
     Microsoft.KubernetesConfiguration by the Extension publisher.
    :type extension_type: str
    :param auto_upgrade_minor_version: Flag to note if this instance
     participates in auto upgrade of minor version, or not.
    :type auto_upgrade_minor_version: bool
    :param release_train: ReleaseTrain this extension instance participates in
     for auto-upgrade (e.g. Stable, Preview, etc.) - only if
     autoUpgradeMinorVersion is 'true'.
    :type release_train: str
    :param version: Version of the extension for this extension instance, if
     it is 'pinned' to a specific version.
    :type version: str
    :param scope: Scope at which the extension instance is installed.
    :type scope: ~azure.mgmt.kubernetesconfiguration.models.Scope
    :param install_state: Status of installation of this instance of the
     extension. Possible values include: 'Pending', 'Installed', 'Failed'
    :type install_state: str or
     ~azure.mgmt.kubernetesconfiguration.models.InstallStateType
    :ivar creation_time: DateLiteral (per ISO8601) noting the time the
     resource was created by the client (user).
    :vartype creation_time: str
    :ivar last_modified_time: DateLiteral (per ISO8601) noting the time the
     resource was modified by the client (user).
    :vartype last_modified_time: str
    :ivar last_status_time: DateLiteral (per ISO8601) noting the time of last
     status from the agent.
    :vartype last_status_time: str
    :ivar error_info: Error information from the Agent - e.g. errors during
     installation.
    :vartype error_info:
     ~azure.mgmt.kubernetesconfiguration.models.ErrorDefinition
    :param identity: The identity of the configuration.
    :type identity:
     ~azure.mgmt.kubernetesconfiguration.models.ConfigurationIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'last_status_time': {'readonly': True},
        'error_info': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'extension_type': {'key': 'properties.extensionType', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'Scope'},
        'install_state': {'key': 'properties.installState', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'str'},
        'last_status_time': {'key': 'properties.lastStatusTime', 'type': 'str'},
        'error_info': {'key': 'properties.errorInfo', 'type': 'ErrorDefinition'},
        'identity': {'key': 'identity', 'type': 'ConfigurationIdentity'},
    }

    def __init__(self, *, extension_type: str=None, auto_upgrade_minor_version: bool=None, release_train: str=None, version: str=None, scope=None, install_state=None, identity=None, **kwargs) -> None:
        super(ExtensionInstanceForList, self).__init__(**kwargs)
        self.extension_type = extension_type
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.release_train = release_train
        self.version = version
        self.scope = scope
        self.install_state = install_state
        self.creation_time = None
        self.last_modified_time = None
        self.last_status_time = None
        self.error_info = None
        self.identity = identity


class ExtensionInstanceUpdate(Model):
    """Update Extension Instance request object.

    :param auto_upgrade_minor_version: Flag to note if this instance
     participates in Extension Lifecycle Management or not.
    :type auto_upgrade_minor_version: bool
    :param release_train: ReleaseTrain this extension instance participates in
     for auto-upgrade (e.g. Stable, Preview, etc.) - only if
     autoUpgradeMinorVersion is 'true'.
    :type release_train: str
    :param version: Version number of extension, to 'pin' to a specific
     version.  autoUpgradeMinorVersion must be 'false'.
    :type version: str
    """

    _attribute_map = {
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
    }

    def __init__(self, *, auto_upgrade_minor_version: bool=None, release_train: str=None, version: str=None, **kwargs) -> None:
        super(ExtensionInstanceUpdate, self).__init__(**kwargs)
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.release_train = release_train
        self.version = version


class ExtensionStatus(Model):
    """Status from this instance of the extension.

    :param code: Status code provided by the Extension
    :type code: str
    :param display_status: Short description of status of this instance of the
     extension.
    :type display_status: str
    :param level: Level of the status. Possible values include: 'Error',
     'Warning', 'Information'. Default value: "Information" .
    :type level: str or ~azure.mgmt.kubernetesconfiguration.models.LevelType
    :param message: Detailed message of the status from the Extension
     instance.
    :type message: str
    :param time: DateLiteral (per ISO8601) noting the time of installation
     status.
    :type time: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'display_status': {'key': 'displayStatus', 'type': 'str'},
        'level': {'key': 'level', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'time': {'key': 'time', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, display_status: str=None, level="Information", message: str=None, time: str=None, **kwargs) -> None:
        super(ExtensionStatus, self).__init__(**kwargs)
        self.code = code
        self.display_status = display_status
        self.level = level
        self.message = message
        self.time = time


class Result(Model):
    """Sample result definition.

    :param sample_property: Sample property of type string
    :type sample_property: str
    """

    _attribute_map = {
        'sample_property': {'key': 'sampleProperty', 'type': 'str'},
    }

    def __init__(self, *, sample_property: str=None, **kwargs) -> None:
        super(Result, self).__init__(**kwargs)
        self.sample_property = sample_property


class Scope(Model):
    """Scope of the extensionInstance. It can be either Cluster or Namespace; but
    not both.

    :param cluster: Specifies that the scope of the extensionInstance is
     Cluster
    :type cluster: ~azure.mgmt.kubernetesconfiguration.models.ScopeCluster
    :param namespace: Specifies that the scope of the extensionInstance is
     Namespace
    :type namespace: ~azure.mgmt.kubernetesconfiguration.models.ScopeNamespace
    """

    _attribute_map = {
        'cluster': {'key': 'cluster', 'type': 'ScopeCluster'},
        'namespace': {'key': 'namespace', 'type': 'ScopeNamespace'},
    }

    def __init__(self, *, cluster=None, namespace=None, **kwargs) -> None:
        super(Scope, self).__init__(**kwargs)
        self.cluster = cluster
        self.namespace = namespace


class ScopeCluster(Model):
    """Specifies that the scope of the extensionInstance is Cluster.

    :param release_namespace: Namespace where the extension Release must be
     placed, for a Cluster scoped extensionInstance.  If this namespace does
     not exist, it will be created
    :type release_namespace: str
    """

    _attribute_map = {
        'release_namespace': {'key': 'releaseNamespace', 'type': 'str'},
    }

    def __init__(self, *, release_namespace: str=None, **kwargs) -> None:
        super(ScopeCluster, self).__init__(**kwargs)
        self.release_namespace = release_namespace


class ScopeNamespace(Model):
    """Specifies that the scope of the extensionInstance is Namespace.

    :param target_namespace: Namespace where the extensionInstance will be
     created for an Namespace scoped extensionInstance.  If this namespace does
     not exist, it will be created
    :type target_namespace: str
    """

    _attribute_map = {
        'target_namespace': {'key': 'targetNamespace', 'type': 'str'},
    }

    def __init__(self, *, target_namespace: str=None, **kwargs) -> None:
        super(ScopeNamespace, self).__init__(**kwargs)
        self.target_namespace = target_namespace