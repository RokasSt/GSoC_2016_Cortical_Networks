import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


import build as oc

try:
    import unittest2 as unittest
except ImportError:
    import unittest
    
class TestNetBuildMethods(unittest.TestCase):
      
      def test_GroupsSegs(self):
          pathToNML2="../../NeuroML2/prototypes/Thalamocortical/"
          ###########################
          test_return1=oc.extract_seg_ids({'CellID':'L23PyrRS',
                                          'SegOrSegGroupList':['basal_obl_dends','most_prox_bas_dend'],
                                          'TargetingMode':'segGroups',
                                          'PathToCell':pathToNML2})
          
          
          self.assertEqual(set(['basal_obl_dends','most_prox_bas_dend']), set(test_return1.keys()))
          self.assertEqual(set(test_return1['basal_obl_dends']),set([16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 24, 25, 22, 23, 20, 21, 18, 19, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33, 30, 31, 28, 29, 26, 27, 48, 49, 46, 47, 44, 45, 42, 43, 64, 65, 62, 63, 60, 61, 58, 59, 56, 57, 54, 55, 52, 53, 50, 51, 72, 73, 70, 71, 68, 69, 66, 67]))
          self.assertEqual(set(test_return1['most_prox_bas_dend']),set([16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3]) )
          #########################################
          test_return2=oc.extract_seg_ids({'CellID':'L23PyrRS',
                                           'SegOrSegGroupList':['Seg1_comp_68','Seg1_comp_28'],
                                           'TargetingMode':'segments',
                                           'PathToCell':pathToNML2})
                                           
          self.assertEqual(set(['Seg1_comp_68','Seg1_comp_28']),set(test_return2.keys()) )
          self.assertEqual(set(test_return2['Seg1_comp_68']),set([135]) )
          self.assertEqual(set(test_return2['Seg1_comp_28']),set([55])  )
          #######################################################
          probDict1=oc.get_seg_probabilities(pathToNML2+"L23PyrRS.cell.nml",[55])
          self.assertEqual(['55'],probDict1.keys())
          self.assertEqual(probDict1['55'],1)
          probDict2=oc.get_seg_probabilities(pathToNML2+"L23PyrRS.cell.nml",[16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3])
          self.assertEqual(set(['16', '17', '14', '15', '12', '13', '10', '11', '8', '9', '6', '7', '4', '5', '2', '3']),set(probDict2.keys()))
          totalProb=0
          for seg in probDict2.keys():
              totalProb=totalProb+probDict2[seg]
          self.assertEqual(totalProb,1)
          ##########
          makeDict1=oc.make_target_dict({'Seg1_comp_28':[55], 'Seg1_comp_68': [135]},pathToNML2+"L23PyrRS.cell.nml")
          self.assertEqual(set(['Seg1_comp_28','Seg1_comp_68']),set(makeDict1.keys()))
          self.assertEqual(makeDict1['Seg1_comp_28'].keys(),['55'])
          self.assertEqual(makeDict1['Seg1_comp_68'].keys(),['135'])
          self.assertEqual(makeDict1['Seg1_comp_28']['55'],1)
          self.assertEqual(makeDict1['Seg1_comp_68']['135'],1)
          #######
          makeDict2=oc.make_target_dict({'basal_obl_dends': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 24, 25, 22, 23, 20, 21, 18, 19, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33, 30, 31, 28, 29, 26, 27, 48, 49, 46, 47, 44, 45, 42, 43, 64, 65, 62, 63, 60, 61, 58, 59, 56, 57, 54, 55, 52, 53, 50, 51, 72, 73, 70, 71, 68, 69, 66, 67], 'most_prox_bas_dend': [16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3]},pathToNML2+"L23PyrRS.cell.nml")
          self.assertEqual(set(makeDict2['basal_obl_dends'].keys()),set(['16', '17', '14', '15', '12', '13', '10', '11', '8', '9', '6', '7', '4', '5', '2', '3', '24', '25', '22', '23', '20', '21', '18', '19', '40', '41', '38', '39', '36', '37', '34', '35', '32', '33', '30', '31', '28', '29', '26', '27', '48', '49', '46', '47', '44', '45', '42', '43', '64', '65', '62', '63', '60', '61', '58', '59', '56', '57', '54', '55', '52', '53', '50', '51', '72', '73', '70', '71', '68', '69', '66', '67']))
          totalProb=0
          for seg in makeDict2['most_prox_bas_dend'].keys():
              totalProb=totalProb+makeDict2['most_prox_bas_dend'][seg]
          self.assertEqual(totalProb,1)
          
          
          equal_probabilities=oc.check_seg_probabilities(makeDict2['basal_obl_dends'],1e-06)
          self.assertTrue(equal_probabilities)
          equal_probabilities=oc.check_seg_probabilities(makeDict2['basal_obl_dends'],1e-09)
          self.assertFalse(equal_probabilities)
          
          
          test_target_segs1=oc.get_target_segments({'basal':{'2':1},'apical':{'3':1}},{'basal':10,'apical':2},1e-06)
          all_segs=[2,3]
          self.assertEqual(set(all_segs),set(test_target_segs1))
          count_apical=0
          count_basal=0
          for seg in test_target_segs1:
              if seg==2:
                 count_basal+=1
              if seg==3:
                 count_apical+=1
          self.assertEqual(count_basal,10)
          self.assertEqual(count_apical,2)
          test_target_segs2=oc.get_target_segments(makeDict2,{'basal_obl_dends':100,'most_prox_bas_dend':25},1e-09)
          self.assertEqual(len(test_target_segs2),125)
          basal_segs=makeDict2['basal_obl_dends'].keys()
          most_prox_segs=makeDict2['most_prox_bas_dend'].keys()
          count_basal=0
          count_most_prox=0
          basal_obl=test_target_segs2[0:100]
          most_prox=test_target_segs2[100:125]
          for seg in basal_obl:
              if str(seg) in basal_segs:
                 count_basal+=1
          for seg in most_prox:
              if str(seg) in most_prox_segs:
                 count_most_prox+=1
          self.assertEqual(count_basal,100)
          self.assertEqual(count_most_prox,25)
          
          test_get_unique_target_points=oc.get_unique_membrane_points([2,4,5,5,5,7,7])
          self.assertEqual(set(test_get_unique_target_points.keys()),set(['2','4','5','7']))
          self.assertEqual(1,len(test_get_unique_target_points['2']))
          self.assertEqual(1,len(test_get_unique_target_points['4']))
          self.assertEqual(3,len(test_get_unique_target_points['5']))
          self.assertEqual(2,len(test_get_unique_target_points['7']))
          
          
          
          
          
        
          
          
          
         

