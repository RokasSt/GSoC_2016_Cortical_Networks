import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 



import opencortex.build as oc

if __name__=="__main__":

  pathToNML2=parentdir+"/NeuroML2/prototypes/Thalamocortical/"

  ##### test segment id extraction:
  print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['basal_obl_dends','most_prox_bas_dend'],'TargetingMode':'segGroups','pathToCell':pathToNML2})
  
  print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['comp_16'],'TargetingMode':'segGroups','pathToCell':pathToNML2})
  print oc.extract_seg_ids({'cellID':'L23PyrRS','SegOrSegGroupList':['Seg1_comp_68','Seg1_comp_28'],'TargetingMode':'segments','pathToCell':pathToNML2})
  
  
  print oc.get_unique_membrane_points({'TargetDict':{'Seg1_comp_28':[55], 'Seg1_comp_68': [135]},'ProbDict':{'Seg1_comp_28':0.5,'Seg1_comp_68':0.5},'NumOfUniquePoints':10})
  print oc.get_unique_membrane_points({'TargetDict':{'basal_obl_dends': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 24, 25, 22, 23, 20, 21, 18, 19, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33, 30, 31, 28, 29, 26, 27, 48, 49, 46, 47, 44, 45, 42, 43, 64, 65, 62, 63, 60, 61, 58, 59, 56, 57, 54, 55, 52, 53, 50, 51, 72, 73, 70, 71, 68, 69, 66, 67], 'most_prox_bas_dend': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3]},'ProbDict':{'basal_obl_dends':1,'most_prox_bas_dend':0},'NumOfUniquePoints':10})
  print oc.get_unique_membrane_points({'TargetDict':{'Seg1_comp_28':[55], 'Seg1_comp_68': [135]},'ProbDict':{'Seg1_comp_28':0.5,'Seg1_comp_68':0.5},'NumOfUniquePoints':1})

 
