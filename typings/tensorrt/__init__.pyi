from collections.abc import Buffer, Sequence
from typing import ClassVar, SupportsInt

class DataType:
    FLOAT: ClassVar[DataType]
    HALF: ClassVar[DataType]
    BF16: ClassVar[DataType]
    INT8: ClassVar[DataType]
    INT32: ClassVar[DataType]
    INT64: ClassVar[DataType]
    BOOL: ClassVar[DataType]
    UINT8: ClassVar[DataType]
    @property
    def itemsize(self) -> int: ...
    def __int__(self) -> int: ...

float32: DataType
float16: DataType
bfloat16: DataType

class NetworkDefinitionCreationFlag:
    EXPLICIT_BATCH: ClassVar[NetworkDefinitionCreationFlag]
    STRONGLY_TYPED: ClassVar[NetworkDefinitionCreationFlag]
    def __int__(self) -> int: ...

class BuilderFlag:
    FP16: ClassVar[BuilderFlag]
    BF16: ClassVar[BuilderFlag]
    INT8: ClassVar[BuilderFlag]
    def __int__(self) -> int: ...

class MemoryPoolType:
    WORKSPACE: ClassVar[MemoryPoolType]
    def __int__(self) -> int: ...

class TensorIOMode:
    INPUT: ClassVar[TensorIOMode]
    OUTPUT: ClassVar[TensorIOMode]
    NONE: ClassVar[TensorIOMode]
    def __int__(self) -> int: ...

class ILogger:
    class Severity:
        INTERNAL_ERROR: ClassVar[ILogger.Severity]
        ERROR: ClassVar[ILogger.Severity]
        WARNING: ClassVar[ILogger.Severity]
        INFO: ClassVar[ILogger.Severity]
        VERBOSE: ClassVar[ILogger.Severity]
        def __int__(self) -> int: ...

    def log(self, severity: Severity, msg: str) -> None: ...

class Logger(ILogger):
    INTERNAL_ERROR: ClassVar[ILogger.Severity]
    ERROR: ClassVar[ILogger.Severity]
    WARNING: ClassVar[ILogger.Severity]
    INFO: ClassVar[ILogger.Severity]
    VERBOSE: ClassVar[ILogger.Severity]
    min_severity: ILogger.Severity
    def __init__(self, min_severity: ILogger.Severity = ...) -> None: ...

class ITensor:
    name: str
    dtype: DataType
    shape: Sequence[int]

class INetworkDefinition:
    num_inputs: int
    num_outputs: int
    def get_input(self, index: int) -> ITensor: ...
    def get_output(self, index: int) -> ITensor: ...

class IOptimizationProfile:
    def set_shape(
        self,
        input: str,
        min: Sequence[int],
        opt: Sequence[int],
        max: Sequence[int],
    ) -> bool: ...

class IBuilderConfig:
    builder_optimization_level: int
    def set_flag(self, flag: BuilderFlag) -> None: ...
    def set_memory_pool_limit(self, pool: MemoryPoolType, pool_size: int) -> None: ...
    def add_optimization_profile(self, profile: IOptimizationProfile) -> int: ...

class IHostMemory(Buffer):
    def __buffer__(self, flags: int, /) -> memoryview: ...
    @property
    def nbytes(self) -> int: ...

class Builder:
    platform_has_fast_fp16: bool
    def __init__(self, logger: ILogger) -> None: ...
    def create_network(self, flags: SupportsInt = ...) -> INetworkDefinition: ...
    def create_builder_config(self) -> IBuilderConfig: ...
    def create_optimization_profile(self) -> IOptimizationProfile: ...
    def build_serialized_network(
        self,
        network: INetworkDefinition,
        config: IBuilderConfig,
    ) -> IHostMemory | None: ...

class IParserError: ...

class OnnxParser:
    num_errors: int
    def __init__(self, network: INetworkDefinition, logger: ILogger) -> None: ...
    def parse(self, model: Buffer, path: str = ...) -> bool: ...
    def get_error(self, index: int) -> IParserError: ...

class ICudaEngine:
    num_io_tensors: int
    def get_tensor_name(self, index: int) -> str: ...
    def get_tensor_dtype(self, name: str) -> DataType: ...
    def get_tensor_shape(self, name: str) -> Sequence[int]: ...
    def get_tensor_mode(self, name: str) -> TensorIOMode: ...

class Runtime:
    def __init__(self, logger: ILogger) -> None: ...
    def deserialize_cuda_engine(
        self,
        serialized_engine: Buffer,
    ) -> ICudaEngine | None: ...
