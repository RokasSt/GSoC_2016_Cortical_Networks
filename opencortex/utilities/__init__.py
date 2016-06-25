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


import opencortex.build as oc_build



def add_advanced_chem_projection(net, 
                                 proj_counter,
                                 presynaptic_population, 
                                 postsynaptic_population, 
                                 synapse_list,  
                                 targeting_mode,
                                 seg_length_dict,
                                 num_of_conn_dict,
                                 minimal_prob_range,
                                 distance_dependent_params,
                                 delays_dict,
                                 weights_dict):
                            
    ############# postCompSpec keys: 'Mode','NoPerPostCell' or 'NoPerPreCell','DistDependConn','MinimalProbRange'
                  
    
    distDependentConn=distanceDependentParams['DistDependConn']
    
    if presynaptic_population.size==0 or postsynaptic_population.size==0:
        return None
    
    proj_array={}
    syn_counter=0
    for synapse_id in synapse_list:
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
                                                             synapse_list,
                                                             postCompSpec,
                                                             delaysInfo,
                                                             weightsInfo) 
       else:
          proj_array              =add_convergent_spatial_projection(net,
                                                                     proj_array,
                                                                     presynaptic_population,
                                                                     postsynaptic_population,
                                                                     synapse_list,
                                                                     postCompSpec,
                                                                     distanceDependentParams,
                                                                     delaysInfo,
                                                                     weightsInfo)
       
    if targetingMode=='divergent':
       if distDependentConn==None:
          proj_array              =add_divergent_projection(net,
                                                            proj_array,
                                                            presynaptic_population,
                                                            postsynaptic_population,
                                                            synapse_list,
                                                            postCompSpec,
                                                            delaysInfo,
                                                            weightsInfo)
       else:
          proj_array              =add_divergent_spatial_projection(net,
                                                                    proj_array,
                                                                    presynaptic_population,
                                                                    postsynaptic_population,
                                                                    synapse_list,
                                                                    postCompSpec,
                                                                    distanceDependentParams,
                                                                    delaysInfo,
                                                                    weightsInfo)
    

    return proj_array, proj_counter

#######################################################################################################################################

def build_connectivity(net,popObjects,connInfo,pathToCells,extra_params=None):

    final_synapse_list=[]
    final_proj_array=[]
    cached_target_dict={}
    
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
                              subset_dict, weights, delays, dist_par=parse_extra_params(extra_params,prePop,postPop)
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
                              
                           if postPop not in cached_target_dict.keys():
                           
                              cell_nml_file = '%s.cell.nml'%cellID
                           
                              if pathToCells != None:
                                 document_cell = neuroml.loaders.NeuroMLLoader.load(os.path.join(pathToCells,cell_nml_file))
                              else:
                                document_cell=neuroml.loaders.NeuroMLLoader.load(cell_nml_file)
                              
                              cellObject=document_cell.cells[0]
                              target_segments=extract_seg_ids(cell_object=cellObject,target_compartment_array=target_comp_groups,targeting_mode='segGroups')
                              segLengthtDict=make_target_dict(cell_object,target_segments)
                              postTargetParams={'TargetDict':segLengthDict,'SubsetsOfConnections':subset_dict}
                              cached_target_dict[postPop]=postTargetParams
                              
                           else:
                              segLengthDict=cached_target_dict[postPop]['TargetDict']
                              subset_dict=cached_target_dict[postPop]['SubsetsOfConnections']
                              
                                    
                           targetingMode=mode
                           distanceDependence={'DistDependConn':dist_par,'prePositions':preCellObject['Positions'],'postPositions':postCellObject['Positions']}
                           synapseList=projInfo['SynapseList']                                                
                           final_synapse_list.extend(projInfo['SynapseList'])
                           
                           if projInfo['type']=='chem':
                              compound_proj, proj_counter=add_advanced_chem_projection(net=net, 
                                                                                       proj_counter=proj_counter,
                                                                                       presynaptic_population=preCellObject['PopObj'], 
                                                                                       postsynaptic_population=postCellObject['PopObj'], 
                                                                                       synapse_list=synapseList,  
                                                                                       targeting_mode=targetingMode,
                                                                                       seg_length_dict=segLengthDict,
                                                                                       num_of_conn_dict=subset_dict,
                                                                                       minimal_prob_range=1e-06,
                                                                                       distance_dependent_params=distanceDependence,
                                                                                       delays_dict=delays,
                                                                                       weights_dict=weights)
                                                        
                                                        
                              proj_counter+=1                      
                              final_proj_array.extend(compound_proj)
                              
                           if projInfo['elec']=='elec':
                              pass
                              #TODO
          
    final_synapse_list=np.unique(final_synapse_list)
                          
    return final_synapse_list, final_proj_array
    
################################################################################################################################################################    

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
                                   
