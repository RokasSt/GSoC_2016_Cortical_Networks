from neuroml import *
from pyneuroml import pynml
import neuroml.writers as writers 

from pyneuroml.lems import generate_lems_file_for_neuroml

import random


def SingleCellSim(cell_ref,nc_simConfig,sim_duration):
    

    net_doc = pynml.read_neuroml2_file("%s.nml"%nc_simConfig)
    net_doc.id=nc_simConfig

    net=net_doc.networks[0]
    net.id=nc_simConfig


    net_doc.includes.append(IncludeType("../generatedNeuroML2/%s.cell.nml"%cell_ref))

    net_file = '%s.net.nml'%(net_doc.id)
    writers.NeuroMLWriter.write(net_doc, net_file)

    print("Written network with 1 cell in network to: %s"%(net_file))

    from neuroml.utils import validate_neuroml2

    validate_neuroml2(net_file)

    generate_lems_file_for_neuroml("Sim_"+net_doc.id, 
                               net_file, 
                               net_doc.id, 
                               sim_duration,
                               0.025, 
                               "LEMS_%s.xml"%net_doc.id,
                               ".",
                               gen_plots_for_all_v = True,
                               plot_all_segments = False,
                               gen_saves_for_all_v = True,
                               save_all_segments = False,
                               copy_neuroml = False,
                               seed = 1234)

#pynml.nml2_to_svg(net_file)


if __name__=="__main__":

  #SingleCellSim("SupBasket","Test_Cell3_supbask_FigA2a")
  #SingleCellSim("L23PyrRS","Cell1_supppyrRS_10ms",10)
  #SingleCellSim("L23PyrRS","Cell1_supppyrRS_FIgA1RS",800)
  #SingleCellSim("L23PyrFRB","Cell2_suppyrFRB_10ms",10)
  #SingleCellSim("L23PyrFRB","Cell2_suppyrFRB_FigA1FRB",800)
  #SingleCellSim("SupBasket","Cell3_supbask_10ms",10)
  #SingleCellSim("SupAxAx","Cell4_supaxax_10ms",10)
  #SingleCellSim("SupAxAx","Cell4_supaxax_FigA2a",300)
  #SingleCellSim("SupLTSInter","Cell5_supLTS_10ms",10)
  #SingleCellSim("SupLTSInter","Cell5_supLTS_FigA2b",300)
  #SingleCellSim("L4SpinyStellate","Cell6_spinstell_10ms",30)
  #SingleCellSim("L4SpinyStellate","Cell6_spinstell_FigA3_167",700)
  #SingleCellSim("L4SpinyStellate","Cell6_spinstell_FigA3_250",700)
  #SingleCellSim("L4SpinyStellate","Cell6_spinstell_FigA3_333",700)
  #SingleCellSim("L5TuftedPyrIB","Cell7_tuftIB_10ms",10)
  #SingleCellSim("L5TuftedPyrIB","Cell7_tuftIB_FIgA4_900",700)
  #SingleCellSim("L5TuftedPyrIB","Cell7_tuftIB_FigA4_1100",700)
  #SingleCellSim("L5TuftedPyrIB","Cell7_tuftIB_FigA4_1300",700)
  #SingleCellSim("L5TuftedPyrIB","Cell7_tuftIB_FigA4_1500",700)
  #SingleCellSim("L5TuftedPyrRS","Cell8_tuftRS_10ms",10)
  #SingleCellSim("L5TuftedPyrRS","Cell8_tuftRS_FigA5_800",700)
  #SingleCellSim("L5TuftedPyrRS","Cell8_tuftRS_Fig5A_1000",700)
  #SingleCellSim("L5TuftedPyrRS","Cell8_tuftRS_Fig5A_1200",700)
  #SingleCellSim('L5TuftedPyrRS','Cell8_tuftRS_Fig5A_1400',700)
  #SingleCellSim("L6NonTuftedPyrRS","Cell9_nontuftRS_10ms",50)
  #SingleCellSim("L6NonTuftedPyrRS","Cell9_nontuftRS_FigA6_500",800)
  #SingleCellSim("L6NonTuftedPyrRS","Cell9_nontuftRS_FigA6_800",800)
  #SingleCellSim("L6NonTuftedPyrRS","Cell9_nontuftRS_FigA6_1000",800)
  #SingleCellSim("DeepBasket","Cell10_deepbask_10ms",10)
  #SingleCellSim("DeepAxAx","Cell11_deepaxax_10ms",10)
  #SingleCellSim("DeepLTSInter","Cell12_deepLTS_10ms",10)
  #SingleCellSim("DeepLTSInter","Cell12_deepLTS_FigA2b",300)
  #SingleCellSim("TCR","Cell13_TCR_10ms",10)
  #SingleCellSim("TCR","Cell13_TCR_FigA7_100",350)
  #SingleCellSim("TCR","Cell13_TCR_FigA7_600",1500)
  #SingleCellSim("nRT","Cell14_nRT_10ms",30)
  #SingleCellSim("nRT","Cell14_nRT_FigA8_00",200)
  #SingleCellSim("nRT","Cell14_nRT_FigA8_300",450)
  #SingleCellSim("nRT","Cell14_nRT_FigA8_500",450)



  

