from mininet.topo import Topo
from mininet.link import Link, TCIntf
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

class CustomTopo2(Topo):
    "Definición de una topología personalizada."
    
    def build(self):
        "Construcción de topología."
        
        # Adición de hosts y switches
        h1, h2 = [self.addHost('h%s' % n) for n in range(1, 3)]
        s1, s2, s3, s4 = [self.addSwitch('s%s' % n) for n in range(1, 5)]
        
        # Establecimiento de enlaces
        self.addLink(h1, s1)
        self.addLink(s1, s2, bw=250, delay='150ms', loss=5, intf=TCIntf)
        self.addLink(s2, s3, bw=100, delay='70ms' , loss=4, intf=TCIntf)
        self.addLink(s3, s4, bw=150, delay='200ms', loss=3, intf=TCIntf)
        self.addLink(h2, s4)

topo = CustomTopo2()
setLogLevel('info')
net = Mininet(topo=topo)
net.start()

CLI(net)
net.stop()

