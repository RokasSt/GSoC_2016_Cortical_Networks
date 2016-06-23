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
                             postTargetingSpec,
                             delaysInfo=None,
                             weightsInfo=None):
                             
    targetDict=postTargetingSpec['TargetDict']
    subsets=postTargetingSpec['ConnSubsets']
    minimalProbRange=postTargetingSpec['MinimalProbRange']
    total_given=sum(subsets.values())
    count=0
    for i in range(0, presynaptic_population.size):
        
        postsynaptic_cells=random.sample(range(0,postsynaptic_population.size),total_given)
        
        target_seg_array=get_target_segments(targetDict,subsets,minimalProbRange)
        
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
                                     
     
   

#####################################################################################################################################################

def add_advanced_chem_projection(net, 
                                 proj_counter,
                                 presynaptic_population, 
                                 postsynaptic_population, 
                                 synapseList,  
                                 targetingParams,
                                 postCompSpec,
                                 distanceDependence,
                                 delaysInfo,
                                 weightsInfo):
                            
    ############# postCompSpec keys: 'Mode','NoPerPostCell' or 'NoPerPreCell','DistDependConn','MinimalProbRange'
                  
    targetingMode=targetingParams['Mode']
    
    distDependentConn=distanceDependence['DistDependConn']
    
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
       
    if targetingMode=='convergent':
       if distDependentConn==None:
          proj_array              =add_convergent_projection(net,
                                                             proj_array,
                                                             presynaptic_population,
                                                             postsynaptic_population,
                                                             synapseList,
                                                             postCompSpec,
                                                             delaysInfo,
                                                             weightsInfo) 
       else:
          proj_array              =add_convergent_spatial_projection(net,
                                                                     proj_array,
                                                                     presynaptic_population,
                                                                     postsynaptic_population,
                                                                     synapseList,
                                                                     postCompSpec,
                                                                     distanceDependence,
                                                                     delaysInfo,
                                                                     weightsInfo)
       
    if targetingMode=='divergent':
       if distDependentConn==None:
          proj_array              =add_divergent_projection(net,
                                                            proj_array,
                                                            presynaptic_population,
                                                            postsynaptic_population,
                                                            synapseList,
                                                            postCompSpec,
                                                            delaysInfo,
                                                            weightsInfo)
       else:
          proj_array              =add_divergent_spatial_projection(net,
                                                                    proj_array,
                                                                    presynaptic_population,
                                                                    postsynaptic_population,
                                                                    synapseList,
                                                                    postCompSpec,
                                                                    distanceDependence,
                                                                    delaysInfo,
                                                                    weightsInfo)
    

    return proj_array, proj_counter

 
##############################################################################################################################################
def parse_extra_params(extra_params,pre_pop,post_pop):

    subset_dict=None
    weights=None
    delays=None
    distDependence=None
    for params_set in range(0,len(extra_params)):
        if extra_params[params_set]['pre']==pre_pop and extra_params[params_set]['post']==post_pop:
           if 'subsetDict' in extra_params[params_set].keys():
              prob_dict=extra_params[params_set]['subsetDict']
           if 'DistDependConn' in extra_params[params_set].keys():
              distDependence=extra_params[params_set]['DistDependConn']
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
                        
                        
    return subset_dict, weights, delays, distDependence
    
############################################################################################################################
def parse_targeting_params(targetingParams):

    if targetingParams['Mode']=='convergent':
       numberPerPostCell=targetingParams['NumPerPostCell']
       mode='convergent'
       noOfConn=numberPerPostCell
    if targetingParams['Mode']=='divergent':
       numberPerPreCell=targetingParams['NumPerPreCell']
       mode='divergent'
       noOfConn=numberPerPreCell
       
    return mode, noOfConn
    
############################################################################################################################
def make_target_dict(target_segs,cellPath):
    targetDict={}
    for target in target_segs.keys():
        targetDict[target]=get_seg_probabilities(cellPath,target_segs[target])
    return targetDict
    
############################################################################################################################


