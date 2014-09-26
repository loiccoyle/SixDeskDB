import numpy as np
import matplotlib.pyplot as plt

def plot_averem(path, seed, angle, nturns, a0, a1):

    f22=np.loadtxt('fort.22.%s.%s'%(seed,angle))
    f23=np.loadtxt('fort.23.%s.%s'%(seed,angle))
    f24=np.loadtxt('fort.24.%s.%s'%(seed,angle))
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    
    ax.plot(f22[:,0], f22[:,1], marker='+', label = "Minimum")
    ax.plot(f23[:,0], f23[:,1], marker='x', label = "Mean")
    ax.plot(f24[:,0], f24[:,1], marker='*', label = "Maximum")
    ax.legend(loc="upper left")
    ax.set_title('Averaged Amplitude(6d), %s turns' %nturns)
    ax.set_xlabel('Initial Amplitude [sigma]')
    ax.set_ylabel('Averaged Amplitude [sigma]')
    ax.set_xlim(a0,a1)
    plt.show()

def plot_distance(path, seed, angle, nturns, a0, a1):

    f13=np.loadtxt('fort.13.%s.%s'%(seed,angle))
    f26=np.loadtxt('fort.26.%s.%s'%(seed,angle))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    
    ax.plot(f13[:,0], f13[:,1], marker='+')
    ax.plot(f26[:,0], f26[:,1], marker='x', label = "Range from Chaos to Loss")
    ax.legend(loc="upper left")
    ax.set_title('Averaged Amplitude(6d), %s turns' %nturns)
    ax.set_xlabel('Initial Amplitude [sigma]')
    ax.set_ylabel('Distance in Phase Space of 2 initially close-by Particles')
    #ax.set_yscale("log", nonposy="clip")
    ax.set_xlim(a0,a1)
    plt.show()

def plot_kvar(path, seed, angle, nturns, a0, a1):
    return

def plot_maxslope(path, seed, angle, nturns, a0, a1):
    
    f12=np.loadtxt('fort.12.%s.%s'%(seed,angle))
    f26=np.loadtxt('fort.26.%s.%s'%(seed,angle))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
  
    
    ax.plot(f12[:,0], f12[:,1], marker='+')
    ax.plot(f26[:,0], f26[:,1], marker='x', label = "Range from Chaos to Loss")
    ax.legend(loc="upper left")
    ax.set_title('Averaged Amplitude(6d), %s turns' %nturns)
    ax.set_xlabel('Initial Amplitude [sigma]')
    ax.set_ylabel('Maximum Slope of Distance in Phase Space')
    ax.set_xlim(a0,a1)
    plt.show()

def plot_smear(path, seed, angle, nturns, a0, a1):

    f18=np.loadtxt('fort.18.%s.%s'%(seed,angle))
    f19=np.loadtxt('fort.19.%s.%s'%(seed,angle))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    
    ax.plot(f18[:,0], f18[:,1], marker='+', label="Horizontal" )
    ax.plot(f19[:,0], f19[:,1], marker='x', label = "Vertical")
    ax.legend(loc="upper left")
    ax.set_title('Averaged Amplitude(6d), %s turns' %nturns)
    ax.set_xlabel('Initial Amplitude [sigma]')
    ax.set_ylabel('Smear [%]')
    ax.set_xlim(a0,a1)
    plt.show()

def plot_survival(path, seed, angle, nturns, a0, a1):
   
    f15=np.loadtxt('fort.15.%s.%s'%(seed,angle))
    f14=np.loadtxt('fort.14.%s.%s'%(seed,angle))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)

    ax.plot(f15[:,0], f15[:,1], marker='+')
    ax.plot(f14[:,0], f14[:,1], marker='x', label = "Chaotic Border")
    ax.legend(loc="upper left")
    ax.set_title('Averaged Amplitude(6d), %s turns' %nturns)
    ax.set_xlabel('Initial Amplitude [sigma]')
    ax.set_ylabel('Survival Time')
    #ax.set_yscale("log", nonposy="clip")
    ax.set_xlim(a0,a1)
    
    plt.show()