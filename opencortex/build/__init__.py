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
import math
import operator

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


##################################################################################################################    
def add_divergent_projection(net,
                             proj_array,
                             presynaptic_population,
                             postsynaptic_population,
                             synapseList,
                             segTargetDict,
                             subsetDict,
                             minimalProbRange,
                             delaysInfo=None,
                             weightsInfo=None):
                             
    targetDict=postTargetingSpec['TargetDict']
    subsets=postTargetingSpec['ConnSubsets']
    minimalProbRange=postTargetingSpec['MinimalProbRange']
    total_given=sum(subsets.values())
    count=0
    for i in range(0, presynaptic_population.size):
        
        postsynaptic_cells=random.sample(range(0,postsynaptic_population.size),total_given)
        
        target_seg_array=get_target_segments(segTargetDict,subsets,minimalProbRange)
        
        for j in postsynaptic_cells:
            if i != j or presynaptic_population.id != postsynaptic_population.id:
               post_seg_id=target_seg_array[0]
               del target_seg_array[0]
               fraction_along=random.random()                 
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
                                  weight = weight,
                                  post_fraction=fraction_along)
               count+=1
                   
    for synapse_id in synapseList:
        net.projections.append(proj_array[synapse_id])

    return proj_array                         
    
############################################################################################################    

def add_convergent_projection(net,
                              proj_array,
                              presynaptic_population,
                              postsynaptic_population,
                              synapseList,
                              postTargetingSpec,
                              delaysInfo=None,
                              weightsInfo=None):
                              
    targetDict=postTargetingSpec['TargetDict']
    subsets=postTargetingSpec['ConnSubsets']
    minimalProbRange=postTargetingSpec['MinimalProbRange']
    total_given=sum(subsets.values())
    count=0
    for i in range(0, postsynaptic_population.size):
    
        presynaptic_cells=random.sample(range(0,postsynaptic_population.size),total_given)
        
        target_seg_array=get_target_segments(targetDict,subsets,minimalProbRange)
        
        membrane_points=get_unique_membrane_points(target_seg_array)
        
        targetSegList=membrane_points.keys()
        
        for j in presynaptic_cells:
            if i != j or presynaptic_population.id != postsynaptic_population.id:
               found_target=False
               fraction=0.5
               post_seg_id=0
               if membrane_points.values() != []:
                  while not found_target:
                     target_seg_id=random.sample(targetSegList,1)[0]
                     if membrane_points[target_seg_id] !=[]:
                        fraction=membrane_points[target_seg_id][0]
                        post_seg_id=int(target_seg_id)
                        del membrane_points[target_seg_id][0]
                        found_target=True
                     else:
                        targetSegList.remove(target_seg_id)
                                
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
                                  j, 
                                  0, 
                                  postsynaptic_population, 
                                  i, 
                                  post_seg_id,
                                  delay = delay,
                                  weight = weight,
                                  post_fraction=fraction)
               count+=1
                   
    for synapse_id in synapseList:
        net.projections.append(proj_array[synapse_id])

    return proj_array
    
#########################################################################################
    
def add_divergent_spatial_projection(net,
                                     proj_array,
                                     presynaptic_population,
                                     postsynaptic_population,
                                     synapseList,
                                     postTargetingSpec,
                                     distanceParams,
                                     delaysInfo,
                                     weightsInfo):
                                     
    targetDict=postTargetingSpec['TargetDict']
    subsets=postTargetingSpec['ConnSubsets']
    minimalProbRange=postTargetingSpec['MinimalProbRange']
    total_given=sum(subsets.values())
    distanceRule=distanceParams['DistDependConn']
    prePositions=distanceParams['prePositions']
    postPositions=distanceParams['postPositions']
    count=0
    for i in range(0, presynaptic_population.size):
        preCellPosition=prePositions[i]
        target_seg_array=get_target_segments(targetDict,subsets,minimalProbRange)
        conn_counter=0
        for j in range(0,postsynaptic_population.size):
            if i != j or presynaptic_population.id != postsynaptic_population.id:
               postCellPosition=postPositions[j]
               r=math.sqrt(sum([(a - b)**2 for a,b in zip(preCellPosition,postCellPosition)])) 
               if random.random() < eval(distanceRule):
                  conn_counter+=1
                  post_seg_id=target_seg_array[0]
                  del target_seg_array[0]
                  fraction_along=random.random()                 
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
                                     weight = weight,
                                     post_fraction=fraction_along)
                  count+=1
               if conn_counter==total_given:
                  break
                   
    for synapse_id in synapseList:
        net.projections.append(proj_array[synapse_id])

    return proj_array               

