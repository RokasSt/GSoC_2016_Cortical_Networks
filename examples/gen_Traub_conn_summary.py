import json



#  1 From L23PyrRS

conn_dict_Traub=[]
proj1={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_SupPyr_SupPyr','Syn_NMDA_SupPyr_SupPyr'],'NumPerPostCell':50,'LocOnPostCell':'basal_obl_dends'}
conn_dict_Traub.append(proj1)

proj2={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_SupPyr_SupPyr','Syn_NMDA_SupPyr_SupPyr'],'NumPerPostCell':50,'LocOnPostCell':'basal_obl_dends'}
conn_dict_Traub.append(proj2)

proj3={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'SupBasket','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_RSPyr_SupFS'],'NumPerPostCell':90,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj3)

proj4={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_RSPyr_SupFS'],'NumPerPostCell':90,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj4)

proj5={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_SupPyr_SupLTS','Syn_NMDA_RSPyr_SupLTS'],'NumPerPostCell':90,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj5)

proj7={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_SupPyr_L4SS','Syn_NMDA_SupPyr_L4SS'],'NumPerPostCell':3,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj7)

proj8={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':60,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub.append(proj8)

proj9={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':60,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub.append(proj9)

proj10={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':30,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj10)

proj11={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':30,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj11)

proj12={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_SupPyr_DeepLTS','Syn_NMDA_RSPyr_DeepLTS'],'NumPerPostCell':30,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj12)

proj13={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':60,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub.append(proj13)

proj14={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_SupPyr_L6NT','Syn_NMDA_SupPyr_L6NT'],'NumPerPostCell':3,'LocOnPostCell':'apical_dend'}
conn_dict_Traub.append(proj14)

proj15={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':30,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj15)

### at the moment Syn_Elect_SupPyr_SupPyr is not in the generatedNeuroML2 directory which is copied to the '../NeuroML2/prototypes/Thalamocortical/
#proj16={'type':'elect','PreCellGroup':'L23PyrRS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_Elect_SupPyr_SupPyr'],'NumPerPostCell':0.72,'LocOnPostCell':'axon_group'}
#conn_dict_Traub.append(proj16)

#proj17={'type':'elect','PreCellGroup':'L23PyrRS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_Elect_SupPyr_SupPyr'],'NumPerPostCell':0.375,'LocOnPostCell':'axon_group'}
#conn_dict_Traub.append(proj17)


#  2 From L23PyrFRB

proj18={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_SupPyr_SupPyr','Syn_NMDA_SupPyr_SupPyr'],'NumPerPostCell':5,'LocOnPostCell':'basal_obl_dends'}
conn_dict_Traub.append(proj18)

proj19={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_SupPyr_SupPyr','Syn_NMDA_SupPyr_SupPyr'],'NumPerPostCell':5,'LocOnPostCell':'basal_obl_dends'}
conn_dict_Traub.append(proj19)

proj20={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'SupBasket','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_FRBPyr_SupFS'],'NumPerPostCell':5,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj20)

proj21={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_FRBPyr_SupFS'],'NumPerPostCell':5,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj21)

proj22={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_SupPyr_SupLTS','Syn_NMDA_FRBPyr_SupLTS'],'NumPerPostCell':5,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj22)

proj23={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_SupPyr_L4SS','Syn_NMDA_SupPyr_L4SS'],'NumPerPostCell':1,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj23)

proj24={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':3,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub.append(proj24)

proj25={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':3,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub.append(proj25)

proj26={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':3,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj26)

proj27={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_SupPyr_L4SS','Syn_NMDA_SupPyr_L4SS'],'NumPerPostCell':1,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj27)

proj28={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':3,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj24)

proj29={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_SupPyr_DeepLTS','Syn_NMDA_FRBPyr_DeepLTS'],'NumPerPostCell':3,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj29)

proj30={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_SupPyr_L6NT','Syn_NMDA_SupPyr_L6NT'],'NumPerPostCell':1,'LocOnPostCell':'apical_dend'}
conn_dict_Traub.append(proj30)

proj31={'type':'elec','PreCellGroup':'L23PyrFRB','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_Elect_SupPyr_SupPyr'],'NumPerPostCell':0.08,'LocOnPostCell':'axon_group'}
conn_dict_Traub.append(proj31)



#  3 From SupBask

proj32={'type':'chem','PreCellGroup':'SupBasket','PostCellGroup':'L23PyrRS','SynapseList':['Syn_GABAA_SupBask_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'prox_dends_soma'}
conn_dict_Traub.append(proj32)

proj33={'type':'chem','PreCellGroup':'SupBasket','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_GABAA_SupBask_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'prox_dends_soma'}
conn_dict_Traub.append(proj33)

proj34={'type':'chem','PreCellGroup':'SupBasket','PostCellGroup':'SupBasket','SynapseList':['Syn_GABAA_SupBask_SupBask'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj34)

proj35={'type':'chem','PreCellGroup':'SupBasket','PostCellGroup':'SupAxAx','SynapseList':['Syn_GABAA_SupBask_SupAxAx'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj35)

proj36={'type':'chem','PreCellGroup':'SupBasket','PostCellGroup':'SupLTS','SynapseList':['Syn_GABAA_SupBask_SupLTS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj36)

proj37={'type':'chem','PreCellGroup':'SupBasket','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_SupBask_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'prox_dends_soma'}
conn_dict_Traub.append(proj37)
#### at the moment Syn_Elect_CortIN_CortIN is not in the generatedNeuroML2 directory
#proj38={'type':'elec','PreCellGroup':'SupBasket','PostCellGroup':'SupBasket','SynapseList':['Syn_Elect_CortIN_CortIN'],'NumPerPostCell':2.22,'LocOnPostCell':'mid_tip_dends'}
#conn_dict_Traub.append(proj38)



#  4 From SupAxAx

proj39={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L23PyrRS','SynapseList':['Syn_GABAA_SupAxAx_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj39)

proj40={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_GABAA_SupAxAx_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj40)

proj41={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_SupAxAx_L4SS'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj41)

proj42={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L5TuftIB','SynapseList':['Syn_GABAA_SupAxAx_DeepPyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj42)

proj43={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L5TuftRS','SynapseList':['Syn_GABAA_SupAxAx_DeepPyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj43)

proj44={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_GABAA_SupAxAx_DeepPyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj44)


#  5 From SupLTS

proj45={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_GABAA_SupLTS_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub.append(proj45)

proj46={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_GABAA_SupLTS_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub.append(proj46)

proj47={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'SupBasket','SynapseList':['Syn_GABAA_SupLTS_FS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj47)

proj48={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'SupAxAx','SynapseList':['Syn_GABAA_SupLTS_FS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj48)

proj49={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'SupLTS','SynapseList':['Syn_GABAA_SupLTS_LTS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj49)

proj50={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_SupLTS_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj50)

proj51={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_GABAA_SupLTS_L5Pyr'],'NumPerPostCell':20,'LocOnPostCell':'dend_tips_shaft'}
conn_dict_Traub.append(proj51)

proj52={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_GABAA_SupLTS_L5Pyr'],'NumPerPostCell':20,'LocOnPostCell':'dend_tips_shaft'}
conn_dict_Traub.append(proj52)

proj53={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'DeepBask','SynapseList':['Syn_GABAA_SupLTS_FS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub.append(proj53)

proj54={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_GABAA_SupLTS_FS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub.append(proj54)

proj55={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'DeepLTS','SynapseList':['Syn_GABAA_SupLTS_LTS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub.append(proj55)

proj56={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_GABAA_SupLTS_L6NT'],'NumPerPostCell':20,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub.append(proj56)

proj57={'type':'elec','PreCellGroup':'SupLTS','PostCellGroup':'SupLTS','SynapseList':['Syn_Elect_CortIN_CortIN'],'NumPerPostCell':2.22,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj57)


# 6 from L4 Spiny Stellate

proj58={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'basal_dends'}
conn_dict_Traub.append(proj58)

proj59={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'basal_dends'}
conn_dict_Traub.append(proj59)

proj60={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'SupBasket','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj60)

proj61={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj61)

proj62={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj62)

proj63={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_L4SS_L4SS','Syn_NMDA_L4SS_L4SS'],'NumPerPostCell':30,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj63)

proj64={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'L4SS_dends'}
conn_dict_Traub.append(proj64)

proj65={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'L4SS_dends'}
conn_dict_Traub.append(proj65)

proj66={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj66)

proj67={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj67)

proj68={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj68)

proj69={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'L4SS'}
conn_dict_Traub.append(proj69)

proj70={'type':'elec','PreCellGroup':'L4SpinStell','PostCellGroup':'L4SpinStell','SynapseList':['Syn_Elect_L4SS_L4SS'],'NumPerPostCell':1,'LocOnPostCell':'axon_group'}
conn_dict_Traub.append(proj70)

# 7 From L5 Tufted IB Pyr

proj71={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_L5IB_SupPyr','Syn_NMDA_L5IB_SupPyr'],'NumPerPostCell':2,'LocOnPostCell':'mid_apic_dends'}
conn_dict_Traub.append(proj71)

proj72={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_L5IB_SupPyr','Syn_NMDA_L5IB_SupPyr'],'NumPerPostCell':2,'LocOnPostCell':'mid_apic_dends'}
conn_dict_Traub.append(proj72)

proj73={'type':'chem','PreCellGroup':'L5TUftIB','PostCellGroup':'SupBasket','SynapseList':['Syn_AMPA_L5IB_SupFS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj73)

proj74={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L5IB_SupFS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj74)

proj75={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_L5IB_SupLTS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj75)

proj76={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_L5IB_L4SS','Syn_NMDA_L5IB_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj76)

proj77={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_L5IB_L5Pyr','Syn_NMDA_L5IB_DeepPyr'],'NumPerPostCell':50,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub.append(proj77)

proj78={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_L5IB_L5Pyr','Syn_NMDA_L5IB_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub.append(proj78)

proj79={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_L5IB_DeepFS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj79)

proj80={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_L5IB_DeepFS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj80)

proj81={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_L5IB_DeepLTS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_tens'}
conn_dict_Traub.append(proj81)

proj82={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_L5IB_L6NT','Syn_NMDA_L5IB_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'L5Pyr_dends'}
conn_dict_Traub.append(proj82)

proj83={'type':'elec','PreCellGroup':'L5TuftIB','PostCellGroup':'L5TuftIB','SynapseList':['Syn_Elect_DeepPyr_DeepPyr'],'NumPerPostCell':0.4375,'LocOnPostCell':'axon_group'}
conn_dict_Traub.append(proj83)

proj84={'type':'elec','PreCellGroup':'L5TuftIB','PostCellGroup':'L5TuftRS','SynapseList':['Syn_Elect_DeepPyr_DeepPyr'],'NumPerPostCell':0.05,'LocOnPostCell':'axon_group'}
conn_dict_Traub.append(proj84)

#s 8 From L5 Tufted RS Pyr

proj85={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_L5RS_SupPyr','Syn_NMDA_L5RS_SupPyr'],'NumPerPostCell':2,'LocOnPostCell':'mid_apic_dends'}
conn_dict_Traub.append(proj85)

proj86={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_L5RS_SupPyr','Syn_NMDA_L5RS_SupPyr'],'NumPerPostCell':2,'LocOnPostCell':'mid_apic_dends'}
conn_dict_Traub.append(proj86)

proj87={'type':'chem','PreCellGroup':'L5TUftRS','PostCellGroup':'SupBasket','SynapseList':['Syn_AMPA_L5RS_SupFS','Syn_NMDA_L5RS_SupIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj87)

proj88={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L5RS_SupFS','Syn_NMDA_L5RS_SupIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj88)

proj89={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_L5RS_SupLTS','Syn_NMDA_L5RS_SupIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj89)

proj90={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_L5RS_L4SS','Syn_NMDA_L5RS_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj90)

proj91={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_L5RS_L5Pyr','Syn_NMDA_L5RS_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub.append(proj91)

proj92={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_L5RS_L5Pyr','Syn_NMDA_L5RS_DeepPyr'],'NumPerPostCell':10,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub.append(proj92)

proj93={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_L5RS_DeepFS','Syn_NMDA_L5RS_DeepIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj93)

proj94={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_L5RS_DeepFS','Syn_NMDA_L5RS_DeepIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj94)

proj95={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_L5RS_DeepLTS','Syn_NMDA_L5RS_DeepIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj95)

proj96={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_L5RS_L6NT','Syn_NMDA_L5RS_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'L5Pyr_dends'}
conn_dict_Traub.append(proj96)

proj97={'type':'elec','PreCellGroup':'L5TuftRS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_Elect_DeepPyr_DeepPyr'],'NumPerPostCell':1.75,'LocOnPostCell':'axon_group'}
conn_dict_Traub.append(proj97)


# 9 From L6 Non Tufted Pyr

proj98={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_L6NT_SupPyr','Syn_NMDA_L6NT_SupPyr'],'NumPerPostCell':10,'LocOnPostCell':'L6Pyr_dends'}
conn_dict_Traub.append(proj98)

proj99={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_L6NT_SupPyr','Syn_NMDA_L6NT_SupPyr'],'NumPerPostCell':10,'LocOnPostCell':'L6Pyr_dends'}
conn_dict_Traub.append(proj99)

proj100={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'SupBasket','SynapseList':['Syn_AMPA_L6NT_SupFS','Syn_NMDA_L6NT_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj100)

proj101={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L6NT_SupFS','Syn_NMDA_L6NT_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj101)

proj102={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_L6NT_SupLTS','Syn_NMDA_L6NT_SupLTS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj102)

proj103={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_L6NT_L4SS','Syn_NMDA_L6NT_L4SS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj103)

proj104={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_L6NT_L5Pyr','Syn_NMDA_L6NT_DeepPyr'],'NumPerPostCell':10,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub.append(proj104)

proj105={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_L6NT_L5Pyr','Syn_NMDA_L6NT_DeepPyr'],'NumPerPostCell':10,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub.append(proj105)

proj106={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_L6NT_DeepFS','Syn_NMDA_L6NT_DeepFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj106)

proj107={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_L6NT_DeepFS','Syn_NMDA_L6NT_DeepFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj107)

proj108={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L6NT_SupFS','Syn_NMDA_L6NT_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj108)

proj109={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_L6NT_DeepLTS','Syn_NMDA_L6NT_DeepLTS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj109)

proj110={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_L6NT_L6NT','Syn_NMDA_L6NT_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'L6Pyr_dends'}
conn_dict_Traub.append(proj110)

proj111={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'TCR','SynapseList':['Syn_AMPA_L6NT_TCR','Syn_NMDA_L6NT_TCR'],'NumPerPostCell':20,'LocOnPostCell':'distal_dends'}
conn_dict_Traub.append(proj111)

proj112={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'nRT','SynapseList':['Syn_AMPA_L6NT_nRT','Syn_NMDA_L6NT_nRT'],'NumPerPostCell':20,'LocOnPostCell':'proximal_dends'}
conn_dict_Traub.append(proj112)

proj113={'type':'elec','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_Elect_DeepPyr_Deep_Pyr'],'NumPerPostCell':1,'LocOnPostCell':'axon_group'}
conn_dict_Traub.append(proj113)

# 10 From Deep Basket

proj114={'type':'chem','PreCellGroup':'DeepBask','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_DeepFS_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'prox_dends_soma'}
conn_dict_Traub.append(proj114)

proj115={'type':'chem','PreCellGroup':'DeepBask','PostCellGroup':'L5TuftIB','SynapseList':['Syn_GABAA_DeepBask_L5Pyr'],'NumPerPostCell':20,'LocOnPostCell':'DeepBask_dends'}
conn_dict_Traub.append(proj115)

proj116={'type':'chem','PreCellGroup':'DeepBask','PostCellGroup':'L5TuftRS','SynapseList':['Syn_GABAA_DeepBask_L5Pyr'],'NumPerPostCell':20,'LocOnPostCell':'DeepBask_dends'}
conn_dict_Traub.append(proj116)

proj117={'type':'chem','PreCellGroup':'DeepBask','PostCellGroup':'DeepBask','SynapseList':['Syn_GABAA_DeepBask_DeepFS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj117)

proj118={'type':'chem','PreCellGroup':'DeepBask','PostCellGroup':'DeepAxAx','SynapseList':['Syn_GABAA_DeepBask_DeepFS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj118)

proj119={'type':'chem','PreCellGroup':'DeepBask','PostCellGroup':'DeepLTS','SynapseList':['Syn_GABAA_DeepBask_DeepLTS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj119)

proj120={'type':'chem','PreCellGroup':'DeepBask','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_GABAA_DeepBask_L6NT'],'NumPerPostCell':20,'LocOnPostCell':'DeepBask_dends'}
conn_dict_Traub.append(proj120)

proj121={'type':'elec','PreCellGroup':'DeepBask','PostCellGroup':'DeepBask','SynapseList':['Syn_Elect_CortIN_CortIN'],'NumPerPostCell':2.5,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj121)


# 11 From Deep AxAx

proj122={'type':'chem','PreCellGroup':'DeepAxAx','PostCellGroup':'L23PyrRS','SynapseList':['Syn_GABAA_DeepAxAx_Pyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj122)

proj123={'type':'chem','PreCellGroup':'DeepAxAx','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_GABAA_DeepAxAx_Pyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj123)

proj124={'type':'chem','PreCellGroup':'DeepAxAx','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_DeepFS_L4SS'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj124)

proj125={'type':'chem','PreCellGroup':'DeepAxAx','PostCellGroup':'L5TuftIB','SynapseList':['Syn_GABAA_DeepAxAx_Pyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj125)

proj126={'type':'chem','PreCellGroup':'DeepAxAx','PostCellGroup':'L5TuftRS','SynapseList':['Syn_GABAA_DeepAxAx_Pyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj126)

proj127={'type':'elec','PreCellGroup':'DeepAxAx','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_GABAA_DeepAxAx_Pyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub.append(proj127)


# 12 From Deep LTS

proj128={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_GABAA_DeepLTS_SupPyr'],'NumPerPostCell':10,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub.append(proj128)

proj129={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_GABAA_DeepLTS_SupPyr'],'NumPerPostCell':10,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub.append(proj129)

proj130={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'SupBasket','SynapseList':['Syn_GABAA_DeepLTS_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj130)

proj131={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'SupAxAx','SynapseList':['Syn_GABAA_DeepLTS_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj131)

proj132={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'SupLTS','SynapseList':['Syn_GABAA_DeepLTS_SupLTS'],'NumPerPostCell':10,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj132)

proj133={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_DeepLTS_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub.append(proj133)

proj134={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_GABAA_DeepLTS_L5IB'],'NumPerPostCell':20,'LocOnPostCell':'dend_tips_shaft'}
conn_dict_Traub.append(proj134)

proj135={'type':'elec','PreCellGroup':'DeepLTS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_GABAA_DeepLTS_L5RS'],'NumPerPostCell':20,'LocOnPostCell':'dend_tips_shaft'}
conn_dict_Traub.append(proj135)

proj136={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'DeepBask','SynapseList':['Syn_GABAA_DeepLTS_DeepFS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub.append(proj136)

proj137={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_GABAA_DeepLTS_DeepFS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub.append(proj137)

proj138={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'DeepLTS','SynapseList':['Syn_GABAA_DeepLTS_DeepLTS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub.append(proj138)

proj139={'type':'chem','PreCellGroup':'DeepLTS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_GABAA_DeepLTS_L6NT'],'NumPerPostCell':20,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub.append(proj139)

proj140={'type':'elec','PreCellGroup':'DeepLTS','PostCellGroup':'DeepLTS','SynapseList':['Syn_Elect_CortIN_CortIN'],'NumPerPostCell':2.5,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj140)


# 13 From TCR

proj141={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_TCR_SupPyr','Syn_NMDA_TCR_SupPyr'],'NumPerPostCell':10,'LocOnPostCell':'TCR_dends'}
conn_dict_Traub.append(proj141)

proj142={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_TCR_SupPyr','Syn_NMDA_TCR_SupPyr'],'NumPerPostCell':10,'LocOnPostCell':'TCR_dends'}
conn_dict_Traub.append(proj142)

proj143={'type':'elec','PreCellGroup':'TCR','PostCellGroup':'SupBasket','SynapseList':['Syn_AMPA_TCR_SupFS','Syn_NMDA_TCR_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'prox_mid_dends'}
conn_dict_Traub.append(proj143)

proj144={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_TCR_SupFS','Syn_NMDA_TCR_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'prox_mid_dends'}
conn_dict_Traub.append(proj144)

proj145={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_TCR_L4SS','Syn_NMDA_TCR_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'dendrite_group'}
conn_dict_Traub.append(proj145)

proj146={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_TCR_L5Pyr','Syn_NMDA_TCR_L5Pyr'],'NumPerPostCell':10,'LocOnPostCell':'tuft_plus'}
conn_dict_Traub.append(proj146)

proj147={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_TCR_L5Pyr','Syn_NMDA_TCR_L5Pyr'],'NumPerPostCell':10,'LocOnPostCell':'tuft_plus'}
conn_dict_Traub.append(proj147)

proj148={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_TCR_DeepBask','Syn_NMDA_TCR_DeepBask'],'NumPerPostCell':20,'LocOnPostCell':'prox_mid_dends'}
conn_dict_Traub.append(proj148)
                                                   ## TODO: add delays!!!!

proj149={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_TCR_DeepAxAx','Syn_NMDA_TCR_DeepAxAx'],'NumPerPostCell':10,'LocOnPostCell':'prox_mid_dends'}
conn_dict_Traub.append(proj149)

proj150={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_TCR_L6NT','Syn_NMDA_TCR_L6NT'],'NumPerPostCell':10,'LocOnPostCell':'TCR_dends'}
conn_dict_Traub.append(proj150)

proj151={'type':'chem','PreCellGroup':'TCR','PostCellGroup':'nRT','SynapseList':['Syn_AMPA_TCR_nRT','Syn_NMDA_TCR_nRT'],'NumPerPostCell':40,'LocOnPostCell':'proximal_dends'}
conn_dict_Traub.append(proj151)



# 14 From nRT

proj152={'type':'chem','PreCellGroup':'nRT','PostCellGroup':'TCR','SynapseList':['Syn_GABAA_nRT_TCR_s','Syn_GABAA_nRT_TCR_s'],'NumPerPostCell':30,'LocOnPostCell':'soma_prox_dends'}
conn_dict_Traub.append(proj152)

proj153={'type':'chem','PreCellGroup':'nRT','PostCellGroup':'nRT','SynapseList':['Syn_GABAA_nRT_nRT_s','Syn_GABAA_nRT_nRT_s'],'NumPerPostCell':10,'LocOnPostCell':'soma_dends'}
conn_dict_Traub.append(proj153)

proj154={'type':'elec','PreCellGroup':'nRT','PostCellGroup':'nRT','SynapseList':['Syn_Elect_nRT_nRT'],'NumPerPostCell':2.5,'LocOnPostCell':'dendrite_group'}
conn_dict_Traub.append(proj154)







if __name__=="__main__":

   with open("Traub_conn_data.json",'w') as fout:
        json.dump(conn_dict_Traub, fout)

