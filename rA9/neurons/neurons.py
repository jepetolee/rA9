from jax.api import jit
import jax.numpy as jnp


# Integrate And Fire Model

class IF:
    # Vmem => Rest Voltage

    def __init__(self, Vmem, Vth, dt):
        self.Vmem = Vmem
        self.Vth = Vth
        self.dt = dt

    @jit
    def forward(self, x, v_current):
        dV = jnp.divide(jnp.subtract(x, self.Vmem), self.dt)
        v_current += dV
        spike_list = jnp.greater_equal(v_current, self.Vmem).astype(int)
        v_current = jnp.where(v_current >= self.Vth, self.Vmem, v_current)

        return spike_list, v_current


# Leaky Integrate And Fire Model

class LIF:
    # tau => Time Constant; Capacity * Resistance
    # Vmem => Rest Voltage

    def __init__(self, tau, Vmem, Vth,dt):
        self.tau = tau
        self.Vmem = Vmem
        self.Vth = Vth
        self.dt = dt

    @jit
    def forward(self, x, v_current):
        dV_tau = jnp.divide(jnp.subtract(x, self.Vmem), self.dt)
        dV = jnp.divide(dV_tau, self.tau)
        v_current += dV
        spike_list = jnp.greater_equal(v_current, self.Vmem).astype(int)
        v_current = jnp.where(v_current >= self.Vth, self.Vmem, v_current)

        return spike_list, v_current