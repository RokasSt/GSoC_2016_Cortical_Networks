#####################
### Subject to change without notice!!
#####################
#
# 
#
#
#


import opencortex
import neuroml
import pyneuroml
import pyneuroml.lems

import neuroml.writers as writers
import neuroml.loaders as loaders

from pyneuroml import pynml
from pyneuroml.lems.LEMSSimulation import LEMSSimulation

import random
import sys
import os
import shutil
import numpy as np
import json

all_cells = {}
#all_included_on_cells = {}

all_included_files = []

def add_connection(projection, 
                   id, 
                   presynaptic_population, 
                   pre_cell_id, 
                   pre_seg_id, 
                   postsynaptic_population, 
                   post_cell_id, 
                   post_seg_id,
                   delay,
                   weight,
                   pre_fraction=0.5,
                   post_fraction=0.5):
    
                   
                   
 
    connection = neuroml.ConnectionWD(id=id, \
                            pre_cell_id="../%s/%i/%s"%(presynaptic_population.id, pre_cell_id, presynaptic_population.component), \
                            pre_segment_id=pre_seg_id, \
                            pre_fraction_along=pre_fraction,
                            post_cell_id="../%s/%i/%s"%(postsynaptic_population.id, post_cell_id, postsynaptic_population.component), \
                            post_segment_id=post_seg_id,
                            post_fraction_along=post_fraction,
                            delay = '%s ms'%delay,
                            weight = weight)

    projection.connection_wds.append(connection)
    

def add_probabilistic_projection(net, 
                                 prefix, 
                                 presynaptic_population, 
                                 postsynaptic_population, 
                                 synapse_id,  
                                 connection_probability,
                                 delay = 0,
                                 weight = 1):
    
    if presynaptic_population.size==0 or postsynaptic_population.size==0:
        return None

    proj = neuroml.Projection(id="%s_%s_%s"%(prefix,presynaptic_population.id, postsynaptic_population.id), 
                      presynaptic_population=presynaptic_population.id, 
                      postsynaptic_population=postsynaptic_population.id, 
                      synapse=synapse_id)


    count = 0

    for i in range(0, presynaptic_population.size):
        for j in range(0, postsynaptic_population.size):
            if i != j or presynaptic_population.id != postsynaptic_population.id:
                if connection_probability>= 1 or random.random() < connection_probability:
                    
                    add_connection(proj, 
                                   count, 
                                   presynaptic_population, 
                                   i, 
                                   0, 
                                   postsynaptic_population, 
                                   j, 
                                   0,
                                   delay = delay,
                                   weight = weight)
                    count+=1

    net.projections.append(proj)

    return proj
    
def add_advanced_projection(net, 
                            proj_counter,
                            presynaptic_population, 
                            postsynaptic_population, 
                            synapseList,  
                            connection_probability,
                            postTargetParams,
                            delaysInfo=None,
                            weightsInfo=None):
                            

    if presynaptic_population.size==0 or postsynaptic_population.size==0:
        return None
    
    proj_array={}
    syn_counter=0
    for synapse_id in synapseList:
        proj = neuroml.Projection(id="Proj%dsyn%d_%s_%s"%(proj_counter,syn_counter,presynaptic_population.id, postsynaptic_population.id), 
                      presynaptic_population=presynaptic_population.id, 
                      postsynaptic_population=postsynaptic_population.id, 
                      synapse=synapse_id)
        syn_counter+=1              
        proj_array[synapse_id]=proj

    count = 0

    for i in range(0, presynaptic_population.size):
        for j in range(0, postsynaptic_population.size):
            if i != j or presynaptic_population.id != postsynaptic_population.id:
                if connection_probability>= 1 or random.random() < connection_probability:
                   target_array=get_unique_membrane_points(postTargetParams)
                   #### at the moment get_unique_mebrane_points is only used to pick up the single target segment id on the postsynaptic cell
                   post_seg_id=0
                   if len(target_array)==1:
                      post_seg_id=int(target_array[0][0])
                   for synapse_id in synapseList:
                       delay=0
                       weight=1
                       if delaysInfo !=None:
                          for synapseComp in delaysInfo.keys():
                              if synapseComp in synapse_id:
                                 delay=delaysInfo[synapseComp]
                       if weightsInfo !=None:
                          for synapseComp in weightsInfo.keys():
                              if synapseComp in synapse_id:
                                 weight=weightsInfo[synapseComp]
                       
                       add_connection(proj_array[synapse_id], 
                                      count, 
                                      presynaptic_population, 
                                      i, 
                                      0, 
                                      postsynaptic_population, 
                                      j, 
                                      post_seg_id,
                                      delay = delay,
                                      weight = weight)
                   count+=1
                   
    for synapse_id in synapseList:
        net.projections.append(proj_array[synapse_id])

    return proj_array, proj_counter
 
