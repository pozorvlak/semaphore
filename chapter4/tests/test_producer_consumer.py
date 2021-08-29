from pathlib import Path

from hypothesis import given, settings, strategies as st, HealthCheck

import sync


@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@given(st.random_module())
def test_exclusive_queue(capsys, random):
    capsys.readouterr()
    program = Path(__file__).parent.parent / "producer_consumer.py"
    sim = sync.Sync(sync.Options(delay=0, max_steps=1000), program)
    sim.run()
