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

    