###########################################################################################################

def add_convergent_spatial_projection(net,
                                     proj_array,
                                     presynaptic_population,
                                     postsynaptic_population,
                                     synapseList,
                                     postTargetingSpec,
                                     distanceParams,
                                     delaysInfo,
                                     weightsInfo):
                                     
    targetDict=postTargetingSpec['TargetDict']
    subsets=postTargetingSpec['ConnSubsets']
    minimalProbRange=postTargetingSpec['MinimalProbRange']
    total_given=sum(subsets.values())
    distanceRule=distanceParams['DistDependConn']
    prePositions=distanceParams['prePositions']
    postPositions=distanceParams['postPositions']
    count=0
    for i in range(0, postsynaptic_population.size):
    
        postCellPosition=postPositions[i]
        conn_counter=0
              
        target_seg_array=get_target_segments(targetDict,subsets,minimalProbRange)
        
        membrane_points=get_unique_membrane_points(target_seg_array)
        
        targetSegList=membrane_points.keys()
        
        for j in range(0,presynaptic_population.size):
            preCellPosition=prePositions[j]
            if i != j or presynaptic_population.id != postsynaptic_population.id:
               r=math.sqrt(sum([(a - b)**2 for a,b in zip(preCellPosition,postCellPosition)])) 
               if random.random() < eval(distanceRule):
                  conn_counter+=1
                  found_target=False
                  fraction=0.5
                  post_seg_id=0
                  if membrane_points.values() != []:
                     while not found_target:
                        target_seg_id=random.sample(targetSegList,1)[0]
                        if membrane_points[target_seg_id] !=[]:
                           fraction=membrane_points[target_seg_id][0]
                           post_seg_id=int(target_seg_id)
                           del membrane_points[target_seg_id][0]
                           found_target=True
                        else:
                           targetSegList.remove(target_seg_id)
                                
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
                                     j, 
                                     0, 
                                     postsynaptic_population, 
                                     i, 
                                     post_seg_id,
                                     delay = delay,
                                     weight = weight,
                                     post_fraction=fraction)
                  count+=1
               if conn_counter==total_given:
                  break
                   
    for synapse_id in synapseList:
        net.projections.append(proj_array[synapse_id])

    return proj_array                       
                                     
     

############################################################################################################################
def make_target_dict(cell_object,
                     target_segs):
    '''This method constructs the dictionary whose keys are the names of target segment groups or individual segments and the corresponding values are the length dictionaries
    returned by the get_seg_lengths.'''
    targetDict={}
    for target in target_segs.keys():
        targetDict[target]=get_seg_lengths(cell_object,target_segs[target])
    return targetDict
    
############################################################################################################################

def get_target_cells(pop_size,
                     fraction_to_target,
                     cell_positions=None,
                     list_of_xvectors=None,
                     list_of_yvectors=None,
                     list_of_zvectors=None):
                     
    '''This method returns the list of target cells according to which fraction of randomly selected cells is targeted and whether these cells are localized in the specific 
    rectangular regions of the network. These regions are specified by list_of_xvectors, list_of_yvectors and list_of_zvectors. These lists must have the same length.
    
    The input variable list_of_xvectors stores the lists whose elements define the left and right margins of the target rectangular regions along the x dimension.
    
    Similarly, the input variables list_of_yvectors and list_of_zvectors store the lists whose elements define the left and right margins of the target rectangular regions along
    the y and z dimensions, respectively.'''
    
    if cell_positions==None:
    
       target_cells=random.sample(range(pop_size),int(round(fraction_to_target*pop_size)   )   )
       
    else:
       
       region_specific_targets_per_cell_group=[]
       
       for region in range(0,len(list_of_xvectors)):
       
           for cell in range(0,pop_size):
           
               if (list_of_xvectors[region][0] <  cell_positions[cell,0]) and \
                  (cell_positions[cell,0] < list_of_xvectors[region][1]):
               
               if (list_of_yvectors[region][0] <  cell_positions[cell,1]) and \
                  (cell_positions[cell,1] <  list_of_yvectors[region][1]) :
                
                  if (list_of_zvectors[region][0] <  cell_positions[cell,2]) and \
                     (cell_positions[cell,2] < list_of_zvectors[region][1]):
                     
                     region_specific_targets_per_cell_group.append(cell)
                                                                        
    target_cells=random.sample(region_specific_targets_per_cell_group,int(round(fraction_to_target*len(region_specific_targets_per_cell_group))))
                                                                   

    return target_cells

################################################################################################################################