####################################################################################################################################################################    
    
def replace_network_components(net_file_name,path_to_net):

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

##############################################################################################################################
def check_size_and_layer(cell_model,list_of_tuples):

    error_counter=0
    
    layers=[]
    
    sizes=[]
    
    if not isinstance(list_of_tuples,list):
       print("TypeError in population parameters: the population dictionary value for the key '%s' must a list.")
       print("The current type is %s"%(cell_model,type(list_of_tuples) ) )
       error_counter+=1
    else:
       for tuple_var in range(0,len(list_of_tuples)):
           if not isinstance(list_of_tuples[tuple_var],tuple):
              print("TypeError in population parameters: the list values stored in the population dictionary must be tuples.")
              print("The current type is %s"%(type(list_of_tuples[tuple_var])  ) )
              error_counter+=1
           else:
              if not isinstance(list_of_tuples[tuple_var][0],int):
                 print("TypeError in population parameters: the first element in tuples inside the population dictionary must be a 'int'")
                 print(" as it specifies the size of cell population. The current type of the first element is %s"%( type(list_of_tuples[tuple_var][0])  )  )
                 error_counter+=1
                 size=list_of_tuples[tuple_var][0]
                 sizes.append(size) 
                 
              if not isinstance(list_of_tuples[tuple_var][1],str):
                 print("TypeError in population parameters: the second element in tuples inside the population dictionary must be a 'string'")
                 print(" as it specifies the layer of cell population. The current type of the second element is %s"%( type(list_of_tuples[tuple_var][1]) ) )
                 error_counter+=1
              else:
                 layer=list_of_tuples[tuple_var][1]
                 layers.append(layer)
                 
    return error_counter, sizes, layers
    
 
def check_synapse_location(synapse_id,pathToSynapses):
    
    found=False
    
    src_files=os.listdir(pathToSynapses)
    
    for file_name in src_files:
        if synapse_id in file_name:
           found=True   
           
           
    return found  
    
    
def get_segment_groups(cell_id,path_to_cells):
   
    cell_nml_file =os.path.join(path_to_cells,'%s.cell.nml'%cell_id)
    document_cell=neuroml.loaders.NeuroMLLoader.load(cell_nml_file)
    cell_object=document_cell.cells[0]
    segment_groups=[]
    for segment_group in cell_object.morphology.segment_groups:
        
        segment_groups.append(segment_group.id)
        
    return segment_groups
    
    
def check_segment_group(segment_groups,target_segment_group):
    segment_group_exist=False
    if target_segment_group in segment_groups:
       segment_group_exist=True
    return segment_group_exist

