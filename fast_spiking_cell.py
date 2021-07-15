import izhikevich_cell as izh

class fsCell(izh.izhCell):
    def __init__(self, stimVal):
        # Define Neuron Parameters
        super().__init__(stimVal)
        self.celltype='Fast Spiking'
        self.C=20
        self.vr=-55
        self.vt=-40
        self.k=1
        self.a=0.2
        self.b=1 # Not used
        self.c=-45
        self.d=150 # Not used
        self.vpeak=25
        self.vb=-55
        
    def simulate(self):
        # Run the simulation
        for i in range(0,self.n-1):
            self.v[0,i+1]=self.v[0,i]+self.tau*(self.k*(self.v[0,i]-self.vr)*(self.v[0,i]-self.vt)-self.u[0,i]+self.I[0,i])/self.C
            
            Uv=0
            if self.v[0,i]>=-55:
                self.Uv=0.025*(self.v[0,i]-self.vb)**3
                
            self.u[0,i+1]=self.u[0,i]+self.tau*self.a*(Uv-self.u[0,i])
            
            if self.v[0,i+1]>=self.vpeak:
                self.v[0,i]=self.vpeak
                self.v[0,i+1]=self.c

myCell = fsCell(400)
myCell.simulate()

if __name__=='__main__':
    izh.plotMyData(myCell)
