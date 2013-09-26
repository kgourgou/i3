"""A two-node Bayes net with deterministic CPTs."""

from i3 import bayesnet


def get(rng):
  """Return binary Bayes net."""
  node_1 = bayesnet.BayesNetNode(
    index=0,
    domain_size=2,
    cpt_probabilities=[0.0, 1.0])
  node_2 = bayesnet.BayesNetNode(
    index=1,
    domain_size=3,
    cpt_probabilities=[
      0.0, 1.0, 0.0,
      0.0, 0.0, 1.0])
  net = bayesnet.BayesNet(
    rng=rng,
    nodes=[node_1, node_2],
    edges=[(node_1, node_2)])
  net.compile()
  return net