############################################################################################################################# 
def parse_extra_params(extra_params,pre_pop,post_pop):

    prob_dict=None
    weights=None
    delays=None
    for params_set in range(0,len(extra_params)):
        if extra_params[params_set]['pre']==pre_pop and extra_params[params_set]['post']==post_pop:
           if 'ProbDict' in extra_params[params_set].keys():
              prob_dict=extra_params[params_set]['ProbDict']
           if 'weights' in extra_params[params_set].keys() and 'synComps' in extra_params[params_set].keys():
              if isinstance(extra_params[params_set]['synComps'],list) and isinstance(extra_params[params_set]['weights'],list):
                 if len(extra_params[params_set]['synComps'])==len(extra_params[params_set]['weights']):
                    weights={}
                    for syn_comp in range(0,len(extra_params[params_set]['synComps'])):
                        weights[extra_params[params_set]['synComps'][syn_comp]]=extra_params[params_set]['weights'][syn_comp]
           if 'delays' in extra_params[params_set].keys() and 'synComps' in extra_params[params_set].keys():
              if isinstance(extra_params[params_set]['synComps'],list) and isinstance(extra_params[params_set]['delays'],list):
                 if len(extra_params[params_set]['synComps'])==len(extra_params[params_set]['delays']):
                    delays={}
                    for syn_comp in range(0,len(extra_params[params_set]['synComps'])):
                        delays[extra_params[params_set]['synComps'][syn_comp][syn_comp]]=extra_params[params_set]['delays'][syn_comp]
                        
                        
    return prob_dict, weights, delays
############################################################################################################################


def use_conn_summary(net,popObjects,connFile,pathToCells,extra_params=None):

    final_synapse_list=[]
    final_proj_array=[]
    with open(connFile,'r') as json_conn:
         conn_data=json.load(json_conn)
    proj_counter=0
    for prePop in popObjects.keys():
    
        for subset_pre in popObjects[prePop].keys():
        
            preCellObject=popObjects[prePop][subset_pre]
            
            for postPop in popObjects.keys():
            
                for subset_post in popObjects[postPop].keys():
                
                    postCellObject=popObjects[postPop][subset_post]
            
                    for stored_proj in range(0,len(conn_data)):
                    
                        projInfo=conn_data[stored_proj]
                        
                        if projInfo['PreCellGroup']==prePop and projInfo['PostCellGroup']==postPop:
                    
                           connP=float(projInfo['NumPerPostCell'])/preCellObject['size']
                           
                           target_comp_groups=projInfo['LocOnPostCell']
                           
                           if extra_params != None:
                              prob_dict, weights, delays=parse_extra_params(extra_params,prePop,postPop)
                           else:
                              prob_dict=None
                              weights=None
                              delays=None     
                           if prob_dict ==None:
                              prob_dict={}
                                    
                           if not isinstance(target_comp_groups,list):
                              prob_dict[target_comp_groups]=1
                              target_comp_groups=[target_comp_groups]
                              
                           target_segments=extract_seg_ids({'cellID':postPop,'SegOrSegGroupList':target_comp_groups,'TargetingMode':'segGroups','pathToCell':pathToCells})
                           postTargetParams={'TargetDict':target_segments,'ProbDict':prob_dict,'NumOfUniquePoints':1}
                           synapseList=projInfo['SynapseList']                                                
                           final_synapse_list.extend(projInfo['SynapseList'])
                           compound_proj=add_advanced_projection(net, 
                                                        proj_counter,
                                                        preCellObject['popObj'], 
                                                        postCellObject['popObj'], 
                                                        synapseList,  
                                                        connP,
                                                        postTargetParams,
                                                        delaysInfo=delays,
                                                        weightsInfo=weights)
                                                        
                           proj_counter+=1                      
                           final_proj_array.extend(compound_proj)
          
    final_synapse_list=np.unique(final_synapse_list)
                          
    return final_synapse_list, final_proj_array
                           
                           
                        
    

