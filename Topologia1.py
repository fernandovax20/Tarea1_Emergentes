from mininet.topo import Topo
from mininet.link import Link, TCIntf
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

class CustomTopo1(Topo):
    "Definición de una topología simple."
    
    def build(self):
        "Construcción de topología personalizada."
        
        # Adición de hosts y switches
        h1, h2, h3, h4 = [self.addHost('h%s' % n) for n in range(1, 5)]
        s1, s2, s3, s4 = [self.addSwitch('s%s' % n) for n in range(1, 5)]
        
        # Establecimiento de enlaces
        self.addLink(h1, s1)
        self.addLink(h2, s1)

        self.addLink(s1, s2)

        self.addLink(s2, s3, bw=5, delay='20ms', loss=10, intf=TCIntf)
        self.addLink(s3, s4, bw=15, delay='40ms', loss=2, intf=TCIntf)

        self.addLink(h3, s3)
        self.addLink(h4, s4)
        
        # Conexión entre árboles completada


topo = CustomTopo1()
setLogLevel('info')
net = Mininet(topo=topo)
net.start()

CLI(net)
net.stop()
