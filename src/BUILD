python_sources(
    name="no_configuration.py",
    dependencies=[
        "//:root#opentelemetry-exporter-otlp",
        "//:root#opentelemetry-instrumentation-logging",
    ],
)

pex_binary(
    name="no_configuration",
    entry_point="no_configuration.py"
)