############################################################################################################################

def extract_seg_ids(input_dict):
    
    cellID=input_dict['cellID']
    targetCompArray=input_dict['SegOrSegGroupList']
    targetingMode=input_dict['TargetingMode']
    pathToNML=input_dict['pathToCell']
    
    '''input_dict stores a unique cellID, an array of target compartment names (e.g. segment group names or individual segment names), a targeting mode - "segments" or "segGroup", and a path to the cell.nml'''

   
    
    loaded_cell_array={}
    cell_nml_file = '%s.cell.nml'%cellID
    if pathToNML != None:
       document_cell = neuroml.loaders.NeuroMLLoader.load(pathToNML+cell_nml_file)
    else:
       document_cell=neuroml.loaders.NeuroMLLoader.load(cell_nml_file)
    loaded_cell_array[cellID]=document_cell.cells[0]
    #print("Loaded morphology file from: %s, with id: %s"%(cell_nml_file, loaded_cell_array[cellID].id))
    segment_id_array=[]
    segment_group_array={}
    cell_segment_array=[]
    #print("Now printing segment ids")
    for segment in loaded_cell_array[cellID].morphology.segments:
        segment_id_array.append(segment.id)   
        #print segment.id
        #print segment.name
        # the block below is added for handling targeting at the segment level
        segment_name_and_id=[]
        segment_name_and_id.append(segment.name)
        segment_name_and_id.append(segment.id)
        cell_segment_array.append(segment_name_and_id)
    #print("Now printing segment group ids their segments and groups")
    for segment_group in loaded_cell_array[cellID].morphology.segment_groups:
        pooled_segment_group_data={}
        segment_list=[]
        segment_group_list=[]
        #print segment_group.id
        for member in segment_group.members:
            segment_list.append(member.segments)
            #print member.segments
        for included_segment_group in segment_group.includes:
            segment_group_list.append(included_segment_group.segment_groups)
                   
           
        pooled_segment_group_data["segments"]=segment_list
        pooled_segment_group_data["groups"]=segment_group_list
        segment_group_array[segment_group.id]=pooled_segment_group_data  
               
        #print segment_group_array[segment_group.id]["segments"]
               
        #print segment_group_array[segment_group.id]["groups"]
    cell_segment_group={} 
    cell_segment_group[cellID]=segment_group_array

    target_segment_array={}

    if targetingMode=="segments":
       
       for segment_counter in range(0,len(cell_segment_array)):
           for target_segment in range(0,len(targetCompArray)):
               if cell_segment_array[segment_counter][0]==targetCompArray[target_segment]: 
                  target_segment_array[targetCompArray[target_segment]]=[cell_segment_array[segment_counter][1]]
          
                          
    if targetingMode=="segGroups":
       
       for segment_group in cell_segment_group[cellID].keys():
           for target_group in range(0,len(targetCompArray)):
               if targetCompArray[target_group]==segment_group:
                  segment_target_array=[]
                  if cell_segment_group[cellID][segment_group]["segments"] !=[]:
                     for segment in cell_segment_group[cellID][segment_group]["segments"]:
                         segment_target_array.append(segment)
                  if cell_segment_group[cellID][segment_group]["groups"] !=[]:
                     for included_segment_group in cell_segment_group[cellID][segment_group]["groups"]:
                         for included_segment_group_segment in cell_segment_group[cellID][included_segment_group]["segments"]:
                             segment_target_array.append(included_segment_group_segment)
                  target_segment_array[targetCompArray[target_group]]=segment_target_array
          
    

    return target_segment_array        
