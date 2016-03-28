from lib import munge
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

amps = munge.amplitudes('music/Somebody That I Used To Know')

plt.plot(amps)
plt.show()
