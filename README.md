# MCORD-Server

Each detector is represented in the system by an ordered four numbers $\left(z, \varphi, no, side \right)$
Therefore, you need mapping from ip HUBs to $\left(z, \varphi \right)$ and mapping from  id bars to bar numbers in MCORD-Server.
This mapping should be saved somewhere permanently - shouldn't it be some database behind SCADA?
MCORD-Server communicates with HUBs using the generally accepted text format (JSON seems to be the best option).
An important issue is to determine the role of MCORD-Server in collecting measurement data - if it will perform calculations 
that require high performance, it seems that the best technology is c++.