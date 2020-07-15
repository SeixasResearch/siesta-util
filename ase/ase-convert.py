from ase.io import read, write
write('initial.xyz', read('MoS2-initial.traj@-7:'))
