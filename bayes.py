import csv
import traceback

#Contant strings - Following standards to name contants in all caps.
POSTERIOR = "Posterior"
SPECIES_NAME = "Species Name"

def get_all_spiders():
    with open("Output1531.csv", "r") as csvread:
        lines = csv.reader(csvread)
        headers = next(lines)
        samplelist = []
        for line in lines:
            dict = {}
            dict[headers[0]] = line[0]               # Species Name
            dict[headers[1]] = line[1]               # Sex
            dict[headers[2]] = float(line[2])        # P(X | Sex_Male)
            dict[headers[3]] = float(line[3])        # P(X | Sex_Female)
            #dict["Colour"] = colour
            prior = 1 / 1531
            dict["Prior"] =  prior # float(line[3])            
            dict[POSTERIOR] = prior
            # dict[headers[4]] = line[4]               Sum(P(Sex))
            dict[headers[5]] = line[5]               # Overall Appearance
            dict[headers[6]] = float(line[6])        # P(X | Overall Appearance_inconspicuous, generally dark)
            dict[headers[7]] = float(line[7])        # P(X | Overall Appearance_bright, red, orange)
            dict[headers[8]] = float(line[8])        # P(X | Overall Appearance_conspicuous contrast legs/prosoma)
            dict[headers[9]] = float(line[9])        # P(X | Overall Appearance_pale, ground or cave dweller)
            # dict[headers[10]] = line[10]             Sum of P(Overall Appearance)
            dict[headers[11]] = line[11]             # Length of femur I :<relative to prosoma>
            dict[headers[12]] = float(line[12])      # P(X | Length of femur I :&lt;relative to prosoma&gt;_equal in length)     
            dict[headers[13]] = float(line[13])      # P(X | Length of femur I :&lt;relative to prosoma&gt;_longer than prosoma)    
            dict[headers[14]] = float(line[14])      # P(X | Length of femur I :&lt;relative to prosoma&gt;_shorter than prosoma)
            #dict[headers[15]] = line[15]              Sum of P(Length of femur I :<relative to prosoma>)
            dict[headers[16]] = line[16]             # Prosoma <appearance>
            dict[headers[17]] = float(line[17])      # P(X | Prosoma <appearance>_inconspicuous))     
            dict[headers[18]] = float(line[18])      # P(X | Prosoma <appearance>_margins with teeth))    
            dict[headers[19]] = float(line[19])      # P(X | Prosoma <appearance>_with conspicuous hairs/spines))
            dict[headers[20]] = float(line[20])      # P(X | Prosoma <appearance>_with pits (dorsally))
            # dict[headers[21]] = float(line[21])      Sum of P(Prosoma <appearance>)
            dict[headers[22]] = line[22]             # Fovea as darkened groove    
            dict[headers[23]] = float(line[23])      # P(X | Fovea as darkened groove_yes)
            dict[headers[24]] = float(line[24])      # P(X | Fovea as darkened groove_no)
            # dict[headers[25]] = float(line[25])      Sum P(Fovea as darkened groove)
            dict[headers[26]] = line[26]             # Opisthosoma <appearance>
            dict[headers[27]] = float(line[27])      # P(X | Opisthosoma <appearance>_conspicuously hairy)     
            dict[headers[28]] = float(line[28])      # P(X | Opisthosoma <appearance>_patterned)  
            dict[headers[29]] = float(line[29])      # P(X | Opisthosoma <appearance>_unicolourous, inconspicuous)
            dict[headers[30]] = float(line[30])      # P(X | Opisthosoma <appearance>_with scutum)
            # dict[headers[31]] = float(line[31])      Sum of P(Opisthosoma <appearance>)
            dict[headers[32]] = line[32]             # Dorsal spines on femur I: <count>
            dict[headers[33]] = float(line[33])      # P(X | Dorsal spines on femur I: <count>_multiple) 
            dict[headers[34]] = float(line[34])      # P(X | Dorsal spines on femur I: <count>_none)
            dict[headers[35]] = float(line[35])      # P(X | Dorsal spines on femur I: <count>_one)
            # dict[headers[36]] = float(line[36])      Sum P(Dorsal spines on femur I: <count> )
            dict[headers[37]] = line[37]             # Posterior eye row: &lt;form&gt;
            dict[headers[38]] = float(line[38])      # P(X | Posterior eye row: <form>_procurved) 
            dict[headers[39]] = float(line[39])      # P(X | Posterior eye row: <form>_recurved)
            dict[headers[40]] = float(line[40])      # P(X | Posterior eye row: <form>_straight)
            # dict[headers[41]] = float(line[41])      Sum P(Posterior eye row: <form>)
            dict[headers[42]] = line[42]             # Posterior median eye (PME) separation: <relative to diameter (d)>
            dict[headers[43]] = float(line[43])      # P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly greater than d)
            dict[headers[44]] = float(line[44])      # P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly less than d)
            dict[headers[45]] = float(line[45])      # P(X | Posterior median eye (PME) separation: <relative to diameter (d)>_distinctly equal to d)
            # dict[headers[46]] = float(line[46])      Sum P(Posterior median eye (PME) separation: <relative to diameter (d)>)
            dict[headers[47]] = line[47]             # Headregion of male: <appearance>
            dict[headers[48]] = float(line[48])      # P(X | Headregion of male: <appearance>_complex)
            dict[headers[49]] = float(line[49])      # P(X | Headregion of male: <appearance>_inconspicuous)
            dict[headers[50]] = float(line[50])      # P(X | Headregion of male: <appearance>_sulci present)
            dict[headers[51]] = float(line[51])      # P(X | Headregion of male: <appearance>_with horns/tufts)
            dict[headers[52]] = float(line[52])      # P(X | Headregion of male: <appearance>_with lobe (simple))
            # dict[headers[53]] = float(line[53])      Sum P(Headregion of male: <appearance>)
            dict[headers[54]] = line[54]             # Eyes: <appearance>
            dict[headers[55]] = float(line[55])      # P(X | Eyes: <appearance>_normal)
            dict[headers[56]] = float(line[56])      # P(X | Eyes: <appearance>_reduced)
            # dict[headers[57]] = float(line[57])      Sum P(Eyes: <appearance>)
            dict[headers[58]] = line[58]             # Anterior median eyes: <size relative to anterior lateral eyes ALE>
            dict[headers[59]] = float(line[59])      # P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_about the same as ALE)
            dict[headers[60]] = float(line[60])      # P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly larger than ALE)
            dict[headers[61]] = float(line[61])      # P(X | Anterior median eyes: <size relative to anterior lateral eyes ALE>_distinctly smaller than ALE)
            # dict[headers[62]] = float(line[62])      Sum(Anterior median eyes: <size relative to anterior lateral eyes ALE>)
            dict[headers[63]] = line[63]             # Prolateral spines on femur I: <count>
            dict[headers[64]] = float(line[64])      # P(X | Prolateral spines on femur I: <count>_multiple)
            dict[headers[65]] = float(line[65])      # P(X | Prolateral spines on femur I: <count>_none)
            dict[headers[66]] = float(line[66])      # P(X | Prolateral spines on femur I: <count>_one)
            # dict[headers[67]] = float(line[671])      Sum P(Prolateral spines on femur I: <count> )
            dict[headers[68]] = line[68]             # Prolateral spines on tibia I: <count>
            dict[headers[69]] = float(line[69])      # P(X | Prolateral spines on tibia I: <count>_multiple)
            dict[headers[70]] = float(line[70])      # P(X | Prolateral spines on tibia I: <count>_none)
            dict[headers[71]] = float(line[71])      # P(X | Prolateral spines on tibia I: <count>_one)
            # dict[headers[72]] = float(line[72])      Sum P(Prolateral spines on tibia I: <count> )
            dict[headers[73]] = line[73]             # Anterior cheliceral teeth: <appearance>
            dict[headers[74]] = float(line[74])      # P(X | Anterior cheliceral teeth: <appearance>_conspicuously large)
            dict[headers[75]] = float(line[75])      # P(X | Anterior cheliceral teeth: <appearance>_unremarkable in size)
            # dict[headers[76]] = float(line[76])      Sum P(Anterior cheliceral teeth: <appearance>)
            dict[headers[77]] = line[77]             # Conspicuous structures on chelicerae: <appearance>
            dict[headers[78]] = float(line[78])      # P(X | Conspicuous structures on chelicerae: <appearance>_apophyses/teeth-like processes/tubercles)
            dict[headers[79]] = float(line[79])      # P(X | Conspicuous structures on chelicerae: <appearance>_none)
            dict[headers[80]] = float(line[80])      # P(X | Conspicuous structures on chelicerae: <appearance>_spines)           
            # dict[headers[81]] = float(line[81])      Sum P(Conspicuous structures on chelicerae: <appearance>)
            dict[headers[82]] = line[82]             # Maxillae: <appearance>
            dict[headers[83]] = float(line[83])      # P(X | Maxillae: <appearance>_one or more teeth/tubercles)            
            dict[headers[84]] = float(line[84])      # P(X | Maxillae: <appearance>_unremarkable)
            # dict[headers[85]] = float(line[85])      Sum P(Maxillae: <appearance>)
            dict[headers[86]] = line[86]             # Sternum: <appearance>
            dict[headers[87]] = float(line[87])      # P(X | Sternum: <appearance>_pitted)
            dict[headers[88]] = float(line[88])      # P(X | Sternum: <appearance>_rugose)
            dict[headers[89]] = float(line[89])      # P(X | Sternum: <appearance>_smooth)
            # dict[headers[90]] = float(line[90])      Sum P(Sternum: <appearance>)
            dict[headers[91]] = line[91]             # Sternum <It extends between coxae IV>
            dict[headers[92]] = float(line[92])      # P(X | Sternum <It extends between coxae IV>_yes)            
            dict[headers[93]] = float(line[93])      # P(X | Sternum <It extends between coxae IV>_no)
            # dict[headers[94]] = float(line[94])      Sum P(Sternum <It extends between coxae IV>)
            dict[headers[95]] = line[95]             # Width of sternum between coxae IV: <relative to width of coxae IV (d)>
            dict[headers[96]] = float(line[96])      # P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly greater than d)
            dict[headers[97]] = float(line[97])      # P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_distinctly less than d)
            dict[headers[98]] = float(line[98])      # P(X | Width of sternum between coxae IV: <relative to width of coxae IV (d)>_equal to d)
            # dict[headers[99]] = float(line[99])      Sum P(Width of sternum between coxae IV: <relative to width of coxae IV (d)>)
            dict[headers[100]] = line[100]             # tmi range
            dict[headers[101]] = float(line[101])      # 10-19
            dict[headers[102]] = float(line[102])      # 20-29
            dict[headers[103]] = float(line[103])      # 30-39
            dict[headers[104]] = float(line[104])      # 40-49
            dict[headers[105]] = float(line[105])      # 50-59
            dict[headers[106]] = float(line[106])      # 60-69          
            dict[headers[107]] = float(line[107])      # 70-79
            dict[headers[108]] = float(line[108])      # 80-89
            dict[headers[109]] = float(line[109])      # 90-98
            # dict[headers[110]] = float(line[110])      sum
            dict[headers[111]] = (line[111])      # metatarsus (TmIV)
            dict[headers[112]] = float(line[112])      # present    
            dict[headers[113]] = float(line[113])      # absent
            #dict[headers[114]] = float(line[114])       sum
            dict[headers[115]] = (line[115])      # Dorsal spines on metatarsus I: <count>
            dict[headers[116]] = float(line[116])      # multiple
            dict[headers[117]] = float(line[117])      # none
            dict[headers[118]] = float(line[118])      # one      
            # dict[headers[119]] = float(line[119])      sum
            dict[headers[120]] = (line[120])      # Tibia IV: <number of dorsal spines>
            dict[headers[121]] = float(line[121])      # one
            dict[headers[122]] = float(line[122])      # two
            # dict[headers[123]] = float(line[123])        sum
            dict[headers[124]] = (line[124])      # Numbers of dorsal spines on tibia I, II, III, IV: <tibial spine formula>         
            dict[headers[125]] = float(line[125])      # 0000
            dict[headers[126]] = float(line[126])      # 0011 
            dict[headers[127]] = float(line[127])      # 1111
            dict[headers[128]] = float(line[128])      # 2211 
            dict[headers[129]] = float(line[129])      # 2221
            dict[headers[130]] = float(line[130])      # 2222      
            # dict[headers[131]] = float(line[131])         sum
            dict[headers[132]] = (line[132])      # Tibia I-II ventrally: <presence of spines>
            dict[headers[133]] = float(line[133])      # no spines
            dict[headers[134]] = float(line[134])      # stout spines
            # dict[headers[135]] = float(line[135])       sum
            dict[headers[136]] = (line[136])      # Male pedipalp: femur <appearance>    
            dict[headers[137]] = float(line[137])      # unremarkable
            dict[headers[138]] = float(line[138])      # conspicuous
            # dict[headers[139]] = float(line[139])      sum


            dict[headers[140]] = (line[140])      #Male pedipalp patella <appearance>
            dict[headers[141]] = float(line[141])      # consp swollen
            dict[headers[142]] = float(line[142])      # unremarkable
            dict[headers[143]] = float(line[143])      # apophyses
            dict[headers[144]] = float(line[144])      # consp spines
            # dict[headers[145]] = float(line[145])       sum
            dict[headers[146]] = (line[146])      # Male pedipalp: tibia <appearance>
            dict[headers[147]] = float(line[147])      # unremar
            dict[headers[148]] = float(line[148])      # complex apophyses   
            dict[headers[149]] = float(line[149])      # multiple compl
            dict[headers[150]] = float(line[150])      # multiple simp
            dict[headers[151]] = float(line[151])      # one or more
            dict[headers[152]] = float(line[152])      # with simp
            dict[headers[153]] = float(line[153])      # tuft or hair
            # dict[headers[154]] = float(line[154])      sum    
            dict[headers[155]] = (line[155])           # Male pedipalp: cymbium <appearance>
            dict[headers[156]] = float(line[156])      #  margins
            dict[headers[157]] = float(line[157])      # simple
            dict[headers[158]] = float(line[158])      # conical ele
            # dict[headers[159]] = float(line[159])       sum
            dict[headers[160]] = (line[160])      # Male pedipalp: paracymbium <form>  
            dict[headers[161]] = float(line[161])      # complex
            dict[headers[162]] = float(line[162])      # simple
            # dict[headers[163]] = float(line[163])      sum
            dict[headers[164]] = (line[164])      # Male pedipalp: branches of paracymbium <presence of teeth>
            dict[headers[165]] = float(line[165])      # absent
            dict[headers[166]] = float(line[166])      # present    
            # dict[headers[167]] = float(line[167])       sum
            dict[headers[168]] = (line[168])      #Male pedipalp: embolus <appearance>
            dict[headers[169]] = float(line[169])      # consp, circ
            dict[headers[170]] = float(line[170])      # consp, curl
            dict[headers[171]] = float(line[171])      # unremark
            # dict[headers[172]] = float(line[172])       sum          
            dict[headers[173]] = (line[173])      # Male pedipalp: lamella characteristica <presence>
            dict[headers[174]] = float(line[174])      # absent
            dict[headers[175]] = float(line[175])      # consp
            # dict[headers[176]] = float(line[176])       sum
            dict[headers[177]] = (line[177])      # Female palp: claw <presence>
            dict[headers[178]] = float(line[178])      # consp      
            dict[headers[179]] = float(line[179])      # incons
            # dict[headers[180]] = float(line[180])       sum
            dict[headers[181]] = (line[181])      # epigyne appe
            dict[headers[182]] = float(line[182])      # unremar
            dict[headers[183]] = float(line[183])      # atrium
            dict[headers[184]] = float(line[184])      # septum 
            dict[headers[185]] = float(line[185])      # lateral   
            dict[headers[186]] = float(line[186])      # scape
            dict[headers[187]] = float(line[187])      # parmula
            # dict[headers[188]] = float(line[188])      sum
            dict[headers[189]] = (line[189])      # Epigyne: <form>
            dict[headers[190]] = float(line[190])      # flat
            dict[headers[191]] = float(line[191])      # protrudes
            # dict[headers[192]] = float(line[192])       sum
            dict[headers[193]] = (line[193])      # Epigyne: <seminal receptacles>
            dict[headers[194]] = float(line[194])      # visible
            dict[headers[195]] = float(line[195])      # not visible
            # dict[headers[196]] = float(line[196])      sum
            dict[headers[197]] = (line[197])      # Distribution
                                                       #  albania
            dict[headers[198]] = float(line[198])      # andora
            dict[headers[199]] = float(line[199])      # armenia
            dict[headers[200]] = float(line[200])      # austria
            dict[headers[201]] = float(line[201])      # azerbaijan
            dict[headers[202]] = float(line[202])      # belarus
            dict[headers[203]] = float(line[203])      # belgium
            dict[headers[204]] = float(line[204])      # bosnia
            dict[headers[205]] = float(line[205])      # bulgaria
            dict[headers[206]] = float(line[206])      # croatia
            dict[headers[207]] = float(line[207])      # cyprus
            dict[headers[208]] = float(line[208])      # czech
            dict[headers[209]] = float(line[209])      # denmark
            dict[headers[210]] = float(line[210])      # estonia
            dict[headers[211]] = float(line[211])      # faroe   
            dict[headers[212]] = float(line[212])      # finlan
            dict[headers[213]] = float(line[213])      # franc
            dict[headers[214]] = float(line[214])      # corsica france
            dict[headers[215]] = float(line[215])      # georgia
            dict[headers[216]] = float(line[216])      # germany
            dict[headers[217]] = float(line[217])      # gibraltar
            dict[headers[218]] = float(line[218])      # greece
            dict[headers[219]] = float(line[219])      # crete greece
            dict[headers[220]] = float(line[220])      # hunagry
            dict[headers[221]] = float(line[221])      #iceland
            dict[headers[222]] = float(line[222])      # ireland
            dict[headers[223]] = float(line[223])      # italy
            dict[headers[224]] = float(line[224])      # sardinia
            dict[headers[225]] = float(line[225])      # sicily
            dict[headers[226]] = float(line[226])      # kosovo
            dict[headers[227]] = float(line[227])      # latvia
            dict[headers[228]] = float(line[228])      # liehcteinsein
            dict[headers[229]] = float(line[229])      # lithuania
            dict[headers[230]] = float(line[230])      # luxembourg
            dict[headers[231]] = float(line[231])      # macedonia
            dict[headers[232]] = float(line[232])      # malta
            dict[headers[233]] = float(line[233])      # moltova
            dict[headers[234]] = float(line[234])      # montenegre
            dict[headers[235]] = float(line[235])      # netherlands  
            dict[headers[236]] = float(line[236])      # northern islands
            dict[headers[237]] = float(line[237])      # norway
            dict[headers[238]] = float(line[238])      # poland
            dict[headers[239]] = float(line[239])      # portugal
            dict[headers[240]] = float(line[240])      # romania
            dict[headers[241]] = float(line[241])      # rusia central
            dict[headers[242]] = float(line[242])      # rusia eastern
            dict[headers[243]] = float(line[243])      # rusia franz
            dict[headers[244]] = float(line[244])      # rusia kiliningrad
            dict[headers[245]] = float(line[245])      # rusia northern  
            dict[headers[246]] = float(line[246])      # rusia nowaya
            dict[headers[247]] = float(line[247])      # rusia southern
            dict[headers[248]] = float(line[248])      # rusia western
            dict[headers[249]] = float(line[249])      # serbia
            dict[headers[250]] = float(line[250])      # slovakia
            dict[headers[251]] = float(line[251])      # slovenia
            dict[headers[252]] = float(line[252])      # spain
            dict[headers[253]] = float(line[253])      # spain balaeric islands
            dict[headers[254]] = float(line[254])      # svalbard
            dict[headers[255]] = float(line[255])      # sweden
            dict[headers[256]] = float(line[256])      # switzerland
            dict[headers[257]] = float(line[257])      # turkey asia
            dict[headers[258]] = float(line[258])      # turkey europw
            dict[headers[259]] = float(line[259])      # ukraine
            dict[headers[260]] = float(line[260])      # UK
            dict[headers[261]] = float(line[261])
            


            samplelist.append(dict)

    print("OLD: ", samplelist)
    return samplelist