def get_seg_lengths(cell_object,
                    target_segments):
                    
    '''This method constructs the dictionary whose keys are the ids of target segments on the cell specified by the cell_object and the corresponding values are the lengths of 
    individual segments. The methods returns this newly generated dictionary and the total length of segments.'''
    
    lengthDict={}
    totalLength=0
    for seg in cell_object.morphology.segments:
        for target_seg in target_segments:
            if target_seg==seg.id:
            
               if seg.distal !=None:
                  xd=seg.distal.x
                  yd=seg.distal.y
                  zd=seg.distal.z
                  
               if seg.proximal !=None:
                  xp=seg.proximal.x
                  yp=seg.proximal.y
                  zp=seg.proximal.z
               else:
                  if seg.parent != None:
                     get_segment_parent=seg.parent
                     get_segment_parent_id=get_segment_parent.segments
                     for segment_parent in cellObject.morphology.segments:
                         if segment_parent.id==get_segment_parent_id:
                            xp=segment_parent.distal.x
                            yp=segment_parent.distal.y
                            zp=segment_parent.distal.z
               dist=[xd,yd,zd]
               prox=[xp,yp,zp] 
               length=math.sqrt(sum([(a - b)**2 for a,b in zip(dist,prox)])) 
               lengthDict[str(target_seg)]=length
               totalLength=totalLength+length
 
    return lengthDict, totalLength
############################################################################################################################


def extract_seg_ids(cell_object,
                    target_compartment_array,
                    targeting_mode):
                    
    '''This method extracts the segment ids that map on the target segment groups or individual segments. 
       cell_object is the loaded cell object using neuroml.loaders.NeuroMLLoader, target_compartment_array is an array of target compartment names (e.g. segment group names or individual segment names) and targeting_mode is one of the strings: "segments" or "segGroup". '''
    
    segment_id_array=[]
    segment_group_array={}
    cell_segment_array=[]
    print("Now printing segment ids")
    for segment in cell_object.morphology.segments:
        segment_id_array.append(segment.id)   
        segment_name_and_id=[]
        segment_name_and_id.append(segment.name)
        segment_name_and_id.append(segment.id)
        cell_segment_array.append(segment_name_and_id)
    for segment_group in loaded_cell_array[cellID].morphology.segment_groups:
        pooled_segment_group_data={}
        segment_list=[]
        segment_group_list=[]
        for member in segment_group.members:
            segment_list.append(member.segments)
        for included_segment_group in segment_group.includes:
            segment_group_list.append(included_segment_group.segment_groups)
                   
           
        pooled_segment_group_data["segments"]=segment_list
        pooled_segment_group_data["groups"]=segment_group_list
        segment_group_array[segment_group.id]=pooled_segment_group_data  
               
    cell_segment_group={} 
    cell_segment_group[cellID]=segment_group_array

    target_segment_array={}

    if targetingMode=="segments":
       
       for segment_counter in range(0,len(cell_segment_array)):
           for target_segment in range(0,len(target_compartment_array)):
               if cell_segment_array[segment_counter][0]==target_compartment_array[target_segment]: 
                  target_segment_array[target_compartment_array[target_segment]]=[cell_segment_array[segment_counter][1]]
          
                          
    if targetingMode=="segGroups":
       
       for segment_group in cell_segment_group[cellID].keys():
           for target_group in range(0,len(target_compartment_array)):
               if target_compartment_array[target_group]==segment_group:
                  segment_target_array=[]
                  if cell_segment_group[cellID][segment_group]["segments"] !=[]:
                     for segment in cell_segment_group[cellID][segment_group]["segments"]:
                         segment_target_array.append(segment)
                  if cell_segment_group[cellID][segment_group]["groups"] !=[]:
                     for included_segment_group in cell_segment_group[cellID][segment_group]["groups"]:
                         for included_segment_group_segment in cell_segment_group[cellID][included_segment_group]["segments"]:
                             segment_target_array.append(included_segment_group_segment)
                  target_segment_array[target_compartment_array[target_group]]=segment_target_array
          
    

    return target_segment_array        
######################################################################################
def get_target_segments(seg_specifications,subset_dict,minimalProbRange):
    
    target_segs_per_cell=[]
    for target_group in subset_dict.keys():
        print target_group
        no_per_target_group=subset_dict[target_group]
        print seg_specifications.keys()
        if target_group in seg_specifications.keys():
           equal_probabilities=check_seg_probabilities(seg_specifications[target_group],minimalProbRange)
           if equal_probabilities:   
              print "probabilities of segments are effectively equal"
              y=0
              while y !=no_per_target_group:
                    segment=random.sample(seg_specifications[target_group],1)[0]
                    target_segs_per_cell.append(int(segment))
                    y=y+1
           else:
              target_segs_per_group=[]
              not_selected=True
              while not_selected:
                   p=random.random()
                   print "printing a random number"
                   print p
                   for segment in seg_specifications[target_group].keys():
                       if p < seg_specifications[target_group][segment]:
                          print segment 
                          target_segs_per_group.append(int(segment))
                          if len(target_segs_per_group)==no_per_target_group:
                             not_selected=False
                             break
              target_segs_per_cell.extend(target_segs_per_group)
             
    return target_segs_per_cell

