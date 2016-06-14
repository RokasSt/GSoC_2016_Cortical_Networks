import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


import opencortex.build as oc

#### distribute cells for the sake of network visualization; no spatial dependence of connection probability at the moment 

popDict = {}
popDict['L23PyrRS'] = [(1000, 'L23')]
popDict['SupBasket'] = [(90, 'L23')]
popDict['SupAxAx'] = [(90, 'L23')]
popDict['L5TuftedPyrIB'] = [(800, 'L5')]
popDict['L5TuftedPyrRS']=[(200,'L5')]
popDict['L4SpinyStellate']=[(240,'L4')]
popDict['L23PyrFRB']=[(50,'L23')]
popDict['L6NonTuftedPyrRS']=[(500,'L6')]
popDict['DeepAxAx']=[(100,'L6')]
popDict['DeepBasket']=[(100,'L6')]
popDict['DeepLTSInter']=[(100,'L6')]
popDict['SupLTSInter']=[(90,'L23')]
popDict['nRT']=[(100,'Thalamus')]
popDict['TCR']=[(100,'Thalamus')]


t1=-0
t2=-250
t3=-250
t4=-200.0
t5=-300.0
t6=-300.0
t7=-200.0
t8=-200.0

boundaries={}

boundaries['L1']=[0,t1]
boundaries['L23']=[t1,t1+t2+t3]
boundaries['L4']=[t1+t2+t3,t1+t2+t3+t4]
boundaries['L5']=[t1+t2+t3+t4,t1+t2+t3+t4+t5]
boundaries['L6']=[t1+t2+t3+t4+t5,t1+t2+t3+t4+t5+t6]
boundaries['Thalamus']=[t1+t2+t3+t4+t5+t6+t7,t1+t2+t3+t4+t5+t6+t7+t8]

xs = [0,500]
zs = [0,500] 

nml_doc, network = oc.generate_network("TestTraubBuildFull")


for cellModel in popDict.keys():
    oc.add_cell_and_channels(nml_doc, '../NeuroML2/prototypes/Thalamocortical/%s.cell.nml'%cellModel,cellModel)



popObjs=oc.add_populations_in_layers(network,boundaries,popDict,xs,zs)


#extra_params=[{'pre':'L23PyrRS','post':'SupBasket','weights':[0.05],'delays':[5],'synComps':['NMDA']}]


synapseList,projArray=oc.build_connectivity(network,popObjs,"Traub_conn_data.json","../NeuroML2/prototypes/Thalamocortical/")                  

oc.add_synapses(nml_doc,'../NeuroML2/prototypes/Thalamocortical/',synapseList)

nml_file_name = '%s.net.nml'%network.id
oc.save_network(nml_doc, nml_file_name, validate=True)

oc.generate_lems_simulation(nml_doc, 
                            network, 
                            nml_file_name, 
                            duration =      300, 
                            dt =            0.025)
                                              
