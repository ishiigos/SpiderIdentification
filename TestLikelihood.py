# Generating the table of likelihoods for the different character states for the Lyniphiidae species
import pandas as pd
import csv

# Reading the Excel file and converting it into csv
#ls_testExt = pd.read_excel("TestExt3.xlsx")
# print(xls_testExt)

# csvconvert = xls_testExt.to_csv(
#   r'C:\Users\ishii\OneDrive\Desktop\TestExt3csv.csv', index=None, header=True)

# Open the generated csv file and print it's contents as a dictionary

def get_neighbouring_countries(country):
    print(country)

def get_countries():

    return []

with open("Ext1531csv.csv", "r") as csvread:
    lines = csv.reader(csvread)
    next(lines)
#csvread = open("TestExt3csv.csv", "r")
    print("This is the csv \n", csvread)
    samplelist = []
    #lines = csv.reader(csvread)

    countries = get_countries() 
    
    like_male = 1/2
    like_female = 1/2

    like_igd = 1/4
    like_bro = 1/4
    like_clp = 1/4
    like_pgc = 1/4
    sum_OA = 0

    like_equal_to_prosoma = 1/3
    like_longer_than_prosoma = 1/3
    like_shorter_than_prosoma = 1/3
    sum_length_femur_p = 0

    like_inconsp_prosoma = 1/4
    like_margins_with_teeth = 1/4
    like_consp_hair = 1/4
    like_pits = 1/4
    sum_prosoma_app=0

    like_fovea_yes = 1/2
    like_fovea_no = 1/2
    sum_fovea_groove = 0

    like_consp_hairy_opisthosoma = 1/4
    like_patterned_opisthosoma = 1/4
    like_unicolour_opisthosoma = 1/4
    like_scutum_opisthosoma = 1/4
    sum_opisthosoma_app = 0

    like_multiple_dorsal_spine_femur = 1/3
    like_none_dorsal_spine_femur = 1/3
    like_one_dorsal_spine_femur = 1/3
    sum_dorsal_spine_femur_count = 0
    
    like_procurved_eye = 1/3
    like_recurved_eye = 1/3
    like_straight_eye = 1/3
    sum_posterior_eye_form = 0
    
    like_greater_than_d_pme = 1/3
    like_less_than_d_pme  = 1/3
    like_equal_to_d_pme = 1/3
    sum_pme_separation_rel_to_d = 0
    
    like_complex_headregion = 1/5
    like_inconsp_headregion = 1/5
    like_sulci_headregion = 1/5
    like_horn_headregion = 1/5
    like_lobe_headregion  = 1/5
    sum_headregion_m_app = 0
    
    like_eyes_normal = 1/2
    like_eyes_reduced = 1/2
    sum_eyes_app = 0
    
    like_about_the_same_ale = 1/3
    like_greater_than_ale_ = 1/3
    like_less_than_ale = 1/3        
    sum_ame_rel_to_lateral = 0

    like_multiple_prolateral_spine_femur = 1/3
    like_none_prolateral_spine_femur = 1/3
    like_one_prolateral_spine_femur = 1/3
    sum_pro_spines_femur_count = 0

    like_multiple_prolateral_spine_tibia = 1/3
    like_none_prolateral_spine_tibia = 1/3
    like_one_prolateral_spine_tibia = 1/3
    sum_pro_spines_tibia_count = 0
    
    like_conspicuously_large_teeth = 1/2
    like_unremarkable_teeth = 1/2
    sum_ant_teeth_app = 0
    
    like_apophyses_consp_str_app = 1/3
    like_none_consp_str_app = 1/3
    like_spines_consp_str_app = 1/3
    sum_consp_str_app = 0
    
    like_one_or_more_maxillae = 1/2
    like_unremarkable_maxillae = 1/2
    sum_maxillae_app = 0
    
    like_pitted_sternum = 1/3
    like_rugose_sternum = 1/3
    like_smooth_sternum = 1/3
    sum_sternum_app = 0

    like_sternum_yes = 1/2
    like_sternum_no = 1/2
    sum_sternum_coxae = 0
    
    like_distinctly_greater_sternum = 1/3
    like_distinctly_smaller_sternum = 1/3
    like_equal_sternum = 1/3
    sum_sternum_width_coxae = 0
    
    #like_11, like_12, like_13, like_14, like_15 = 1/5
    sum_tmi_rel_to_meta = 0
    like_10_to_19 = 1/9
    like_20_to_29 = 1/9
    like_30_to_39 = 1/9
    like_40_to_49 = 1/9
    like_50_to_59 = 1/9
    like_60_to_69 = 1/9
    like_70_to_79 = 1/9
    like_80_to_89 = 1/9
    like_90_to_98 = 1/9
    sum_tmi_range = 0
    
    like_tricho_present_metatarsus = 1/2
    like_tricho_absent_metatarsus = 1/2
    sum_meta_dorsal_tmiv = 0

    like_multiple_dorsal_spine_metatarsus = 1/3
    like_none_dorsal_spine_metatarsus = 1/3
    like_one_dorsal_spine_metatarsus = 1/3
    sum_dorsal_spine_meta_count = 0

    like_one_dorsal_spine_tibia = 1/2
    like_two_dorsal_spine_tibia = 1/2
    sum_tibia_no_of_spine = 0

    like_0000 = 1/6
    like_0011 = 1/6
    like_1111 = 1/6
    like_2211 = 1/6
    like_2221 = 1/6
    like_2222 = 1/6
    sum_tibia_spine_formula = 0

    like_no_ventral_tibia_spines = 1/2
    like_stout_ventral_tibia_spines = 1/2
    sum_tibia_ventral = 0

    like_m_pedipalp_unremarkable = 1/2
    like_m_pedipalp_conspicuous = 1/2
    sum_m_pedipalp_femur_app = 0

    like_consp_swollen_patella = 1/4
    like_unremarkable_patella = 1/4
    like_apophyses_patella = 1/4
    like_consp_spines_patella = 1/4
    sum_m_pedipalp_patella_app = 0

    like_unremarkable_tibia = 1/7
    like_complex_tibia = 1/7
    like_multiple_complex_tibia = 1/7
    like_multiple_simple_tibia = 1/7
    like_one_or_more_spines_tibia = 1/7
    like_simple_tibia = 1/7
    like_tufts_tibia = 1/7
    sum_m_pedipalp_tibia_app = 0

    like_margins_cymbium = 1/3
    like_simple_cymbium = 1/3
    like_elevations_cymbium = 1/3
    sum_m_pedipalp_cymbium_app = 0

    like_complex_paracym = 1/2
    like_simple_paracym = 1/2
    sum_m_pedipalp_paracymbium_form = 0

    like_absent_para_branches = 1/2
    like_present_para_branches = 1/2
    sum_m_pedipalp_para_branches =0

    like_consp_cir_embolus = 1/3
    like_consp_curl_embolus = 1/3
    like_unremarkable_embolus = 1/3
    sum_m_pedipalp_embolus_app = 0

    like_m_pedipalp_lamella_absent = 1/2
    like_m_pedipalp_lamella_conspicuous = 1/2
    sum_m_pedipalp_lamella = 0

    like_consp_f_claw = 1/2
    like_inconsp_f_claw = 1/2
    sum_f_palp_claw = 0

    like_unremarkable_epigyne = 1/6
    like_atrium_epigyne = 1/6
    like_septum_epigyne = 1/6
    like_lateral_plate_epigyne = 1/6 
    like_scape_epigyne = 1/6
    like_parmula_epigyne = 1/6
    sum_epigyne_app = 0

    like_flat_epigyne = 1/2
    like_protrud_epigyne = 1/2
    sum_epigyne_form = 0

    like_visible_seminal = 1/2
    like_not_visible_seminal = 1/2
    sum_epigyne_seminal = 0 

    sum_length_p = 0

    like_40_to_60 = 1/13
    like_60_to_80 = 1/13
    like_80_to_100 = 1/13
    like_100_to_120 = 1/13
    like_120_to_140 = 1/13
    like_140_to_160 = 1/13
    like_160_to_180 = 1/13
    like_180_to_200 = 1/13
    like_200_to_220 = 1/13
    like_220_to_240 = 1/13
    like_240_to_260 = 1/13
    like_260_to_280 = 1/13
    like_280_to_300 = 1/13
    sum_length_p_range = 0 

    countries =  ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Faroe Islands", "Finland", "France", "France / Corsica", "Georgia", "Germany", "Gibraltar (UK)", "Greece", "Greece / Crete", "Hungary", "Iceland", "Ireland", "Italy", "Italy / Sardinia", "Italy / Sicily", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Malta", "Moldova", "Montenegro", "Netherlands", "Northern Island", "Norway", "Poland", "Portugal", "Romania", "Russia, Central", "Russia, Eastern", "Russia, Franz Jozef Land", "Russia, Kaliningrad Region", "Russia, Northern", "Russia, Novaya Zemlya", "Russia, Southern", "Russia, Western", "Serbia", "Slovakia", "Slovenia", "Spain", "Spain / Balearic Islands", "Svalbard", "Sweden", "Switzerland", "Turkey (Asia)", "Turkey (Europe)", "Ukraine", "United Kingdom"]

    sum_sex = 0
    for line in lines:
        dict = {}
        species_name = line[0]
        sex = line[1]
        OA = line[2]
        length_p = line[3]
        length_p_range = line[4]
        length_femur_p = line[5]
        prosoma_app = line[6]
        fovea_as_groove = line[7]
        opisthosoma_app = line[8]
        dorsal_spine_femur_count = line[9]
        posterior_eye_form = line[10]
        pme_separation_rel_to_d = line[11]
        headregion_m_app = line[12]
        eyes_app = line[13]
        ame_rel_to_lateral = line[14]
        pro_spines_femur_count = line[15]
        pro_spines_tibia_count = line[16]
        ant_teeth_app = line[17]
        consp_str_app = line[18]
        maxillae_app = line[19]
        sternum_app = line[20]
        sternum_coxae = line[21]
        sternum_width_coxae = line[22]
        tmi_rel_to_meta = line[23]
        tmi_range = line[24]
        meta_dorsal_tmiv = line[25]
        dorsal_spine_meta_count = line[26]
        tibia_no_of_spine = line[27]
        tibia_spine_formula = line[28]
        tibia_ventral = line[29]
        m_pedipalp_femur_app = line[30]
        m_pedipalp_patella_app = line[31]
        m_pedipalp_tibia_app = line[32]
        m_pedipalp_cymbium_app = line[33]
        m_pedipalp_paracymbium_form = line[34]
        m_pedipalp_para_branches = line[35]
        m_pedipalp_embolus_app = line[36]
        m_pedipalp_lamella = line[37]
        dist = line[38]
        f_palp_claw = line[39]
        epigyne_app = line[40]
        epigyne_form = line[41]
        epigyne_seminal = line[42]
        desc = line[43]

        # print(fovea_as_groove)
        #print("here", species_name, sex, OA, length_p, length_p_range, length_femur_p, prosoma_app, fovea_as_groove, opisthosoma_app, dorsal_spine_femur_count, posterior_eye_form, pme_separation_rel_to_d, headregion_m_app, eyes_app, ame_rel_to_lateral, pro_spines_femur_count, pro_spines_tibia_count, ant_teeth_app, consp_str_app, maxillae_app, sternum_app, sternum_coxae, sternum_width_coxae, tmi_rel_to_meta, tmi_range, meta_dorsal_tmiv, dorsal_spine_meta_count, tibia_no_of_spine, tibia_spine_formula, tibia_ventral, m_pedipalp_femur_app, m_pedipalp_patella_app, m_pedipalp_tibia_app, m_pedipalp_cymbium_app, m_pedipalp_paracymbium_form, m_pedipalp_para_branches, m_pedipalp_embolus_app, m_pedipalp_lamella, f_palp_claw, epigyne_app, epigyne_form, epigyne_seminal, desc, dist)

        if sex == "Male":
            like_male = 0.9
            like_female = 0.1
            sum_sex = like_male + like_female
            dict["Species Name"] = species_name
            dict["Sex"] = sex
            dict["P(X | Sex_Male)"] = like_male
            dict["P(X | Sex_Female)"] = like_female
            dict["Sum P(Sex)"] = sum_sex
        elif sex == "Female":
            like_male = 0.1
            like_female = 0.9
            sum_sex = like_male + like_female
            dict["Species Name"] = species_name
            dict["Sex"] = sex
            dict["P(X | Sex_Male)"] = like_male
            dict["P(X | Sex_Female)"] = like_female
            dict["Sum P(Sex)"] = sum_sex
        else:
            sum_sex = like_male + like_female
            dict["Species Name"] = species_name
            dict["Sex"] = sex
            dict["P(X | Sex_Male)"] = like_male
            dict["P(X | Sex_Female)"] = like_female
            dict["Sum P(Sex)"] = sum_sex

        if OA == "inconspicuous, generally dark":
            like_igd = 0.9
            like_bro = 0.001
            like_clp = 0.09
            like_pgc = 0.009
            sum_OA = like_igd + like_bro + like_clp + like_pgc
            dict["Overall Appearance"] = OA
            dict["P(X | Overall Appearance_inconspicuous, generally dark)"] = like_igd
            dict["P(X | Overall Appearance_bright, red, orange)"] = like_bro
            dict["P(X | Overall Appearance_conspicuous contrast legs/prosoma)"] = like_clp
            dict["P(X | Overall Appearance_pale, ground or cave dweller)"] = like_pgc
            dict["Sum of P(OA)"] = sum_OA
            # samplelist.append(dict)
        elif OA == "bright, red, orange":
            like_igd = 0.01
            like_bro = 0.9
            like_clp = 0.045
            like_pgc = 0.045
            sum_OA = like_igd + like_bro + like_clp + like_pgc
            dict["Overall Appearance"] = OA
            dict["P(X | Overall Appearance_inconspicuous, generally dark)"] = like_igd
            dict["P(X | Overall Appearance_bright, red, orange)"] = like_bro
            dict["P(X | Overall Appearance_conspicuous contrast legs/prosoma)"] = like_clp
            dict["P(X | Overall Appearance_pale, ground or cave dweller)"] = like_pgc
            dict["Sum of P(OA)"] = sum_OA
        elif OA == "conspicuous contrast legs/prosoma":
            like_igd = 0.045
            like_bro = 0.01
            like_clp = 0.9
            like_pgc = 0.045
            sum_OA = like_igd + like_bro + like_clp + like_pgc
            dict["Overall Appearance"] = OA
            dict["P(X | Overall Appearance_inconspicuous, generally dark)"] = like_igd
            dict["P(X | Overall Appearance_bright, red, orange)"] = like_bro
            dict["P(X | Overall Appearance_conspicuous contrast legs/prosoma)"] = like_clp
            dict["P(X | Overall Appearance_pale, ground or cave dweller)"] = like_pgc
            dict["Sum of P(OA)"] = sum_OA
        elif OA == "pale, ground or cave dweller (careful with older specimens: fading)":
            like_igd = 0.005
            like_bro = 0.005
            like_clp = 0.09
            like_pgc = 0.9
            sum_OA = like_igd + like_bro + like_clp + like_pgc
            dict["Overall Appearance"] = OA
            dict["P(X | Overall Appearance_inconspicuous, generally dark)"] = like_igd
            dict["P(X | Overall Appearance_bright, red, orange)"] = like_bro
            dict["P(X | Overall Appearance_conspicuous contrast legs/prosoma)"] = like_clp
            dict["P(X | Overall Appearance_pale, ground or cave dweller)"] = like_pgc
            dict["Sum of P(OA)"] = sum_OA
        else:
            sum_OA = like_igd + like_bro + like_clp + like_pgc
            dict["Overall Appearance"] = OA
            dict["P(X | Overall Appearance_inconspicuous, generally dark)"] = like_igd
            dict["P(X | Overall Appearance_bright, red, orange)"] = like_bro
            dict["P(X | Overall Appearance_conspicuous contrast legs/prosoma)"] = like_clp
            dict["P(X | Overall Appearance_pale, ground or cave dweller)"] = like_pgc
            dict["Sum of P(OA)"] = sum_OA

        if length_femur_p == "equal in length":
            like_equal_to_prosoma = 0.9
            like_longer_than_prosoma = 0.05
            like_shorter_than_prosoma = 0.05
            sum_length_femur_p = like_equal_to_prosoma + like_longer_than_prosoma + like_shorter_than_prosoma
            dict["Length of femur I :<relative to prosoma>"] = length_femur_p
            dict["P(X | Length of femur I :<relative to prosoma>_equal in length)"] = like_equal_to_prosoma
            dict["P(X | Length of femur I :<relative to prosoma>_longer than prosoma)"] = like_longer_than_prosoma
            dict["P(X | Length of femur I :<relative to prosoma>_shorter than prosoma)"] = like_shorter_than_prosoma
            dict["Sum of P(Length of femur I :<relative to prosoma>)"] = sum_length_femur_p
            # samplelist.append(dict)
        elif length_femur_p == "longer than prosoma":
            like_equal_to_prosoma = 0.09
            like_longer_than_prosoma = 0.9
            like_shorter_than_prosoma = 0.01
            sum_length_femur_p = like_equal_to_prosoma + like_longer_than_prosoma + like_shorter_than_prosoma
            dict["Length of femur I :<relative to prosoma>"] = length_femur_p
            dict["P(X | Length of femur I :<relative to prosoma>_equal in length)"] = like_equal_to_prosoma
            dict["P(X | Length of femur I :<relative to prosoma>_longer than prosoma)"] = like_longer_than_prosoma
            dict["P(X | Length of femur I :<relative to prosoma>_shorter than prosoma)"] = like_shorter_than_prosoma
            dict["Sum of P(Length of femur I :<relative to prosoma>)"] = sum_length_femur_p
        elif length_femur_p == "shorter than prosoma":
            like_equal_to_prosoma = 0.09
            like_longer_than_prosoma = 0.01
            like_shorter_than_prosoma = 0.9
            sum_length_femur_p = like_equal_to_prosoma + like_longer_than_prosoma + like_shorter_than_prosoma
            dict["Length of femur I :<relative to prosoma>"] = length_femur_p
            dict["P(X | Length of femur I :<relative to prosoma>_equal in length)"] = like_equal_to_prosoma
            dict["P(X | Length of femur I :<relative to prosoma>_longer than prosoma)"] = like_longer_than_prosoma
            dict["P(X | Length of femur I :<relative to prosoma>_shorter than prosoma)"] = like_shorter_than_prosoma
            dict["Sum of P(Length of femur I :<relative to prosoma>)"] = sum_length_femur_p
        else:
            sum_length_femur_p = like_equal_to_prosoma + like_longer_than_prosoma + like_shorter_than_prosoma
            dict["Length of femur I :<relative to prosoma>"] = length_femur_p
            dict["P(X | Length of femur I :<relative to prosoma>_equal in length)"] = like_equal_to_prosoma
            dict["P(X | Length of femur I :<relative to prosoma>_longer than prosoma)"] = like_longer_than_prosoma
            dict["P(X | Length of femur I :<relative to prosoma>_shorter than prosoma)"] = like_shorter_than_prosoma
            dict["Sum of P(Length of femur I :<relative to prosoma>)"] = sum_length_femur_p

        if prosoma_app == "inconspicuous":
            like_inconsp_prosoma = 0.8
            like_margins_with_teeth = 0.0667
            like_consp_hair = 0.0667
            like_pits = 0.0667
            sum_prosoma_app = like_inconsp_prosoma + like_margins_with_teeth + like_consp_hair + like_pits
            dict["Prosoma <appearance>"] = prosoma_app
            dict["P(X | Prosoma <appearance>_inconspicuous)"] = like_inconsp_prosoma
            dict["P(X | Prosoma <appearance>_margins with teeth)"] = like_margins_with_teeth
            dict["P(X | Prosoma <appearance>_with conspicuous hairs/spines)"] = like_consp_hair
            dict["P(X | Prosoma <appearance>_with pits (dorsally))"] = like_pits
            dict["Sum of P(Prosoma <appearance>)"] = sum_prosoma_app
            # samplelist.append(dict)
        elif prosoma_app == "margins with teeth":
            like_inconsp_prosoma = 0.04
            like_margins_with_teeth = 0.8
            like_consp_hair = 0.08
            like_pits = 0.08
            sum_prosoma_app = like_inconsp_prosoma + like_margins_with_teeth + like_consp_hair + like_pits
            dict["Prosoma <appearance>"] = prosoma_app
            dict["P(X | Prosoma <appearance>_inconspicuous)"] = like_inconsp_prosoma
            dict["P(X | Prosoma <appearance>_margins with teeth)"] = like_margins_with_teeth
            dict["P(X | Prosoma <appearance>_with conspicuous hairs/spines)"] = like_consp_hair
            dict["P(X | Prosoma <appearance>_with pits (dorsally))"] = like_pits
            dict["Sum of P(Prosoma <appearance>)"] = sum_prosoma_app
        elif prosoma_app == "with conspicuous hairs/spines":
            like_inconsp_prosoma = 0.04
            like_margins_with_teeth = 0.08
            like_consp_hair = 0.8
            like_pits = 0.08
            sum_prosoma_app = like_inconsp_prosoma + like_margins_with_teeth + like_consp_hair + like_pits
            dict["Prosoma <appearance>"] = prosoma_app
            dict["P(X | Prosoma <appearance>_inconspicuous)"] = like_inconsp_prosoma
            dict["P(X | Prosoma <appearance>_margins with teeth)"] = like_margins_with_teeth
            dict["P(X | Prosoma <appearance>_with conspicuous hairs/spines)"] = like_consp_hair
            dict["P(X | Prosoma <appearance>_with pits (dorsally))"] = like_pits
            dict["Sum of P(Prosoma <appearance>)"] = sum_prosoma_app
        elif prosoma_app == "with pits (dorsally)":
            like_inconsp_prosoma = 0.04
            like_margins_with_teeth = 0.08
            like_consp_hair = 0.08
            like_pits = 0.8
            sum_prosoma_app = like_inconsp_prosoma + like_margins_with_teeth + like_consp_hair + like_pits
            dict["Prosoma <appearance>"] = prosoma_app
            dict["P(X | Prosoma <appearance>_inconspicuous)"] = like_inconsp_prosoma
            dict["P(X | Prosoma <appearance>_margins with teeth)"] = like_margins_with_teeth
            dict["P(X | Prosoma <appearance>_with conspicuous hairs/spines)"] = like_consp_hair
            dict["P(X | Prosoma <appearance>_with pits (dorsally))"] = like_pits
            dict["Sum of P(Prosoma <appearance>)"] = sum_prosoma_app
        else:
            sum_prosoma_app = like_inconsp_prosoma + like_margins_with_teeth + like_consp_hair + like_pits
            dict["Prosoma <appearance>"] = prosoma_app
            dict["P(X | Prosoma <appearance>_inconspicuous)"] = like_inconsp_prosoma
            dict["P(X | Prosoma <appearance>_margins with teeth)"] = like_margins_with_teeth
            dict["P(X | Prosoma <appearance>_with conspicuous hairs/spines)"] = like_consp_hair
            dict["P(X | Prosoma <appearance>_with pits (dorsally))"] = like_pits
            dict["Sum of P(Prosoma <appearance>)"] = sum_prosoma_app

        if fovea_as_groove == "yes":
            like_fovea_yes = 0.8
            like_fovea_no = 0.2
            sum_fovea_groove = like_fovea_yes + like_fovea_no 
            dict["Fovea as darkened groove"] = fovea_as_groove
            dict["P(X | Fovea as darkened groove_yes)"] = like_fovea_yes
            dict["P(X | Fovea as darkened groove_no)"] = like_fovea_no
            dict["Sum P(Fovea Groove)"] = sum_fovea_groove
        elif fovea_as_groove == "no":
            like_fovea_yes = 0.2
            like_fovea_no = 0.8
            sum_fovea_groove = like_fovea_yes + like_fovea_no 
            dict["Fovea as darkened groove"] = fovea_as_groove
            dict["P(X | Fovea as darkened groove_yes)"] = like_fovea_yes
            dict["P(X | Fovea as darkened groove_no)"] = like_fovea_no
            dict["Sum P(Fovea Groove)"] = sum_fovea_groove
        else:
            sum_fovea_groove = like_fovea_yes + like_fovea_no
            dict["Fovea as darkened groove"] = fovea_as_groove
            dict["P(X | Fovea as darkened groove_yes)"] = like_fovea_yes
            dict["P(X | Fovea as darkened groove_no)"] = like_fovea_no
            dict["Sum P(Fovea Groove)"] = sum_fovea_groove

        if opisthosoma_app == "conspicuously hairy":
            like_consp_hairy_opisthosoma = 0.9
            like_patterned_opisthosoma = 0.09
            like_unicolour_opisthosoma = 0.005
            like_scutum_opisthosoma = 0.005
            sum_opisthosoma_app = like_consp_hairy_opisthosoma + like_patterned_opisthosoma + like_unicolour_opisthosoma + like_scutum_opisthosoma
            dict["Opisthosoma <appearance>"] = opisthosoma_app
            dict["P(X | Opisthosoma <appearance>_conspicuously hairy)"] = like_consp_hairy_opisthosoma
            dict["P(X | Opisthosoma <appearance>_patterned)"] = like_patterned_opisthosoma
            dict["P(X | Opisthosoma <appearance>_unicolourous, inconspicuous)"] = like_unicolour_opisthosoma
            dict["P(X | Opisthosoma <appearance>_with scutum)"] = like_scutum_opisthosoma
            dict["Sum of P(Opisthosoma <appearance>)"] = sum_opisthosoma_app
            # samplelist.append(dict)
        elif opisthosoma_app == "patterned":
            like_consp_hairy_opisthosoma = 0.09
            like_patterned_opisthosoma = 0.9
            like_unicolour_opisthosoma = 0.005
            like_scutum_opisthosoma = 0.005
            sum_opisthosoma_app = like_consp_hairy_opisthosoma + like_patterned_opisthosoma + like_unicolour_opisthosoma + like_scutum_opisthosoma
            dict["Opisthosoma <appearance>"] = opisthosoma_app
            dict["P(X | Opisthosoma <appearance>_conspicuously hairy)"] = like_consp_hairy_opisthosoma
            dict["P(X | Opisthosoma <appearance>_patterned)"] = like_patterned_opisthosoma
            dict["P(X | Opisthosoma <appearance>_unicolourous, inconspicuous)"] = like_unicolour_opisthosoma
            dict["P(X | Opisthosoma <appearance>_with scutum)"] = like_scutum_opisthosoma
            dict["Sum of P(Opisthosoma <appearance>)"] = sum_opisthosoma_app
        elif opisthosoma_app == "unicolourous, inconspicuous":
            like_consp_hairy_opisthosoma = 0.033
            like_patterned_opisthosoma = 0.033
            like_unicolour_opisthosoma = 0.9
            like_scutum_opisthosoma = 0.033
            sum_opisthosoma_app = like_consp_hairy_opisthosoma + like_patterned_opisthosoma + like_unicolour_opisthosoma + like_scutum_opisthosoma
            dict["Opisthosoma <appearance>"] = opisthosoma_app
            dict["P(X | Opisthosoma <appearance>_conspicuously hairy)"] = like_consp_hairy_opisthosoma
            dict["P(X | Opisthosoma <appearance>_patterned)"] = like_patterned_opisthosoma
            dict["P(X | Opisthosoma <appearance>_unicolourous, inconspicuous)"] = like_unicolour_opisthosoma
            dict["P(X | Opisthosoma <appearance>_with scutum)"] = like_scutum_opisthosoma
            dict["Sum of P(Opisthosoma <appearance>)"] = sum_opisthosoma_app
        elif opisthosoma_app == "with scutum":
            like_consp_hairy_opisthosoma = 0.045
            like_patterned_opisthosoma = 0.045
            like_unicolour_opisthosoma = 0.01
            like_scutum_opisthosoma = 0.9
            sum_opisthosoma_app = like_consp_hairy_opisthosoma + like_patterned_opisthosoma + like_unicolour_opisthosoma + like_scutum_opisthosoma
            dict["Opisthosoma <appearance>"] = opisthosoma_app
            dict["P(X | Opisthosoma <appearance>_conspicuously hairy)"] = like_consp_hairy_opisthosoma
            dict["P(X | Opisthosoma <appearance>_patterned)"] = like_patterned_opisthosoma
            dict["P(X | Opisthosoma <appearance>_unicolourous, inconspicuous)"] = like_unicolour_opisthosoma
            dict["P(X | Opisthosoma <appearance>_with scutum)"] = like_scutum_opisthosoma
            dict["Sum of P(Opisthosoma <appearance>)"] = sum_opisthosoma_app
        else:
            sum_opisthosoma_app = like_consp_hairy_opisthosoma + like_patterned_opisthosoma + like_unicolour_opisthosoma + like_scutum_opisthosoma
            dict["Opisthosoma <appearance>"] = opisthosoma_app
            dict["P(X | Opisthosoma <appearance>_conspicuously hairy)"] = like_consp_hairy_opisthosoma
            dict["P(X | Opisthosoma <appearance>_patterned)"] = like_patterned_opisthosoma
            dict["P(X | Opisthosoma <appearance>_unicolourous, inconspicuous)"] = like_unicolour_opisthosoma
            dict["P(X | Opisthosoma <appearance>_with scutum)"] = like_scutum_opisthosoma
            dict["Sum of P(Opisthosoma <appearance>)"] = sum_opisthosoma_app

        if dorsal_spine_femur_count == "multiple":
            like_multiple_dorsal_spine_femur = 0.7
            like_none_dorsal_spine_femur = 0.09
            like_one_dorsal_spine_femur = 0.21
            sum_dorsal_spine_femur_count = like_multiple_dorsal_spine_femur + like_none_dorsal_spine_femur + like_one_dorsal_spine_femur
            dict["Dorsal spines on femur I: <count>"] = dorsal_spine_femur_count
            dict["P(X | Dorsal spines on femur I: <count>_multiple)"] = like_multiple_dorsal_spine_femur
            dict["P(X | Dorsal spines on femur I: <count>_none)"] = like_none_dorsal_spine_femur
            dict["P(X | Dorsal spines on femur I: <count>_one)"] = like_one_dorsal_spine_femur
            dict["Sum P(Dorsal spines on femur I: <count>)"] = sum_dorsal_spine_femur_count
        elif dorsal_spine_femur_count == "none":
            like_multiple_dorsal_spine_femur = 0.09
            like_none_dorsal_spine_femur = 0.7
            like_one_dorsal_spine_femur = 0.21
            sum_dorsal_spine_femur_count = like_multiple_dorsal_spine_femur + like_none_dorsal_spine_femur + like_one_dorsal_spine_femur
            dict["Dorsal spines on femur I: <count>"] = dorsal_spine_femur_count
            dict["P(X | Dorsal spines on femur I: <count>_multiple)"] = like_multiple_dorsal_spine_femur
            dict["P(X | Dorsal spines on femur I: <count>_none)"] = like_none_dorsal_spine_femur
            dict["P(X | Dorsal spines on femur I: <count>_one)"] = like_one_dorsal_spine_femur
            dict["Sum P(Dorsal spines on femur I: <count>)"] = sum_dorsal_spine_femur_count
        elif dorsal_spine_femur_count == "one":
            like_multiple_dorsal_spine_femur = 0.09
            like_none_dorsal_spine_femur = 0.21
            like_one_dorsal_spine_femur = 0.7
            sum_dorsal_spine_femur_count = like_multiple_dorsal_spine_femur + like_none_dorsal_spine_femur + like_one_dorsal_spine_femur
            dict["Dorsal spines on femur I: <count>"] = dorsal_spine_femur_count
            dict["P(X | Dorsal spines on femur I: <count>_multiple)"] = like_multiple_dorsal_spine_femur
            dict["P(X | Dorsal spines on femur I: <count>_none)"] = like_none_dorsal_spine_femur
            dict["P(X | Dorsal spines on femur I: <count>_one)"] = like_one_dorsal_spine_femur
            dict["Sum P(Dorsal spines on femur I: <count>)"] = sum_dorsal_spine_femur_count
        else:
            sum_dorsal_spine_femur_count = like_multiple_dorsal_spine_femur + like_none_dorsal_spine_femur + like_one_dorsal_spine_femur
            dict["Dorsal spines on femur I: <count>"] = dorsal_spine_femur_count
            dict["P(X | Dorsal spines on femur I: <count>_multiple)"] = like_multiple_dorsal_spine_femur
            dict["P(X | Dorsal spines on femur I: <count>_none)"] = like_none_dorsal_spine_femur
            dict["P(X | Dorsal spines on femur I: <count>_one)"] = like_one_dorsal_spine_femur
            dict["Sum P(Dorsal spines on femur I: <count>)"] = sum_dorsal_spine_femur_count

        if posterior_eye_form == "procurved":
            like_procurved_eye = 0.8
            like_recurved_eye = 0.04
            like_straight_eye = 0.16
            sum_posterior_eye_form = like_procurved_eye + like_recurved_eye + like_straight_eye
            dict["Posterior eye row: <form>"] = posterior_eye_form
            dict["P(X | Posterior eye row: <form>_procurved)"] = like_procurved_eye
            dict["P(X | Posterior eye row: <form>_recurved)"] = like_recurved_eye
            dict["P(X | Posterior eye row: <form>_straight)"] = like_straight_eye
            dict["Sum P(Posterior eye row: <form>_)"] = sum_posterior_eye_form
        elif posterior_eye_form == "recurved":
            like_procurved_eye = 0.04
            like_recurved_eye = 0.8
            like_straight_eye = 0.16
            sum_posterior_eye_form = like_procurved_eye + like_recurved_eye + like_straight_eye
            dict["Posterior eye row: <form>"] = posterior_eye_form
            dict["P(X | Posterior eye row: <form>_procurved)"] = like_procurved_eye
            dict["P(X | Posterior eye row: <form>_recurved)"] = like_recurved_eye
            dict["P(X | Posterior eye row: <form>_straight)"] = like_straight_eye
            dict["Sum P(Posterior eye row: <form>_)"] = sum_posterior_eye_form
        elif posterior_eye_form == "straight":
            like_procurved_eye = 0.1
            like_recurved_eye = 0.1
            like_straight_eye = 0.8
            sum_posterior_eye_form = like_procurved_eye + like_recurved_eye + like_straight_eye
            dict["Posterior eye row: <form>"] = posterior_eye_form
            dict["P(X | Posterior eye row: <form>_procurved)"] = like_procurved_eye
            dict["P(X | Posterior eye row: <form>_recurved)"] = like_recurved_eye
            dict["P(X | Posterior eye row: <form>_straight)"] = like_straight_eye
            dict["Sum P(Posterior eye row: <form>_)"] = sum_posterior_eye_form
        else:
            sum_posterior_eye_form = like_procurved_eye + like_recurved_eye + like_straight_eye
            dict["Posterior eye row: <form>"] = posterior_eye_form
            dict["P(X | Posterior eye row: <form>_procurved)"] = like_procurved_eye
            dict["P(X | Posterior eye row: <form>_recurved)"] = like_recurved_eye
            dict["P(X | Posterior eye row: <form>_straight)"] = like_straight_eye
            dict["Sum P(Posterior eye row: <form>_)"] = sum_posterior_eye_form

        if pme_separation_rel_to_d == "distinctly greater than d":
            like_greater_than_d_pme_ = 0.6
            like_less_than_d_pme = 0.16
            like_equal_to_d_pme = 0.24
            sum_pme_separation_rel_to_d = like_greater_than_d_pme + like_less_than_d_pme + like_equal_to_d_pme
            dict["Posterior median eye (PME) separation: <relative to diameter (d)>"] = pme_separation_rel_to_d
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly greater than d)"] = like_greater_than_d_pme
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly less than d)"] = like_less_than_d_pme
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_equal to d)"] = like_equal_to_d_pme
            dict["Sum P(Posterior median eye (PME) separation: <relative to diameter (d)>)"] =sum_pme_separation_rel_to_d
        elif pme_separation_rel_to_d == "distinctly less than d":
            like_greater_than_d_pme_ = 0.16
            like_less_than_d_pme = 0.6
            like_equal_to_d_pme = 0.24
            sum_pme_separation_rel_to_d = like_greater_than_d_pme + like_less_than_d_pme + like_equal_to_d_pme
            dict["Posterior median eye (PME) separation: <relative to diameter (d)>"] = pme_separation_rel_to_d
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly greater than d)"] = like_greater_than_d_pme
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly less than d)"] = like_less_than_d_pme
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_equal to d)"] = like_equal_to_d_pme
            dict["Sum P(Posterior median eye (PME) separation: <relative to diameter (d)>)"] =sum_pme_separation_rel_to_d
        elif pme_separation_rel_to_d == "equal to d":
            like_greater_than_d_pme_ = 0.2
            like_less_than_d_pme = 0.2
            like_equal_to_d_pme = 0.6
            sum_pme_separation_rel_to_d = like_greater_than_d_pme + like_less_than_d_pme + like_equal_to_d_pme
            dict["Posterior median eye (PME) separation: <relative to diameter (d)>"] = pme_separation_rel_to_d
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly greater than d)"] = like_greater_than_d_pme
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly less than d)"] = like_less_than_d_pme
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_equal to d)"] = like_equal_to_d_pme
            dict["Sum P(Posterior median eye (PME) separation: <relative to diameter (d)>)"] =sum_pme_separation_rel_to_d
        else:
            sum_pme_separation_rel_to_d = like_greater_than_d_pme + like_less_than_d_pme + like_equal_to_d_pme
            dict["Posterior median eye (PME) separation: <relative to diameter (d)>"] = pme_separation_rel_to_d
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly greater than d)"] = like_greater_than_d_pme
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly less than d)"] = like_less_than_d_pme
            dict["P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_equal to d)"] = like_equal_to_d_pme
            dict["Sum P(Posterior median eye (PME) separation: <relative to diameter (d)>)"] =sum_pme_separation_rel_to_d

        if headregion_m_app == "complex":
            like_complex_headregion = 0.7
            like_inconsp_headregion = 0.027
            like_sulci_headregion =0.105
            like_horn_headregion =0.063
            like_lobe_headregion =0.105
            sum_headregion_m_app = like_complex_headregion + like_inconsp_headregion + like_sulci_headregion + like_horn_headregion + like_lobe_headregion
            dict["Headregion of male: <appearance>"] = headregion_m_app
            dict["P(X | Headregion of male: <appearance>_complex)"] = like_complex_headregion
            dict["P(X | Headregion of male: <appearance>_inconspicuous)"] = like_inconsp_headregion
            dict["P(X | Headregion of male: <appearance>_sulci present)"] = like_sulci_headregion
            dict["P(X | Headregion of male: <appearance>_with horns/tufts)"] = like_horn_headregion
            dict["P(X | Headregion of male: <appearance>_with lobe (simple))"] = like_lobe_headregion
            dict["Sum P(Headregion of male: <appearance>)"] = sum_headregion_m_app
        elif headregion_m_app == "inconspicuous":
            like_complex_headregion = 0.075
            like_inconsp_headregion = 0.7
            like_sulci_headregion =0.075
            like_horn_headregion =0.075
            like_lobe_headregion =0.075
            sum_headregion_m_app = like_complex_headregion + like_inconsp_headregion + like_sulci_headregion + like_horn_headregion + like_lobe_headregion
            dict["Headregion of male: <appearance>"] = headregion_m_app
            dict["P(X | Headregion of male: <appearance>_complex)"] = like_complex_headregion
            dict["P(X | Headregion of male: <appearance>_inconspicuous)"] = like_inconsp_headregion
            dict["P(X | Headregion of male: <appearance>_sulci present)"] = like_sulci_headregion
            dict["P(X | Headregion of male: <appearance>_with horns/tufts)"] = like_horn_headregion
            dict["P(X | Headregion of male: <appearance>_with lobe (simple))"] = like_lobe_headregion
            dict["Sum P(Headregion of male: <appearance>)"] = sum_headregion_m_app
        elif headregion_m_app == "sulci present":
            like_complex_headregion = 0.21
            like_inconsp_headregion = 0.0135
            like_sulci_headregion = 0.7
            like_horn_headregion = 0.0135
            like_lobe_headregion = 0.063
            sum_headregion_m_app = like_complex_headregion + like_inconsp_headregion + like_sulci_headregion + like_horn_headregion + like_lobe_headregion
            dict["Headregion of male: <appearance>"] = headregion_m_app
            dict["P(X | Headregion of male: <appearance>_complex)"] = like_complex_headregion
            dict["P(X | Headregion of male: <appearance>_inconspicuous)"] = like_inconsp_headregion
            dict["P(X | Headregion of male: <appearance>_sulci present)"] = like_sulci_headregion
            dict["P(X | Headregion of male: <appearance>_with horns/tufts)"] = like_horn_headregion
            dict["P(X | Headregion of male: <appearance>_with lobe (simple))"] = like_lobe_headregion
            dict["Sum P(Headregion of male: <appearance>)"] = sum_headregion_m_app
        elif headregion_m_app == "with horns/tufts":
            like_complex_headregion = 0.21
            like_inconsp_headregion = 0.03
            like_sulci_headregion = 0.03
            like_horn_headregion = 0.7
            like_lobe_headregion = 0.03
            sum_headregion_m_app = like_complex_headregion + like_inconsp_headregion + like_sulci_headregion + like_horn_headregion + like_lobe_headregion
            dict["Headregion of male: <appearance>"] = headregion_m_app
            dict["P(X | Headregion of male: <appearance>_complex)"] = like_complex_headregion
            dict["P(X | Headregion of male: <appearance>_inconspicuous)"] = like_inconsp_headregion
            dict["P(X | Headregion of male: <appearance>_sulci present)"] = like_sulci_headregion
            dict["P(X | Headregion of male: <appearance>_with horns/tufts)"] = like_horn_headregion
            dict["P(X | Headregion of male: <appearance>_with lobe (simple))"] = like_lobe_headregion
            dict["Sum P(Headregion of male: <appearance>)"] = sum_headregion_m_app
        elif headregion_m_app == "with lobe(simple)":
            like_complex_headregion = 0.105
            like_inconsp_headregion = 0.063
            like_sulci_headregion = 0.105
            like_horn_headregion = 0.027
            like_lobe_headregion = 0.7
            sum_headregion_m_app = like_complex_headregion + like_inconsp_headregion + like_sulci_headregion + like_horn_headregion + like_lobe_headregion
            dict["Headregion of male: <appearance>"] = headregion_m_app
            dict["P(X | Headregion of male: <appearance>_complex)"] = like_complex_headregion
            dict["P(X | Headregion of male: <appearance>_inconspicuous)"] = like_inconsp_headregion
            dict["P(X | Headregion of male: <appearance>_sulci present)"] = like_sulci_headregion
            dict["P(X | Headregion of male: <appearance>_with horns/tufts)"] = like_horn_headregion
            dict["P(X | Headregion of male: <appearance>_with lobe (simple))"] = like_lobe_headregion
            dict["Sum P(Headregion of male: <appearance>)"] = sum_headregion_m_app
        else:
            sum_headregion_m_app = like_complex_headregion + like_inconsp_headregion + like_sulci_headregion + like_horn_headregion + like_lobe_headregion
            dict["Headregion of male: <appearance>"] = headregion_m_app
            dict["P(X | Headregion of male: <appearance>_complex)"] = like_complex_headregion
            dict["P(X | Headregion of male: <appearance>_inconspicuous)"] = like_inconsp_headregion
            dict["P(X | Headregion of male: <appearance>_sulci present)"] = like_sulci_headregion
            dict["P(X | Headregion of male: <appearance>_with horns/tufts)"] = like_horn_headregion
            dict["P(X | Headregion of male: <appearance>_with lobe (simple))"] = like_lobe_headregion
            dict["Sum P(Headregion of male: <appearance>)"] = sum_headregion_m_app

        if eyes_app == "normal":
            like_eyes_normal = 0.8
            like_eyes_reduced = 0.2
            sum_eyes_app = like_eyes_normal + like_eyes_reduced 
            dict["Eyes: <appearance>"] = eyes_app
            dict["P(X | Eyes: <appearance>_normal)"] = like_eyes_normal
            dict["P(X | Eyes: <appearance>_reduced)"] = like_eyes_reduced
            dict["Sum P(Eyes: <appearance>)"] = sum_eyes_app
        elif eyes_app == "reduced":
            like_eyes_normal = 0.8
            like_eyes_reduced = 0.2
            sum_eyes_app = like_eyes_normal + like_eyes_reduced 
            dict["Eyes: <appearance>"] = eyes_app
            dict["P(X | Eyes: <appearance>_normal)"] = like_eyes_normal
            dict["P(X | Eyes: <appearance>_reduced)"] = like_eyes_reduced
            dict["Sum P(Eyes: <appearance>)"] = sum_eyes_app
        else:
            sum_eyes_app = like_eyes_normal + like_eyes_reduced 
            dict["Eyes: <appearance>"] = eyes_app
            dict["P(X | Eyes: <appearance>_normal)"] = like_eyes_normal
            dict["P(X | Eyes: <appearance>_reduced)"] = like_eyes_reduced
            dict["Sum P(Eyes: <appearance>)"] = sum_eyes_app

        if ame_rel_to_lateral == "about the same as ALE":
            like_about_the_same_ale = 0.8
            like_greater_than_ale_ = 0.1
            like_less_than_ale = 0.1
            sum_ame_rel_to_lateral = like_about_the_same_ale + like_greater_than_ale_ + like_less_than_ale
            dict["Anterior median eyes: <size relative to anterior lateral eyes ALE>"] = ame_rel_to_lateral
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_about the same as ALE)"] = like_about_the_same_ale
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly larger than ALE)"] = like_greater_than_ale_
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly smaller than ALE)"] = like_less_than_ale
            dict["Sum(Anterior median eyes: <size relative to anterior lateral eyes ALE>)"] =sum_ame_rel_to_lateral
        elif ame_rel_to_lateral == "distinctly larger than ALE":
            like_about_the_same_ale = 0.16
            like_greater_than_ale_ = 0.8
            like_less_than_ale = 0.04
            sum_ame_rel_to_lateral = like_about_the_same_ale + like_greater_than_ale_ + like_less_than_ale
            dict["Anterior median eyes: <size relative to anterior lateral eyes ALE>"] = ame_rel_to_lateral
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_about the same as ALE)"] = like_about_the_same_ale
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly larger than ALE)"] = like_greater_than_ale_
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly smaller than ALE)"] = like_less_than_ale
            dict["Sum(Anterior median eyes: <size relative to anterior lateral eyes ALE>)"] =sum_ame_rel_to_lateral
        elif ame_rel_to_lateral == "distinctly smaller than ALE":
            like_about_the_same_ale = 0.16
            like_greater_than_ale_ = 0.04
            like_less_than_ale = 0.8
            sum_ame_rel_to_lateral = like_about_the_same_ale + like_greater_than_ale_ + like_less_than_ale
            dict["Anterior median eyes: <size relative to anterior lateral eyes ALE>"] = ame_rel_to_lateral
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_about the same as ALE)"] = like_about_the_same_ale
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly larger than ALE)"] = like_greater_than_ale_
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly smaller than ALE)"] = like_less_than_ale
            dict["Sum(Anterior median eyes: <size relative to anterior lateral eyes ALE>)"] =sum_ame_rel_to_lateral
        else:
            sum_ame_rel_to_lateral = like_about_the_same_ale + like_greater_than_ale_ + like_less_than_ale
            dict["Anterior median eyes: <size relative to anterior lateral eyes ALE>"] = ame_rel_to_lateral
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_about the same as ALE)"] = like_about_the_same_ale
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly larger than ALE)"] = like_greater_than_ale_
            dict["P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly smaller than ALE)"] = like_less_than_ale
            dict["Sum(Anterior median eyes: <size relative to anterior lateral eyes ALE>)"] =sum_ame_rel_to_lateral

        if pro_spines_femur_count == "multiple":
            like_multiple_prolateral_spine_femur = 0.7
            like_none_prolateral_spine_femur = 0.09
            like_one_prolateral_spine_femur = 0.21
            sum_pro_spines_femur_count = like_multiple_prolateral_spine_femur + like_none_prolateral_spine_femur + like_one_prolateral_spine_femur
            dict["Prolateral spines on femur I: <count>"] = pro_spines_femur_count
            dict["P(X | Prolateral spines on femur I: <count>_multiple)"] = like_multiple_prolateral_spine_femur
            dict["P(X | Prolateral spines on femur I: <count>_none)"] = like_none_prolateral_spine_femur
            dict["P(X | Prolateral spines on femur I: <count>_one)"] = like_one_prolateral_spine_femur
            dict["Sum P(Prolateral spines on femur I: <count>)"] = sum_pro_spines_femur_count
        if pro_spines_femur_count == "none":
            like_multiple_prolateral_spine_femur = 0.09
            like_none_prolateral_spine_femur = 0.7
            like_one_prolateral_spine_femur = 0.21
            sum_pro_spines_femur_count = like_multiple_prolateral_spine_femur + like_none_prolateral_spine_femur + like_one_prolateral_spine_femur
            dict["Prolateral spines on femur I: <count>"] = pro_spines_femur_count
            dict["P(X | Prolateral spines on femur I: <count>_multiple)"] = like_multiple_prolateral_spine_femur
            dict["P(X | Prolateral spines on femur I: <count>_none)"] = like_none_prolateral_spine_femur
            dict["P(X | Prolateral spines on femur I: <count>_one)"] = like_one_prolateral_spine_femur
            dict["Sum P(Prolateral spines on femur I: <count>)"] = sum_pro_spines_femur_count
        if pro_spines_femur_count == "one":
            like_multiple_prolateral_spine_femur = 0.09
            like_none_prolateral_spine_femur = 0.21
            like_one_prolateral_spine_femur = 0.7
            sum_pro_spines_femur_count = like_multiple_prolateral_spine_femur + like_none_prolateral_spine_femur + like_one_prolateral_spine_femur
            dict["Prolateral spines on femur I: <count>"] = pro_spines_femur_count
            dict["P(X | Prolateral spines on femur I: <count>_multiple)"] = like_multiple_prolateral_spine_femur
            dict["P(X | Prolateral spines on femur I: <count>_none)"] = like_none_prolateral_spine_femur
            dict["P(X | Prolateral spines on femur I: <count>_one)"] = like_one_prolateral_spine_femur
            dict["Sum P(Prolateral spines on femur I: <count>)"] = sum_pro_spines_femur_count
        else:
            sum_pro_spines_femur_count = like_multiple_prolateral_spine_femur + like_none_prolateral_spine_femur + like_one_prolateral_spine_femur
            dict["Prolateral spines on femur I: <count>"] = pro_spines_femur_count
            dict["P(X | Prolateral spines on femur I: <count>_multiple)"] = like_multiple_prolateral_spine_femur
            dict["P(X | Prolateral spines on femur I: <count>_none)"] = like_none_prolateral_spine_femur
            dict["P(X | Prolateral spines on femur I: <count>_one)"] = like_one_prolateral_spine_femur
            dict["Sum P(Prolateral spines on femur I: <count>)"] = sum_pro_spines_femur_count

        if pro_spines_tibia_count == "multiple":
            like_multiple_prolateral_spine_tibia = 0.7
            like_none_prolateral_spine_tibia = 0.09
            like_one_prolateral_spine_tibia = 0.21
            sum_pro_spines_tibia_count = like_multiple_prolateral_spine_tibia + like_none_prolateral_spine_tibia + like_one_prolateral_spine_tibia
            dict["Prolateral spines on tibia I: <count>"] = pro_spines_tibia_count
            dict["P(X | Prolateral spines on tibia I: <count>_multiple)"] = like_multiple_prolateral_spine_tibia
            dict["P(X | Prolateral spines on tibia I: <count>_none)"] = like_none_prolateral_spine_tibia
            dict["P(X | Prolateral spines on tibia I: <count>_one)"] = like_one_prolateral_spine_tibia
            dict["Sum P(Prolateral spines on tibia I: <count>)"] = sum_pro_spines_tibia_count
        if pro_spines_tibia_count == "none":
            like_multiple_prolateral_spine_tibia = 0.09
            like_none_prolateral_spine_tibia = 0.7
            like_one_prolateral_spine_tibia = 0.21
            sum_pro_spines_tibia_count = like_multiple_prolateral_spine_tibia + like_none_prolateral_spine_tibia + like_one_prolateral_spine_tibia
            dict["Prolateral spines on tibia I: <count>"] = pro_spines_tibia_count
            dict["P(X | Prolateral spines on tibia I: <count>_multiple)"] = like_multiple_prolateral_spine_tibia
            dict["P(X | Prolateral spines on tibia I: <count>_none)"] = like_none_prolateral_spine_tibia
            dict["P(X | Prolateral spines on tibia I: <count>_one)"] = like_one_prolateral_spine_tibia
            dict["Sum P(Prolateral spines on tibia I: <count>)"] = sum_pro_spines_tibia_count
        if pro_spines_tibia_count == "one":
            like_multiple_prolateral_spine_tibia = 0.09
            like_none_prolateral_spine_tibia = 0.21
            like_one_prolateral_spine_tibia = 0.7
            sum_pro_spines_tibia_count = like_multiple_prolateral_spine_tibia + like_none_prolateral_spine_tibia + like_one_prolateral_spine_tibia
            dict["Prolateral spines on tibia I: <count>"] = pro_spines_tibia_count
            dict["P(X | Prolateral spines on tibia I: <count>_multiple)"] = like_multiple_prolateral_spine_tibia
            dict["P(X | Prolateral spines on tibia I: <count>_none)"] = like_none_prolateral_spine_tibia
            dict["P(X | Prolateral spines on tibia I: <count>_one)"] = like_one_prolateral_spine_tibia
            dict["Sum P(Prolateral spines on tibia I: <count>)"] = sum_pro_spines_tibia_count
        else:
            sum_pro_spines_tibia_count = like_multiple_prolateral_spine_tibia + like_none_prolateral_spine_tibia + like_one_prolateral_spine_tibia
            dict["Prolateral spines on tibia I: <count>"] = pro_spines_tibia_count
            dict["P(X | Prolateral spines on tibia I: <count>_multiple)"] = like_multiple_prolateral_spine_tibia
            dict["P(X | Prolateral spines on tibia I: <count>_none)"] = like_none_prolateral_spine_tibia
            dict["P(X | Prolateral spines on tibia I: <count>_one)"] = like_one_prolateral_spine_tibia
            dict["Sum P(Prolateral spines on tibia I: <count>)"] = sum_pro_spines_tibia_count

        if ant_teeth_app == "conspicuously large":
            like_conspicuously_large_teeth = 0.8
            like_unremarkable_teeth = 0.2
            sum_ant_teeth_app = like_conspicuously_large_teeth + like_unremarkable_teeth
            dict["Anterior cheliceral teeth: <appearance>"] = ant_teeth_app
            dict["P(X | Anterior cheliceral teeth: <appearance>_conspicuously large)"] = like_conspicuously_large_teeth
            dict["P(X | Anterior cheliceral teeth: <appearance>_unremarkable in size)"] = like_unremarkable_teeth
            dict["Sum P(Anterior cheliceral teeth: <appearance>)"] = sum_ant_teeth_app
        elif ant_teeth_app == "unremarkable in size":
            like_conspicuously_large_teeth = 0.2
            like_unremarkable_teeth = 0.8
            sum_ant_teeth_app = like_conspicuously_large_teeth + like_unremarkable_teeth
            dict["Anterior cheliceral teeth: <appearance>"] = ant_teeth_app
            dict["P(X | Anterior cheliceral teeth: <appearance>_conspicuously large)"] = like_conspicuously_large_teeth
            dict["P(X | Anterior cheliceral teeth: <appearance>_unremarkable in size)"] = like_unremarkable_teeth
            dict["Sum P(Anterior cheliceral teeth: <appearance>)"] = sum_ant_teeth_app
        else:
            sum_ant_teeth_app = like_conspicuously_large_teeth + like_unremarkable_teeth
            dict["Anterior cheliceral teeth: <appearance>"] = ant_teeth_app
            dict["P(X | Anterior cheliceral teeth: <appearance>_conspicuously large)"] = like_conspicuously_large_teeth
            dict["P(X | Anterior cheliceral teeth: <appearance>_unremarkable in size)"] = like_unremarkable_teeth
            dict["Sum P(Anterior cheliceral teeth: <appearance>)"] = sum_ant_teeth_app

        if consp_str_app == "apophyses/teeth-like processes/tubercles":
            like_apophyses_consp_str_app = 0.7
            like_none_consp_str_app = 0.09
            like_spines_consp_str_app = 0.21
            sum_consp_str_app = like_apophyses_consp_str_app + like_none_consp_str_app + like_spines_consp_str_app
            dict["Conspicuous structures on chelicerae: <appearance>"] = consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_apophyses/teeth-like processes/tubercles)"] = like_apophyses_consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_none)"] = like_none_consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_spines)"] = like_spines_consp_str_app
            dict["Sum P(Conspicuous structures on chelicerae: <appearance>)"] = sum_consp_str_app
        elif consp_str_app == "none":
            like_apophyses_consp_str_app = 0.15
            like_none_consp_str_app = 0.7
            like_spines_consp_str_app = 0.15
            sum_consp_str_app = like_apophyses_consp_str_app + like_none_consp_str_app + like_spines_consp_str_app
            dict["Conspicuous structures on chelicerae: <appearance>"] = consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_apophyses/teeth-like processes/tubercles)"] = like_apophyses_consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_none)"] = like_none_consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_spines)"] = like_spines_consp_str_app
            dict["Sum P(Conspicuous structures on chelicerae: <appearance>)"] = sum_consp_str_app
        elif consp_str_app == "spines":
            like_apophyses_consp_str_app = 0.21
            like_none_consp_str_app = 0.09
            like_spines_consp_str_app = 0.7
            sum_consp_str_app = like_apophyses_consp_str_app + like_none_consp_str_app + like_spines_consp_str_app
            dict["Conspicuous structures on chelicerae: <appearance>"] = consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_apophyses/teeth-like processes/tubercles)"] = like_apophyses_consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_none)"] = like_none_consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_spines)"] = like_spines_consp_str_app
            dict["Sum P(Conspicuous structures on chelicerae: <appearance>)"] = sum_consp_str_app
        else:         
            sum_consp_str_app = like_apophyses_consp_str_app + like_none_consp_str_app + like_spines_consp_str_app
            dict["Conspicuous structures on chelicerae: <appearance>"] = consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_apophyses/teeth-like processes/tubercles)"] = like_apophyses_consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_none)"] = like_none_consp_str_app
            dict["P(X | Conspicuous structures on chelicerae: <appearance>_spines)"] = like_spines_consp_str_app
            dict["Sum P(Conspicuous structures on chelicerae: <appearance>)"] = sum_consp_str_app

        if maxillae_app == "one or more teeth/tubercles":
            like_one_or_more_maxillae = 0.7
            like_unremarkable_maxillae = 0.3
            sum_maxillae_app = like_one_or_more_maxillae + like_unremarkable_maxillae
            dict["Maxillae: <appearance>"] = maxillae_app
            dict["P(X | Maxillae: <appearance>_one or more teeth/tubercles)"] = like_one_or_more_maxillae
            dict["P(X | Maxillae: <appearance>_unremarkable)"] = like_unremarkable_maxillae
            dict["Sum P(Maxillae: <appearance>)"] = sum_maxillae_app
        elif maxillae_app == "unremarkable":
            like_one_or_more_maxillae = 0.3
            like_unremarkable_maxillae = 0.7
            sum_maxillae_app = like_one_or_more_maxillae + like_unremarkable_maxillae
            dict["Maxillae: <appearance>"] = maxillae_app
            dict["P(X | Maxillae: <appearance>_one or more teeth/tubercles)"] = like_one_or_more_maxillae
            dict["P(X | Maxillae: <appearance>_unremarkable)"] = like_unremarkable_maxillae
            dict["Sum P(Maxillae: <appearance>)"] = sum_maxillae_app
        else:         
            sum_maxillae_app = like_one_or_more_maxillae + like_unremarkable_maxillae
            dict["Maxillae: <appearance>"] = maxillae_app
            dict["P(X | Maxillae: <appearance>_one or more teeth/tubercles)"] = like_one_or_more_maxillae
            dict["P(X | Maxillae: <appearance>_unremarkable)"] = like_unremarkable_maxillae
            dict["Sum P(Maxillae: <appearance>)"] = sum_maxillae_app

        if sternum_app == "pitted":
            like_pitted_sternum = 0.9
            like_rugose_sternum = 0.09
            like_smooth_sternum = 0.01
            sum_sternum_app = like_pitted_sternum + like_rugose_sternum + like_smooth_sternum
            dict["Sternum: <appearance>"] = sternum_app
            dict["P(X | Sternum: <appearance>_pitted)"] = like_pitted_sternum
            dict["P(X | Sternum: <appearance>_rugose)"] = like_rugose_sternum
            dict["P(X | Sternum: <appearance>_smooth)"] = like_smooth_sternum
            dict["Sum P(Sternum: <appearance>)"] = sum_sternum_app
        elif sternum_app == "rugose":
            like_pitted_sternum = 0.09
            like_rugose_sternum = 0.9
            like_smooth_sternum = 0.01
            sum_sternum_app = like_pitted_sternum + like_rugose_sternum + like_smooth_sternum
            dict["Sternum: <appearance>"] = sternum_app
            dict["P(X | Sternum: <appearance>_pitted)"] = like_pitted_sternum
            dict["P(X | Sternum: <appearance>_rugose)"] = like_rugose_sternum
            dict["P(X | Sternum: <appearance>_smooth)"] = like_smooth_sternum
            dict["Sum P(Sternum: <appearance>)"] = sum_sternum_app
        elif sternum_app == "smooth":
            like_pitted_sternum = 0.05
            like_rugose_sternum = 0.05
            like_smooth_sternum = 0.9
            sum_sternum_app = like_pitted_sternum + like_rugose_sternum + like_smooth_sternum
            dict["Sternum: <appearance>"] = sternum_app
            dict["P(X | Sternum: <appearance>_pitted)"] = like_pitted_sternum
            dict["P(X | Sternum: <appearance>_rugose)"] = like_rugose_sternum
            dict["P(X | Sternum: <appearance>_smooth)"] = like_smooth_sternum
            dict["Sum P(Sternum: <appearance>)"] = sum_sternum_app
        else:  
            sum_sternum_app = like_pitted_sternum + like_rugose_sternum + like_smooth_sternum
            dict["Sternum: <appearance>"] = sternum_app
            dict["P(X | Sternum: <appearance>_pitted)"] = like_pitted_sternum
            dict["P(X | Sternum: <appearance>_rugose)"] = like_rugose_sternum
            dict["P(X | Sternum: <appearance>_smooth)"] = like_smooth_sternum
            dict["Sum P(Sternum: <appearance>)"] = sum_sternum_app

        if sternum_coxae == "yes":
            like_sternum_yes = 0.8
            like_sternum_no = 0.2
            sum_sternum_coxae = like_sternum_yes + like_sternum_no
            dict["Sternum: <extends between coxae IV>"] = sternum_coxae
            dict["P(X | Sternum: <extends between coxae IV>_yes)"] = like_sternum_yes
            dict["P(X | Sternum: <extends between coxae IV>_no)"] = like_sternum_no
            dict["Sum P(Sternum: <extends between coxae IV>)"] = sum_sternum_coxae
        elif sternum_coxae == "no":
            like_sternum_yes = 0.2
            like_sternum_no = 0.8
            sum_sternum_coxae = like_sternum_yes + like_sternum_no
            dict["Sternum: <extends between coxae IV>"] = sternum_coxae
            dict["P(X | Sternum: <extends between coxae IV>_yes)"] = like_sternum_yes
            dict["P(X | Sternum: <extends between coxae IV>_no)"] = like_sternum_no
            dict["Sum P(Sternum: <extends between coxae IV>)"] = sum_sternum_coxae
        else:
            sum_sternum_coxae = like_sternum_yes + like_sternum_no
            dict["Sternum: <extends between coxae IV>"] = sternum_coxae
            dict["P(X | Sternum: <extends between coxae IV>_yes)"] = like_sternum_yes
            dict["P(X | Sternum: <extends between coxae IV>_no)"] = like_sternum_no
            dict["Sum P(Sternum: <extends between coxae IV>)"] = sum_sternum_coxae

        if sternum_width_coxae == "distinctly greater than d":
            like_distinctly_greater_sternum = 0.7
            like_distinctly_smaller_sternum = 0.09
            like_equal_sternum = 0.21
            sum_sternum_width_coxae = like_distinctly_greater_sternum + like_distinctly_smaller_sternum + like_equal_sternum
            dict["Width of sternum between coxae IV: <relative to width of coxae IV (d)>"] = sternum_width_coxae
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly greater than d)"] = like_distinctly_greater_sternum
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly less than d)"] = like_distinctly_smaller_sternum
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_equal to d)"] = like_equal_sternum
            dict["Sum P(Width of sternum between coxae IV: <relative to width of coxae IV (d)>)"] = sum_sternum_width_coxae
        elif sternum_width_coxae == "distinctly less than d":
            like_distinctly_greater_sternum = 0.09
            like_distinctly_smaller_sternum = 0.7
            like_equal_sternum = 0.21
            sum_sternum_width_coxae = like_distinctly_greater_sternum + like_distinctly_smaller_sternum + like_equal_sternum
            dict["Width of sternum between coxae IV: <relative to width of coxae IV (d)>"] = sternum_width_coxae
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly greater than d)"] = like_distinctly_greater_sternum
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly less than d)"] = like_distinctly_smaller_sternum
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_equal to d)"] = like_equal_sternum
            dict["Sum P(Width of sternum between coxae IV: <relative to width of coxae IV (d)>)"] = sum_sternum_width_coxae
        elif sternum_width_coxae == "equal to d":
            like_distinctly_greater_sternum = 0.15
            like_distinctly_smaller_sternum = 0.15
            like_equal_sternum = 0.7
            sum_sternum_width_coxae = like_distinctly_greater_sternum + like_distinctly_smaller_sternum + like_equal_sternum
            dict["Width of sternum between coxae IV: <relative to width of coxae IV (d)>"] = sternum_width_coxae
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly greater than d)"] = like_distinctly_greater_sternum
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly less than d)"] = like_distinctly_smaller_sternum
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_equal to d)"] = like_equal_sternum
            dict["Sum P(Width of sternum between coxae IV: <relative to width of coxae IV (d)>)"] = sum_sternum_width_coxae
        else:
            sum_sternum_width_coxae = like_distinctly_greater_sternum + like_distinctly_smaller_sternum + like_equal_sternum
            dict["Width of sternum between coxae IV: <relative to width of coxae IV (d)>"] = sternum_width_coxae
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly greater than d)"] = like_distinctly_greater_sternum
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly less than d)"] = like_distinctly_smaller_sternum
            dict["P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_equal to d)"] = like_equal_sternum
            dict["Sum P(Width of sternum between coxae IV: <relative to width of coxae IV (d)>)"] = sum_sternum_width_coxae

        if tmi_range == "0.10-0.19":
            like_10_to_19 = 0.9
            like_20_to_29 = 0.09
            like_30_to_39 = 0.0045
            like_40_to_49 = 0.0045
            like_50_to_59 = 0.0045
            like_60_to_69 = 0.00045
            like_70_to_79 = 0.00045
            like_80_to_89 = 0.000045
            like_90_to_98 = 0.000045
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range
        elif tmi_range == "0.20-0.29":
            like_10_to_19 = 0.045
            like_20_to_29 = 0.9
            like_30_to_39 = 0.045
            like_40_to_49 = 0.0045
            like_50_to_59 = 0.0045
            like_60_to_69 = 0.00045
            like_70_to_79 = 0.00045
            like_80_to_89 = 0.00005
            like_90_to_98 = 0.00005
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range
        elif tmi_range == "0.30-0.39":
            like_10_to_19 = 0.0045
            like_20_to_29 = 0.045
            like_30_to_39 = 0.9
            like_40_to_49 = 0.045
            like_50_to_59 = 0.0045
            like_60_to_69 = 0.00045
            like_70_to_79 = 0.00045
            like_80_to_89 = 0.00005
            like_90_to_98 = 0.00005
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range
        elif tmi_range == "0.40-0.49":
            like_10_to_19 = 0.00045
            like_20_to_29 = 0.0045
            like_30_to_39 = 0.045
            like_40_to_49 = 0.9
            like_50_to_59 = 0.045
            like_60_to_69 = 0.0045
            like_70_to_79 = 0.00045
            like_80_to_89 = 0.00005
            like_90_to_98 = 0.00005
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range"] = tmi_range
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range 
        elif tmi_range == "0.50-0.59":
            like_10_to_19 = 0.00005
            like_20_to_29 = 0.00045
            like_30_to_39 = 0.0045
            like_40_to_49 = 0.045
            like_50_to_59 = 0.9
            like_60_to_69 = 0.045
            like_70_to_79 = 0.0045
            like_80_to_89 = 0.00045
            like_90_to_98 = 0.00005
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range
        elif tmi_range == "0.60-0.69":
            like_10_to_19 = 0.00005
            like_20_to_29 = 0.00005
            like_30_to_39 = 0.00045
            like_40_to_49 = 0.0045
            like_50_to_59 = 0.045
            like_60_to_69 = 0.9
            like_70_to_79 = 0.045
            like_80_to_89 = 0.0045
            like_90_to_98 = 0.00045
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range
        elif tmi_range == "0.70-0.79":
            like_10_to_19 = 0.00005
            like_20_to_29 = 0.00005
            like_30_to_39 = 0.00045
            like_40_to_49 = 0.00045
            like_50_to_59 = 0.0045
            like_60_to_69 = 0.045
            like_70_to_79 = 0.9
            like_80_to_89 = 0.045
            like_90_to_98 = 0.0045
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range
        elif tmi_range == "0.80-0.89":
            like_10_to_19 = 0.00005
            like_20_to_29 = 0.00005
            like_30_to_39 = 0.00045
            like_40_to_49 = 0.00045
            like_50_to_59 = 0.0045
            like_60_to_69 = 0.0045
            like_70_to_79 = 0.045
            like_80_to_89 = 0.9
            like_90_to_98 = 0.045
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range
        elif tmi_range == "0.90-0.98":
            like_10_to_19 = 0.00005
            like_20_to_29 = 0.00005
            like_30_to_39 = 0.00045
            like_40_to_49 = 0.00045
            like_50_to_59 = 0.0045
            like_60_to_69 = 0.0045
            like_70_to_79 = 0.045
            like_80_to_89 = 0.045
            like_90_to_98 = 0.9
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range
        else: 
            sum_tmi_range = like_10_to_19 + like_20_to_29 + like_30_to_39 + like_40_to_49 + like_50_to_59 + like_60_to_69 + like_70_to_79 + like_80_to_89 + like_90_to_98
            dict["Position of TmI by range: <relative to metatarsus>"] = tmi_range
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.10-0.19)"] = like_10_to_19
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.20-0.29)"] = like_20_to_29
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.30-0.39)"] = like_30_to_39
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.40-0.49)"] = like_40_to_49
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.50-0.59)"] = like_50_to_59
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.60-0.69)"] = like_60_to_69
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.70-0.79)"] = like_70_to_79
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.80-0.89)"] = like_80_to_89
            dict["P(X | Position of TmI by range: <relative to metatarsus>_0.90-0.98)"] = like_90_to_98
            dict["Sum P(Position of TmI by range: <relative to metatarsus>)"] = sum_tmi_range

        if meta_dorsal_tmiv == "trichobothrium present":
            like_tricho_present_metatarsus = 0.8
            like_tricho_absent_metatarsus = 0.2
            sum_meta_dorsal_tmiv = like_tricho_present_metatarsus + like_tricho_absent_metatarsus
            dict["Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>"] = meta_dorsal_tmiv
            dict["P(X | Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>_trichobothrium present)"] = like_tricho_present_metatarsus
            dict["P(X | Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>_trichobothrium absent)"] = like_tricho_absent_metatarsus
            dict["Sum P(Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>)"] = sum_meta_dorsal_tmiv
        elif meta_dorsal_tmiv == "trichobothrium absent":
            like_tricho_present_metatarsus = 0.2
            like_tricho_absent_metatarsus = 0.8
            sum_meta_dorsal_tmiv = like_tricho_present_metatarsus + like_tricho_absent_metatarsus
            dict["Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>"] = meta_dorsal_tmiv
            dict["P(X | Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>_trichobothrium present)"] = like_tricho_present_metatarsus
            dict["P(X | Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>_trichobothrium absent)"] = like_tricho_absent_metatarsus
            dict["Sum P(Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>)"] = sum_meta_dorsal_tmiv
        else:  
            sum_meta_dorsal_tmiv = like_tricho_present_metatarsus + like_tricho_absent_metatarsus
            dict["Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>"] = meta_dorsal_tmiv
            dict["P(X | Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>_trichobothrium present)"] = like_tricho_present_metatarsus
            dict["P(X | Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>_trichobothrium absent)"] = like_tricho_absent_metatarsus
            dict["Sum P(Metatarsus IV dorsally: <presence of trichobothrium (TmIV)>)"] = sum_meta_dorsal_tmiv

        if dorsal_spine_meta_count == "multiple":
            like_multiple_dorsal_spine_metatarsus = 0.7
            like_none_dorsal_spine_metatarsus = 0.09
            like_one_dorsal_spine_metatarsus = 0.21
            sum_dorsal_spine_meta_count = like_multiple_dorsal_spine_metatarsus + like_none_dorsal_spine_metatarsus + like_one_dorsal_spine_metatarsus
            dict["Dorsal spines on metatarsus I: <count>"] = dorsal_spine_meta_count
            dict["P(X | Dorsal spines on metatarsus I: <count>_multiple)"] = like_multiple_dorsal_spine_metatarsus
            dict["P(X | Dorsal spines on metatarsus I: <count>_none)"] = like_none_dorsal_spine_metatarsus
            dict["P(X | Dorsal spines on metatarsus I: <count>_one)"] = like_one_dorsal_spine_metatarsus
            dict["Sum P(Dorsal spines on metatarsus I: <count>)"] = sum_dorsal_spine_meta_count
        elif dorsal_spine_meta_count == "none":
            like_multiple_dorsal_spine_metatarsus = 0.09
            like_none_dorsal_spine_metatarsus = 0.7
            like_one_dorsal_spine_metatarsus = 0.21
            sum_dorsal_spine_meta_count = like_multiple_dorsal_spine_metatarsus + like_none_dorsal_spine_metatarsus + like_one_dorsal_spine_metatarsus
            dict["Dorsal spines on metatarsus I: <count>"] = dorsal_spine_meta_count
            dict["P(X | Dorsal spines on metatarsus I: <count>_multiple)"] = like_multiple_dorsal_spine_metatarsus
            dict["P(X | Dorsal spines on metatarsus I: <count>_none)"] = like_none_dorsal_spine_metatarsus
            dict["P(X | Dorsal spines on metatarsus I: <count>_one)"] = like_one_dorsal_spine_metatarsus
            dict["Sum P(Dorsal spines on metatarsus I: <count>)"] = sum_dorsal_spine_meta_count
        elif dorsal_spine_meta_count == "one":
            like_multiple_dorsal_spine_metatarsus = 0.09
            like_none_dorsal_spine_metatarsus = 0.21
            like_one_dorsal_spine_metatarsus = 0.7
            sum_dorsal_spine_meta_count = like_multiple_dorsal_spine_metatarsus + like_none_dorsal_spine_metatarsus + like_one_dorsal_spine_metatarsus
            dict["Dorsal spines on metatarsus I: <count>"] = dorsal_spine_meta_count
            dict["P(X | Dorsal spines on metatarsus I: <count>_multiple)"] = like_multiple_dorsal_spine_metatarsus
            dict["P(X | Dorsal spines on metatarsus I: <count>_none)"] = like_none_dorsal_spine_metatarsus
            dict["P(X | Dorsal spines on metatarsus I: <count>_one)"] = like_one_dorsal_spine_metatarsus
            dict["Sum P(Dorsal spines on metatarsus I: <count>)"] = sum_dorsal_spine_meta_count
        else:  
            sum_dorsal_spine_meta_count = like_multiple_dorsal_spine_metatarsus + like_none_dorsal_spine_metatarsus + like_one_dorsal_spine_metatarsus
            dict["Dorsal spines on metatarsus I: <count>"] = dorsal_spine_meta_count
            dict["P(X | Dorsal spines on metatarsus I: <count>_multiple)"] = like_multiple_dorsal_spine_metatarsus
            dict["P(X | Dorsal spines on metatarsus I: <count>_none)"] = like_none_dorsal_spine_metatarsus
            dict["P(X | Dorsal spines on metatarsus I: <count>_one)"] = like_one_dorsal_spine_metatarsus
            dict["Sum P(Dorsal spines on metatarsus I: <count>)"] = sum_dorsal_spine_meta_count

        if tibia_no_of_spine == "one dorsal spine":
            like_one_dorsal_spine_tibia = 0.8
            like_two_dorsal_spine_tibia = 0.2
            sum_tibia_no_of_spine = like_one_dorsal_spine_tibia + like_two_dorsal_spine_tibia
            dict["Tibia IV: <number of dorsal spines>"] = tibia_no_of_spine
            dict["P(X | Tibia IV: <number of dorsal spines>_one dorsal spine)"] = like_one_dorsal_spine_tibia
            dict["P(X | Tibia IV: <number of dorsal spines>_two dorsal spines)"] = like_two_dorsal_spine_tibia
            dict["Sum P(Tibia IV: <number of dorsal spines>)"] = sum_tibia_no_of_spine
        elif tibia_no_of_spine == "two dorsal spines":
            like_one_dorsal_spine_tibia = 0.2
            like_two_dorsal_spine_tibia = 0.8
            sum_tibia_no_of_spine = like_one_dorsal_spine_tibia + like_two_dorsal_spine_tibia
            dict["Tibia IV: <number of dorsal spines>"] = tibia_no_of_spine
            dict["P(X | Tibia IV: <number of dorsal spines>_one dorsal spine)"] = like_one_dorsal_spine_tibia
            dict["P(X | Tibia IV: <number of dorsal spines>_two dorsal spines)"] = like_two_dorsal_spine_tibia
            dict["Sum P(Tibia IV: <number of dorsal spines>)"] = sum_tibia_no_of_spine
        else:  
            sum_tibia_no_of_spine = like_one_dorsal_spine_tibia + like_two_dorsal_spine_tibia
            dict["Tibia IV: <number of dorsal spines>"] = tibia_no_of_spine
            dict["P(X | Tibia IV: <number of dorsal spines>_one dorsal spine)"] = like_one_dorsal_spine_tibia
            dict["P(X | Tibia IV: <number of dorsal spines>_two dorsal spines)"] = like_two_dorsal_spine_tibia
            dict["Sum P(Tibia IV: <number of dorsal spines>)"] = sum_tibia_no_of_spine

        if tibia_spine_formula == "0":
            like_0000 = 0.8
            like_0011 = 0.16
            like_1111 = 0.032
            like_2211 = 0.0064
            like_2221 = 0.00128
            like_2222 = 0.00032
            sum_tibia_spine_formula = like_0000 + like_0011 + like_1111 + like_2211 + like_2221 + like_2222
            dict["Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>"] = tibia_spine_formula
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_0)"] = like_0000
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_11)"] = like_0011
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_1111)"] = like_1111
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2211)"] = like_2211
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2221)"] = like_2221
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2222)"] = like_2222
            dict["Sum P(Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>)"] = sum_tibia_spine_formula
        elif tibia_spine_formula == "11":
            like_0000 = 0.08
            like_0011 = 0.8
            like_1111 = 0.08
            like_2211 = 0.032
            like_2221 = 0.0064
            like_2222 = 0.0016
            sum_tibia_spine_formula = like_0000 + like_0011 + like_1111 + like_2211 + like_2221 + like_2222
            dict["Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>"] = tibia_spine_formula
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_0)"] = like_0000
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_11)"] = like_0011
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_1111)"] = like_1111
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2211)"] = like_2211
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2221)"] = like_2221
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2222)"] = like_2222
            dict["Sum P(Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>)"] = sum_tibia_spine_formula
        elif tibia_spine_formula == "1111":
            like_0000 = 0.016
            like_0011 = 0.08
            like_1111 = 0.8
            like_2211 = 0.08
            like_2221 = 0.016
            like_2222 = 0.008
            sum_tibia_spine_formula = like_0000 + like_0011 + like_1111 + like_2211 + like_2221 + like_2222
            dict["Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>"] = tibia_spine_formula
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_0)"] = like_0000
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_11)"] = like_0011
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_1111)"] = like_1111
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2211)"] = like_2211
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2221)"] = like_2221
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2222)"] = like_2222
            dict["Sum P(Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>)"] = sum_tibia_spine_formula
        elif tibia_spine_formula == "2211":
            like_0000 = 0.004
            like_0011 = 0.004
            like_1111 = 0.08
            like_2211 = 0.8
            like_2221 = 0.08
            like_2222 = 0.032
            sum_tibia_spine_formula = like_0000 + like_0011 + like_1111 + like_2211 + like_2221 + like_2222
            dict["Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>"] = tibia_spine_formula
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_0)"] = like_0000
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_11)"] = like_0011
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_1111)"] = like_1111
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2211)"] = like_2211
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2221)"] = like_2221
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2222)"] = like_2222
            dict["Sum P(Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>)"] = sum_tibia_spine_formula
        elif tibia_spine_formula == "2221":
            like_0000 = 0.0016
            like_0011 = 0.0064
            like_1111 = 0.032
            like_2211 = 0.08
            like_2221 = 0.8
            like_2222 = 0.08
            sum_tibia_spine_formula = like_0000 + like_0011 + like_1111 + like_2211 + like_2221 + like_2222
            dict["Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>"] = tibia_spine_formula
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_0)"] = like_0000
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_11)"] = like_0011
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_1111)"] = like_1111
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2211)"] = like_2211
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2221)"] = like_2221
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2222)"] = like_2222
            dict["Sum P(Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>)"] = sum_tibia_spine_formula
        elif tibia_spine_formula == "2222":
            like_0000 = 0.00032
            like_0011 = 0.00128
            like_1111 = 0.0064
            like_2211 = 0.032
            like_2221 = 0.16
            like_2222 = 0.8
            sum_tibia_spine_formula = like_0000 + like_0011 + like_1111 + like_2211 + like_2221 + like_2222
            dict["Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>"] = tibia_spine_formula
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_0)"] = like_0000
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_11)"] = like_0011
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_1111)"] = like_1111
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2211)"] = like_2211
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2221)"] = like_2221
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2222)"] = like_2222
            dict["Sum P(Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>)"] = sum_tibia_spine_formula
        else:  
            sum_tibia_spine_formula = like_0000 + like_0011 + like_1111 + like_2211 + like_2221 + like_2222
            dict["Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>"] = tibia_spine_formula
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_0)"] = like_0000
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_11)"] = like_0011
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_1111)"] = like_1111
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2211)"] = like_2211
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2221)"] = like_2221
            dict["P(X | Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>_2222)"] = like_2222
            dict["Sum P(Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>)"] = sum_tibia_spine_formula

        if tibia_ventral == "no spines":
            like_no_ventral_tibia_spines = 0.7
            like_stout_ventral_tibia_spines = 0.3
            sum_tibia_ventral = like_no_ventral_tibia_spines + like_stout_ventral_tibia_spines
            dict["Tibia I-II ventrally: <presence of spines>"] = tibia_ventral
            dict["P(X | Tibia I-II ventrally: <presence of spines>_no spines)"] = like_no_ventral_tibia_spines
            dict["P(X | Tibia I-II ventrally: <presence of spines>_stout spines in two rows)"] = like_stout_ventral_tibia_spines
            dict["Sum P(Tibia I-II ventrally: <presence of spines>)"] = sum_tibia_ventral
        elif tibia_ventral == "stout spines in two rows":
            like_no_ventral_tibia_spines = 0.3
            like_stout_ventral_tibia_spines = 0.7
            sum_tibia_ventral = like_no_ventral_tibia_spines + like_stout_ventral_tibia_spines
            dict["Tibia I-II ventrally: <presence of spines>"] = tibia_ventral
            dict["P(X | Tibia I-II ventrally: <presence of spines>_no spines)"] = like_no_ventral_tibia_spines
            dict["P(X | Tibia I-II ventrally: <presence of spines>_stout spines in two rows)"] = like_stout_ventral_tibia_spines
            dict["Sum P(Tibia I-II ventrally: <presence of spines>)"] = sum_tibia_ventral
        else:
            sum_tibia_ventral = like_no_ventral_tibia_spines + like_stout_ventral_tibia_spines
            dict["Tibia I-II ventrally: <presence of spines>"] = tibia_ventral
            dict["P(X | Tibia I-II ventrally: <presence of spines>_no spines)"] = like_no_ventral_tibia_spines
            dict["P(X | Tibia I-II ventrally: <presence of spines>_stout spines in two rows)"] = like_stout_ventral_tibia_spines
            dict["Sum P(Tibia I-II ventrally: <presence of spines>)"] = sum_tibia_ventral

        if m_pedipalp_femur_app == "unremarkable":
            like_m_pedipalp_unremarkable = 0.9
            like_m_pedipalp_conspicuous = 0.1
            sum_m_pedipalp_femur_app = like_m_pedipalp_unremarkable + like_m_pedipalp_conspicuous
            dict["Male pedipalp: femur <appearance>"] = m_pedipalp_femur_app
            dict["P(X | Male pedipalp: femur <appearance>_unremarkable)"] = like_m_pedipalp_unremarkable
            dict["P(X | Male pedipalp: femur <appearance>_conspicuous)"] = like_m_pedipalp_conspicuous
            dict["Sum P(Male pedipalp: femur <appearance>)"] = sum_m_pedipalp_femur_app
        elif m_pedipalp_femur_app == "conspicuous":
            like_m_pedipalp_unremarkable = 0.1
            like_m_pedipalp_conspicuous = 0.9
            sum_m_pedipalp_femur_app = like_m_pedipalp_unremarkable + like_m_pedipalp_conspicuous
            dict["Male pedipalp: femur <appearance>"] = m_pedipalp_femur_app
            dict["P(X | Male pedipalp: femur <appearance>_unremarkable)"] = like_m_pedipalp_unremarkable
            dict["P(X | Male pedipalp: femur <appearance>_conspicuous)"] = like_m_pedipalp_conspicuous
            dict["Sum P(Male pedipalp: femur <appearance>)"] = sum_m_pedipalp_femur_app
        else:
            sum_m_pedipalp_femur_app = like_m_pedipalp_unremarkable + like_m_pedipalp_conspicuous
            dict["Male pedipalp: femur <appearance>"] = m_pedipalp_femur_app
            dict["P(X | Male pedipalp: femur <appearance>_unremarkable)"] = like_m_pedipalp_unremarkable
            dict["P(X | Male pedipalp: femur <appearance>_conspicuous)"] = like_m_pedipalp_conspicuous
            dict["Sum P(Male pedipalp: femur <appearance>)"] = sum_m_pedipalp_femur_app

        if m_pedipalp_patella_app == "conspicuously swollen":
            like_consp_swollen_patella = 0.7
            like_unremarkable_patella = 0.21
            like_apophyses_patella = 0.045
            like_consp_spines_patella = 0.045
            sum_m_pedipalp_patella_app = like_consp_swollen_patella + like_unremarkable_patella + like_apophyses_patella + like_consp_spines_patella
            dict["Male pedipalp: patella <appearance>"] = m_pedipalp_patella_app
            dict["P(X | Male pedipalp: patella <appearance>_conspicuously swollen)"] = like_consp_swollen_patella
            dict["P(X | Male pedipalp: patella <appearance>_unremarkable)"] = like_unremarkable_patella
            dict["P(X | Male pedipalp: patella <appearance>_with apophyses)"] = like_apophyses_patella
            dict["P(X | Male pedipalp: patella <appearance>_with conspicuous spines (single or tufts))"] = like_consp_spines_patella
            dict["Sum P(Male pedipalp: patella <appearance>)"] = sum_m_pedipalp_patella_app
        elif m_pedipalp_patella_app == "unremarkable":
            like_consp_swollen_patella = 0.21
            like_unremarkable_patella = 0.7
            like_apophyses_patella = 0.045
            like_consp_spines_patella = 0.045
            sum_m_pedipalp_patella_app = like_consp_swollen_patella + like_unremarkable_patella + like_apophyses_patella + like_consp_spines_patella
            dict["Male pedipalp: patella <appearance>"] = m_pedipalp_patella_app
            dict["P(X | Male pedipalp: patella <appearance>_conspicuously swollen)"] = like_consp_swollen_patella
            dict["P(X | Male pedipalp: patella <appearance>_unremarkable)"] = like_unremarkable_patella
            dict["P(X | Male pedipalp: patella <appearance>_with apophyses)"] = like_apophyses_patella
            dict["P(X | Male pedipalp: patella <appearance>_with conspicuous spines (single or tufts))"] = like_consp_spines_patella
            dict["Sum P(Male pedipalp: patella <appearance>)"] = sum_m_pedipalp_patella_app
        elif m_pedipalp_patella_app == "with apophyses":
            like_consp_swollen_patella = 0.045
            like_unremarkable_patella = 0.045
            like_apophyses_patella = 0.7
            like_consp_spines_patella = 0.21
            sum_m_pedipalp_patella_app = like_consp_swollen_patella + like_unremarkable_patella + like_apophyses_patella + like_consp_spines_patella
            dict["Male pedipalp: patella <appearance>"] = m_pedipalp_patella_app
            dict["P(X | Male pedipalp: patella <appearance>_conspicuously swollen)"] = like_consp_swollen_patella
            dict["P(X | Male pedipalp: patella <appearance>_unremarkable)"] = like_unremarkable_patella
            dict["P(X | Male pedipalp: patella <appearance>_with apophyses)"] = like_apophyses_patella
            dict["P(X | Male pedipalp: patella <appearance>_with conspicuous spines (single or tufts))"] = like_consp_spines_patella
            dict["Sum P(Male pedipalp: patella <appearance>)"] = sum_m_pedipalp_patella_app
        elif m_pedipalp_patella_app == "with conspicuous spines (single or tufts)":
            like_consp_swollen_patella = 0.045
            like_unremarkable_patella = 0.045
            like_apophyses_patella = 0.21
            like_consp_spines_patella = 0.7
            sum_m_pedipalp_patella_app = like_consp_swollen_patella + like_unremarkable_patella + like_apophyses_patella + like_consp_spines_patella
            dict["Male pedipalp: patella <appearance>"] = m_pedipalp_patella_app
            dict["P(X | Male pedipalp: patella <appearance>_conspicuously swollen)"] = like_consp_swollen_patella
            dict["P(X | Male pedipalp: patella <appearance>_unremarkable)"] = like_unremarkable_patella
            dict["P(X | Male pedipalp: patella <appearance>_with apophyses)"] = like_apophyses_patella
            dict["P(X | Male pedipalp: patella <appearance>_with conspicuous spines (single or tufts))"] = like_consp_spines_patella
            dict["Sum P(Male pedipalp: patella <appearance>)"] = sum_m_pedipalp_patella_app
        else:  
            sum_m_pedipalp_patella_app = like_consp_swollen_patella + like_unremarkable_patella + like_apophyses_patella + like_consp_spines_patella
            dict["Male pedipalp: patella <appearance>"] = m_pedipalp_patella_app
            dict["P(X | Male pedipalp: patella <appearance>_conspicuously swollen)"] = like_consp_swollen_patella
            dict["P(X | Male pedipalp: patella <appearance>_unremarkable)"] = like_unremarkable_patella
            dict["P(X | Male pedipalp: patella <appearance>_with apophyses)"] = like_apophyses_patella
            dict["P(X | Male pedipalp: patella <appearance>_with conspicuous spines (single or tufts))"] = like_consp_spines_patella
            dict["Sum P(Male pedipalp: patella <appearance>)"] = sum_m_pedipalp_patella_app

        if m_pedipalp_tibia_app == "unremarkable":
            like_unremarkable_tibia = 0.6
            like_complex_tibia = 0.0666666667
            like_multiple_complex_tibia = 0.0666666667
            like_multiple_simple_tibia = 0.0666666667
            like_one_or_more_spines_tibia = 0.0666666667
            like_simple_tibia = 0.0666666667
            like_tufts_tibia = 0.0666666667
            sum_m_pedipalp_tibia_app = like_unremarkable_tibia + like_complex_tibia + like_multiple_complex_tibia + like_multiple_simple_tibia + like_one_or_more_spines_tibia + like_simple_tibia + like_tufts_tibia
            dict["Male pedipalp: tibia <appearance>"] = m_pedipalp_tibia_app
            dict["P(X | Male pedipalp: tibia <appearance>_unremarkable)"] = like_unremarkable_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with complex apophysis)"] = like_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, complex apophysis)"] = like_multiple_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, simple apophysis)"] = like_multiple_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with one or more spines)"] = like_one_or_more_spines_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with simple apophysis)"] = like_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with tufts of hair or spines)"] = like_tufts_tibia
            dict["Sum P(Male pedipalp: tibia <appearance>)"] = sum_m_pedipalp_tibia_app
        elif m_pedipalp_tibia_app == "with complex apophysis":
            like_unremarkable_tibia = 0.0256
            like_complex_tibia = 0.6
            like_multiple_complex_tibia = 0.24
            like_multiple_simple_tibia = 0.048
            like_one_or_more_spines_tibia = 0.0192
            like_simple_tibia = 0.048
            like_tufts_tibia = 0.0192
            sum_m_pedipalp_tibia_app = like_unremarkable_tibia + like_complex_tibia + like_multiple_complex_tibia + like_multiple_simple_tibia + like_one_or_more_spines_tibia + like_simple_tibia + like_tufts_tibia
            dict["Male pedipalp: tibia <appearance>"] = m_pedipalp_tibia_app
            dict["P(X | Male pedipalp: tibia <appearance>_unremarkable)"] = like_unremarkable_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with complex apophysis)"] = like_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, complex apophysis)"] = like_multiple_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, simple apophysis)"] = like_multiple_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with one or more spines)"] = like_one_or_more_spines_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with simple apophysis)"] = like_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with tufts of hair or spines)"] = like_tufts_tibia
            dict["Sum P(Male pedipalp: tibia <appearance>)"] = sum_m_pedipalp_tibia_app
        elif m_pedipalp_tibia_app == "with multiple, complex apophysis":
            like_unremarkable_tibia = 0.0256
            like_complex_tibia = 0.24
            like_multiple_complex_tibia = 0.6
            like_multiple_simple_tibia = 0.048
            like_one_or_more_spines_tibia = 0.0192
            like_simple_tibia = 0.048
            like_tufts_tibia = 0.0192
            sum_m_pedipalp_tibia_app = like_unremarkable_tibia + like_complex_tibia + like_multiple_complex_tibia + like_multiple_simple_tibia + like_one_or_more_spines_tibia + like_simple_tibia + like_tufts_tibia
            dict["Male pedipalp: tibia <appearance>"] = m_pedipalp_tibia_app
            dict["P(X | Male pedipalp: tibia <appearance>_unremarkable)"] = like_unremarkable_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with complex apophysis)"] = like_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, complex apophysis)"] = like_multiple_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, simple apophysis)"] = like_multiple_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with one or more spines)"] = like_one_or_more_spines_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with simple apophysis)"] = like_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with tufts of hair or spines)"] = like_tufts_tibia
            dict["Sum P(Male pedipalp: tibia <appearance>)"] = sum_m_pedipalp_tibia_app
        elif m_pedipalp_tibia_app == "with multiple, simple apophysis":
            like_unremarkable_tibia = 0.0256
            like_complex_tibia = 0.048
            like_multiple_complex_tibia = 0.048
            like_multiple_simple_tibia = 0.6
            like_one_or_more_spines_tibia = 0.0192
            like_simple_tibia = 0.24
            like_tufts_tibia = 0.0192
            sum_m_pedipalp_tibia_app = like_unremarkable_tibia + like_complex_tibia + like_multiple_complex_tibia + like_multiple_simple_tibia + like_one_or_more_spines_tibia + like_simple_tibia + like_tufts_tibia
            dict["Male pedipalp: tibia <appearance>"] = m_pedipalp_tibia_app
            dict["P(X | Male pedipalp: tibia <appearance>_unremarkable)"] = like_unremarkable_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with complex apophysis)"] = like_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, complex apophysis)"] = like_multiple_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, simple apophysis)"] = like_multiple_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with one or more spines)"] = like_one_or_more_spines_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with simple apophysis)"] = like_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with tufts of hair or spines)"] = like_tufts_tibia
            dict["Sum P(Male pedipalp: tibia <appearance>)"] = sum_m_pedipalp_tibia_app
        elif m_pedipalp_tibia_app == "with one or more spines":
            like_unremarkable_tibia = 0.064
            like_complex_tibia = 0.024
            like_multiple_complex_tibia = 0.024 
            like_multiple_simple_tibia = 0.024
            like_one_or_more_spines_tibia = 0.6
            like_simple_tibia = 0.024
            like_tufts_tibia = 0.24
            sum_m_pedipalp_tibia_app = like_unremarkable_tibia + like_complex_tibia + like_multiple_complex_tibia + like_multiple_simple_tibia + like_one_or_more_spines_tibia + like_simple_tibia + like_tufts_tibia
            dict["Male pedipalp: tibia <appearance>"] = m_pedipalp_tibia_app
            dict["P(X | Male pedipalp: tibia <appearance>_unremarkable)"] = like_unremarkable_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with complex apophysis)"] = like_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, complex apophysis)"] = like_multiple_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, simple apophysis)"] = like_multiple_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with one or more spines)"] = like_one_or_more_spines_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with simple apophysis)"] = like_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with tufts of hair or spines)"] = like_tufts_tibia
            dict["Sum P(Male pedipalp: tibia <appearance>)"] = sum_m_pedipalp_tibia_app
        elif m_pedipalp_tibia_app == "with simple apophysis":
            like_unremarkable_tibia = 0.0256
            like_complex_tibia = 0.048
            like_multiple_complex_tibia = 0.048
            like_multiple_simple_tibia = 0.24
            like_one_or_more_spines_tibia = 0.0192
            like_simple_tibia = 0.6
            like_tufts_tibia = 0.0192
            sum_m_pedipalp_tibia_app = like_unremarkable_tibia + like_complex_tibia + like_multiple_complex_tibia + like_multiple_simple_tibia + like_one_or_more_spines_tibia + like_simple_tibia + like_tufts_tibia
            dict["Male pedipalp: tibia <appearance>"] = m_pedipalp_tibia_app
            dict["P(X | Male pedipalp: tibia <appearance>_unremarkable)"] = like_unremarkable_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with complex apophysis)"] = like_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, complex apophysis)"] = like_multiple_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, simple apophysis)"] = like_multiple_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with one or more spines)"] = like_one_or_more_spines_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with simple apophysis)"] = like_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with tufts of hair or spines)"] = like_tufts_tibia
            dict["Sum P(Male pedipalp: tibia <appearance>)"] = sum_m_pedipalp_tibia_app
        elif m_pedipalp_tibia_app == "with tufts of hair or spines":
            like_unremarkable_tibia = 0.064
            like_complex_tibia = 0.024
            like_multiple_complex_tibia = 0.024
            like_multiple_simple_tibia = 0.024
            like_one_or_more_spines_tibia = 0.24
            like_simple_tibia = 0.024
            like_tufts_tibia = 0.6
            sum_m_pedipalp_tibia_app = like_unremarkable_tibia + like_complex_tibia + like_multiple_complex_tibia + like_multiple_simple_tibia + like_one_or_more_spines_tibia + like_simple_tibia + like_tufts_tibia
            dict["Male pedipalp: tibia <appearance>"] = m_pedipalp_tibia_app
            dict["P(X | Male pedipalp: tibia <appearance>_unremarkable)"] = like_unremarkable_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with complex apophysis)"] = like_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, complex apophysis)"] = like_multiple_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, simple apophysis)"] = like_multiple_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with one or more spines)"] = like_one_or_more_spines_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with simple apophysis)"] = like_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with tufts of hair or spines)"] = like_tufts_tibia
            dict["Sum P(Male pedipalp: tibia <appearance>)"] = sum_m_pedipalp_tibia_app
        else:         
            sum_m_pedipalp_tibia_app = like_unremarkable_tibia + like_complex_tibia + like_multiple_complex_tibia + like_multiple_simple_tibia + like_one_or_more_spines_tibia + like_simple_tibia + like_tufts_tibia
            dict["Male pedipalp: tibia <appearance>"] = m_pedipalp_tibia_app
            dict["P(X | Male pedipalp: tibia <appearance>_unremarkable)"] = like_unremarkable_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with complex apophysis)"] = like_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, complex apophysis)"] = like_multiple_complex_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with multiple, simple apophysis)"] = like_multiple_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with one or more spines)"] = like_one_or_more_spines_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with simple apophysis)"] = like_simple_tibia
            dict["P(X | Male pedipalp: tibia <appearance>_with tufts of hair or spines)"] = like_tufts_tibia
            dict["Sum P(Male pedipalp: tibia <appearance>)"] = sum_m_pedipalp_tibia_app

        if m_pedipalp_cymbium_app == "margins with notches/bulges":
            like_margins_cymbium = 0.6
            like_simple_cymbium = 0.16
            like_elevations_cymbium = 0.24
            sum_m_pedipalp_cymbium_app = like_margins_cymbium + like_simple_cymbium + like_elevations_cymbium
            dict["Male pedipalp: cymbium <appearance>"] = m_pedipalp_cymbium_app
            dict["P(X | Male pedipalp: cymbium <appearance>_margins with notches/bulges)"] = like_margins_cymbium
            dict["P(X | Male pedipalp: cymbium <appearance>_simple)"] = like_simple_cymbium
            dict["P(X | Male pedipalp: cymbium <appearance>_with dorsal projections/conical elevations"] = like_elevations_cymbium
            dict["Sum P(Male pedipalp: cymbium <appearance>)"] = sum_m_pedipalp_cymbium_app
        elif m_pedipalp_cymbium_app == "simple":
            like_margins_cymbium = 0.2
            like_simple_cymbium = 0.6
            like_elevations_cymbium = 0.2 
            sum_m_pedipalp_cymbium_app = like_margins_cymbium + like_simple_cymbium + like_elevations_cymbium
            dict["Male pedipalp: cymbium <appearance>"] = m_pedipalp_cymbium_app
            dict["P(X | Male pedipalp: cymbium <appearance>_margins with notches/bulges)"] = like_margins_cymbium
            dict["P(X | Male pedipalp: cymbium <appearance>_simple)"] = like_simple_cymbium
            dict["P(X | Male pedipalp: cymbium <appearance>_with dorsal projections/conical elevations"] = like_elevations_cymbium
            dict["Sum P(Male pedipalp: cymbium <appearance>)"] = sum_m_pedipalp_cymbium_app
        elif m_pedipalp_cymbium_app == "with dorsal projections/conical elevations":
            like_margins_cymbium = 0.24
            like_simple_cymbium = 0.16
            like_elevations_cymbium = 0.6
            sum_m_pedipalp_cymbium_app = like_margins_cymbium + like_simple_cymbium + like_elevations_cymbium
            dict["Male pedipalp: cymbium <appearance>"] = m_pedipalp_cymbium_app
            dict["P(X | Male pedipalp: cymbium <appearance>_margins with notches/bulges)"] = like_margins_cymbium
            dict["P(X | Male pedipalp: cymbium <appearance>_simple)"] = like_simple_cymbium
            dict["P(X | Male pedipalp: cymbium <appearance>_with dorsal projections/conical elevations"] = like_elevations_cymbium
            dict["Sum P(Male pedipalp: cymbium <appearance>)"] = sum_m_pedipalp_cymbium_app
        else:         
            sum_m_pedipalp_cymbium_app = like_margins_cymbium + like_simple_cymbium + like_elevations_cymbium
            dict["Male pedipalp: cymbium <appearance>"] = m_pedipalp_cymbium_app
            dict["P(X | Male pedipalp: cymbium <appearance>_margins with notches/bulges)"] = like_margins_cymbium
            dict["P(X | Male pedipalp: cymbium <appearance>_simple)"] = like_simple_cymbium
            dict["P(X | Male pedipalp: cymbium <appearance>_with dorsal projections/conical elevations"] = like_elevations_cymbium
            dict["Sum P(Male pedipalp: cymbium <appearance>)"] = sum_m_pedipalp_cymbium_app

        if m_pedipalp_paracymbium_form == "complex":
            like_complex_paracym = 0.7
            like_simple_paracym = 0.3
            sum_m_pedipalp_paracymbium_form = like_complex_paracym + like_simple_paracym
            dict["Male pedipalp: paracymbium <form>"] = m_pedipalp_paracymbium_form
            dict["P(X | Male pedipalp: paracymbium <form>_complex)"] = like_complex_paracym
            dict["P(X | Male pedipalp: paracymbium <form>_simple)"] = like_simple_paracym
            dict["Sum P(Male pedipalp: paracymbium <form>)"] = sum_m_pedipalp_paracymbium_form
        elif m_pedipalp_paracymbium_form == "simple":
            like_complex_paracym = 0.3
            like_simple_paracym = 0.7
            sum_m_pedipalp_paracymbium_form = like_complex_paracym + like_simple_paracym
            dict["Male pedipalp: paracymbium <form>"] = m_pedipalp_paracymbium_form
            dict["P(X | Male pedipalp: paracymbium <form>_complex)"] = like_complex_paracym
            dict["P(X | Male pedipalp: paracymbium <form>_simple)"] = like_simple_paracym
            dict["Sum P(Male pedipalp: paracymbium <form>)"] = sum_m_pedipalp_paracymbium_form
        else:         
            sum_m_pedipalp_paracymbium_form = like_complex_paracym + like_simple_paracym
            dict["Male pedipalp: paracymbium <form>"] = m_pedipalp_paracymbium_form
            dict["P(X | Male pedipalp: paracymbium <form>_complex)"] = like_complex_paracym
            dict["P(X | Male pedipalp: paracymbium <form>_simple)"] = like_simple_paracym
            dict["Sum P(Male pedipalp: paracymbium <form>)"] = sum_m_pedipalp_paracymbium_form

        if m_pedipalp_para_branches == "teeth absent":
            like_absent_para_branches = 0.7
            like_present_para_branches = 0.3
            sum_m_pedipalp_para_branches = like_absent_para_branches + like_present_para_branches
            dict["Male pedipalp: branches of paracymbium <presence of teeth>"] = m_pedipalp_para_branches
            dict["P(X | Male pedipalp: branches of paracymbium <presence of teeth>_teeth absent)"] = like_absent_para_branches
            dict["P(X | Male pedipalp: branches of paracymbium <presence of teeth>_teeth present)"] = like_present_para_branches
            dict["Sum P(Male pedipalp: branches of paracymbium <presence of teeth>)"] = sum_m_pedipalp_para_branches
        elif m_pedipalp_para_branches == "teeth present":
            like_absent_para_branches = 0.3
            like_present_para_branches = 0.7
            sum_m_pedipalp_para_branches = like_absent_para_branches + like_present_para_branches
            dict["Male pedipalp: branches of paracymbium <presence of teeth>"] = m_pedipalp_para_branches
            dict["P(X | Male pedipalp: branches of paracymbium <presence of teeth>_teeth absent)"] = like_absent_para_branches
            dict["P(X | Male pedipalp: branches of paracymbium <presence of teeth>_teeth present)"] = like_present_para_branches
            dict["Sum P(Male pedipalp: branches of paracymbium <presence of teeth>)"] = sum_m_pedipalp_para_branches
        else:         
            sum_m_pedipalp_para_branches = like_absent_para_branches + like_present_para_branches
            dict["Male pedipalp: branches of paracymbium <presence of teeth>"] = m_pedipalp_para_branches
            dict["P(X | Male pedipalp: branches of paracymbium <presence of teeth>_teeth absent)"] = like_absent_para_branches
            dict["P(X | Male pedipalp: branches of paracymbium <presence of teeth>_teeth present)"] = like_present_para_branches
            dict["Sum P(Male pedipalp: branches of paracymbium <presence of teeth>)"] = sum_m_pedipalp_para_branches

        if m_pedipalp_embolus_app == "conspicuous, circular":
            like_consp_cir_embolus = 0.7
            like_consp_curl_embolus = 0.21
            like_unremarkable_embolus = 0.09
            sum_m_pedipalp_embolus_app = like_consp_cir_embolus + like_consp_curl_embolus + like_unremarkable_embolus
            dict["Male pedipalp: embolus <appearance>"] = m_pedipalp_embolus_app
            dict["P(X | Male pedipalp: embolus <appearance>_conspicuous, circular)"] = like_consp_cir_embolus
            dict["P(X | Male pedipalp: embolus <appearance>_conspicuous, curled)"] = like_consp_curl_embolus
            dict["P(X | Male pedipalp: embolus <appearance>_unremarkable)"] = like_unremarkable_embolus
            dict["Sum P(Male pedipalp: embolus <appearance>)"] = sum_m_pedipalp_embolus_app
        elif m_pedipalp_embolus_app == "conspicuous, curled":
            like_consp_cir_embolus = 0.21
            like_consp_curl_embolus = 0.7
            like_unremarkable_embolus = 0.09
            sum_m_pedipalp_embolus_app = like_consp_cir_embolus + like_consp_curl_embolus + like_unremarkable_embolus
            dict["Male pedipalp: embolus <appearance>"] = m_pedipalp_embolus_app
            dict["P(X | Male pedipalp: embolus <appearance>_conspicuous, circular)"] = like_consp_cir_embolus
            dict["P(X | Male pedipalp: embolus <appearance>_conspicuous, curled)"] = like_consp_curl_embolus
            dict["P(X | Male pedipalp: embolus <appearance>_unremarkable)"] = like_unremarkable_embolus
            dict["Sum P(Male pedipalp: embolus <appearance>)"] = sum_m_pedipalp_embolus_app
        elif m_pedipalp_embolus_app == "unremarkable":
            like_consp_cir_embolus = 0.15
            like_consp_curl_embolus = 0.15
            like_unremarkable_embolus = 0.7
            sum_m_pedipalp_embolus_app = like_consp_cir_embolus + like_consp_curl_embolus + like_unremarkable_embolus
            dict["Male pedipalp: embolus <appearance>"] = m_pedipalp_embolus_app
            dict["P(X | Male pedipalp: embolus <appearance>_conspicuous, circular)"] = like_consp_cir_embolus
            dict["P(X | Male pedipalp: embolus <appearance>_conspicuous, curled)"] = like_consp_curl_embolus
            dict["P(X | Male pedipalp: embolus <appearance>_unremarkable)"] = like_unremarkable_embolus
            dict["Sum P(Male pedipalp: embolus <appearance>)"] = sum_m_pedipalp_embolus_app
        else:
            sum_m_pedipalp_embolus_app = like_consp_cir_embolus + like_consp_curl_embolus + like_unremarkable_embolus
            dict["Male pedipalp: embolus <appearance>"] = m_pedipalp_embolus_app
            dict["P(X | Male pedipalp: embolus <appearance>_conspicuous, circular)"] = like_consp_cir_embolus
            dict["P(X | Male pedipalp: embolus <appearance>_conspicuous, curled)"] = like_consp_curl_embolus
            dict["P(X | Male pedipalp: embolus <appearance>_unremarkable)"] = like_unremarkable_embolus
            dict["Sum P(Male pedipalp: embolus <appearance>)"] = sum_m_pedipalp_embolus_app    

        if m_pedipalp_lamella == "absent":
            like_m_pedipalp_lamella_absent = 0.7
            like_m_pedipalp_lamella_conspicuous = 0.3
            sum_m_pedipalp_lamella = like_m_pedipalp_lamella_absent + like_m_pedipalp_lamella_conspicuous
            dict["Male pedipalp: lamella characteristica <presence>"] = m_pedipalp_lamella
            dict["P(X | Male pedipalp: lamella characteristica <presence>_absent)"] = like_m_pedipalp_lamella_absent
            dict["P(X | Male pedipalp: lamella characteristica <presence>_conspicuous)"] = like_m_pedipalp_lamella_conspicuous
            dict["Sum P(Male pedipalp: lamella characteristica <presence>)"] = sum_m_pedipalp_lamella
        elif m_pedipalp_lamella == "conspicuous":
            like_m_pedipalp_lamella_absent = 0.3
            like_m_pedipalp_lamella_conspicuous = 0.7
            sum_m_pedipalp_lamella = like_m_pedipalp_lamella_absent + like_m_pedipalp_lamella_conspicuous
            dict["Male pedipalp: lamella characteristica <presence>"] = m_pedipalp_lamella
            dict["P(X | Male pedipalp: lamella characteristica <presence>_absent)"] = like_m_pedipalp_lamella_absent
            dict["P(X | Male pedipalp: lamella characteristica <presence>_conspicuous)"] = like_m_pedipalp_lamella_conspicuous
            dict["Sum P(Male pedipalp: lamella characteristica <presence>)"] = sum_m_pedipalp_lamella
        else:
            sum_m_pedipalp_lamella = like_m_pedipalp_lamella_absent + like_m_pedipalp_lamella_conspicuous
            dict["Male pedipalp: lamella characteristica <presence>"] = m_pedipalp_lamella
            dict["P(X | Male pedipalp: lamella characteristica <presence>_absent)"] = like_m_pedipalp_lamella_absent
            dict["P(X | Male pedipalp: lamella characteristica <presence>_conspicuous)"] = like_m_pedipalp_lamella_conspicuous
            dict["Sum P(Male pedipalp: lamella characteristica <presence>)"] = sum_m_pedipalp_lamella

        if f_palp_claw == "conspicuous":
            like_consp_f_claw = 0.8
            like_inconsp_f_claw = 0.2
            sum_f_palp_claw = like_consp_f_claw + like_inconsp_f_claw
            dict["Female palp: claw <presence>"] = f_palp_claw
            dict["P(X | Female palp: claw <presence>_conspicuous)"] = like_consp_f_claw
            dict["P(X | Female palp: claw <presence>_not present/ inconspicuous)"] = like_inconsp_f_claw
            dict["Sum P(Female palp: claw <presence>)"] = sum_f_palp_claw
        elif f_palp_claw == "not present/ inconspicuous":
            like_consp_f_claw = 0.2
            like_inconsp_f_claw = 0.8
            sum_f_palp_claw = like_consp_f_claw + like_inconsp_f_claw
            dict["Female palp: claw <presence>"] = f_palp_claw
            dict["P(X | Female palp: claw <presence>_conspicuous)"] = like_consp_f_claw
            dict["P(X | Female palp: claw <presence>_not present/ inconspicuous)"] = like_inconsp_f_claw
            dict["Sum P(Female palp: claw <presence>)"] = sum_f_palp_claw
        else:  
            sum_f_palp_claw = like_consp_f_claw + like_inconsp_f_claw
            dict["Female palp: claw <presence>"] = f_palp_claw
            dict["P(X | Female palp: claw <presence>_conspicuous)"] = like_consp_f_claw
            dict["P(X | Female palp: claw <presence>_not present/ inconspicuous)"] = like_inconsp_f_claw
            dict["Sum P(Female palp: claw <presence>)"] = sum_f_palp_claw      

        if epigyne_app == "unremarkable":
            like_unremarkable_epigyne = 0.7
            like_atrium_epigyne = 0.06
            like_septum_epigyne = 0.06
            like_lateral_plate_epigyne = 0.06
            like_scape_epigyne = 0.06
            like_parmula_epigyne = 0.06
            sum_epigyne_app = like_unremarkable_epigyne + like_atrium_epigyne + like_septum_epigyne + like_lateral_plate_epigyne + like_scape_epigyne + like_parmula_epigyne
            dict["Epigyne: <appearance>"] = epigyne_app
            dict["P(X | Epigyne: <appearance>_unremarkable)"] = like_unremarkable_epigyne
            dict["P(X | Epigyne: <appearance>_with atrium/cavity)"] = like_atrium_epigyne
            dict["P(X | Epigyne: <appearance>_with septum/medial structure)"] = like_septum_epigyne
            dict["P(X | Epigyne: <appearance>_with lateral plates)"] = like_lateral_plate_epigyne
            dict["P(X | Epigyne: <appearance>_with scape(from anterior margin))"] = like_scape_epigyne
            dict["P(X | Epigyne: <appearance>_with parmula(from posterior margin))"] = like_parmula_epigyne
            dict["Sum P(Epigyne: <appearance>)"] = sum_epigyne_app
        elif epigyne_app == "with atrium/cavity":
            like_unremarkable_epigyne = 0.027
            like_atrium_epigyne = 0.7
            like_septum_epigyne = 0.105
            like_lateral_plate_epigyne = 0.105 
            like_scape_epigyne = 0.0315
            like_parmula_epigyne = 0.0315
            sum_epigyne_app = like_unremarkable_epigyne + like_atrium_epigyne + like_septum_epigyne + like_lateral_plate_epigyne + like_scape_epigyne + like_parmula_epigyne
            dict["Epigyne: <appearance>"] = epigyne_app
            dict["P(X | Epigyne: <appearance>_unremarkable)"] = like_unremarkable_epigyne
            dict["P(X | Epigyne: <appearance>_with atrium/cavity)"] = like_atrium_epigyne
            dict["P(X | Epigyne: <appearance>_with septum/medial structure)"] = like_septum_epigyne
            dict["P(X | Epigyne: <appearance>_with lateral plates)"] = like_lateral_plate_epigyne
            dict["P(X | Epigyne: <appearance>_with scape(from anterior margin))"] = like_scape_epigyne
            dict["P(X | Epigyne: <appearance>_with parmula(from posterior margin))"] = like_parmula_epigyne
            dict["Sum P(Epigyne: <appearance>)"] = sum_epigyne_app
        elif epigyne_app == "with septum/medial structure":
            like_unremarkable_epigyne = 0.027
            like_atrium_epigyne = 0.105
            like_septum_epigyne = 0.7
            like_lateral_plate_epigyne = 0.105
            like_scape_epigyne = 0.315
            like_parmula_epigyne = 0.315
            sum_epigyne_app = like_unremarkable_epigyne + like_atrium_epigyne + like_septum_epigyne + like_lateral_plate_epigyne + like_scape_epigyne + like_parmula_epigyne
            dict["Epigyne: <appearance>"] = epigyne_app
            dict["P(X | Epigyne: <appearance>_unremarkable)"] = like_unremarkable_epigyne
            dict["P(X | Epigyne: <appearance>_with atrium/cavity)"] = like_atrium_epigyne
            dict["P(X | Epigyne: <appearance>_with septum/medial structure)"] = like_septum_epigyne
            dict["P(X | Epigyne: <appearance>_with lateral plates)"] = like_lateral_plate_epigyne
            dict["P(X | Epigyne: <appearance>_with scape(from anterior margin))"] = like_scape_epigyne
            dict["P(X | Epigyne: <appearance>_with parmula(from posterior margin))"] = like_parmula_epigyne
            dict["Sum P(Epigyne: <appearance>)"] = sum_epigyne_app
        elif epigyne_app == "with lateral plates":
            like_unremarkable_epigyne = 0.027
            like_atrium_epigyne = 0.105
            like_septum_epigyne = 0.105
            like_lateral_plate_epigyne = 0.7
            like_scape_epigyne = 0.0315
            like_parmula_epigyne = 0.0315
            sum_epigyne_app = like_unremarkable_epigyne + like_atrium_epigyne + like_septum_epigyne + like_lateral_plate_epigyne + like_scape_epigyne + like_parmula_epigyne
            dict["Epigyne: <appearance>"] = epigyne_app
            dict["P(X | Epigyne: <appearance>_unremarkable)"] = like_unremarkable_epigyne
            dict["P(X | Epigyne: <appearance>_with atrium/cavity)"] = like_atrium_epigyne
            dict["P(X | Epigyne: <appearance>_with septum/medial structure)"] = like_septum_epigyne
            dict["P(X | Epigyne: <appearance>_with lateral plates)"] = like_lateral_plate_epigyne
            dict["P(X | Epigyne: <appearance>_with scape(from anterior margin))"] = like_scape_epigyne
            dict["P(X | Epigyne: <appearance>_with parmula(from posterior margin))"] = like_parmula_epigyne
            dict["Sum P(Epigyne: <appearance>)"] = sum_epigyne_app
        elif epigyne_app == "with scape(from anterior margin)":
            like_unremarkable_epigyne = 0.027
            like_atrium_epigyne = 0.021
            like_septum_epigyne = 0.021
            like_lateral_plate_epigyne =0.021 
            like_scape_epigyne = 0.7
            like_parmula_epigyne = 0.21
            sum_epigyne_app = like_unremarkable_epigyne + like_atrium_epigyne + like_septum_epigyne + like_lateral_plate_epigyne + like_scape_epigyne + like_parmula_epigyne
            dict["Epigyne: <appearance>"] = epigyne_app
            dict["P(X | Epigyne: <appearance>_unremarkable)"] = like_unremarkable_epigyne
            dict["P(X | Epigyne: <appearance>_with atrium/cavity)"] = like_atrium_epigyne
            dict["P(X | Epigyne: <appearance>_with septum/medial structure)"] = like_septum_epigyne
            dict["P(X | Epigyne: <appearance>_with lateral plates)"] = like_lateral_plate_epigyne
            dict["P(X | Epigyne: <appearance>_with scape(from anterior margin))"] = like_scape_epigyne
            dict["P(X | Epigyne: <appearance>_with parmula(from posterior margin))"] = like_parmula_epigyne
            dict["Sum P(Epigyne: <appearance>)"] = sum_epigyne_app
        elif epigyne_app == "with parmula(from posterior margin)":
            like_unremarkable_epigyne = 0.027
            like_atrium_epigyne = 0.021
            like_septum_epigyne = 0.021
            like_lateral_plate_epigyne = 0.021
            like_scape_epigyne = 0.21
            like_parmula_epigyne = 0.7
            sum_epigyne_app = like_unremarkable_epigyne + like_atrium_epigyne + like_septum_epigyne + like_lateral_plate_epigyne + like_scape_epigyne + like_parmula_epigyne
            dict["Epigyne: <appearance>"] = epigyne_app
            dict["P(X | Epigyne: <appearance>_unremarkable)"] = like_unremarkable_epigyne
            dict["P(X | Epigyne: <appearance>_with atrium/cavity)"] = like_atrium_epigyne
            dict["P(X | Epigyne: <appearance>_with septum/medial structure)"] = like_septum_epigyne
            dict["P(X | Epigyne: <appearance>_with lateral plates)"] = like_lateral_plate_epigyne
            dict["P(X | Epigyne: <appearance>_with scape(from anterior margin))"] = like_scape_epigyne
            dict["P(X | Epigyne: <appearance>_with parmula(from posterior margin))"] = like_parmula_epigyne
            dict["Sum P(Epigyne: <appearance>)"] = sum_epigyne_app
        else:         
            sum_epigyne_app = like_unremarkable_epigyne + like_atrium_epigyne + like_septum_epigyne + like_lateral_plate_epigyne + like_scape_epigyne + like_parmula_epigyne
            dict["Epigyne: <appearance>"] = epigyne_app
            dict["P(X | Epigyne: <appearance>_unremarkable)"] = like_unremarkable_epigyne
            dict["P(X | Epigyne: <appearance>_with atrium/cavity)"] = like_atrium_epigyne
            dict["P(X | Epigyne: <appearance>_with septum/medial structure)"] = like_septum_epigyne
            dict["P(X | Epigyne: <appearance>_with lateral plates)"] = like_lateral_plate_epigyne
            dict["P(X | Epigyne: <appearance>_with scape(from anterior margin))"] = like_scape_epigyne
            dict["P(X | Epigyne: <appearance>_with parmula(from posterior margin))"] = like_parmula_epigyne
            dict["Sum P(Epigyne: <appearance>)"] = sum_epigyne_app

        if epigyne_form == "flat":
            like_flat_epigyne = 0.7
            like_protrud_epigyne = 0.3
            sum_epigyne_form = like_flat_epigyne + like_protrud_epigyne
            dict["Epigyne: <form>"] = epigyne_form
            dict["P(X | Epigyne: <form>_flat)"] = like_flat_epigyne
            dict["P(X | Epigyne: <form>_protrudes)"] = like_protrud_epigyne
            dict["Sum P(Epigyne: <form>)"] = sum_epigyne_form
        elif epigyne_form == "protrudes":
            like_flat_epigyne = 0.3
            like_protrud_epigyne = 0.7
            sum_epigyne_form = like_flat_epigyne + like_protrud_epigyne
            dict["Epigyne: <form>"] = epigyne_form
            dict["P(X | Epigyne: <form>_flat)"] = like_flat_epigyne
            dict["P(X | Epigyne: <form>_protrudes)"] = like_protrud_epigyne
            dict["Sum P(Epigyne: <form>)"] = sum_epigyne_form
        else:   
            sum_epigyne_form = like_flat_epigyne + like_protrud_epigyne
            dict["Epigyne: <form>"] = epigyne_form
            dict["P(X | Epigyne: <form>_flat)"] = like_flat_epigyne
            dict["P(X | Epigyne: <form>_protrudes)"] = like_protrud_epigyne
            dict["Sum P(Epigyne: <form>)"] = sum_epigyne_form    

        if epigyne_seminal == "underlying structures (e.g., seminal receptacles) not visible":
            like_visible_seminal = 0.2
            like_not_visible_seminal = 0.8
            sum_epigyne_seminal = like_visible_seminal + like_not_visible_seminal
            dict["Epigyne: <seminal receptacles>"] = epigyne_seminal
            dict["P(X | Epigyne: <seminal receptacles>_underlying structures (e.g., seminal receptacles) visible)"] = like_visible_seminal
            dict["P(X | Epigyne: <seminal receptacles>_underlying structures (e.g., seminal receptacles) not visible)"] = like_not_visible_seminal
            dict["Sum P(Epigyne: <seminal receptacles>)"] = sum_epigyne_seminal
        elif epigyne_seminal == "underlying structures (e.g., seminal receptacles) visible":
            like_visible_seminal = 0.8
            like_not_visible_seminal = 0.2
            sum_epigyne_seminal = like_visible_seminal + like_not_visible_seminal
            dict["Epigyne: <seminal receptacles>"] = epigyne_seminal
            dict["P(X | Epigyne: <seminal receptacles>_underlying structures (e.g., seminal receptacles) visible)"] = like_visible_seminal
            dict["P(X | Epigyne: <seminal receptacles>_underlying structures (e.g., seminal receptacles) not visible)"] = like_not_visible_seminal
            dict["Sum P(Epigyne: <seminal receptacles>)"] = sum_epigyne_seminal
        else:   
            sum_epigyne_seminal = like_visible_seminal + like_not_visible_seminal
            dict["Epigyne: <seminal receptacles>"] = epigyne_seminal
            dict["P(X | Epigyne: <seminal receptacles>_underlying structures (e.g., seminal receptacles) visible)"] = like_visible_seminal
            dict["P(X | Epigyne: <seminal receptacles>_underlying structures (e.g., seminal receptacles) not visible)"] = like_not_visible_seminal
            dict["Sum P(Epigyne: <seminal receptacles>)"] = sum_epigyne_seminal

        probab_country = 1/64
        dict["Distribution"] = dist
        for country in countries:
            if country in dist:
                probab_country = 0.9
                dict[f"P(X | Distribution_{country})"] = probab_country
            else:
                probab_country = 0.00015873
                dict[f"P(X | Distribution_{country})"] = probab_country

        if length_p_range == "0.4-0.6":
            like_40_to_60 = 0.9
            like_60_to_80 = 0.09
            like_80_to_100 = 0.009/2
            like_100_to_120 = 0.009/2
            like_120_to_140 = 0.0009/3
            like_140_to_160 = 0.0009/3
            like_160_to_180 = 0.0009/3
            like_180_to_200 = 0.00009/4
            like_200_to_220 = 0.00009/4
            like_220_to_240 = 0.00009/4
            like_240_to_260 = 0.00009/4
            like_260_to_280 =  0.00001/2
            like_280_to_300 =  0.00001/2
            sum_length_p_range = like_40_to_60 + like_60_to_80 + like_80_to_100 + like_100_to_120 + like_120_to_140 + like_140_to_160 + like_160_to_180 + like_180_to_200 + like_200_to_220 + like_220_to_240 + like_240_to_260 + like_260_to_280 + like_280_to_300
            dict["Length of prosoma by range [mm]"] = tmi_range
            dict["P(X | Length of prosoma by range [mm]_0.4-0.6)"] = like_40_to_60
            dict["P(X | Length of prosoma by range [mm]_0.6-0.8)"] = like_60_to_80
            dict["P(X | Length of prosoma by range [mm]_0.8-1.0)"] = like_80_to_100
            dict["P(X | Length of prosoma by range [mm]_1.0-1.2)"] = like_100_to_120
            dict["P(X | Length of prosoma by range [mm]_1.2-1.4)"] = like_120_to_140
            dict["P(X | Length of prosoma by range [mm]_1.4-1.6)"] = like_140_to_160
            dict["P(X | Length of prosoma by range [mm]_1.6-1.8)"] = like_160_to_180
            dict["P(X | Length of prosoma by range [mm]_1.8-2.0)"] = like_180_to_200
            dict["P(X | Length of prosoma by range [mm]_2.0-2.2)"] = like_200_to_220
            dict["P(X | Length of prosoma by range [mm]_2.2-2.4)"] = like_220_to_240
            dict["P(X | Length of prosoma by range [mm]_2.4-2.6)"] = like_240_to_260
            dict["P(X | Length of prosoma by range [mm]_2.6-2.8)"] = like_260_to_280
            dict["P(X | Length of prosoma by range [mm]_2.8-3.0)"] = like_280_to_300
            dict["Sum P(Length of prosoma by range [mm])"] = sum_length_p_range
        elif length_p_range == "0.6-0.8":
            like_40_to_60 = 0.045
            like_60_to_80 = 0.9
            like_80_to_100 = 0.045
            like_100_to_120 = 0.0045
            like_120_to_140 = 0.0045
            like_140_to_160 = 0.0003
            like_160_to_180 = 0.0003
            like_180_to_200 = 0.0003
            like_200_to_220 = 0.0000225 
            like_220_to_240 = 0.0000225
            like_240_to_260 = 0.0000225
            like_260_to_280 = 0.0000225
            like_280_to_300 =  0.00001
            sum_length_p_range = like_40_to_60 + like_60_to_80 + like_80_to_100 + like_100_to_120 + like_120_to_140 + like_140_to_160 + like_160_to_180 + like_180_to_200 + like_200_to_220 + like_220_to_240 + like_240_to_260 + like_260_to_280 + like_280_to_300
            dict["Length of prosoma by range [mm]"] = tmi_range
            dict["P(X | Length of prosoma by range [mm]_0.4-0.6)"] = like_40_to_60
            dict["P(X | Length of prosoma by range [mm]_0.6-0.8)"] = like_60_to_80
            dict["P(X | Length of prosoma by range [mm]_0.8-1.0)"] = like_80_to_100
            dict["P(X | Length of prosoma by range [mm]_1.0-1.2)"] = like_100_to_120
            dict["P(X | Length of prosoma by range [mm]_1.2-1.4)"] = like_120_to_140
            dict["P(X | Length of prosoma by range [mm]_1.4-1.6)"] = like_140_to_160
            dict["P(X | Length of prosoma by range [mm]_1.6-1.8)"] = like_160_to_180
            dict["P(X | Length of prosoma by range [mm]_1.8-2.0)"] = like_180_to_200
            dict["P(X | Length of prosoma by range [mm]_2.0-2.2)"] = like_200_to_220
            dict["P(X | Length of prosoma by range [mm]_2.2-2.4)"] = like_220_to_240
            dict["P(X | Length of prosoma by range [mm]_2.4-2.6)"] = like_240_to_260
            dict["P(X | Length of prosoma by range [mm]_2.6-2.8)"] = like_260_to_280
            dict["P(X | Length of prosoma by range [mm]_2.8-3.0)"] = like_280_to_300
            dict["Sum P(Length of prosoma by range [mm])"] = sum_length_p_range
        elif length_p_range == "0.8-1.0":
            like_40_to_60 = 0.0045
            like_120_to_140 = 0.0045
            like_60_to_80 = 0.045
            like_100_to_120 = 0.045
            like_80_to_100 = 0.9
            like_140_to_160 = 0.0003
            like_160_to_180 = 0.0003
            like_180_to_200 = 0.0003
            like_200_to_220 = 0.0000225
            like_220_to_240 = 0.0000225
            like_240_to_260 = 0.0000225
            like_260_to_280 = 0.0000225
            like_280_to_300 =  0.00001
            sum_length_p_range = like_40_to_60 + like_60_to_80 + like_80_to_100 + like_100_to_120 + like_120_to_140 + like_140_to_160 + like_160_to_180 + like_180_to_200 + like_200_to_220 + like_220_to_240 + like_240_to_260 + like_260_to_280 + like_280_to_300
            dict["Length of prosoma by range [mm]"] = tmi_range
            dict["P(X | Length of prosoma by range [mm]_0.4-0.6)"] = like_40_to_60
            dict["P(X | Length of prosoma by range [mm]_0.6-0.8)"] = like_60_to_80
            dict["P(X | Length of prosoma by range [mm]_0.8-1.0)"] = like_80_to_100
            dict["P(X | Length of prosoma by range [mm]_1.0-1.2)"] = like_100_to_120
            dict["P(X | Length of prosoma by range [mm]_1.2-1.4)"] = like_120_to_140
            dict["P(X | Length of prosoma by range [mm]_1.4-1.6)"] = like_140_to_160
            dict["P(X | Length of prosoma by range [mm]_1.6-1.8)"] = like_160_to_180
            dict["P(X | Length of prosoma by range [mm]_1.8-2.0)"] = like_180_to_200
            dict["P(X | Length of prosoma by range [mm]_2.0-2.2)"] = like_200_to_220
            dict["P(X | Length of prosoma by range [mm]_2.2-2.4)"] = like_220_to_240
            dict["P(X | Length of prosoma by range [mm]_2.4-2.6)"] = like_240_to_260
            dict["P(X | Length of prosoma by range [mm]_2.6-2.8)"] = like_260_to_280
            dict["P(X | Length of prosoma by range [mm]_2.8-3.0)"] = like_280_to_300
            dict["Sum P(Length of prosoma by range [mm])"] = sum_length_p_range
        elif length_p_range == "1.0-1.2":
            like_40_to_60 = 0.00045
            like_160_to_180 = 0.00045
            like_60_to_80 = 0.0045
            like_140_to_160 = 0.0045
            like_80_to_100 = 0.045
            like_120_to_140 = 0.045
            like_100_to_120 = 0.9
            like_180_to_200 = 0.00003
            like_200_to_220 = 0.00003
            like_220_to_240 = 0.00003
            like_240_to_260 = 0.00000225
            like_260_to_280 = 0.00000225
            like_280_to_300 =  0.000001
            sum_length_p_range = like_40_to_60 + like_60_to_80 + like_80_to_100 + like_100_to_120 + like_120_to_140 + like_140_to_160 + like_160_to_180 + like_180_to_200 + like_200_to_220 + like_220_to_240 + like_240_to_260 + like_260_to_280 + like_280_to_300
            dict["Length of prosoma by range [mm]"] = tmi_range
            dict["P(X | Length of prosoma by range [mm]_0.4-0.6)"] = like_40_to_60
            dict["P(X | Length of prosoma by range [mm]_0.6-0.8)"] = like_60_to_80
            dict["P(X | Length of prosoma by range [mm]_0.8-1.0)"] = like_80_to_100
            dict["P(X | Length of prosoma by range [mm]_1.0-1.2)"] = like_100_to_120
            dict["P(X | Length of prosoma by range [mm]_1.2-1.4)"] = like_120_to_140
            dict["P(X | Length of prosoma by range [mm]_1.4-1.6)"] = like_140_to_160
            dict["P(X | Length of prosoma by range [mm]_1.6-1.8)"] = like_160_to_180
            dict["P(X | Length of prosoma by range [mm]_1.8-2.0)"] = like_180_to_200
            dict["P(X | Length of prosoma by range [mm]_2.0-2.2)"] = like_200_to_220
            dict["P(X | Length of prosoma by range [mm]_2.2-2.4)"] = like_220_to_240
            dict["P(X | Length of prosoma by range [mm]_2.4-2.6)"] = like_240_to_260
            dict["P(X | Length of prosoma by range [mm]_2.6-2.8)"] = like_260_to_280
            dict["P(X | Length of prosoma by range [mm]_2.8-3.0)"] = like_280_to_300
            dict["Sum P(Length of prosoma by range [mm])"] = sum_length_p_range
        else:
            sum_length_p_range = like_40_to_60 + like_60_to_80 + like_80_to_100 + like_100_to_120 + like_120_to_140 + like_140_to_160 + like_160_to_180 + like_180_to_200 + like_200_to_220 + like_220_to_240 + like_240_to_260 + like_260_to_280 + like_280_to_300
            dict["Length of prosoma by range [mm]"] = tmi_range
            dict["P(X | Length of prosoma by range [mm]_0.4-0.6)"] = like_40_to_60
            dict["P(X | Length of prosoma by range [mm]_0.6-0.8)"] = like_60_to_80
            dict["P(X | Length of prosoma by range [mm]_0.8-1.0)"] = like_80_to_100
            dict["P(X | Length of prosoma by range [mm]_1.0-1.2)"] = like_100_to_120
            dict["P(X | Length of prosoma by range [mm]_1.2-1.4)"] = like_120_to_140
            dict["P(X | Length of prosoma by range [mm]_1.4-1.6)"] = like_140_to_160
            dict["P(X | Length of prosoma by range [mm]_1.6-1.8)"] = like_160_to_180
            dict["P(X | Length of prosoma by range [mm]_1.8-2.0)"] = like_180_to_200
            dict["P(X | Length of prosoma by range [mm]_2.0-2.2)"] = like_200_to_220
            dict["P(X | Length of prosoma by range [mm]_2.2-2.4)"] = like_220_to_240
            dict["P(X | Length of prosoma by range [mm]_2.4-2.6)"] = like_240_to_260
            dict["P(X | Length of prosoma by range [mm]_2.6-2.8)"] = like_260_to_280
            dict["P(X | Length of prosoma by range [mm]_2.8-3.0)"] = like_280_to_300
            dict["Sum P(Length of prosoma by range [mm])"] = sum_length_p_range
        
        samplelist.append(dict)
df = pd.DataFrame(samplelist)
df.to_csv("Output1531.csv", index=None)

print(df, "\n\n\n")
print(samplelist)
