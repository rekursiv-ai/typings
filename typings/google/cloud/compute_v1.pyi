from collections.abc import Iterable, Iterator

class ImagesClient:
    def get_from_family(self, *, project: str, family: str) -> Image: ...

class Image:
    self_link: str

class Operation:
    def result(self, timeout: int) -> object: ...

class InstancesClient:
    def insert(
        self,
        *,
        project: str,
        zone: str,
        instance_resource: Instance,
    ) -> Operation: ...
    def delete(self, *, project: str, zone: str, instance: str) -> Operation: ...
    def aggregated_list(
        self,
        *,
        request: AggregatedListInstancesRequest,
    ) -> Iterator[tuple[str, ScopedInstances]]: ...

class AggregatedListInstancesRequest:
    def __init__(self, *, project: str, filter: str, max_results: int) -> None: ...

class AttachedDisk:
    boot: bool
    auto_delete: bool
    initialize_params: AttachedDiskInitializeParams
    device_name: str
    source: str

class AttachedDiskInitializeParams:
    def __init__(
        self,
        *,
        source_image: str,
        disk_size_gb: int,
        disk_type: str,
    ) -> None: ...

class NetworkInterface:
    network: str
    subnetwork: str
    access_configs: list[AccessConfig]

class AccessConfig:
    class Type:
        ONE_TO_ONE_NAT: _EnumValue

    nat_i_p: str
    def __init__(self, *, name: str, type_: str, network_tier: str) -> None: ...

class Metadata:
    def __init__(self, *, items: list[Items]) -> None: ...

class Items:
    def __init__(self, *, key: str, value: str) -> None: ...

class ServiceAccount:
    def __init__(self, *, email: str, scopes: list[str]) -> None: ...

class ShieldedInstanceConfig:
    def __init__(
        self,
        *,
        enable_secure_boot: bool,
        enable_vtpm: bool,
        enable_integrity_monitoring: bool,
    ) -> None: ...

class Scheduling:
    class OnHostMaintenance:
        TERMINATE: _EnumValue
        MIGRATE: _EnumValue

    class ProvisioningModel:
        SPOT: _EnumValue

    class InstanceTerminationAction:
        DELETE: _EnumValue

    automatic_restart: bool
    on_host_maintenance: str
    provisioning_model: str
    preemptible: bool
    max_run_duration: Duration
    instance_termination_action: str

class Duration:
    def __init__(self, *, seconds: int) -> None: ...

class Instance:
    name: str
    machine_type: str
    disks: list[AttachedDisk]
    network_interfaces: list[NetworkInterface]
    metadata: Metadata
    service_accounts: list[ServiceAccount]
    shielded_instance_config: ShieldedInstanceConfig
    scheduling: Scheduling
    tags: Tags
    labels: dict[str, str]
    status: str

class Tags:
    def __init__(self, *, items: list[str]) -> None: ...

class ScopedInstances:
    instances: Iterable[Instance] | None

class _EnumValue:
    name: str
