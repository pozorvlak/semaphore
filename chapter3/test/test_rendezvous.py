from pathlib import Path

from hypothesis import given, strategies as st

import sync


@given(st.random_module())
def test_rendezvous(random):
    program = Path(__file__).parent.parent / "rendezvous.py"
    sim = sync.Sync(sync.Options(delay=0, max_steps=1000), program)
    sim.run()