######################################################################################
def get_unique_membrane_points(input_dict):


    seg_specifications=input_dict['TargetDict']
    prob_dict=input_dict['ProbDict']
    no_of_points_per_cell=input_dict['NumOfUniquePoints']
    
    '''input_dict stores the 'TargetDict' which should be in the format of the output of the function extract_seg_ids; the 'ProbDict' stores the corresponding targeting probabilities of these groups/individual segments; no_of_points_per_cell is the number of unique membrane points that has to be found by the function.'''
    

    target_points_per_cell=np.zeros([no_of_points_per_cell,2])
    
    x=0
    while x==0:
        seg_search_array=[]
        fraction_along_search_array=[]
        y=0
        while y != no_of_points_per_cell:
            segment_group=random.sample(range(0,len(seg_specifications.keys())),1)
            segment_group=segment_group[0]
            if seg_specifications.keys()[segment_group] in prob_dict.keys() :
               if random.random() <  prob_dict[seg_specifications.keys()[segment_group]]:
                  seg_or_seg_group=seg_specifications.keys()[segment_group]
                  for specified_target in seg_specifications.keys():
                      if specified_target==seg_or_seg_group:
                         segment_ids=seg_specifications[specified_target]
                         segment_id=random.sample(segment_ids,1)
                         segment_id=segment_id[0]
                         seg_search_array.append(segment_id)
                         fraction_along_search_array.append(random.random())
                         y=y+1
                         break
            if len(fraction_along_search_array)==len(set(fraction_along_search_array)):
                x=1
             
        for point in range(0,no_of_points_per_cell):
            target_points_per_cell[point,0]=seg_search_array[point]
            target_points_per_cell[point,1]=fraction_along_search_array[point]
    
    
    return target_points_per_cell


#######################################################################################

def include_cell_prototype(nml_doc,cell_nml2_path):
    
    nml_doc.includes.append(neuroml.IncludeType(cell_nml2_path)) 
    
# Helper method which will be made redundant with a better generated Python API...
def _get_cells_of_all_known_types(nml_doc):
    
    all_cells = []
    all_cells.extend(nml_doc.cells)
    all_cells.extend(nml_doc.izhikevich_cells)
    all_cells.extend(nml_doc.izhikevich2007_cells)
    all_cells.extend(nml_doc.iaf_cells)
    all_cells.extend(nml_doc.iaf_ref_cells)
    
    return all_cells

# Helper method which will be made redundant with a better generated Python API...
def _get_channels_of_all_known_types(nml_doc):
    
    all_channels = []
    all_channels.extend(nml_doc.ion_channel)
    all_channels.extend(nml_doc.ion_channel_hhs)
    all_channels.extend(nml_doc.ion_channel_kses)
    all_channels.extend(nml_doc.decaying_pool_concentration_models)
    all_channels.extend(nml_doc.fixed_factor_concentration_models)
    all_channels.extend(nml_doc.ComponentType)
    
    return all_channels

# Helper method which will be made redundant with a better generated Python API...
def _add_to_neuroml_doc(nml_doc, element):
    
    if isinstance(element, neuroml.Cell):
        nml_doc.cells.append(element)
    elif isinstance(element, neuroml.IzhikevichCell):
        nml_doc.izhikevich_cells.append(element)
    elif isinstance(element, neuroml.Izhikevich2007Cell):
        nml_doc.izhikevich2007_cells.append(element)
    elif isinstance(element, neuroml.IafRefCell):
        nml_doc.iaf_ref_cells.append(element)
    elif isinstance(element, neuroml.IafCell):
        nml_doc.iaf_cells.append(element)
        
    elif isinstance(element, neuroml.IonChannelKS):
        nml_doc.ion_channel_kss.append(element)
    elif isinstance(element, neuroml.IonChannelHH):
        nml_doc.ion_channel_hhs.append(element)
    elif isinstance(element, neuroml.IonChannel):
        nml_doc.ion_channel.append(element)
    elif isinstance(element, neuroml.FixedFactorConcentrationModel):
        nml_doc.fixed_factor_concentration_models.append(element)
    elif isinstance(element, neuroml.ComponentType):
        nml_doc.ComponentType.append(element)
        
    
def _copy_to_dir_for_model(nml_doc,file_name):
    
    dir_for_model = nml_doc.id
    if not os.path.isdir(dir_for_model):
        os.mkdir(dir_for_model)
    
    shutil.copy(file_name, dir_for_model)
    
    
