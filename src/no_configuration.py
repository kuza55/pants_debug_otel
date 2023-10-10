from opentelemetry import trace
from opentelemetry.instrumentation.logging import LoggingInstrumentor
import random
import logging

with trace.get_tracer("my.tracer").start_as_current_span("foo"):
        with trace.get_tracer("my.tracer").start_as_current_span("bar"):
                    logging.warning("baz %d", random.randrange(1024))