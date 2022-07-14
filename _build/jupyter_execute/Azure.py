#!/usr/bin/env python
# coding: utf-8

# # Access to Quantinuum and IonQ Backends
# 
# You can get access to [Quantinuum](https://www.quantinuum.com/) and [IonQ](https://ionq.com/) simulators, emulators, and quantum machines through Microsoft Azure. When creating your workspace, first-time users automatically get free 500 (USD) Azure Quantum Credits for use with each participating quantum hardware provider. If you have consumed all the credits and need more, you can apply to the [Azure Quantum Credits program](https://microsoft.qualtrics.com/jfe/form/SV_3fl9dfFrkC3g0aG?aq_source=organic). For this Hackathon, we will use the simulators and emulators that do not use Azure Quantum Credits and hence are entirely free.
# 
# ## Apply for Azure Quantum Credit Free Trial
# 
# If you don’t have an Azure subscription, you can [create a free Azure account](https://azure.microsoft.com/en-us/free/). If you are a student and have a university email, check out the free Azure accounts [for students](https://azure.microsoft.com/en-us/free/students/). With Azure, you can create, deploy, and manage applications across multiple clouds, on-premises, and at the edge. You will get 200 (USD) Azure credit to use in other Azure services. For information regarding the application process to the Azure Quantum Credits Program see [here](https://docs.microsoft.com/en-us/azure/quantum/azure-quantum-credits?tabs=tabid-portal). Read over the details carefully
# 
# Notice that Azure credits are not the same as Azure Quantum Credits. When you create a new Azure account, you get 200 (USD) of free Azure Credits to use in your first 30 days on Microsoft services. You can only use general-purpose Azure Credits with the Microsoft providers. 3rd-party providers (providers that Microsoft doesn't own) aren't eligible. Azure Quantum Credits can be used to run programs on quantum hardware. First-time users automatically get free 500 (USD) Azure Quantum Credits on top of the 200 (USD) free Azure Credits for use with each participating quantum hardware provider. Once you have consumed all the credits, you will get error messages when submitting new jobs, and you can then upgrade to a new plan to keep using the selected quantum hardware providers.
# 
# ### Important
# You must provide a credit or debit card during the application process. Microsoft Azure will make a temporary authorization on this card, but you won’t be charged unless you move to pay-as-you-go pricing.
# 
# Although, there are no costs or charges to using your free credits, there may be some small storage costs, as the input and output of your credits jobs are stored in a storage account that you pay for. Job data is typically <1MB per job. For more details, see [Azure Blob Storage pricing](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/). 

# ## Create an Azure Quantum workspace
# 
# Follow the directions [here](https://docs.microsoft.com/en-us/azure/quantum/how-to-create-workspace?tabs=tabid-quick) to create an Azure Quantum workspace. Briefly:
# 
# 1) Sign in to the Azure portal, using the credentials for your Azure subscription.
# 
# 2) Select Create a resource and then search for Azure Quantum. You should see a tile for the Azure Quantum service on the results page.
# 
# 3) Select Azure Quantum and then select Create. This opens a form to create a workspace.
# 
# 4) Select a subscription to associate with the new workspace, i.e. Azure subscription 1
# 
# 5) Select "Quick create"
# 
# 6) Type in a Workspace name of your choice, i.e. "TKET"
# 
# 7) Region, slect your region, i.e. West US (You will see that you have access to IonQ and Quantinuum) and click create. (do read the providers' terms and conditions carefully)
# 
# 
# Deployment of your workspace usually takes about 5 minutes to complete. Once done, you should see a message "Your deployment is complete". The status and deployment details will be updated in the portal.
# 
# The important information for connecting your account to your computer is the `Resource ID` and `Location`, which you can find in the "Overview" section of your Quantum workspace.
# 

# ## Submitting a job through Azure Quantum
# 
# To submit a simple job, or quantum program, to Quantinuum or IonQ we will need to install `pytket-qsharp`. It is an extension to `pytket` that allows `pytket` circuits to be executed on remote devices and simulators via Azure Quantum. 
# 
# In order to use `pytket-qsharp` you will first need to install the `dotnet SDK (6.0)` and the `iqsharp` tool. (On some Linux systems it is also necessary to modify your PATH.)
# 1) See [this page](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) for instructions on installing the SDK on your operating system.
# 
# 2) On Linux, ensure that the dotnet tools directory is on your path. Typically this will be ~/.dotnet/tools.
# 
# 3) Open terminal and run `dotnet tool install -g Microsoft.Quantum.IQSharp`in `C:\` directory. You should get a mesaage stating that 'microsoft.quantum.iqsharp' was successfully installed.
# 
# 4) Then run `dotnet iqsharp install --user` in the terminal/
# 
# Alternatively, you can set up an environment with all the required packages using conda:
# 
# `conda create -n qsharp-env -c quantum-engineering qsharp notebook`
# 
# `conda activate qsharp-env`
# 
# Now we are ready to install `pytket-qsharp`. In your jupyter notebook run:
# 
# `pip install pytket-qsharp`
# 
# And then prepare the Q# environment by running:
# 
# `from pytket.extensions.qsharp import AzureBackend`

# In[1]:


#pip install pytket-qsharp;


# In[2]:


#from pytket.extensions.qsharp import AzureBackend


