"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import wandb.proto.wandb_base_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class TelemetryRecord(google.protobuf.message.Message):
    """
    Telemetry
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMPORTS_INIT_FIELD_NUMBER: builtins.int
    IMPORTS_FINISH_FIELD_NUMBER: builtins.int
    FEATURE_FIELD_NUMBER: builtins.int
    PYTHON_VERSION_FIELD_NUMBER: builtins.int
    CLI_VERSION_FIELD_NUMBER: builtins.int
    HUGGINGFACE_VERSION_FIELD_NUMBER: builtins.int
    ENV_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    DEPRECATED_FIELD_NUMBER: builtins.int
    ISSUES_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    @property
    def imports_init(self) -> global___Imports: ...
    @property
    def imports_finish(self) -> global___Imports: ...
    @property
    def feature(self) -> global___Feature: ...
    python_version: builtins.str
    cli_version: builtins.str
    huggingface_version: builtins.str
    @property
    def env(self) -> global___Env:
        """string  framework = 7;"""
    @property
    def label(self) -> global___Labels: ...
    @property
    def deprecated(self) -> global___Deprecated: ...
    @property
    def issues(self) -> global___Issues: ...
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        imports_init: global___Imports | None = ...,
        imports_finish: global___Imports | None = ...,
        feature: global___Feature | None = ...,
        python_version: builtins.str = ...,
        cli_version: builtins.str = ...,
        huggingface_version: builtins.str = ...,
        env: global___Env | None = ...,
        label: global___Labels | None = ...,
        deprecated: global___Deprecated | None = ...,
        issues: global___Issues | None = ...,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info", "deprecated", b"deprecated", "env", b"env", "feature", b"feature", "imports_finish", b"imports_finish", "imports_init", b"imports_init", "issues", b"issues", "label", b"label"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info", "cli_version", b"cli_version", "deprecated", b"deprecated", "env", b"env", "feature", b"feature", "huggingface_version", b"huggingface_version", "imports_finish", b"imports_finish", "imports_init", b"imports_init", "issues", b"issues", "label", b"label", "python_version", b"python_version"]) -> None: ...

global___TelemetryRecord = TelemetryRecord

class TelemetryResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___TelemetryResult = TelemetryResult

class Imports(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TORCH_FIELD_NUMBER: builtins.int
    KERAS_FIELD_NUMBER: builtins.int
    TENSORFLOW_FIELD_NUMBER: builtins.int
    FASTAI_FIELD_NUMBER: builtins.int
    SKLEARN_FIELD_NUMBER: builtins.int
    XGBOOST_FIELD_NUMBER: builtins.int
    CATBOOST_FIELD_NUMBER: builtins.int
    LIGHTGBM_FIELD_NUMBER: builtins.int
    PYTORCH_LIGHTNING_FIELD_NUMBER: builtins.int
    IGNITE_FIELD_NUMBER: builtins.int
    TRANSFORMERS_FIELD_NUMBER: builtins.int
    JAX_FIELD_NUMBER: builtins.int
    METAFLOW_FIELD_NUMBER: builtins.int
    ALLENNLP_FIELD_NUMBER: builtins.int
    AUTOGLUON_FIELD_NUMBER: builtins.int
    AUTOKERAS_FIELD_NUMBER: builtins.int
    CATALYST_FIELD_NUMBER: builtins.int
    DEEPCHEM_FIELD_NUMBER: builtins.int
    DEEPCTR_FIELD_NUMBER: builtins.int
    PYCARET_FIELD_NUMBER: builtins.int
    PYTORCHVIDEO_FIELD_NUMBER: builtins.int
    RAY_FIELD_NUMBER: builtins.int
    SIMPLETRANSFORMERS_FIELD_NUMBER: builtins.int
    SKORCH_FIELD_NUMBER: builtins.int
    SPACY_FIELD_NUMBER: builtins.int
    FLASH_FIELD_NUMBER: builtins.int
    OPTUNA_FIELD_NUMBER: builtins.int
    RECBOLE_FIELD_NUMBER: builtins.int
    MMCV_FIELD_NUMBER: builtins.int
    MMDET_FIELD_NUMBER: builtins.int
    TORCHDRUG_FIELD_NUMBER: builtins.int
    TORCHTEXT_FIELD_NUMBER: builtins.int
    TORCHVISION_FIELD_NUMBER: builtins.int
    ELEGY_FIELD_NUMBER: builtins.int
    DETECTRON2_FIELD_NUMBER: builtins.int
    FLAIR_FIELD_NUMBER: builtins.int
    FLAX_FIELD_NUMBER: builtins.int
    SYFT_FIELD_NUMBER: builtins.int
    TTS_FIELD_NUMBER: builtins.int
    MONAI_FIELD_NUMBER: builtins.int
    HUGGINGFACE_HUB_FIELD_NUMBER: builtins.int
    HYDRA_FIELD_NUMBER: builtins.int
    DATASETS_FIELD_NUMBER: builtins.int
    SACRED_FIELD_NUMBER: builtins.int
    JOBLIB_FIELD_NUMBER: builtins.int
    DASK_FIELD_NUMBER: builtins.int
    ASYNCIO_FIELD_NUMBER: builtins.int
    PADDLEOCR_FIELD_NUMBER: builtins.int
    PPDET_FIELD_NUMBER: builtins.int
    PADDLESEG_FIELD_NUMBER: builtins.int
    PADDLENLP_FIELD_NUMBER: builtins.int
    MMSEG_FIELD_NUMBER: builtins.int
    MMOCR_FIELD_NUMBER: builtins.int
    MMCLS_FIELD_NUMBER: builtins.int
    TIMM_FIELD_NUMBER: builtins.int
    FAIRSEQ_FIELD_NUMBER: builtins.int
    DEEPCHECKS_FIELD_NUMBER: builtins.int
    COMPOSER_FIELD_NUMBER: builtins.int
    SPARSEML_FIELD_NUMBER: builtins.int
    ANOMALIB_FIELD_NUMBER: builtins.int
    ZENML_FIELD_NUMBER: builtins.int
    COLOSSALAI_FIELD_NUMBER: builtins.int
    ACCELERATE_FIELD_NUMBER: builtins.int
    MERLIN_FIELD_NUMBER: builtins.int
    NANODET_FIELD_NUMBER: builtins.int
    SEGMENTATION_MODELS_PYTORCH_FIELD_NUMBER: builtins.int
    SENTENCE_TRANSFORMERS_FIELD_NUMBER: builtins.int
    DGL_FIELD_NUMBER: builtins.int
    TORCH_GEOMETRIC_FIELD_NUMBER: builtins.int
    JINA_FIELD_NUMBER: builtins.int
    KORNIA_FIELD_NUMBER: builtins.int
    ALBUMENTATIONS_FIELD_NUMBER: builtins.int
    KERAS_CV_FIELD_NUMBER: builtins.int
    MMENGINE_FIELD_NUMBER: builtins.int
    torch: builtins.bool
    keras: builtins.bool
    tensorflow: builtins.bool
    fastai: builtins.bool
    sklearn: builtins.bool
    xgboost: builtins.bool
    catboost: builtins.bool
    lightgbm: builtins.bool
    pytorch_lightning: builtins.bool
    ignite: builtins.bool
    transformers: builtins.bool
    jax: builtins.bool
    metaflow: builtins.bool
    allennlp: builtins.bool
    autogluon: builtins.bool
    autokeras: builtins.bool
    catalyst: builtins.bool
    """bool avalanche = 17;"""
    deepchem: builtins.bool
    """bool dalle_pytorch = 19;
    bool datasets = 20;
    """
    deepctr: builtins.bool
    pycaret: builtins.bool
    """bool deeppavlov = 23;
    bool detectron = 24;
    bool paddle = 25;
    bool parlai = 26;
    bool prophet = 27;
    """
    pytorchvideo: builtins.bool
    ray: builtins.bool
    simpletransformers: builtins.bool
    skorch: builtins.bool
    spacy: builtins.bool
    flash: builtins.bool
    optuna: builtins.bool
    recbole: builtins.bool
    mmcv: builtins.bool
    mmdet: builtins.bool
    torchdrug: builtins.bool
    torchtext: builtins.bool
    torchvision: builtins.bool
    elegy: builtins.bool
    detectron2: builtins.bool
    flair: builtins.bool
    flax: builtins.bool
    syft: builtins.bool
    TTS: builtins.bool
    monai: builtins.bool
    huggingface_hub: builtins.bool
    hydra: builtins.bool
    datasets: builtins.bool
    sacred: builtins.bool
    joblib: builtins.bool
    dask: builtins.bool
    asyncio: builtins.bool
    paddleocr: builtins.bool
    ppdet: builtins.bool
    paddleseg: builtins.bool
    paddlenlp: builtins.bool
    mmseg: builtins.bool
    mmocr: builtins.bool
    mmcls: builtins.bool
    timm: builtins.bool
    fairseq: builtins.bool
    deepchecks: builtins.bool
    composer: builtins.bool
    sparseml: builtins.bool
    anomalib: builtins.bool
    zenml: builtins.bool
    colossalai: builtins.bool
    accelerate: builtins.bool
    merlin: builtins.bool
    nanodet: builtins.bool
    segmentation_models_pytorch: builtins.bool
    sentence_transformers: builtins.bool
    dgl: builtins.bool
    torch_geometric: builtins.bool
    jina: builtins.bool
    kornia: builtins.bool
    albumentations: builtins.bool
    keras_cv: builtins.bool
    mmengine: builtins.bool
    def __init__(
        self,
        *,
        torch: builtins.bool = ...,
        keras: builtins.bool = ...,
        tensorflow: builtins.bool = ...,
        fastai: builtins.bool = ...,
        sklearn: builtins.bool = ...,
        xgboost: builtins.bool = ...,
        catboost: builtins.bool = ...,
        lightgbm: builtins.bool = ...,
        pytorch_lightning: builtins.bool = ...,
        ignite: builtins.bool = ...,
        transformers: builtins.bool = ...,
        jax: builtins.bool = ...,
        metaflow: builtins.bool = ...,
        allennlp: builtins.bool = ...,
        autogluon: builtins.bool = ...,
        autokeras: builtins.bool = ...,
        catalyst: builtins.bool = ...,
        deepchem: builtins.bool = ...,
        deepctr: builtins.bool = ...,
        pycaret: builtins.bool = ...,
        pytorchvideo: builtins.bool = ...,
        ray: builtins.bool = ...,
        simpletransformers: builtins.bool = ...,
        skorch: builtins.bool = ...,
        spacy: builtins.bool = ...,
        flash: builtins.bool = ...,
        optuna: builtins.bool = ...,
        recbole: builtins.bool = ...,
        mmcv: builtins.bool = ...,
        mmdet: builtins.bool = ...,
        torchdrug: builtins.bool = ...,
        torchtext: builtins.bool = ...,
        torchvision: builtins.bool = ...,
        elegy: builtins.bool = ...,
        detectron2: builtins.bool = ...,
        flair: builtins.bool = ...,
        flax: builtins.bool = ...,
        syft: builtins.bool = ...,
        TTS: builtins.bool = ...,
        monai: builtins.bool = ...,
        huggingface_hub: builtins.bool = ...,
        hydra: builtins.bool = ...,
        datasets: builtins.bool = ...,
        sacred: builtins.bool = ...,
        joblib: builtins.bool = ...,
        dask: builtins.bool = ...,
        asyncio: builtins.bool = ...,
        paddleocr: builtins.bool = ...,
        ppdet: builtins.bool = ...,
        paddleseg: builtins.bool = ...,
        paddlenlp: builtins.bool = ...,
        mmseg: builtins.bool = ...,
        mmocr: builtins.bool = ...,
        mmcls: builtins.bool = ...,
        timm: builtins.bool = ...,
        fairseq: builtins.bool = ...,
        deepchecks: builtins.bool = ...,
        composer: builtins.bool = ...,
        sparseml: builtins.bool = ...,
        anomalib: builtins.bool = ...,
        zenml: builtins.bool = ...,
        colossalai: builtins.bool = ...,
        accelerate: builtins.bool = ...,
        merlin: builtins.bool = ...,
        nanodet: builtins.bool = ...,
        segmentation_models_pytorch: builtins.bool = ...,
        sentence_transformers: builtins.bool = ...,
        dgl: builtins.bool = ...,
        torch_geometric: builtins.bool = ...,
        jina: builtins.bool = ...,
        kornia: builtins.bool = ...,
        albumentations: builtins.bool = ...,
        keras_cv: builtins.bool = ...,
        mmengine: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["TTS", b"TTS", "accelerate", b"accelerate", "albumentations", b"albumentations", "allennlp", b"allennlp", "anomalib", b"anomalib", "asyncio", b"asyncio", "autogluon", b"autogluon", "autokeras", b"autokeras", "catalyst", b"catalyst", "catboost", b"catboost", "colossalai", b"colossalai", "composer", b"composer", "dask", b"dask", "datasets", b"datasets", "deepchecks", b"deepchecks", "deepchem", b"deepchem", "deepctr", b"deepctr", "detectron2", b"detectron2", "dgl", b"dgl", "elegy", b"elegy", "fairseq", b"fairseq", "fastai", b"fastai", "flair", b"flair", "flash", b"flash", "flax", b"flax", "huggingface_hub", b"huggingface_hub", "hydra", b"hydra", "ignite", b"ignite", "jax", b"jax", "jina", b"jina", "joblib", b"joblib", "keras", b"keras", "keras_cv", b"keras_cv", "kornia", b"kornia", "lightgbm", b"lightgbm", "merlin", b"merlin", "metaflow", b"metaflow", "mmcls", b"mmcls", "mmcv", b"mmcv", "mmdet", b"mmdet", "mmengine", b"mmengine", "mmocr", b"mmocr", "mmseg", b"mmseg", "monai", b"monai", "nanodet", b"nanodet", "optuna", b"optuna", "paddlenlp", b"paddlenlp", "paddleocr", b"paddleocr", "paddleseg", b"paddleseg", "ppdet", b"ppdet", "pycaret", b"pycaret", "pytorch_lightning", b"pytorch_lightning", "pytorchvideo", b"pytorchvideo", "ray", b"ray", "recbole", b"recbole", "sacred", b"sacred", "segmentation_models_pytorch", b"segmentation_models_pytorch", "sentence_transformers", b"sentence_transformers", "simpletransformers", b"simpletransformers", "sklearn", b"sklearn", "skorch", b"skorch", "spacy", b"spacy", "sparseml", b"sparseml", "syft", b"syft", "tensorflow", b"tensorflow", "timm", b"timm", "torch", b"torch", "torch_geometric", b"torch_geometric", "torchdrug", b"torchdrug", "torchtext", b"torchtext", "torchvision", b"torchvision", "transformers", b"transformers", "xgboost", b"xgboost", "zenml", b"zenml"]) -> None: ...

global___Imports = Imports

class Feature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WATCH_FIELD_NUMBER: builtins.int
    FINISH_FIELD_NUMBER: builtins.int
    SAVE_FIELD_NUMBER: builtins.int
    OFFLINE_FIELD_NUMBER: builtins.int
    RESUMED_FIELD_NUMBER: builtins.int
    GRPC_FIELD_NUMBER: builtins.int
    METRIC_FIELD_NUMBER: builtins.int
    KERAS_FIELD_NUMBER: builtins.int
    SAGEMAKER_FIELD_NUMBER: builtins.int
    ARTIFACT_INCREMENTAL_FIELD_NUMBER: builtins.int
    METAFLOW_FIELD_NUMBER: builtins.int
    PRODIGY_FIELD_NUMBER: builtins.int
    SET_INIT_NAME_FIELD_NUMBER: builtins.int
    SET_INIT_ID_FIELD_NUMBER: builtins.int
    SET_INIT_TAGS_FIELD_NUMBER: builtins.int
    SET_INIT_CONFIG_FIELD_NUMBER: builtins.int
    SET_RUN_NAME_FIELD_NUMBER: builtins.int
    SET_RUN_TAGS_FIELD_NUMBER: builtins.int
    SET_CONFIG_ITEM_FIELD_NUMBER: builtins.int
    LAUNCH_FIELD_NUMBER: builtins.int
    TORCH_PROFILER_TRACE_FIELD_NUMBER: builtins.int
    SB3_FIELD_NUMBER: builtins.int
    SERVICE_FIELD_NUMBER: builtins.int
    INIT_RETURN_RUN_FIELD_NUMBER: builtins.int
    LIGHTGBM_WANDB_CALLBACK_FIELD_NUMBER: builtins.int
    LIGHTGBM_LOG_SUMMARY_FIELD_NUMBER: builtins.int
    CATBOOST_WANDB_CALLBACK_FIELD_NUMBER: builtins.int
    CATBOOST_LOG_SUMMARY_FIELD_NUMBER: builtins.int
    TENSORBOARD_LOG_FIELD_NUMBER: builtins.int
    ESTIMATOR_HOOK_FIELD_NUMBER: builtins.int
    XGBOOST_WANDB_CALLBACK_FIELD_NUMBER: builtins.int
    XGBOOST_OLD_WANDB_CALLBACK_FIELD_NUMBER: builtins.int
    ATTACH_FIELD_NUMBER: builtins.int
    TENSORBOARD_PATCH_FIELD_NUMBER: builtins.int
    TENSORBOARD_SYNC_FIELD_NUMBER: builtins.int
    KFP_WANDB_LOG_FIELD_NUMBER: builtins.int
    MAYBE_RUN_OVERWRITE_FIELD_NUMBER: builtins.int
    KERAS_METRICS_LOGGER_FIELD_NUMBER: builtins.int
    KERAS_MODEL_CHECKPOINT_FIELD_NUMBER: builtins.int
    KERAS_WANDB_EVAL_CALLBACK_FIELD_NUMBER: builtins.int
    FLOW_CONTROL_OVERFLOW_FIELD_NUMBER: builtins.int
    SYNC_FIELD_NUMBER: builtins.int
    watch: builtins.bool
    """wandb.watch() called"""
    finish: builtins.bool
    """wandb.finish() called"""
    save: builtins.bool
    """wandb.save() called"""
    offline: builtins.bool
    """offline run was synced"""
    resumed: builtins.bool
    """run was resumed"""
    grpc: builtins.bool
    """grpc-server (java integration)"""
    metric: builtins.bool
    """define_metric() called"""
    keras: builtins.bool
    """Keras WandbCallback used"""
    sagemaker: builtins.bool
    """User is using sagemaker"""
    artifact_incremental: builtins.bool
    """Artifact(incremental=True) used"""
    metaflow: builtins.bool
    """Using metaflow integration"""
    prodigy: builtins.bool
    """Using prodigy integration"""
    set_init_name: builtins.bool
    """users set run name from wandb.init"""
    set_init_id: builtins.bool
    """users set run id from wandb.init"""
    set_init_tags: builtins.bool
    """users set tags within wandb.init"""
    set_init_config: builtins.bool
    """users set run config in wandb.init"""
    set_run_name: builtins.bool
    """user sets run name via wandb.run.name = ..."""
    set_run_tags: builtins.bool
    """user sets run name via wandb.run.tags = ..."""
    set_config_item: builtins.bool
    """users set key in run config via run.config.key or run.config["key"]"""
    launch: builtins.bool
    """run is created through wandb launch"""
    torch_profiler_trace: builtins.bool
    """wandb.profiler.torch_trace_handler() called"""
    sb3: builtins.bool
    """Using stable_baselines3 integration"""
    service: builtins.bool
    """Using wandb service internal process"""
    init_return_run: builtins.bool
    """wandb.init() called in the same process returning previous run"""
    lightgbm_wandb_callback: builtins.bool
    """lightgbm callback used"""
    lightgbm_log_summary: builtins.bool
    """lightgbm log summary used"""
    catboost_wandb_callback: builtins.bool
    """catboost callback used"""
    catboost_log_summary: builtins.bool
    """catboost log summary used"""
    tensorboard_log: builtins.bool
    """wandb.tensorflow.log or wandb.tensorboard.log used"""
    estimator_hook: builtins.bool
    """wandb.tensorflow.WandbHook used"""
    xgboost_wandb_callback: builtins.bool
    """xgboost callback used"""
    xgboost_old_wandb_callback: builtins.bool
    """xgboost old callback used (to be depreciated)"""
    attach: builtins.bool
    """attach to a run in another process"""
    tensorboard_patch: builtins.bool
    """wandb.tensorboard.patch(...)"""
    tensorboard_sync: builtins.bool
    """wandb.init(sync_tensorboard=True)"""
    kfp_wandb_log: builtins.bool
    """wandb.integration.kfp.wandb_log"""
    maybe_run_overwrite: builtins.bool
    """Run might have been overwritten"""
    keras_metrics_logger: builtins.bool
    """Keras WandbMetricsLogger used"""
    keras_model_checkpoint: builtins.bool
    """Keras WandbModelCheckpoint used"""
    keras_wandb_eval_callback: builtins.bool
    """Keras WandbEvalCallback used"""
    flow_control_overflow: builtins.bool
    """Hit flow control threshold"""
    sync: builtins.bool
    """Run was synced with wandb sync"""
    def __init__(
        self,
        *,
        watch: builtins.bool = ...,
        finish: builtins.bool = ...,
        save: builtins.bool = ...,
        offline: builtins.bool = ...,
        resumed: builtins.bool = ...,
        grpc: builtins.bool = ...,
        metric: builtins.bool = ...,
        keras: builtins.bool = ...,
        sagemaker: builtins.bool = ...,
        artifact_incremental: builtins.bool = ...,
        metaflow: builtins.bool = ...,
        prodigy: builtins.bool = ...,
        set_init_name: builtins.bool = ...,
        set_init_id: builtins.bool = ...,
        set_init_tags: builtins.bool = ...,
        set_init_config: builtins.bool = ...,
        set_run_name: builtins.bool = ...,
        set_run_tags: builtins.bool = ...,
        set_config_item: builtins.bool = ...,
        launch: builtins.bool = ...,
        torch_profiler_trace: builtins.bool = ...,
        sb3: builtins.bool = ...,
        service: builtins.bool = ...,
        init_return_run: builtins.bool = ...,
        lightgbm_wandb_callback: builtins.bool = ...,
        lightgbm_log_summary: builtins.bool = ...,
        catboost_wandb_callback: builtins.bool = ...,
        catboost_log_summary: builtins.bool = ...,
        tensorboard_log: builtins.bool = ...,
        estimator_hook: builtins.bool = ...,
        xgboost_wandb_callback: builtins.bool = ...,
        xgboost_old_wandb_callback: builtins.bool = ...,
        attach: builtins.bool = ...,
        tensorboard_patch: builtins.bool = ...,
        tensorboard_sync: builtins.bool = ...,
        kfp_wandb_log: builtins.bool = ...,
        maybe_run_overwrite: builtins.bool = ...,
        keras_metrics_logger: builtins.bool = ...,
        keras_model_checkpoint: builtins.bool = ...,
        keras_wandb_eval_callback: builtins.bool = ...,
        flow_control_overflow: builtins.bool = ...,
        sync: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["artifact_incremental", b"artifact_incremental", "attach", b"attach", "catboost_log_summary", b"catboost_log_summary", "catboost_wandb_callback", b"catboost_wandb_callback", "estimator_hook", b"estimator_hook", "finish", b"finish", "flow_control_overflow", b"flow_control_overflow", "grpc", b"grpc", "init_return_run", b"init_return_run", "keras", b"keras", "keras_metrics_logger", b"keras_metrics_logger", "keras_model_checkpoint", b"keras_model_checkpoint", "keras_wandb_eval_callback", b"keras_wandb_eval_callback", "kfp_wandb_log", b"kfp_wandb_log", "launch", b"launch", "lightgbm_log_summary", b"lightgbm_log_summary", "lightgbm_wandb_callback", b"lightgbm_wandb_callback", "maybe_run_overwrite", b"maybe_run_overwrite", "metaflow", b"metaflow", "metric", b"metric", "offline", b"offline", "prodigy", b"prodigy", "resumed", b"resumed", "sagemaker", b"sagemaker", "save", b"save", "sb3", b"sb3", "service", b"service", "set_config_item", b"set_config_item", "set_init_config", b"set_init_config", "set_init_id", b"set_init_id", "set_init_name", b"set_init_name", "set_init_tags", b"set_init_tags", "set_run_name", b"set_run_name", "set_run_tags", b"set_run_tags", "sync", b"sync", "tensorboard_log", b"tensorboard_log", "tensorboard_patch", b"tensorboard_patch", "tensorboard_sync", b"tensorboard_sync", "torch_profiler_trace", b"torch_profiler_trace", "watch", b"watch", "xgboost_old_wandb_callback", b"xgboost_old_wandb_callback", "xgboost_wandb_callback", b"xgboost_wandb_callback"]) -> None: ...

global___Feature = Feature

class Env(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JUPYTER_FIELD_NUMBER: builtins.int
    KAGGLE_FIELD_NUMBER: builtins.int
    WINDOWS_FIELD_NUMBER: builtins.int
    M1_GPU_FIELD_NUMBER: builtins.int
    START_SPAWN_FIELD_NUMBER: builtins.int
    START_FORK_FIELD_NUMBER: builtins.int
    START_FORKSERVER_FIELD_NUMBER: builtins.int
    START_THREAD_FIELD_NUMBER: builtins.int
    MAYBE_MP_FIELD_NUMBER: builtins.int
    jupyter: builtins.bool
    """jupyter env detected"""
    kaggle: builtins.bool
    """kaggle env detected"""
    windows: builtins.bool
    """windows detected"""
    m1_gpu: builtins.bool
    """apple silicon M1 gpu found"""
    start_spawn: builtins.bool
    """multiprocessing spawn"""
    start_fork: builtins.bool
    """multiprocessing fork"""
    start_forkserver: builtins.bool
    """multiprocessing forkserver"""
    start_thread: builtins.bool
    """thread start method"""
    maybe_mp: builtins.bool
    """maybe user running multiprocessing"""
    def __init__(
        self,
        *,
        jupyter: builtins.bool = ...,
        kaggle: builtins.bool = ...,
        windows: builtins.bool = ...,
        m1_gpu: builtins.bool = ...,
        start_spawn: builtins.bool = ...,
        start_fork: builtins.bool = ...,
        start_forkserver: builtins.bool = ...,
        start_thread: builtins.bool = ...,
        maybe_mp: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["jupyter", b"jupyter", "kaggle", b"kaggle", "m1_gpu", b"m1_gpu", "maybe_mp", b"maybe_mp", "start_fork", b"start_fork", "start_forkserver", b"start_forkserver", "start_spawn", b"start_spawn", "start_thread", b"start_thread", "windows", b"windows"]) -> None: ...

global___Env = Env

class Labels(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_STRING_FIELD_NUMBER: builtins.int
    REPO_STRING_FIELD_NUMBER: builtins.int
    CODE_VERSION_FIELD_NUMBER: builtins.int
    code_string: builtins.str
    """code identification"""
    repo_string: builtins.str
    """repo identification"""
    code_version: builtins.str
    """code version"""
    def __init__(
        self,
        *,
        code_string: builtins.str = ...,
        repo_string: builtins.str = ...,
        code_version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code_string", b"code_string", "code_version", b"code_version", "repo_string", b"repo_string"]) -> None: ...

global___Labels = Labels

class Deprecated(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KERAS_CALLBACK__DATA_TYPE_FIELD_NUMBER: builtins.int
    RUN__MODE_FIELD_NUMBER: builtins.int
    RUN__SAVE_NO_ARGS_FIELD_NUMBER: builtins.int
    RUN__JOIN_FIELD_NUMBER: builtins.int
    PLOTS_FIELD_NUMBER: builtins.int
    RUN__LOG_SYNC_FIELD_NUMBER: builtins.int
    INIT__CONFIG_INCLUDE_KEYS_FIELD_NUMBER: builtins.int
    INIT__CONFIG_EXCLUDE_KEYS_FIELD_NUMBER: builtins.int
    KERAS_CALLBACK__SAVE_MODEL_FIELD_NUMBER: builtins.int
    keras_callback__data_type: builtins.bool
    """wandb.keras.WandbCallback(data_type=...) called"""
    run__mode: builtins.bool
    """wandb.run.mode called"""
    run__save_no_args: builtins.bool
    """wandb.run.save() called without arguments"""
    run__join: builtins.bool
    """wandb.run.join() called"""
    plots: builtins.bool
    """wandb.plots.* called"""
    run__log_sync: builtins.bool
    """wandb.run.log(sync=...) called"""
    init__config_include_keys: builtins.bool
    """wandb.init(config_include_keys=...) called"""
    init__config_exclude_keys: builtins.bool
    """wandb.init(config_exclude_keys=...) called"""
    keras_callback__save_model: builtins.bool
    """wandb.keras.WandbCallback(save_model=True) called"""
    def __init__(
        self,
        *,
        keras_callback__data_type: builtins.bool = ...,
        run__mode: builtins.bool = ...,
        run__save_no_args: builtins.bool = ...,
        run__join: builtins.bool = ...,
        plots: builtins.bool = ...,
        run__log_sync: builtins.bool = ...,
        init__config_include_keys: builtins.bool = ...,
        init__config_exclude_keys: builtins.bool = ...,
        keras_callback__save_model: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["init__config_exclude_keys", b"init__config_exclude_keys", "init__config_include_keys", b"init__config_include_keys", "keras_callback__data_type", b"keras_callback__data_type", "keras_callback__save_model", b"keras_callback__save_model", "plots", b"plots", "run__join", b"run__join", "run__log_sync", b"run__log_sync", "run__mode", b"run__mode", "run__save_no_args", b"run__save_no_args"]) -> None: ...

global___Deprecated = Deprecated

class Issues(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SETTINGS__VALIDATION_WARNINGS_FIELD_NUMBER: builtins.int
    SETTINGS__UNEXPECTED_ARGS_FIELD_NUMBER: builtins.int
    SETTINGS__PREPROCESSING_WARNINGS_FIELD_NUMBER: builtins.int
    settings__validation_warnings: builtins.bool
    """validation warnings for settings?"""
    settings__unexpected_args: builtins.bool
    """unexpected settings init args?"""
    settings__preprocessing_warnings: builtins.bool
    """preprocessing warnings for settings?"""
    def __init__(
        self,
        *,
        settings__validation_warnings: builtins.bool = ...,
        settings__unexpected_args: builtins.bool = ...,
        settings__preprocessing_warnings: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["settings__preprocessing_warnings", b"settings__preprocessing_warnings", "settings__unexpected_args", b"settings__unexpected_args", "settings__validation_warnings", b"settings__validation_warnings"]) -> None: ...

global___Issues = Issues