def check_inputs(input_params,popDict,pathToNML2):
    
    error_counter=0
    
    for cell_receiver in input_params.keys():
    
        try:
           test_key=popDict[cell_receiver]
           
           error_increment, sizes, layers =check_size_and_layer(cell_receiver,test_key)
           
           segment_groups=get_segment_groups(cell_receiver,pathToNML2)
           
           error_counter+=error_increment
           
           cell_type=cell_receiver
           
        except KeyError:
           print("KeyError in input parameters: cell type '%s' specified is not in the keys of population dictionary"%cell_receiver)
           error_counter+=1
           layers=None
           cell_type=None
           
        if not isinstance(input_params[cell_receiver],list):
       
           print("TypeError in input parameters: the dictionary value for '%s' must be a list. The current type is %s"%(cell_receiver,type(input_params[cell_receiver])))
           
           error_counter+=1
           
        else:
        
           for input_group_ind in range(0,len(input_params[cell_receiver])):
           
               input_group_params=input_params[cell_receiver][input_group_ind]
               
               try:
               
                 test_key=input_group_params['InputType']
                 
                 if not isinstance(test_key,str):
                 
                    print("TypeError in input parameters: the value of the key 'InputType' must be of type 'string'.\ The current type is %s"%type(test_key) )
                    
                    error_counter+=1 
                    
                    
                 if test_key not in ['GeneratePoissonTrains','PulseGenerators']:
                 
                    print("ValueError in input parameters: the value of the key 'InputType' must be one of the following: 'GeneratePoissonTrains','PulseGenerators'")
                    
                    error_counter+=1
                    
                 else:
                 
                 
                 
                    if test_key=="GeneratePoissonTrains":
                    
                       try:
                          test_train_type=input_group_params['TrainType']
                          
                          if not isinstance(test_train_type,str):
                             print("TypeError in input parameters: the value of the key 'TrainType' must be of type 'string'. The current type is %s"%type(test_train_type))
                             error_counter+=1
                          else:
                          
                             if test_train_type not in ['persistent','transient']:
                             
                                print("ValueError in input parameters: the value of the key 'TrainType' when 'InputType' is 'GeneratePoissonTrains' must be one of the following:")
                                print("'persistent' or 'transient'")
                                error_counter+=1
                                
                             else:
                             
                                if test_train_type=="persistent":
                                
                                   try:
                                      test_rates=input_group_params['AverageRateList']
                                      if not isinstance(test_rates,list):
                                         print("TypeError in input parameters: the value of the key 'AverageRateList' must be of type 'list'.")
                                         print(" The current type is %s"%type(test_rates) )
                                         error_counter+=1
                                      else:
                                         for r in range(0,len(test_rates)):
                                             if not isinstance(test_rates[r],float):
                                                print("TypeError in input parameters: the list values of the key 'AverageRateList' must be of type 'float'.")
                                                print("The current type is %s"%type(test_rates[r]))
                                                error_counter+=1
                                      
                                   except KeyError:
                                      print("KeyError in input parameters: the key 'AverageRateList' is not in the keys of input parameters")
                                      error_counter+=1
                                      
                                if test_train_type=="transient":
                                
                                   try:
                                      test_rates=input_group_params['AverageRateList']
                                      if not isinstance(test_rates,list):
                                         print("TypeError in input parameters: the value of the key 'AverageRateList' must be of type 'list'.")
                                         print("The current type is %s"%type(test_rates))
                                         error_counter+=1
                                      else:
                                         for r in range(0,len(test_rates)):
                                             if not isinstance(test_rates[r],float):
                                                print("TypeError in input parameters: the list values of the key 'AverageRateList' must be of type 'float'.")
                                                print(" The current type is %s"%type(test_rates[r]) )
                                                error_counter+=1
                                      
                                   except KeyError:
                                      print("KeyError in input parameters: the key 'AverageRateList' is not in the keys of input parameters")
                                      error_counter+=1
                                   
                                   try:
                                      test_rates=input_group_params['DelayList']
                                      
                                      if not isinstance(test_rates,list):
                                         print("TypeError in input parameters: the value of the key 'DelayList' must be of type 'list'.")
                                         print("The current type is %s"%type(test_rates))
                                         error_counter+=1
                                      else:
                                         for r in range(0,len(test_rates)):
                                             if not isinstance(test_rates[r],float):
                                                print("TypeError in input parameters: the list values of the key 'DelayList' must be of type 'float'.")
                                                print("The current type is %s"%type(test_rates[r]) )
                                                error_counter+=1
                                         
                                   except KeyError:
                                      print("KeyError in input parameters: the key 'DelayList' is not in the keys of input parameters")
                                      error_counter+=1
                                   
                                   try:
                                      test_rates=input_group_params['DurationList']
                                      if not isinstance(test_rates,list):
                                         print("TypeError in input parameters: the value of the key 'DurationList' must be of type 'list'.")
                                         print("The current type is %s"%type(test_rates) )
                                         error_counter+=1
                                      else:
                                         for r in range(0,len(test_rates)):
                                             if not isinstance(test_rates[r],float):
                                                print("TypeError in input parameters: the list values of the key 'DurationList' must be of type 'float'.")
                                                print("The current type is %s"%type(test_rates[r]) )
                                                error_counter+=1
                                      
                                   except KeyError:
                                      print("KeyError in input parameters: the key 'DurationList' is not in the keys of input parameters")
                                      error_counter+=1
                                      
                                      
                          
                       except KeyError:
                          print("KeyError in input parameters: the key 'TrainType' is not in the keys of input parameters")
                          error_counter+=1
                          
                          
                       try:
                          test_synapse=input_group_params['Synapse']
                          
                          if not isinstance(test_synapse,str):
                             print("TypeError in input parameters: the value of the key 'Synapse' must be of type 'string'.")
                             print(" The current type is %s"%type(test_synapse))
                             error_counter+=1
                             
                          else:
                             found=check_synapse_location(test_synapse,pathToNML2)
                             if not found:
                                print("ValueError in input parameters: the value '%s' of the key 'Synapse' is not found in %s"%(test_synapse,pathToNML2))
                                error_counter+=1
                       except KeyError:
                           print("KeyError in input parameters: the key 'Synapse' is not in the keys of input parameters")   
                           error_counter+=1
                           
                           
                    ####################### TODO       
                    if test_key=='PulseGenerators':
                    
                       pass
                          
                    
               except KeyError:
                 print("KeyError in input parameters: the key 'InputType' is not in input parameters")
                 error_counter+=1
                 
                 
               try: 
               
                 test_key=input_group_params['Layer']
                 
                 if not isinstance(test_key,str):
                 
                    print("TypeError in input parameters: the value of the key 'Layer' must be of type 'string'. The current type is %s"%type(test_key) )
                    
                    error_counter+=1 
                    
                 if layers !=None:
                    if not test_key in layers:
                       print("ValueError in input parameters: the population dictionary does not specify the cell type '%s' in the layer '%s'"%(cell_receiver,test_key) )
                       error_counter+=1
                       
               except KeyError:
                 print("KeyError: the key 'Layer' is not in input parameters")
                 error_counter+=1 
                 
                 
               try:
               
                 test_key=input_group_params['TargetDict']
                 if not isinstance(test_key,dict):
                    print("TypeError: the value of the key 'TargetDict' in input parameters must be of type 'dict'. The current type is %s"%type(test_key)  ) 
                    error_counter+=1
                 else:
                    if cell_type != None:
                    
                       for target_segment_group in test_key.keys():
                       
                           if not check_segment_group(segment_groups,target_segment_group):
                              print("ValueError: '%s' is not a segment group of the cell type '%s'"%(target_segment_group,cell_receiver) )
                              error_counter+=1
                           else:
                              if not isinstance(test_key[target_segment_group],int):
                                print("TypeError: the value of the key '%s' must be of type 'int'. The current type is %s"%(target_segment_group,type(test_key[target_segment_group])))
                                error_counter+=1
               except KeyError:
                 print("KeyError: the key 'TargetDict' is not in input parameters")
                 error_counter+=1
              
              
               try:
                 
                 test_key=input_group_params['FractionToTarget']
                 
                 if not isinstance(test_key,float):
                    print("TypeError: the value of the key 'FractionToTarget' must be of type 'float'. The current type is %s"%type(test_key) )
                    error_counter+=1
                    
               except KeyError:
               
                 print("KeyError: the key 'FractionToTarget' is not in input parameters")
                 error_counter+=1
               
                 
               try:
                 
                 test_key=input_group_params['LocationSpecific']
                 
                 
                 if not isinstance(test_key,bool):
                    print("TypeError in input parameters: the value of the key 'LocationSpecific' must be of the type 'bool'. The current type is %s"%type(test_key) ) 
                    error_counter+=1
                    
                 else:
                    
                    if test_key:
                    
                       try:
                         
                         test_region_key=input_group_params['TargetRegions']
                         
                         if not isinstance(test_region_key,list):
                         
                            print("TypeError in input parameters: the value of the key 'TargetRegions' must be of the type 'list'. The current type is %s"%type(test_region_key) )
                            error_counter+=1
                            
                         else:
                            for region in range(0,len(test_region_key)):
                            
                                if not isinstance(test_region_key[region],dict):
                                   print("TypeError in input parameters: the list values of the key 'TargetRegions' must be of the type 'dict'.") 
                                   print("The current type is %s"%type(test_region_key[region]) )
                                   error_counter+=1
                                else:
                                    for dim_key in ['XVector','YVector','ZVector']:
                                     
                                        if dim_key not in test_region_key[region].keys():
                                            print("ValueError in input parameters: the list values of the key 'TargetRegions' must be dictionaries with the following keys:")
                                            print("'XVector', 'YVector', 'ZVector'")
                                            error_counter+=1 
                                        else:
                                            if not isinstance(test_region_key[region][dim_key],list):
                                               print("TypeError in input parametres: the 'X/Y/ZVector' must store the value of type 'list'.")
                                               print("The current type is %s"%type(test_region_key[region][dim_key]))
                                               error_counter+=1
                                            else:
                                               if len(test_region_key[region][dim_key]) !=2:
                                                  print("ValueError in input parameters: the lists stored by 'XVector', 'YVector' and 'ZVector' must contain two values")
                                                  error_counter+=1
                                               else:
                                                  if (test_region_key[region][dim_key][0]-test_region_key[region][dim_key][1]) ==0:
                                                     print("ValueError in input parameters: the lists stored by 'XVector', 'YVector' and 'ZVector' must contain two different values")
                                                     error_counter+=1
                         
                       except KeyError:
                         
                         print("KeyError in input parameters: 'LocationSpecific' is True but the key 'TargetRegions' is not in input parameters")
                         error_counter+=1
                         
                      
                    
               except KeyError:
              
                  print("KeyError in input parameters: the key 'LocationSpecific' is not in input parameters")
                  error_counter+=1
                 
           
           
if __name__=="__main__":

    popDict={'TCR':[(4,'Thalamus')]}

    input_params={'TCR':[{'InputType':'GeneratePoissonTrains',
                  'Layer':'Thalamus',
                  'TrainType':'transient',
                  'Synapse':'Syn_AMPA_L6NT_TCR',
                  'AverageRateList':[0.05],
                  'DurationList':[200.0],
                  'DelayList':[20.0],
                  'FractionToTarget':1.0,
                  'LocationSpecific':True,
                  'TargetRegions':[{'XVector':[2,12],'YVector':[3,5],'ZVector':[0,5]}],
                  'TargetDict':{'dendrite_group':1000 }       }]              }
              
              
    check_inputs(input_params,popDict,"../../NeuroML2/prototypes/Thalamocortical/")

    