def add_cell_and_channels(nml_doc,cell_nml2_path, cell_id):
    
    nml2_doc_cell = pynml.read_neuroml2_file(cell_nml2_path, include_includes=False)
    
    for cell in _get_cells_of_all_known_types(nml2_doc_cell):
        if cell.id == cell_id:
            all_cells[cell_id] = cell
            
            _copy_to_dir_for_model(nml_doc,cell_nml2_path)
            new_file = '%s/%s.cell.nml'%(nml_doc.id,cell_id)
            nml_doc.includes.append(neuroml.IncludeType(new_file)) 
            all_included_files.append(new_file)
            
            for included in nml2_doc_cell.includes:
                #Todo replace... quick & dirty...
                old_loc = '%s/%s'%(os.path.dirname(os.path.abspath(cell_nml2_path)), included.href)
                print old_loc
                _copy_to_dir_for_model(nml_doc,old_loc)
                new_loc = '%s/%s'%(nml_doc.id,included.href)
                nml_doc.includes.append(neuroml.IncludeType(new_loc))
                all_included_files.append(new_loc)
                
                
#########################################
def add_synapses(nml_doc,nml2_path,synapseList):
    
   for synapse in synapseList: 
       _copy_to_dir_for_model(nml_doc,nml2_path+"%s.synapse.nml"%synapse)
       new_file = '%s/%s.synapse.nml'%(nml_doc.id,synapse)
       nml_doc.includes.append(neuroml.IncludeType(new_file)) 
            

#########################################
    
def add_exp_two_syn(nml_doc, id, gbase, erev, tau_rise, tau_decay):
    # Define synapse
    syn0 = neuroml.ExpTwoSynapse(id=id, gbase=gbase,
                                 erev=erev,
                                 tau_rise=tau_rise,
                                 tau_decay=tau_decay)
                                 
    nml_doc.exp_two_synapses.append(syn0)
    
    return syn0

def add_poisson_firing_synapse(nml_doc, id, average_rate, synapse_id):

    pfs = neuroml.PoissonFiringSynapse(id=id,
                                       average_rate=average_rate,
                                       synapse=synapse_id, 
                                       spike_target="./%s"%synapse_id)
                                       
    nml_doc.poisson_firing_synapses.append(pfs)

    return pfs

def add_pulse_generator(nml_doc, id, delay, duration, amplitude):

    pg = neuroml.PulseGenerator(id=id,
                                delay=delay,
                                duration=duration,
                                amplitude=amplitude)
                                       
    nml_doc.pulse_generators.append(pg)

    return pg
    
    
def add_single_cell_population(net, pop_id, cell_id, x=0, y=0, z=0, color=None):
    
    pop = neuroml.Population(id=pop_id, component=cell_id, type="populationList", size=1)
    if color is not None:
        pop.properties.append(Property("color",color))
    net.populations.append(pop)

    inst = neuroml.Instance(id=0)
    pop.instances.append(inst)
    inst.location = neuroml.Location(x=x, y=y, z=z)

    return pop
    
    
def add_population_in_rectangular_region(net, pop_id, cell_id, size, x_min, y_min, z_min, x_size, y_size, z_size, color=None):
    
    pop = neuroml.Population(id=pop_id, component=cell_id, type="populationList", size=size)
    if color is not None:
        pop.properties.append(Property("color",color))
    net.populations.append(pop)

    for i in range(0, size) :
            index = i
            inst = neuroml.Instance(id=index)
            pop.instances.append(inst)
            inst.location = neuroml.Location(x=str(x_min +(x_size)*random.random()), y=str(y_min +(y_size)*random.random()), z=str(z_min+(z_size)*random.random()))
    
    return pop

################################################################################    
    
def add_populations_in_layers(net,boundaryDict,popDict,x_vector,z_vector): 

  
# popDict are unique cell model ids; each entry stores a tuple of size and Layer index; these index strings make up the keys() of boundaryDict;
# boundaryDict have layer pointers as keys; each entry stores the left and right bound of the layer in the list format , e.g. [L3_min, L3_max]
   return_pops={}
   

   for cellModel in popDict.keys():

       # the same cell model is allowed to be distributed in multiple layers
       for subset in range(0,len(popDict[cellModel])):
           size, layer = popDict[cellModel][subset]
    
           if size>0:
              return_pops[cellModel]={}
              xl=x_vector[1]-x_vector[0]
              yl=boundaryDict[layer][1]-boundaryDict[layer][0]
              zl=z_vector[1]-z_vector[0]
          
              pop=add_population_in_rectangular_region(net,"%s_%s"%(cellModel,layer),cellModel,size,x_vector[0],boundaryDict[layer][0],z_vector[0],xl,yl,zl)
         
              return_pops[cellModel][layer]={}
              return_pops[cellModel][layer]['popObj']=pop
              return_pops[cellModel][layer]['size']=size
   
   return return_pops
          



