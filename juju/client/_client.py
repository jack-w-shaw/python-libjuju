# DO NOT CHANGE THIS FILE! This file is auto-generated by facade.py.
# Changes will be overwritten/lost when the file is regenerated.

from juju.client._definitions import *

from juju.client.old_clients import _client2 as _2_9_client2
from juju.client.old_clients import _client1 as _2_9_client1
from juju.client.old_clients import _client3 as _2_9_client3
from juju.client.old_clients import _client4 as _2_9_client4
from juju.client.old_clients import _client5 as _2_9_client5
from juju.client.old_clients import _client8 as _2_9_client8
from juju.client.old_clients import _client7 as _2_9_client7
from juju.client.old_clients import _client9 as _2_9_client9
from juju.client.old_clients import _client10 as _2_9_client10
from juju.client.old_clients import _client6 as _2_9_client6
from juju.client.old_clients import _client12 as _2_9_client12
from juju.client.old_clients import _client11 as _2_9_client11
from juju.client.old_clients import _client13 as _2_9_client13
from juju.client.old_clients import _client15 as _2_9_client15
from juju.client.old_clients import _client16 as _2_9_client16
from juju.client.old_clients import _client17 as _2_9_client17
from juju.client.old_clients import _client18 as _2_9_client18
from juju.client.old_clients import _client14 as _2_9_client14

from juju.client import _client2, _client1, _client3, _client4, _client5, _client8, _client7, _client9, _client10, _client6, _client12, _client11, _client13, _client15, _client16, _client17, _client18, _client14


CLIENTS = {
    "2": _client2,
    "1": _client1,
    "3": _client3,
    "4": _client4,
    "5": _client5,
    "8": _client8,
    "7": _client7,
    "9": _client9,
    "10": _client10,
    "6": _client6,
    "12": _client12,
    "11": _client11,
    "13": _client13,
    "15": _client15,
    "16": _client16,
    "17": _client17,
    "18": _client18,
    "14": _client14
}


OLD_CLIENTS = {
    "2": _2_9_client2,
    "1": _2_9_client1,
    "3": _2_9_client3,
    "4": _2_9_client4,
    "5": _2_9_client5,
    "8": _2_9_client8,
    "7": _2_9_client7,
    "9": _2_9_client9,
    "10": _2_9_client10,
    "6": _2_9_client6,
    "12": _2_9_client12,
    "11": _2_9_client11,
    "13": _2_9_client13,
    "15": _2_9_client15,
    "16": _2_9_client16,
    "17": _2_9_client17,
    "18": _2_9_client18,
    "14": _2_9_client14
}


def lookup_facade(name, version, is_2_9=False):
    """
    Given a facade name and version, attempt to pull that facade out
    of the correct client<version>.py file.

    """
    for _version in range(int(version), 0, -1):
        try:
            client_directory = OLD_CLIENTS if is_2_9 else CLIENTS
            facade = getattr(client_directory[str(_version)], name)
            return facade
        except (KeyError, AttributeError):
            continue
    else:
        raise ImportError("No supported version for facade: "
                          "{}".format(name))


class TypeFactory:
    @classmethod
    def from_connection(cls, connection):
        """
        Given a connected Connection object, return an initialized and
        connected instance of an API Interface matching the name of
        this class.

        @param connection: initialized Connection object.

        """
        facade_name = cls.__name__
        if not facade_name.endswith('Facade'):
           raise TypeError('Unexpected class name: {}'.format(facade_name))
        facade_name = facade_name[:-len('Facade')]
        version = connection.facades.get(facade_name)
        if version is None:
            raise Exception('No facade {} in facades {}'.format(facade_name,
                                                                connection.facades))

        server_version = connection.info['server-version']
        c = lookup_facade(cls.__name__, version, server_version.startswith('2.9'))
        c = c()
        c.connect(connection)

        return c

    @classmethod
    def best_facade_version(cls, connection):
        """
        Returns the best facade version for a given facade. This will help with
        trying to provide different functionality for different facade versions.

        @param connection: initialized Connection object.
        """
        facade_name = cls.__name__
        if not facade_name.endswith('Facade'):
           raise TypeError('Unexpected class name: {}'.format(facade_name))
        facade_name = facade_name[:-len('Facade')]
        return connection.facades.get(facade_name)


class ActionFacade(TypeFactory):
    pass


class ActionPrunerFacade(TypeFactory):
    pass


class AdminFacade(TypeFactory):
    pass


class AgentFacade(TypeFactory):
    pass


class AgentToolsFacade(TypeFactory):
    pass


class AllModelWatcherFacade(TypeFactory):
    pass


class AllWatcherFacade(TypeFactory):
    pass


class AnnotationsFacade(TypeFactory):
    pass


class ApplicationFacade(TypeFactory):
    pass


class ApplicationOffersFacade(TypeFactory):
    pass


class ApplicationRelationsWatcherFacade(TypeFactory):
    pass


class ApplicationScalerFacade(TypeFactory):
    pass


class BackupsFacade(TypeFactory):
    pass


class BlockFacade(TypeFactory):
    pass


class BundleFacade(TypeFactory):
    pass


class CAASAdmissionFacade(TypeFactory):
    pass


class CAASAgentFacade(TypeFactory):
    pass


class CAASApplicationFacade(TypeFactory):
    pass


class CAASApplicationProvisionerFacade(TypeFactory):
    pass


class CAASFirewallerEmbeddedFacade(TypeFactory):
    pass


class CAASFirewallerFacade(TypeFactory):
    pass


class CAASModelConfigManagerFacade(TypeFactory):
    pass


class CAASModelOperatorFacade(TypeFactory):
    pass


class CAASOperatorFacade(TypeFactory):
    pass


class CAASOperatorProvisionerFacade(TypeFactory):
    pass


