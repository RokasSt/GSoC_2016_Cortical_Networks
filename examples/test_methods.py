import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 



import opencortex.build as oc

if __name__=="__main__":

  pathToNML2=parentdir+"/NeuroML2/prototypes/Thalamocortical/"

  ##### test segment id extraction:
  #print oc.extract_seg_ids('L23PyrRS',['basal_obl_dends','most_prox_bas_dend'],'segGroups',pathToNML2)
  #print oc.extract_seg_ids('L23PyrRS',['comp_16'],'segGroups',pathToNML2)
  print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['Seg1_comp_68','Seg1_comp_28'],'TargetingMode':'segments','pathToCell':pathToNML2})
  
  #print oc.get_unique_membrane_points([['Seg1_comp_28', 55], ['Seg1_comp_68', 135]],{'SegOrSegGroupList':['Seg1_comp_28'],'ProbDict':{'Seg1_comp_28':1}},4)
  print oc.get_unique_membrane_points({'TargetDict':{'Seg1_comp_28':[55], 'Seg1_comp_68': [135]},'SegOrSegGroupList':['Seg1_comp_28','Seg1_comp_68'],'ProbDict':{'Seg1_comp_28':0.5,'Seg1_comp_68':0.5},'NumOfUniquePoints':10})
