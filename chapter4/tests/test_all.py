from pathlib import Path

from hypothesis import given, settings, strategies as st, HealthCheck
import pytest

import sync


@pytest.mark.parametrize('program_file', [
    "producer_consumer.py",
    "producer_consumer_finite_buffer.py",
    "reader_writer.py",
])
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@given(random=st.random_module())
def test_all(capsys, random, program_file):
    capsys.readouterr()
    program = Path(__file__).parent.parent / program_file
    sim = sync.Sync(sync.Options(delay=0, max_steps=1000), program)
    sim.run()
