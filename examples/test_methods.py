import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 



import opencortex.build as oc

if __name__=="__main__":

  pathToNML2=parentdir+"/NeuroML2/prototypes/Thalamocortical/"

  ##### test segment id extraction:
  #print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['basal_obl_dends','most_prox_bas_dend'],'TargetingMode':'segGroups','pathToCell':pathToNML2})
  
  #print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['comp_16'],'TargetingMode':'segGroups','pathToCell':pathToNML2})
  #print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['Seg1_comp_68','Seg1_comp_28'],'TargetingMode':'segments','pathToCell':pathToNML2})
  
  #print oc.get_seg_probabilities(pathToNML2+"L23PyrRS.cell.nml",[55])
  #print oc.get_seg_probabilities(pathToNML2+"L23PyrRS.cell.nml",[16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3])
  
  target_dict1=oc.make_target_dict({'Seg1_comp_28':[55], 'Seg1_comp_68': [135]},pathToNML2+"L23PyrRS.cell.nml")
  target_dict2=oc.make_target_dict({'basal_obl_dends': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 24, 25, 22, 23, 20, 21, 18, 19, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33, 30, 31, 28, 29, 26, 27, 48, 49, 46, 47, 44, 45, 42, 43, 64, 65, 62, 63, 60, 61, 58, 59, 56, 57, 54, 55, 52, 53, 50, 51, 72, 73, 70, 71, 68, 69, 66, 67], 'most_prox_bas_dend': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3]},pathToNML2+"L23PyrRS.cell.nml")
  print target_dict1
  print target_dict2
  print oc.get_target_segments(target_dict1,{'Seg1_comp_28':5,'Seg1_comp_68':5},1e-06)
  ####################### Ps turn out to be very small - turning the coin won't work for very small values
  print oc.get_target_segments(target_dict2,{'most_prox_bas_dend':5},1e-06)
  
  pathToNML2_golgi=parentdir+"/NeuroML2/prototypes/Golgi/"
  
  print oc.extract_seg_ids({'cellID':'Golgi_10comp_3channels_1CaPool',
                            'SegOrSegGroupList':['apical_dendrite_group','basal_dendrite_group'],
                            'TargetingMode':'segGroups',
                            'pathToCell':pathToNML2_golgi})
                            
                            
  target_dict3=oc.make_target_dict({'basal_dendrite_group': [9, 10], 'apical_dendrite_group': [3, 4, 5, 6, 7, 8]},
                                   pathToNML2_golgi+"Golgi_10comp_3channels_1CaPool.cell.nml")
                                   
  print target_dict3
  
  print oc.get_target_segments({'basal_dendrite_group': {'9': 0.25,'15':0.25,'3':0.25,'8':0.25},'apical':{'10':0.5,'6':0.5}},{'basal_dendrite_group':10,'apical':2},1e-6)

  
  
  
  