def build_connectivity(net,popObjects,connInfo,pathToCells,extra_params=None):

    final_synapse_list=[]
    final_proj_array=[]
    if isinstance(connInfo,list):
       conn_data=connInfo
    else:
       try:
           with open(connInfo,'r') as json_conn:
              conn_data=json.load(json_conn)
       except IOError:
           print "cannot open file %s"%connInfo
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
                           
                           target_comp_groups=projInfo['LocOnPostCell']
                           
                           if 'NumPerPostCell' in projInfo:
                              mode='convergent'
                              mode_string='NumPerPostCell'
                              
                           if 'NumPerPreCell' in projInfo:
                              mode='divergent'
                              mode_string='NumPerPreCell'
                           
                           if extra_params != None:
                              subset_dict, weights, delays,dist_par=parse_extra_params(extra_params,prePop,postPop)
                           else:
                              subset_dict=None
                              weights=None
                              delays=None 
                              dist_par=None   
                           if subset_dict ==None:
                              subset_dict={}
                                    
                           if not isinstance(target_comp_groups,list):
                              subset_dict[target_comp_groups]=projInfo[mode_string]
                              print subset_dict[target_comp_groups]
                              target_comp_groups=[target_comp_groups]
                           
                           target_segments=extract_seg_ids({'CellID':postPop,'SegOrSegGroupList':target_comp_groups,'TargetingMode':'segGroups','PathToCell':pathToCells})
                           targetDict=make_target_dict(target_segments,pathToCells+"%s.cell.nml"%postPop)
                           postTargetParams={'TargetDict':targetDict,'ConnSubsets':subset_dict,'MinimalProbRange':1e-06}
                           targetingParams={'Mode':mode}
                           distanceDependence={'DistDependConn':dist_par,'prePositions':preCellObject['Positions'],'postPositions':postCellObject['Positions']}
                           synapseList=projInfo['SynapseList']                                                
                           final_synapse_list.extend(projInfo['SynapseList'])
                           if projInfo['type']=='chem':
                              compound_proj, proj_counter=add_advanced_chem_projection(net, 
                                                                                       proj_counter,
                                                                                       preCellObject['PopObj'], 
                                                                                       postCellObject['PopObj'], 
                                                                                       synapseList,  
                                                                                       targetingParams,
                                                                                       postTargetParams,
                                                                                       distanceDependence,
                                                                                       delaysInfo=delays,
                                                                                       weightsInfo=weights)
                                                        
                                                        
                              proj_counter+=1                      
                              final_proj_array.extend(compound_proj)
          
    final_synapse_list=np.unique(final_synapse_list)
                          
    return final_synapse_list, final_proj_array
                           
############################################################################################################################

def build_inputs(nml_doc,net,pop_params,input_params,pathToSynapses):                          
                        
    for cell_model in input_params.keys():
    
        for input_group_ind in range(0,len(input_params[cell_model])):
        
            input_group_params=input_params[cell_model][input_group_ind]
        
            layer=input_group_params['Layer'] 
            
            popID=cell_model+"_"+layer
            
            cell_positions=pop_params[cell_model][layer]['Positions']
            
            pop_size=pop_params[cell_model][layer]['Size']
            
            fraction_to_target=input_group_params['FractionToTarget']
            
            if not input_group_params['LocationSpecific']:
             
               target_cell_ids=get_target_cells(pop_size,fraction_to_target)
               
            else:
            
               list_of_regions=input_group_params['TargetRegions']
            
               target_cell_ids=get_target_cells(pop_size,fraction_to_target,cell_positions, list_of_regions)
               
            if target_cell_ids != []:
            
               for cell_id in target_cell_ids:
                   
                   ###TODO
                   pass
                    
           
               

############################################################################################################################