#################################################################################




def add_inputs_to_population(net, id, population, input_comp_id, all_cells=False, only_cells=None):
    
    if all_cells and only_cells is not None:
        opencortex.print_comment_v("Error! Method opencortex.build.%s() called with both arguments all_cells and only_cells set!"%sys._getframe().f_code.co_name)
        exit(-1)
        
    cell_ids = []
    
    if all_cells:
        cell_ids = range(population.size)
    if only_cells is not None:
        if only_cells == []:
            return
        cell_ids = only_cells
        
    input_list = neuroml.InputList(id=id,
                         component=input_comp_id,
                         populations=population.id)
    count = 0
    for cell_id in cell_ids:
        input = neuroml.Input(id=count, 
                      target="../%s/%i/%s"%(population.id, cell_id, population.component), 
                      destination="synapses")  
        input_list.input.append(input)
        count+=1
        
                         
    net.input_lists.append(input_list)
    
    return input_list
    

def generate_network(reference, seed=1234):
    
    nml_doc = neuroml.NeuroMLDocument(id='%s'%reference)
    
    random.seed(seed)
    
    nml_doc.properties.append(neuroml.Property("Python random seed",seed))
    
    # Create network
    network = neuroml.Network(id='%s'%reference)
    nml_doc.networks.append(network)

    opencortex.print_comment_v("Created NeuroMLDocument containing a network with id: %s"%reference)
    
    return nml_doc, network


def save_network(nml_doc, nml_file_name, validate=True, comment=True):

    info = "\n\nThis NeuroML 2 file was generated by OpenCortex v%s using: \n"%(opencortex.__version__)
    info += "    libNeuroML v%s\n"%(neuroml.__version__)
    info += "    pyNeuroML v%s\n\n    "%(pyneuroml.__version__)
    
    if nml_doc.notes:
        nml_doc.notes += info
    else:
        nml_doc.notes = info
    
    writers.NeuroMLWriter.write(nml_doc, nml_file_name)
    
    opencortex.print_comment_v("Saved NeuroML with id: %s to %s"%(nml_doc.id, nml_file_name))
    
    if validate:
        from pyneuroml.pynml import validate_neuroml2

        passed = validate_neuroml2(nml_file_name)
        
        if passed:
            opencortex.print_comment_v("Generated NeuroML file is valid")
        else:
            opencortex.print_comment_v("Generated NeuroML file is NOT valid!")
            
            
def generate_lems_simulation(nml_doc, 
                             network, 
                             nml_file_name, 
                             duration, 
                             dt, 
                             target_dir = '.',
                             include_extra_files = [],
                             gen_plots_for_all_v = True,
                             plot_all_segments = False,
                             gen_plots_for_quantities = {},   #  Dict with displays vs lists of quantity paths
                             gen_plots_for_only_populations = [],   #  List of populations, all pops if = []
                             gen_saves_for_all_v = True,
                             save_all_segments = False,
                             gen_saves_for_only_populations = [],  #  List of populations, all pops if = []
                             gen_saves_for_quantities = {},   #  Dict with file names vs lists of quantity paths
                             seed=12345):
                                 
    lems_file_name = "LEMS_%s.xml"%network.id
    
    include_extra_files.extend(all_included_files)
    
    pyneuroml.lems.generate_lems_file_for_neuroml("Sim_%s"%network.id, 
                                   nml_file_name, 
                                   network.id, 
                                   duration, 
                                   dt, 
                                   lems_file_name,
                                   target_dir,
                                   include_extra_files = include_extra_files,
                                   gen_plots_for_all_v = gen_plots_for_all_v,
                                   plot_all_segments = plot_all_segments,
                                   gen_plots_for_quantities = gen_plots_for_quantities, 
                                   gen_plots_for_only_populations = gen_plots_for_only_populations,  
                                   gen_saves_for_all_v = gen_saves_for_all_v,
                                   save_all_segments = save_all_segments,
                                   gen_saves_for_only_populations = gen_saves_for_only_populations,
                                   gen_saves_for_quantities = gen_saves_for_quantities,
                                   seed=seed)

    return lems_file_name
