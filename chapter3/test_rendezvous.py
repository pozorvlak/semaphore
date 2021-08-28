from hypothesis import given, strategies as st

import sync


@given(st.random_module())
def test_rendezvous(random):
    sim = sync.Sync(sync.Options(delay=0, max_steps=1000), "rendezvous.py")
    sim.run()
