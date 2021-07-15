import izhikevich_cell as izh
import numpy as np

class ltCell(izh.izhCell):
    def __init__(self, stimVal):
        # Define Neuron Parameters
        super().__init__(stimVal)
        self.celltype='Low Threshold Spiking'
        self.C=100
        self.vr=-56
        self.vt=-42
        self.k=1
        self.a=0.03
        self.b=8
        self.c=-45 # Not used
        self.d=150 # Not used
        self.vpeak=25 # Not used
        
    def simulate(self):
        # Run the simulation
        for i in range(0,self.n-1):
            self.v[0,i+1]=self.v[0,i]+self.tau*(self.k*(self.v[0,i]-self.vr)*(self.v[0,i]-self.vt)-self.u[0,i]+self.I[0,i])/self.C
            self.u[0,i+1]=self.u[0,i]+self.tau*self.a*(self.b*(self.v[0,i]-self.vr)-self.u[0,i])
            
            if self.v[0,i+1]>=40-0.1*self.u[0,i+1]:
                self.v[0,i]=40-0.1*self.u[0,i+1]
                self.v[0,i+1]=-53+0.04*self.u[0,i+1]
                self.u[0,i+1]=np.min((self.u[0,i+1]+20,670))

myCell = ltCell(400)
myCell.simulate()

if __name__=='__main__':
    izh.plotMyData(myCell)
