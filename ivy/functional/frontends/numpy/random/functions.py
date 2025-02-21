# local
import ivy
from ivy.functional.frontends.numpy.func_wrapper import (
    to_ivy_arrays_and_back,
    from_zero_dim_arrays_to_scalar,
)


@to_ivy_arrays_and_back
@from_zero_dim_arrays_to_scalar
def random_sample(size=None):
    return ivy.random_uniform(low=0.0, high=1.0, shape=size, dtype="float64")


@to_ivy_arrays_and_back
@from_zero_dim_arrays_to_scalar
def dirichlet(alpha, size=None):
    return ivy.dirichlet(alpha, size=size)


@to_ivy_arrays_and_back
@from_zero_dim_arrays_to_scalar
def uniform(low=0.0, high=1.0, size=None):
    return ivy.random_uniform(low=low, high=high, shape=size, dtype="float64")


@to_ivy_arrays_and_back
@from_zero_dim_arrays_to_scalar
def normal(loc=0.0, scale=1.0, size=None):
    return ivy.random_normal(mean=loc, std=scale, shape=size, dtype="float64")
