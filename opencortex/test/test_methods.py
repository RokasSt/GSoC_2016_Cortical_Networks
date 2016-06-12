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
          test_return1=oc.extract_seg_ids({'cellID':'L23PyrRS',
                                          'SegOrSegGroupList':['basal_obl_dends','most_prox_bas_dend'],
                                          'TargetingMode':'segGroups',
                                          'pathToCell':pathToNML2})
          
          
          self.assertEqual(set(['basal_obl_dends','most_prox_bas_dend']), set(test_return1.keys()))
          self.assertEqual(set(test_return1['basal_obl_dends']),set([16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 24, 25, 22, 23, 20, 21, 18, 19, 40, 41, 38, 39, 36, 37, 34, 35, 32, 33, 30, 31, 28, 29, 26, 27, 48, 49, 46, 47, 44, 45, 42, 43, 64, 65, 62, 63, 60, 61, 58, 59, 56, 57, 54, 55, 52, 53, 50, 51, 72, 73, 70, 71, 68, 69, 66, 67]))
          self.assertEqual(set(test_return1['most_prox_bas_dend']),set([16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3]) )
          #########################################
          test_return2=oc.extract_seg_ids({'cellID':'L23PyrRS',
                                           'SegOrSegGroupList':['Seg1_comp_68','Seg1_comp_28'],
                                           'TargetingMode':'segments',
                                           'pathToCell':pathToNML2})
                                           
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
        
          
          
          
         

