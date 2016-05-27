import pickle



#  1 From L23PyrRS

conn_dict_Traub=[]
proj1={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_SupPyr_SupPyr','Syn_NMDA_SupPyr_SupPyr'],'NumPerPostCell':50,'LocOnPostCell':'basal_obl_dends'}
conn_dict_Traub.append(proj1)

proj2={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_SupPyr_SupPyr','Syn_NMDA_SupPyr_SupPyr'],'NumPerPostCell':50,'LocOnPostCell':'basal_obl_dends'}
conn_dict_Traub.append(proj2)

proj3={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'SupBask','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_RSPyr_SupFS'],'NumPerPostCell':90,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj3)

proj4={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_RSPyr_SupFS'],'NumPerPostCell':90,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj4)

proj5={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_SupPyr_SupLTS','Syn_NMDA_RSPyr_SupLTS'],'NumPerPostCell':90,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj5)

proj6={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'SupBask','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_RSPyr_SupFS'],'NumPerPostCell':90,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj6)

proj7={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_SupPyr_L4SS','Syn_NMDA_SupPyr_L4SS'],'NumPerPostCell':3,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj7)

proj8={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':60,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub.append(proj8)

proj9={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':60,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub_append(proj9)

proj10={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':30,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj10)

proj11={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':30,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj11)

proj12={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_SupPyr_DeepLTS','Syn_NMDA_RSPyr_DeepLTS'],'NumPerPostCell':30,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub.append(proj12)

proj13={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':60,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub.append(proj13)

proj14={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_SupPyr_L6NT','Syn_NMDA_SupPyr_L6NT'],'NumPerPostCell':3,'LocOnPostCell':'apical_dend'}
conn_dict_Traub_append(proj14)

proj15={'type':'chem','PreCellGroup':'L23PyrRS','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':30,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj15)

proj16={'type':'elect','PreCellGroup':'L23PyrRS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_Elect_SupPyr_SupPyr'],'NumPerPostCell':0.72,'LocOnPostCell':'axon_group'}
conn_dict_Traub_append(proj16)

proj17={'type':'elect','PreCellGroup':'L23PyrRS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_Elect_SupPyr_SupPyr'],'NumPerPostCell':0.375,'LocOnPostCell':'axon_group'}
conn_dict_Traub_append(proj17)


#  2 From L23PyrFRB

proj18={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_SupPyr_SupPyr','Syn_NMDA_SupPyr_SupPyr'],'NumPerPostCell':5,'LocOnPostCell':'basal_obl_dends'}
conn_dict_Traub_append(proj18)

proj19={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_SupPyr_SupPyr','Syn_NMDA_SupPyr_SupPyr'],'NumPerPostCell':5,'LocOnPostCell':'basal_obl_dends'}
conn_dict_Traub_append(proj19)

proj20={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'SupBask','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_FRBPyr_SupFS'],'NumPerPostCell':5,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj20)

proj21={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_SupPyr_SupFS','Syn_NMDA_FRBPyr_SupFS'],'NumPerPostCell':5,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj21)

proj22={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_SupPyr_SupLTS','Syn_NMDA_FRBPyr_SupLTS'],'NumPerPostCell':5,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj22)

proj23={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_SupPyr_L4SS','Syn_NMDA_SupPyr_L4SS'],'NumPerPostCell':1,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj23)

proj24={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':3,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub_append(proj24)

proj25={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_SupPyr_L5Pyr','Syn_NMDA_SupPyr_L5Pyr'],'NumPerPostCell':3,'LocOnPostCell':'apic_shaft'}
conn_dict_Traub_append(proj25)

proj26={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':3,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj26)

proj27={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_SupPyr_L4SS','Syn_NMDA_SupPyr_L4SS'],'NumPerPostCell':1,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj27)

proj28={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_SupPyr_DeepFS','Syn_NMDA_SupPyr_DeepFS'],'NumPerPostCell':3,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj24)

proj29={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_SupPyr_DeepLTS','Syn_NMDA_FRBPyr_DeepLTS'],'NumPerPostCell':3,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj29)

proj30={'type':'chem','PreCellGroup':'L23PyrFRB','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_SupPyr_L6NT','Syn_NMDA_SupPyr_L6NT'],'NumPerPostCell':1,'LocOnPostCell':'apical_dend'}
conn_dict_Traub_append(proj30)

proj31={'type':'elec','PreCellGroup':'L23PyrFRB','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_Elect_SupPyr_SupPyr'],'NumPerPostCell':0.08,'LocOnPostCell':'axon_group'}
conn_dict_Traub_append(proj31)



#  3 From SupBask

proj32={'type':'chem','PreCellGroup':'SupBask','PostCellGroup':'L23PyrRS','SynapseList':['Syn_GABAA_SupBask_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'prox_dends_soma'}
conn_dict_Traub_append(proj32)

proj33={'type':'chem','PreCellGroup':'SupBask','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_GABAA_SupBask_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'prox_dends_soma'}
conn_dict_Traub_append(proj33)

proj34={'type':'chem','PreCellGroup':'SupBask','PostCellGroup':'SupBask','SynapseList':['Syn_GABAA_SupBask_supBask'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj34)

proj35={'type':'chem','PreCellGroup':'SupBask','PostCellGroup':'SupAxAx','SynapseList':['Syn_GABAA_SupBask_SupAxAx'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj35)

proj36={'type':'chem','PreCellGroup':'SupBask','PostCellGroup':'SupLTS','SynapseList':['Syn_GABAA_SupBask_SupLTS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj36)

proj37={'type':'chem','PreCellGroup':'SupBask','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_SupBask_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'prox_dends_soma'}
conn_dict_Traub_append(proj37)

proj38={'type':'elec','PreCellGroup':'SupBask','PostCellGroup':'SupBask','SynapseList':['Syn_Elect_CortIN_CortIN'],'NumPerPostCell':2.22,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj38)



#  4 From SupAxAx

proj39={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L23PyrRS','SynapseList':['Syn_GABAA_SupAxAx_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'prox_axon'}
conn_dict_Traub_append(proj39)

proj40={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_GABAA_SupAxAx_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'prox_axon'}
conn_dict_Traub_append(proj40)

proj41={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_SupAxAx_L4SS'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub_append(proj41)

proj42={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L5TuftIB','SynapseList':['Syn_GABAA_SupAxAx_DeepPyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub_append(proj42)

proj43={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L5TuftRS','SynapseList':['Syn_GABAA_SupAxAx_DeepPyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub_append(proj43)

proj44={'type':'chem','PreCellGroup':'SupAxAx','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_GABAA_SupAxAx_DeepPyr'],'NumPerPostCell':5,'LocOnPostCell':'prox_axon'}
conn_dict_Traub_append(proj44)


#  5 From SupLTS

proj45={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_GABAA_SupLTS_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub_append(proj45)

proj46={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_GABAA_SupLTS_SupPyr'],'NumPerPostCell':20,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub_append(proj46)

proj47={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'SupBask','SynapseList':['Syn_GABAA_SupLTS_FS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub_append(proj47)

proj48={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'SupAxAx','SynapseList':['Syn_GABAA_SupLTS_FS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub_append(proj48)

proj49={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'SupLTS','SynapseList':['Syn_GABAA_SupLTS_LTS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub_append(proj49)

proj50={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_GABAA_SupLTS_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub_append(proj50)

proj51={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_GABAA_SupLTS_L5Pyr'],'NumPerPostCell':20,'LocOnPostCell':'dend_tips_shaft'}
conn_dict_Traub_append(proj51)

proj52={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_GABAA_SupLTS_L5Pyr'],'NumPerPostCell':20,'LocOnPostCell':'dend_tips_shaft'}
conn_dict_Traub_append(proj52)

proj53={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'DeepBask','SynapseList':['Syn_GABAA_SupLTS_FS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub_append(proj53)

proj54={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_GABAA_SupLTS_FS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub_append(proj54)

proj55={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'DeepLTS','SynapseList':['Syn_GABAA_SupLTS_LTS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_plus_dends'}
conn_dict_Traub_append(proj55)

proj56={'type':'chem','PreCellGroup':'SupLTS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_GABAA_SupLTS_L6NT'],'NumPerPostCell':20,'LocOnPostCell':'LTS_dends'}
conn_dict_Traub_append(proj56)

proj57={'type':'elec','PreCellGroup':'SupLTS','PostCellGroup':'SupLTS','SynapseList':['Syn_Elect_CortIN_CortIN'],'NumPerPostCell':2.22,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj57)


# 6 from L4 Spiny Stellate

proj58={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'basal_dends'}
conn_dict_Traub_append(proj58)

proj59={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'basal_dends'}
conn_dict_Traub_append(proj59)

proj60={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'SupBask','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj60)

proj61={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj61)

proj62={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj62)

proj63={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_L4SS_L4SS','Syn_NMDA_L4SS_L4SS'],'NumPerPostCell':30,'LocOnPostCell':'mid_dist_dends'}
conn_dict_Traub_append(proj63)

proj64={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'L4SS_dends'}
conn_dict_Traub_append(proj64)

proj65={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'L4SS_dends'}
conn_dict_Traub_append(proj65)

proj66={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj66)

proj67={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj67)

proj68={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_L4SS_IN','Syn_NMDA_L4SS_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj68)

proj69={'type':'chem','PreCellGroup':'L4SpinStell','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_L4SS_Pyr','Syn_NMDA_L4SS_Pyr'],'NumPerPostCell':20,'LocOnPostCell':'L4SS'}
conn_dict_Traub_append(proj69)

proj70={'type':'elec','PreCellGroup':'L4SpinStell','PostCellGroup':'L4SpinStell','SynapseList':['Syn_Elect_L4SS_L4SS'],'NumPerPostCell':1,'LocOnPostCell':'axon_group'}
conn_dict_Traub_append(proj70)

# 7 From L5 Tufted IB Pyr

proj71={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_L5IB_SupPyr','Syn_NMDA_L5IB_SupPyr'],'NumPerPostCell':2,'LocOnPostCell':'mid_apic_dends'}
conn_dict_Traub_append(proj71)

proj72={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_L5IB_SupPyr','Syn_NMDA_L5IB_SupPyr'],'NumPerPostCell':2,'LocOnPostCell':'mid_apic_dends'}
conn_dict_Traub_append(proj72)

proj73={'type':'chem','PreCellGroup':'L5TUftIB','PostCellGroup':'SupBask','SynapseList':['Syn_AMPA_L5IB_SupFS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj73)

proj74={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L5IB_SupFS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj74)

proj75={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_L5IB_SupLTS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj75)

proj76={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_L5IB_L4SS','Syn_NMDA_L5IB_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj76)

proj77={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_L5IB_L5Pyr','Syn_NMDA_L5IB_DeepPyr'],'NumPerPostCell':50,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub_append(proj77)

proj78={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_L5IB_L5Pyr','Syn_NMDA_L5IB_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub_append(proj78)

proj79={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_L5IB_DeepFS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj79)

proj80={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_L5IB_DeepFS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj80)

proj81={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_L5IB_DeepLTS','Syn_NMDA_L5IB_IN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_tens'}
conn_dict_Traub_append(proj81)

proj82={'type':'chem','PreCellGroup':'L5TuftIB','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_L5IB_L6NT','Syn_NMDA_L5IB_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'L5Pyr_dends'}
conn_dict_Traub_append(proj82)

proj83={'type':'elec','PreCellGroup':'L5TuftIB','PostCellGroup':'L5TuftIB','SynapseList':['Syn_Elect_DeepPyr_DeepPyr'],'NumPerPostCell':0.4375,'LocOnPostCell':'axon_group'}
conn_dict_Traub_append(proj83)

proj84={'type':'elec','PreCellGroup':'L5TuftIB','PostCellGroup':'L5TuftRS','SynapseList':['Syn_Elect_DeepPyr_DeepPyr'],'NumPerPostCell':0.05,'LocOnPostCell':'axon_group'}
conn_dict_Traub_append(proj84)

# 8 From L5 Tufted RS Pyr

proj85={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_L5RS_SupPyr','Syn_NMDA_L5RS_SupPyr'],'NumPerPostCell':2,'LocOnPostCell':'mid_apic_dends'}
conn_dict_Traub_append(proj85)

proj86={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_L5RS_SupPyr','Syn_NMDA_L5RS_SupPyr'],'NumPerPostCell':2,'LocOnPostCell':'mid_apic_dends'}
conn_dict_Traub_append(proj86)

proj87={'type':'chem','PreCellGroup':'L5TUftRS','PostCellGroup':'SupBask','SynapseList':['Syn_AMPA_L5RS_SupFS','Syn_NMDA_L5RS_SupIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj87)

proj88={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L5RS_SupFS','Syn_NMDA_L5RS_SupIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj88)

proj89={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_L5RS_SupLTS','Syn_NMDA_L5RS_SupIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj89)

proj90={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_L5RS_L4SS','Syn_NMDA_L5RS_L4SS'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj90)

proj91={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_L5RS_L5Pyr','Syn_NMDA_L5RS_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub_append(proj91)

proj92={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_L5RS_L5Pyr','Syn_NMDA_L5RS_DeepPyr'],'NumPerPostCell':10,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub_append(proj92)

proj93={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_L5RS_DeepFS','Syn_NMDA_L5RS_DeepIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj93)

proj94={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_L5RS_DeepFS','Syn_NMDA_L5RS_DeepIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj94)

proj95={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_L5RS_DeepLTS','Syn_NMDA_L5RS_DeepIN'],'NumPerPostCell':20,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj95)

proj96={'type':'chem','PreCellGroup':'L5TuftRS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_L5RS_L6NT','Syn_NMDA_L5RS_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'L5Pyr_dends'}
conn_dict_Traub_append(proj96)

proj97={'type':'elec','PreCellGroup':'L5TuftRS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_Elect_DeepPyr_DeepPyr'],'NumPerPostCell':1.75,'LocOnPostCell':'axon_group'}
conn_dict_Traub_append(proj97)


# 9 From L6 Non Tufted Pyr

proj98={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L23PyrRS','SynapseList':['Syn_AMPA_L6NT_SupPyr','Syn_NMDA_L6NT_SupPyr'],'NumPerPostCell':10,'LocOnPostCell':'L6Pyr_dends'}
conn_dict_Traub_append(proj98)

proj99={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L23PyrFRB','SynapseList':['Syn_AMPA_L6NT_SupPyr','Syn_NMDA_L6NT_SupPyr'],'NumPerPostCell':10,'LocOnPostCell':'L6Pyr_dends'}
conn_dict_Traub_append(proj99)

proj100={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'SupBask','SynapseList':['Syn_AMPA_L6NT_SupFS','Syn_NMDA_L6NT_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj100)

proj101={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L6NT_SupFS','Syn_NMDA_L6NT_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj101)

proj102={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'SupLTS','SynapseList':['Syn_AMPA_L6NT_SupLTS','Syn_NMDA_L6NT_SupLTS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj102)

proj103={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L4SpinStell','SynapseList':['Syn_AMPA_L6NT_L4SS','Syn_NMDA_L6NT_L4SS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj103)

proj104={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L5TuftIB','SynapseList':['Syn_AMPA_L6NT_L5Pyr','Syn_NMDA_L6NT_DeepPyr'],'NumPerPostCell':10,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub_append(proj104)

proj105={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L5TuftRS','SynapseList':['Syn_AMPA_L6NT_L5Pyr','Syn_NMDA_L6NT_DeepPyr'],'NumPerPostCell':10,'LocOnPostCell':'dends_no_tuft'}
conn_dict_Traub_append(proj105)

proj106={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'DeepBask','SynapseList':['Syn_AMPA_L6NT_DeepFS','Syn_NMDA_L6NT_DeepFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj106)

proj107={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'DeepAxAx','SynapseList':['Syn_AMPA_L6NT_DeepFS','Syn_NMDA_L6NT_DeepFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj107)

proj108={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'SupAxAx','SynapseList':['Syn_AMPA_L6NT_SupFS','Syn_NMDA_L6NT_SupFS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj108)

proj109={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'DeepLTS','SynapseList':['Syn_AMPA_L6NT_DeepLTS','Syn_NMDA_L6NT_DeepLTS'],'NumPerPostCell':10,'LocOnPostCell':'mid_tip_dends'}
conn_dict_Traub_append(proj109)

proj110={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_AMPA_L6NT_L6NT','Syn_NMDA_L6NT_DeepPyr'],'NumPerPostCell':20,'LocOnPostCell':'L6Pyr_dends'}
conn_dict_Traub_append(proj110)

proj111={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'TCR','SynapseList':['Syn_AMPA_L6NT_TCR','Syn_NMDA_L6NT_TCR'],'NumPerPostCell':20,'LocOnPostCell':'distal_dends'}
conn_dict_Traub_append(proj111)

proj112={'type':'chem','PreCellGroup':'L6NonTuftRS','PostCellGroup':'nRT','SynapseList':['Syn_AMPA_L6NT_nRT','Syn_NMDA_L6NT_nRT'],'NumPerPostCell':20,'LocOnPostCell':'proximal_dends'}
conn_dict_Traub_append(proj112)

proj113={'type':'elec','PreCellGroup':'L6NonTuftRS','PostCellGroup':'L6NonTuftRS','SynapseList':['Syn_Elect_DeepPyr_Deep_Pyr'],'NumPerPostCell':1,'LocOnPostCell':'axon_group'}
conn_dict_Traub_append(proj113)

# 10 From Deep Basket

CG3D_DeepBask       CG3D_L4SpinStell    [Syn_GABAA_DeepFS_L4SS]                             20      prox_dends_soma

CG3D_DeepBask       CG3D_L5TuftIB       [Syn_GABAA_DeepBask_L5Pyr]                          20      DeepBask_dends
CG3D_DeepBask       CG3D_L5TuftRS       [Syn_GABAA_DeepBask_L5Pyr]                          20      DeepBask_dends

CG3D_DeepBask       CG3D_DeepBask       [Syn_GABAA_DeepBask_DeepFS]                         20      mid_tip_dends
CG3D_DeepBask       CG3D_DeepAxAx       [Syn_GABAA_DeepBask_DeepFS]                         20      mid_tip_dends
CG3D_DeepBask       CG3D_DeepLTS        [Syn_GABAA_DeepBask_DeepLTS]                        20      mid_tip_dends

CG3D_DeepBask       CG3D_L6NonTuftRS    [Syn_GABAA_DeepBask_L6NT]                           20      DeepBask_dends

                                                              # Half value in appendix. This is num per each tgt, the src conns will add 2.5 to the avg per axon
CG3D_DeepBask       CG3D_DeepBask       [Syn_Elect_CortIN_CortIN]                           2.5     mid_tip_dends


# 11 From Deep AxAx

CG3D_DeepAxAx       CG3D_L23PyrRS       [Syn_GABAA_DeepAxAx_Pyr]                            5       prox_axon
CG3D_DeepAxAx       CG3D_L23PyrFRB      [Syn_GABAA_DeepAxAx_Pyr]                            5       prox_axon

CG3D_DeepAxAx       CG3D_L4SpinStell    [Syn_GABAA_DeepFS_L4SS]                             5       prox_axon

CG3D_DeepAxAx       CG3D_L5TuftIB       [Syn_GABAA_DeepAxAx_Pyr]                            5       prox_axon
CG3D_DeepAxAx       CG3D_L5TuftRS       [Syn_GABAA_DeepAxAx_Pyr]                            5       prox_axon

CG3D_DeepAxAx       CG3D_L6NonTuftRS    [Syn_GABAA_DeepAxAx_Pyr]                            5       prox_axon


# 12 From Deep LTS

CG3D_DeepLTS        CG3D_L23PyrRS       [Syn_GABAA_DeepLTS_SupPyr]                          10      LTS_dends
CG3D_DeepLTS        CG3D_L23PyrFRB      [Syn_GABAA_DeepLTS_SupPyr]                          10      LTS_dends

CG3D_DeepLTS        CG3D_SupBask        [Syn_GABAA_DeepLTS_SupFS]                           10      mid_dist_dends
CG3D_DeepLTS        CG3D_SupAxAx        [Syn_GABAA_DeepLTS_SupFS]                           10      mid_dist_dends
CG3D_DeepLTS        CG3D_SupLTS         [Syn_GABAA_DeepLTS_SupLTS]                          10      mid_dist_dends

CG3D_DeepLTS        CG3D_L4SpinStell    [Syn_GABAA_DeepLTS_L4SS]                            20      mid_dist_dends

CG3D_DeepLTS        CG3D_L5TuftIB       [Syn_GABAA_DeepLTS_L5IB]                            20      dend_tips_shaft
CG3D_DeepLTS        CG3D_L5TuftRS       [Syn_GABAA_DeepLTS_L5RS]                            20      dend_tips_shaft

CG3D_DeepLTS        CG3D_DeepBask       [Syn_GABAA_DeepLTS_DeepFS]                          20      mid_tip_plus_dends
CG3D_DeepLTS        CG3D_DeepAxAx       [Syn_GABAA_DeepLTS_DeepFS]                          20      mid_tip_plus_dends
CG3D_DeepLTS        CG3D_DeepLTS        [Syn_GABAA_DeepLTS_DeepLTS]                         20      mid_tip_plus_dends

CG3D_DeepLTS        CG3D_L6NonTuftRS    [Syn_GABAA_DeepLTS_L6NT]                            20      LTS_dends


CG3D_DeepLTS       CG3D_DeepLTS         [Syn_Elect_CortIN_CortIN]                           2.5     mid_tip_dends


# 13 From TCR

                                                    ## TODO: add delays!!!!
CG3D_TCR            CG3D_L23PyrRS       [Syn_AMPA_TCR_SupPyr,Syn_NMDA_TCR_SupPyr]           10      TCR_dends
CG3D_TCR            CG3D_L23PyrFRB      [Syn_AMPA_TCR_SupPyr,Syn_NMDA_TCR_SupPyr]           10      TCR_dends

CG3D_TCR            CG3D_SupBask        [Syn_AMPA_TCR_SupFS,Syn_NMDA_TCR_SupFS]             10      prox_mid_dends
CG3D_TCR            CG3D_SupAxAx        [Syn_AMPA_TCR_SupFS,Syn_NMDA_TCR_SupFS]             10      prox_mid_dends

CG3D_TCR            CG3D_L4SpinStell    [Syn_AMPA_TCR_L4SS,Syn_NMDA_TCR_L4SS]               20      dendrite_group

CG3D_TCR            CG3D_L5TuftIB       [Syn_AMPA_TCR_L5Pyr,Syn_NMDA_TCR_L5Pyr]             10      tuft_plus
CG3D_TCR            CG3D_L5TuftRS       [Syn_AMPA_TCR_L5Pyr,Syn_NMDA_TCR_L5Pyr]             10      tuft_plus

CG3D_TCR            CG3D_DeepBask       [Syn_AMPA_TCR_DeepBask,Syn_NMDA_TCR_DeepBask]       20      prox_mid_dends
CG3D_TCR            CG3D_DeepAxAx       [Syn_AMPA_TCR_DeepAxAx,Syn_NMDA_TCR_DeepAxAx]       10      prox_mid_dends

CG3D_TCR            CG3D_L6NonTuftRS    [Syn_AMPA_TCR_L6NT,Syn_NMDA_TCR_L6NT]               10      TCR_dends

CG3D_TCR            CG3D_nRT            [Syn_AMPA_TCR_nRT,Syn_NMDA_TCR_nRT]                 40      proximal_dends


# 14 From nRT

CG3D_nRT            CG3D_TCR            [Syn_GABAA_nRT_TCR_s,Syn_GABAA_nRT_TCR_s]           30      soma_prox_dends
CG3D_nRT            CG3D_nRT            [Syn_GABAA_nRT_nRT_s,Syn_GABAA_nRT_nRT_s]           10      soma_dends


CG3D_nRT            CG3D_nRT            [Syn_Elect_nRT_nRT]                                 2.5     dendrite_group
