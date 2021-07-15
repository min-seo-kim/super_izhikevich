import izhikevich_cell as izh

class lsCell(izh.izhCell):
    def __init__(self, stimVal):
        # Define Neuron Parameters
        super().__init__(stimVal)
        self.celltype='Late Spiking'
        self.C=20
        self.vr=-66
        self.vt=-40
        self.k=0.3
        self.a=0.17
        self.b=5
        self.c=-45 
        self.d=100 
        self.vpeak=30
        
    def simulate(self):
        # Run the simulation
        self.vd=self.v.copy()
        for i in range(0,self.n-1):
            self.v[0,i+1]=self.v[0,i]+self.tau*(self.k*(self.v[0,i]-self.vr)*(self.v[0,i]-self.vt)+1.2*(self.vd[0,i]-self.v[0,i])-self.u[0,i]+self.I[0,i])/self.C
            self.u[0,i+1]=self.u[0,i]+self.tau*self.a*(self.b*(self.v[0,i]-self.vr)-self.u[0,i])
            
            if self.v[0,i+1]>=self.vpeak:
                self.v[0,i]=self.vpeak
                self.v[0,i+1]=self.c
                self.u[0,i+1]=self.u[0,i+1]+self.d
                self.vd[0,i+1]=self.vd[0,i]+self.tau*(0.01*(self.v[0,i]-self.vd[0,i]))

myCell = lsCell(300)
myCell.simulate()

if __name__=='__main__':
    izh.plotMyData(myCell)