# def is_valid_characteristic(value):
    # print(value)
    # return hasattr(characteristics, value)

def calculate_posterior(listOfSpiders, key, value, priors): #prior needs to be a list of priors for all the species
    try:
        #print("male:", male,"female: ", female)

        # if(value != '' and  not is_valid_characteristic(value)):
            # print('Invalid Characteristic.')
            # return
        
        scaling_factor = 0

        # Key and value should be validated
        if key != "" and value != "":
            for sample in listOfSpiders:                
                if priors != None and sample[SPECIES_NAME] in priors.keys():
                    sample[POSTERIOR] = priors[sample[SPECIES_NAME]]
                else:
                    print(f"Prior Not found {sample[SPECIES_NAME]}") # this should not be printed
                posterior_probability = sample[POSTERIOR]
                scaling_factor = sample[POSTERIOR] * sample[f"P(X | {key}_{value})"] + scaling_factor
            for posterior in listOfSpiders:
                posterior_probability = posterior[POSTERIOR] * posterior[f"P(X | {key}_{value})"] / scaling_factor
                posterior[POSTERIOR] = posterior_probability

        # Selecting only properties which are required for the UI
        listOfSpiders = [{SPECIES_NAME: spider[SPECIES_NAME], POSTERIOR: spider[POSTERIOR]} for spider in listOfSpiders]
        listOfSpiders.sort(key = lambda x:x[POSTERIOR], reverse = True)
        return listOfSpiders
    except:
        traceback.print_exc() # for printing exception        
        raise Exception("Some Exception occured")
    
    
