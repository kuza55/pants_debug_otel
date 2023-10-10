python_sources()

pex_binary(
    name="no_configuration",
    entry_point="no_configuration.py",
    dependencies=[
        "//:root#opentelemetry-instrumentation-logging",
        "//:root#opentelemetry-instrumentation-aiohttp-client",
        "//:root#opentelemetry-instrumentation-pymysql",
        "//:root#opentelemetry-instrumentation-requests",
        "//:root#opentelemetry-instrumentation-sqlalchemy",
        "//:root#opentelemetry-instrumentation-system-metrics",
    ],
)