class CAASOperatorUpgraderFacade(TypeFactory):
    pass


class CAASUnitProvisionerFacade(TypeFactory):
    pass


class CharmDownloaderFacade(TypeFactory):
    pass


class CharmHubFacade(TypeFactory):
    pass


class CharmRevisionUpdaterFacade(TypeFactory):
    pass


class CharmsFacade(TypeFactory):
    pass


class CleanerFacade(TypeFactory):
    pass


class ClientFacade(TypeFactory):
    pass


class CloudFacade(TypeFactory):
    pass


class ControllerFacade(TypeFactory):
    pass


class CredentialManagerFacade(TypeFactory):
    pass


class CredentialValidatorFacade(TypeFactory):
    pass


class CrossControllerFacade(TypeFactory):
    pass


class CrossModelRelationsFacade(TypeFactory):
    pass


class DeployerFacade(TypeFactory):
    pass


class DiscoverSpacesFacade(TypeFactory):
    pass


class DiskManagerFacade(TypeFactory):
    pass


class EntityWatcherFacade(TypeFactory):
    pass


class EnvironUpgraderFacade(TypeFactory):
    pass


class ExternalControllerUpdaterFacade(TypeFactory):
    pass


class FacadeVersions(TypeFactory):
    pass


class FanConfigurerFacade(TypeFactory):
    pass


class FilesystemAttachmentsWatcherFacade(TypeFactory):
    pass


class FirewallRulesFacade(TypeFactory):
    pass


class FirewallerFacade(TypeFactory):
    pass


class HighAvailabilityFacade(TypeFactory):
    pass


class HostKeyReporterFacade(TypeFactory):
    pass


class ImageManagerFacade(TypeFactory):
    pass


class ImageMetadataFacade(TypeFactory):
    pass


class ImageMetadataManagerFacade(TypeFactory):
    pass


class InstanceMutaterFacade(TypeFactory):
    pass


class InstancePollerFacade(TypeFactory):
    pass


class KeyManagerFacade(TypeFactory):
    pass


class KeyUpdaterFacade(TypeFactory):
    pass


class LeadershipServiceFacade(TypeFactory):
    pass


class LifeFlagFacade(TypeFactory):
    pass


class LogForwardingFacade(TypeFactory):
    pass


class LoggerFacade(TypeFactory):
    pass


class MachineActionsFacade(TypeFactory):
    pass


class MachineManagerFacade(TypeFactory):
    pass


class MachineUndertakerFacade(TypeFactory):
    pass


class MachinerFacade(TypeFactory):
    pass


class MeterStatusFacade(TypeFactory):
    pass


class MetricsAdderFacade(TypeFactory):
    pass


class MetricsDebugFacade(TypeFactory):
    pass


class MetricsManagerFacade(TypeFactory):
    pass


class MigrationFlagFacade(TypeFactory):
    pass


class MigrationMasterFacade(TypeFactory):
    pass


class MigrationMinionFacade(TypeFactory):
    pass


class MigrationStatusWatcherFacade(TypeFactory):
    pass


class MigrationTargetFacade(TypeFactory):
    pass


class ModelConfigFacade(TypeFactory):
    pass


class ModelGenerationFacade(TypeFactory):
    pass


class ModelManagerFacade(TypeFactory):
    pass


class ModelSummaryWatcherFacade(TypeFactory):
    pass


class ModelUpgraderFacade(TypeFactory):
    pass


class NotifyWatcherFacade(TypeFactory):
    pass


class OfferStatusWatcherFacade(TypeFactory):
    pass


class PayloadsFacade(TypeFactory):
    pass


class PayloadsHookContextFacade(TypeFactory):
    pass


class PingerFacade(TypeFactory):
    pass


class ProvisionerFacade(TypeFactory):
    pass


class ProxyUpdaterFacade(TypeFactory):
    pass


class RaftLeaseFacade(TypeFactory):
    pass


class RebootFacade(TypeFactory):
    pass


class RelationStatusWatcherFacade(TypeFactory):
    pass


class RelationUnitsWatcherFacade(TypeFactory):
    pass


class RemoteApplicationWatcherFacade(TypeFactory):
    pass


class RemoteRelationWatcherFacade(TypeFactory):
    pass


class RemoteRelationsFacade(TypeFactory):
    pass


class RemoteRelationsWatcherFacade(TypeFactory):
    pass


class ResourcesFacade(TypeFactory):
    pass


class ResourcesHookContextFacade(TypeFactory):
    pass


class ResumerFacade(TypeFactory):
    pass


class RetryStrategyFacade(TypeFactory):
    pass


class SSHClientFacade(TypeFactory):
    pass


class SecretsFacade(TypeFactory):
    pass


class SecretsManagerFacade(TypeFactory):
    pass


class SecretsRotationWatcherFacade(TypeFactory):
    pass


class SingularFacade(TypeFactory):
    pass


class SpacesFacade(TypeFactory):
    pass


class StatusHistoryFacade(TypeFactory):
    pass


class StorageFacade(TypeFactory):
    pass


class StorageProvisionerFacade(TypeFactory):
    pass


class StringsWatcherFacade(TypeFactory):
    pass


class SubnetsFacade(TypeFactory):
    pass


class UndertakerFacade(TypeFactory):
    pass


class UnitAssignerFacade(TypeFactory):
    pass


class UniterFacade(TypeFactory):
    pass


class UpgradeSeriesFacade(TypeFactory):
    pass


class UpgradeStepsFacade(TypeFactory):
    pass


class UpgraderFacade(TypeFactory):
    pass


class UserManagerFacade(TypeFactory):
    pass


class VolumeAttachmentPlansWatcherFacade(TypeFactory):
    pass


class VolumeAttachmentsWatcherFacade(TypeFactory):
    pass