# Main program
if __name__ == "__main__":
    # Import argparse
    import argparse
    import pandas as pd
    import re

    # Create parser and add arguments
    parser = argparse.ArgumentParser(
        description='Calculate posterior probabilities of the species to check the highest probability of the species based')

    # Optional arguments
    parser.add_argument("-m", "--male", default= '',
                        help="Male")
    parser.add_argument("-f", "--female", default= '',
                        help="Female")
    parser.add_argument("-b", "--blank", default= '',
                        help="Female")
    #parser.add_argument("--red", default=" ",
    #                    help="Red")
    #parser.add_argument("--blue", default=" ",
    #                    help="Blue")
    #parser.add_argument("--purple", default=" ",
    #                    help="Purple")

    # Parse the arguments
    args = parser.parse_args()

    # Store user inputs in variables
    male = args.male
    female = args.female
    blanksex = args.blank
    #red = args.red
    #blue = args.blue
    #purple = args.purple

    # Import the database file

    spiders = get_all_spiders()

    # Parse the functions and get results based on User Input + Handling exceptions for invalid inputs
    if args.male and args.female: #or args.red and args.blue or args.red and args.purple or args.purple and args.blue:
        print("Please enter one of each sex and colour as argument.")
    elif args.male:
        calculate_posterior(spiders, characteristics.sex_male.name)
    elif args.female:
        calculate_posterior(spiders, characteristics.sex_female.name)
    else:
        print("Invalid Input. Please enter either 'mirna' or 'disease' as argument or 'h' for the help menu")

else:
    print("run as module\n")