def get_target_cells(pop_size,fraction_to_target,cell_positions=None,list_of_regions=None):

    if cell_positions==None:
    
       target_cells=random.sample(range(pop_size),int(round(fraction_to_target*pop_size)   )   )
       
    else:
       
       region_specific_targets_per_cell_group=[]
       
       for region in range(0,len(input_group_parameters['regionList'])):
       
           for cell in range(0,pop_size):
           
               if (input_group_parameters['regionList'][region]['xVector'][0] <  cell_positions[cell,0]) and \
                  (cell_positions[cell,0] < input_group_parameters['regionList'][region]['xVector'][1]):
               
               if (input_group_parameters['regionList'][region]['yVector'][0] <  cell_positions[cell,1]) and \
                  (cell_positions[cell,1] <input_group_parameters['regionList'][region]['yVector'][1]) :
                
                  if (input_group_parameters['regionList'][region]['zVector'][0] <  cell_positions[cell,2]) and \
                     (cell_positions[cell,2] < input_group_parameters['regionList'][region]['zVector'][1]):
                     
                     region_specific_targets_per_cell_group.append(cell)
                                                                        
    target_cells=random.sample(region_specific_targets_per_cell_group,int(round(fraction_to_target*len(region_specific_targets_per_cell_group))))
                                                                   

    return target_cells

################################################################################################################################

def get_seg_probabilities(cellPath,targetSegments):
    
    document_cell = neuroml.loaders.NeuroMLLoader.load(cellPath)
    cellObject=document_cell.cells[0]
    lengthDict={}
    totalLength=0
    for seg in cellObject.morphology.segments:
        for target_seg in targetSegments:
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
    lengthProbs={}
    totalProb=0
    for target_seg in lengthDict.keys():
        lengthProbs[target_seg]=lengthDict[target_seg]/totalLength
        totalProb=lengthProbs[target_seg]+totalProb
    return lengthProbs
############################################################################################################################


def extract_seg_ids(input_dict):
    
    cellID=input_dict['CellID']
    targetCompArray=input_dict['SegOrSegGroupList']
    targetingMode=input_dict['TargetingMode']
    pathToNML=input_dict['PathToCell']
    
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
            
####################################################################################################


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

############################################################################################################################
def network_reader(net_file_name,path_to_net):

    nml2_file_path=os.path.join(path_to_net,net_file_name+".net.nml")      
                  
    net_doc = pynml.read_neuroml2_file(nml2_file_path)
    
    popParams=[]
    
    popPositions={}
    
    includeRefs=[]
    
    for include_counter in range(0,len(net_doc.includes)):
    
        include=net_doc.includes[include_counter]
        includeRefs.append(include.href)
        
    print includeRefs
    
    for net_counter in range(0,len(net_doc.networks)):
        net=net_doc.networks[net_counter]
        for pop_counter in range(0,len(net.populations)):
            popDict={}
            pop=net.populations[pop_counter]
            popDict['id']=pop.id
            popDict['component']=pop.component
            popDict['size']=pop.size
            popDict['type']=pop.type
            popParams.append(popDict)
            cellPositions=[]
            
            for instance_counter in range(0,len(pop.instances)):
                cell_location={}
                instance=pop.instances[instance_counter]
                print instance.id
                cell_location['x']=instance.location.x
                cell_location['y']=instance.location.y
                cell_location['z']=instance.location.z
                cellPositions.append(cell_location)
                
            popPositions[popDict['id']]=cellPositions
            
        print popParams
        print popPositions
        
        projDict={}
        
        for proj_counter in range(0,len(net.projections)):
            
            connections=[]
            
            proj=net.projections[proj_counter]
            print proj.id
            for conn_counter in range(0,len(proj.connection_wds)):
                connection_dict={}
                connection=proj.connection_wds[conn_counter]
                print connection.id
                connection_dict['preCellId']=connection.pre_cell_id
                connection_dict['postCellId']=connection.post_cell_id
                if hasattr(connection,'post_segment_id'):
                   connection_dict['postSegmentId']=connection.post_segment_id
                if hasattr(connection,'pre_segment_id'):
                   connection_dict['preSegmentId']=connection.pre_segment_id
                if hasattr(connection,'pre_fraction_along'):
                   connection_dict['preFractionAlong']=connection.pre_fraction_along
                if hasattr(connection,'post_fraction_along'):
                   connection_dict['postFractionAlong']=connection.post_fraction_along
                if hasattr(connection,'delay'):
                   connection_dict['delay']=connection.delay
                if hasattr(connection,'weight'):
                   connection_dict['weight']=connection.weight
                connections.append(connection_dict)
                
            projDict[proj.id]=connections
            
        print projDict


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