# ### Accessing Quantinuum and IonQ targets
# 
# Azure Quantum partners with third-party companies such as IonQ and Quantinuum to deliver solutions to quantum jobs. These company offerings are called providers. Each provider can offer multiple targets with different capabilities. 
# 
# Quantinuum's targets are listed in the table below:
# 
# | Target name | Target ID | Number of qubits | Description | 
# | --- | --- | --- | --- |
# | H1-1 API Validator | quantinuum.hqs-lt-s1-apival | 12 qubits | Quantinuum's "API validator." Use this to validate quantum programs before submitting to hardware or emulation on Quantinuum's platform. Free of cost. |
# | H1-1 Emulator | quantinuum.hqs-lt-s1-sim | 12 qubits | Quantinuum's quantum simulator for H1-1. Uses a noise model that is consistent with their H1-1 hardware offering. Not free of cost. |
# | H1-2 Emulator | quantinuum.hqs-lt-s2-sim | 12 qubits | Quantinuum's quantum simulator for H1-2. Uses a noise model that is consistent with their H1-2 hardware offering. Not free of cost. |
# | Quantinuum System Model: H1 Family | quantinuum.hqs-lt| 12 qubits | Quantinuum's H1 family of trapped-ion quantum computers. Not free of cost. |
# | Quantinuum System Model H1-1 | quantinuum.hqs-lt-s1| 12 qubits | Quantinuum's H1-1 computer. Not free of cost. |
# | Quantinuum System Model H-2 | quantinuum.hqs-lt-s2| 12 qubits | Quantinuum's H1-2 computer. Not free of cost. |
# 
# To learn more about Quantinuum's targets, check out [this documentation](https://docs.microsoft.com/en-us/azure/quantum/provider-quantinuum) and [this](https://docs.microsoft.com/en-us/azure/quantum/provider-honeywell). How to estimate associated costs see [here](https://docs.microsoft.com/en-us/azure/quantum/pricing?tabs=tabid-AQcredits%2Ctabid-AQcreditsQ%2Ctabid-payasgo%2Ctabid-learndevelop&pivots=ide-computing).
# 
# IonQ's targets are listed in this table:
# 
# | Target name | Target ID | Number of qubits | Description | 
# | --- | --- | --- | --- |
# | Quantum simulator | ionq.simulator | 29 qubits | IonQ's cloud-based idealized simulator. Free of cost. |
# | Quantum computer | ionq.qpu | 11 qubits | IonQ's trapped-ion quantum computer. This is real quantum hardware, not a simulation. Not for free |
# 
# To learn more about IonQ's targets, check out [this documentation](https://docs.microsoft.com/en-us/azure/quantum/provider-ionq) and how to estimate associated costs see [here](https://docs.microsoft.com/en-us/azure/quantum/pricing?tabs=tabid-AQcredits%2Ctabid-AQcreditsQ%2Ctabid-payasgo%2Ctabid-learndevelop&pivots=ide-computing).
# 
# To get access to Quantinuum's and IonQ's targets you need your Azure Quantum workspace `Resource ID` and `Loaction`.
# 
# For example, to access the "ionq.simulator" use
# 
# `backend_ionQ = AzureBackend("ionq.simulator",resourceId="your resource ID",
#    location="your location")`
#    
# To access the Qunatinuum Syntax checker you run:
# 
# `backend_Quant = AzureBackend("quantinuum.hqs-lt-s1-apival",resourceId="your resource ID",
#    location="your location")`

# ### Example `pytket` job submission to IonQ
# 
# Let's submit a circuit to IonQ's simulator, which is free. (note that commands are commented out with "#" to be inactive for compilation of this manual. Remove the "#" when you run the code below)

# In[3]:


#backend_ionQ = AzureBackend("ionq.simulator",resourceId="your resource ID",location="westus")


# Below we generate a circuit that will produce a Bell state, assuming the qubits are all initialized in the |0> state:

# In[4]:


#from pytket import Circuit
#from pytket.circuit.display import render_circuit_jupyter
#circ = Circuit(2,2)
#circ.H(0)
#circ.CX(0, 1)


# Suppose we want to measure this Bell state to get some actual results out, so let's append some `Measure` gates to the circuit. The `Circuit` class has the measure_all utility function, which appends `Measure` gates on every qubit. This function will automatically add the classical bits to the circuit if they are not already there. All of these results will be written to the default classical register ('c').

# In[5]:


#circ.measure_all()
#render_circuit_jupyter(circ)


# Check if our circuit is valid to be run.

# In[6]:


#backend_ionQ.valid_circuit(circ)


# We are now good to run this circuit on the device. After submitting, we can use the handle to check the status of the job so that we know when results are ready to be retrieved. The `circuit_status` method works for all backends and returns a `CircuitStatus` object. If we just run `get_result` straight away, the backend will wait for results to complete, blocking any other code from running.

# In[7]:


#quantum_handle = backend_ionQ.process_circuit(circ, n_shots=100)
#print(backend_ionQ.circuit_status(quantum_handle))
#quantum_counts = backend_ionQ.get_result(quantum_handle).get_counts()
#print(quantum_counts)


# ### Example `pytket` job submission to Quantinuum
# 
# Let's submit a circuit to Quantinuum's emulator, which is for a charge. (note that commands are commented out with "#" to be inactive for compilation of this manual. Remove the "#" when you run the code below)

# In[8]:


#backend_Q = AzureBackend("quantinuum.hqs-lt-s1-sim",resourceId="your resource ID",location="westus")


# In[9]:


#backend_Q.valid_circuit(circ)


# In[10]:


#quantum_handle = backend_Q.process_circuit(circ, n_shots=10)
#print(backend_Q.circuit_status(quantum_handle))
#quantum_counts = backend_Q.get_result(quantum_handle).get_counts()
#print(quantum_counts)


# Quantinuum's quotas are tracked based on the QPU usage credit unit, H1 Quantum Credit (HQC) for jobs submitted to System Model H1 quantum computer series, and eHQC for the emulators. The estimated cost for running this Bell state 10 times on a H1 emulator is 5 eHQC. (Note HQC and eHQC are computed using the same formula). Your free Azure Quantum account gives you 160 eHQC. We now have used 5 of the 160 eHQC. 
