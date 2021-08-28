from pathlib import Path

from hypothesis import given, strategies as st

import sync


@given(st.random_module())
def test_exclusive_queue(random):
    program = Path(__file__).parent.parent / "exclusive_queue.py"
    sim = sync.Sync(sync.Options(delay=0, max_steps=1000), program)
    sim.run()
