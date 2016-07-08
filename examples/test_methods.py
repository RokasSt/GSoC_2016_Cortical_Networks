import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 



import opencortex.build as oc
import opencortex.utilities as oc_utils
import neuroml

if __name__=="__main__":
  
  pathToNML2="../NeuroML2/prototypes/Thalamocortical/"
          
  cell_nml_file = 'L23PyrRS.cell.nml'
          
  document_cell = neuroml.loaders.NeuroMLLoader.load(os.path.join(pathToNML2,cell_nml_file))
                                
  cell_object=document_cell.cells[0] 

  ##### test segment id extraction:
  #print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['basal_obl_dends','most_prox_bas_dend'],'TargetingMode':'segGroups','pathToCell':pathToNML2})
  
  #print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['comp_16'],'TargetingMode':'segGroups','pathToCell':pathToNML2})
  #print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['Seg1_comp_68','Seg1_comp_28'],'TargetingMode':'segments','pathToCell':pathToNML2})
  
  #print oc.get_seg_probabilities(pathToNML2+"L23PyrRS.cell.nml",[55])
  #print oc.get_seg_probabilities(pathToNML2+"L23PyrRS.cell.nml",[16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3])
  
  #target_dict1=oc.make_target_dict({'Seg1_comp_28':[55], 'Seg1_comp_68': [135]},pathToNML2+"L23PyrRS.cell.nml")
  #target_dict2=oc.make_target_dict({'basal_obl_dends': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 24, 25, 22, 23, 20, 21, 18, 19, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33, 30, 31, 28, 29, 26, 27, 48, 49, 46, 47, 44, 45, 42, 43, 64, 65, 62, 63, 60, 61, 58, 59, 56, 57, 54, 55, 52, 53, 50, 51, 72, 73, 70, 71, 68, 69, 66, 67], 'most_prox_bas_dend': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3]},pathToNML2+"L23PyrRS.cell.nml")
  #print target_dict1
  #print target_dict2
  #print oc.get_target_segments(target_dict1,{'Seg1_comp_28':5,'Seg1_comp_68':5},1e-06)
  ####################### Ps turn out to be very small - turning the coin won't work for very small values
  #print oc.get_target_segments(target_dict2,{'most_prox_bas_dend':5},1e-06)
  
  #pathToNML2_golgi=parentdir+"/NeuroML2/prototypes/Golgi/"
  
  #print oc.extract_seg_ids({'CellID':'Golgi_10comp_3channels_1CaPool',
                           # 'SegOrSegGroupList':['apical_dendrite_group','basal_dendrite_group'],
                            #'TargetingMode':'segGroups',
                            #'PathToCell':pathToNML2_golgi})
                            
                            
  #target_dict3=oc.make_target_dict({'basal_dendrite_group': [9, 10], 'apical_dendrite_group': [3, 4, 5, 6, 7, 8]},
                                  # pathToNML2_golgi+"Golgi_10comp_3channels_1CaPool.cell.nml")
                                   
  #print target_dict3
  
  #print oc.get_target_segments({'basal_dendrite_group': {'9': 0.8,'15':0.2},'apical':{'10':0.5,'6':0.5}},{'basal_dendrite_group':10,'apical':2},1e-9)
  
  #print oc.get_target_segments({'basal':{'2':1},'apical':{'3':1}},{'basal':10,'apical':2},1e-06)
  
  #print oc.get_target_segments(target_dict2,{'basal_obl_dends':50},1e-09)
  
  #print oc.get_target_segments({'basal_dendrite_group':{'9':0.020,'15':0.180,'16':0.8}},{'basal_dendrite_group':50},1e-6)
  
  #print oc.get_target_segments(target_dict2,{'basal_obl_dends':100,'most_prox_bas_dend':25},1e-09)
  
  #target_segs_list=oc.get_target_segments(target_dict2,{'basal_obl_dends':100,'most_prox_bas_dend':25},1e-06)
  
  #oc.get_unique_membrane_points(target_segs_list)
  
  
  #oc_utils.read_connectivity("L23PyrRS","L23PyrRS","netConnList")
  
  
  makeDict2=oc.make_target_dict(cell_object=cell_object,
                                target_segs={'basal_obl_dends': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 24, 25, 22, 23, 20, 21, 18, 19, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33, 30, 31, 28, 29, 26, 27, 48, 49, 46, 47, 44, 45, 42, 43, 64, 65, 62, 63, 60, 61, 58, 59, 56, 57, 54, 55, 52, 53, 50, 51, 72, 73, 70, 71, 68, 69, 66, 67], 'most_prox_bas_dend': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3]})
                                        
  print  makeDict2
  
  
  target_segs, fractions_list=oc.get_target_segments(makeDict2,{'basal_obl_dends':100,'most_prox_bas_dend':50})
  
  print("Will be printing target_segs")
  print target_segs
  print("Will be printing fractions_list")
  print fractions_list
  
  makeDict3=oc.make_target_dict(cell_object=cell_object,
                                target_segs={'Seg1_comp_28':[55], 'Seg1_comp_68': [135]})
                                
  print makeDict3
  
  
  target_segs2, fractions_list2=oc.get_target_segments(makeDict3,{'Seg1_comp_x':1,'Seg1_comp_y':1})
  
  print("Will be printing target_segs")
  print target_segs2
  print("Will be printing fractions_list")
  print fractions_list2
  
  
  proj_info=oc_utils.read_connectivity('L23PyrRS','L23PyrFRB','netConnList')
  
  print proj_info
  
  
  
  cell_nml_file2 = 'L23PyrFRB.cell.nml'
          
  document_cell2 = neuroml.loaders.NeuroMLLoader.load(os.path.join(pathToNML2,cell_nml_file2))
                                
  cell_object2=document_cell2.cells[0]
  
  target_segments=oc.extract_seg_ids(cell_object=cell_object2,target_compartment_array=['basal_obl_dends'],targeting_mode='segGroups')
                              
  segLengthDict=oc.make_target_dict(cell_object=cell_object2,target_segs=target_segments) 
  
  print segLengthDict
  
  
  network = neuroml.Network(id='Net0')     
  presynaptic_population = neuroml.Population(id="Pop0", component="L23PyrRS", type="populationList", size=1)
  postsynaptic_population=neuroml.Population(id="Pop1", component="L23PyrFRB", type="populationList", size=1)
          
  synapse_list=['AMPA','NMDA']
          
  projection_array={}
          
  for synapse_element in range(0,len(synapse_list) ):
          
      proj = neuroml.Projection(id="Proj%d"%synapse_element, 
                                presynaptic_population=presynaptic_population.id, 
                                postsynaptic_population=postsynaptic_population.id, 
                                synapse=synapse_list[synapse_element])
                                        
      projection_array[synapse_list[synapse_element] ]=proj
              
              
  parsed_target_dict={'basal_obl_dends': {'SegList': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 24, 25, 22, 23, 20, 21, 18, 19, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33, 30, 31, 28, 29, 26, 27, 48, 49, 46, 47, 44, 45, 42, 43, 64, 65, 62, 63, 60, 61, 58, 59, 56, 57, 54, 55, 52, 53, 50, 51, 72, 73, 70, 71, 68, 69, 66, 67], 'LengthDist': [25.0, 50.0, 75.0, 100.0, 125.0, 150.0, 175.0, 200.0, 225.0000012807632, 249.99999701896448, 274.9999982997277, 299.9999413836009, 324.99994266436414, 349.99992870308233, 374.99992998384556, 399.9999756051272, 424.9999756051272, 449.9999756051272, 474.9999756051272, 499.9999756051272, 524.9999756051272, 549.9999756051272, 574.9999756051272, 599.9999756051272, 624.9999756051272, 649.9999756051272, 674.9999756051272, 699.9999756051272, 724.9999756051272, 749.9999756051272, 774.9999756051272, 799.9999756051272, 824.9999741146091, 849.9995943443294, 874.9996247235468, 899.9999308454469, 924.9999175769843, 950.0002631896537, 975.0002596206808, 1000.0001576712268, 1025.0001576712268, 1050.0001576712268, 1075.0001576712268, 1100.0001576712268, 1125.0001576712268, 1150.0001576712268, 1175.0001576712268, 1200.0001576712268, 1225.0001576712268, 1250.0001576712268, 1275.0001576712268, 1300.0001576712268, 1325.0001576712268, 1350.0001576712268, 1375.0001576712268, 1400.0001576712268, 1425.0010159713997, 1450.0009008583847, 1475.0002938437874, 1500.000601351312, 1525.0002368231228, 1549.9998501247107, 1575.0001714886703, 1599.9998485298981, 1624.9998485298981, 1649.9998485298981, 1674.9998485298981, 1699.9998485298981, 1724.9998485298981, 1749.9998485298981, 1774.9998485298981, 1799.9998485298981]}}
    
              
  proj_array=oc.add_chem_projection(net=network,
                                    proj_array=projection_array,
                                    presynaptic_population=presynaptic_population,
                                    postsynaptic_population=postsynaptic_population,
                                    targeting_mode='convergent',
                                    synapse_list=synapse_list,
                                    seg_target_dict=parsed_target_dict,
                                    subset_dict={'basal_obl_dends':50},
                                    delays_dict={'NDMA':5},
                                    weights_dict={'AMPA':1.5,'NMDA':2})
                                            
  print proj_array
  
  
  for proj_key in proj_array.keys():
          
      proj=proj_array[proj_key]
              
      print len(proj.connection_wds)
  
  
  
  
  
  
  