####################################################################################################    

def get_unique_membrane_points(target_segs_list):
    total=len(target_segs_list)
    print total
    segment_set=set(target_segs_list)
    countSegs={}
    print segment_set
    for unique_seg in segment_set:
        key_seg=str(unique_seg)
        countSegs[key_seg]=0
        for seg in range(0,total):
            if unique_seg==target_segs_list[seg]:
               countSegs[key_seg]=countSegs[key_seg]+1    
    if sum(countSegs.values())==total:
       print "A total number of target segments is correctly parsed"  
       print total
    print countSegs
    unique_membrane_points={}
    for unique_seg in countSegs.keys():
        unique_membrane_points[unique_seg]=[]
        ind=True
        while ind:
           for point in range(0,countSegs[unique_seg]):
               unique_membrane_points[unique_seg].append(random.random())
           if len(unique_membrane_points[unique_seg])==len(set(unique_membrane_points[unique_seg])):
              ind=False
              
    print unique_membrane_points
    return unique_membrane_points        
            
###########################################################################################################################


def check_seg_probabilities(lengthProbs,minimalProbRange):
    equalProbs=False
    rescaledProbs={}
    max_value=max(lengthProbs.iteritems(),key=operator.itemgetter(1))[0]
    min_value=min(lengthProbs.iteritems(),key=operator.itemgetter(1))[0]
    if minimalProbRange > lengthProbs[max_value]-lengthProbs[min_value]:
       equalProbs=True
    print "printing a range of probabilities"
    print lengthProbs[max_value]-lengthProbs[min_value]
    return equalProbs


###########################################################################################################################

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
    

def add_transient_poisson_firing_synapse(nml_doc, id, average_rate,delay,duration, synapse_id):

    pfs = neuroml.TransientPoissonFiringSynapse(id=id,
                                       average_rate=average_rate,
                                       delay=delay,
                                       duration=duration,
                                       synapse=synapse_id, 
                                       spike_target="./%s"%synapse_id)
                                       
    nml_doc.transient_poisson_firing_synapses.append(pfs)

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
    
    
def add_population_in_rectangular_region(net, pop_id, cell_id, size, x_min, y_min, z_min, x_size, y_size, z_size,storeSoma=False, color=None):
    
    pop = neuroml.Population(id=pop_id, component=cell_id, type="populationList", size=size)
    if color is not None:
        pop.properties.append(Property("color",color))
    net.populations.append(pop)
    
    if storeSoma==True:
       cellPositions=np.zeros([size,3])
    else:
       cellPositions=None
       
    for i in range(0, size) :
            index = i
            inst = neuroml.Instance(id=index)
            pop.instances.append(inst)
            X=x_min +(x_size)*random.random()
            Y=y_min +(y_size)*random.random()
            Z=z_min +(z_size)*random.random()
            inst.location = neuroml.Location(x=str(X), y=str(Y), z=str(Z) )
            if storeSoma==True:
               cellPositions[i,0]=X
               cellPositions[i,1]=Y
               cellPositions[i,2]=Z
            
    
    return pop, cellPositions

################################################################################    
    
def add_populations_in_layers(net,boundaryDict,popDict,x_vector,z_vector,storeSoma=False): 

  
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
          
              pop, cellPositions=add_population_in_rectangular_region(net,"%s_%s"%(cellModel,layer),cellModel,size,x_vector[0],boundaryDict[layer][0],z_vector[0],xl,yl,zl,storeSoma)
         
              return_pops[cellModel][layer]={}
              return_pops[cellModel][layer]['PopObj']=pop
              return_pops[cellModel][layer]['Size']=size
              return_pops[cellModel][layer]['Positions']=cellPositions
   
   return return_pops
          



###############################################################################################

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
    
##################################################################################################

def add_advanced_inputs_to_population(net, id, population, input_comp_id, all_cells=False, only_cells=None):
    
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
                      destination="synapses",segment_id="%d"%target_points[target_point,0],fraction_along="%f"%target_points[target_point,1])  
        input_list.input.append(input)
        count+=1
        
                         
    net.input_lists.append(input_list)
    
    return input_list

###############################################################################################################

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
