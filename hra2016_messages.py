import json
import sys
#from bunch import *;
from infi.bunch import *;

sys.path.append('/opt/dreamfactory/storage/scripting/python/hra')
from common import *;
#import hra2016_calcengine ;


class ReportMessageVarsBase:
# This is BASE class which stores messages for use in report
# pass in record ( survey data and calculations )
# calculations module must be run first!!
   
    def __init__(self, record):
        
        self.errormsg = '';
        self.critical_error = 0;
        self.record = record ;
        self.messages = Bunch();  # this is a dictionary item 

    # function for TOPN 
    def setTopN(self, rankvarname, msgvar, msgid):
        # example:
        # topn = setTopN('sum_focus_28','alc', 99999)  
        message = self.messages;


        rankvar = message[rankvarname] ;
        topn = rankvar + 1 ;

        topNlist = rankvarname+'_list';
        msgvarname = rankvarname+'_'+msgvar ;
        msgvarrank = msgvarname+'_n'  # e.g., sum_focus_top3_alc_n 
        topNvar = rankvarname+'_'+str(topn);

        message[rankvarname] = topn ;
        message[topNvar] = msgid;
        message[msgvarname] = msgid ;
        message[msgvarrank] = topn;
        message[topNlist].append(msgvarname);


        return topn ;   

                
class ReportMessageVars2016(ReportMessageVarsBase):        
    def __init__(self, record):
        print('initialize ReportMessageVars2016 [v1.0]');
        # initialize parent class
        
        ReportMessageVarsBase.__init__(self,record)

        self.initializevars();
        self.calcmessages();
        
    def initializevars(self):
        message = self.messages;
        record = self.record ;
      
	
        message.sum_overview_msg = -1;
        message.sum_posmsg_tob = -1;
        message.sum_posmsg_paamount = -1;
        message.sum_posmsg_pastrength = -1;
        message.sum_posmsg_wgt = -1;
        message.sum_posmsg_bp = -1;
        message.sum_posmsg_stress = -1;
        message.sum_posmsg_alc = -1;
        message.sum_posmsg_chol = -1;
        message.sum_posmsg_outlook = -1;
        message.sum_posmsg_sbelt = -1;
        message.sum_posmsg_speed = -1;
        message.sum_posmsg_fibfood = -1;
        message.sum_posmsg_fatfood = -1;
        message.sum_posmsg_ps = -1;
        message.sum_posmsg_overhealth = -1;
        message.sum_posmsg_default = -1;
        message.sum_negmsg_tob = -1;
        message.sum_negmsg_paamount = -1;
        message.sum_negmsg_pastrength = -1;
        message.sum_negmsg_wgt = -1;
        message.sum_negmsg_bp = -1;
        message.sum_negmsg_stress = -1;
        message.sum_negmsg_alc = -1;
        message.sum_negmsg_chol = -1;
        message.sum_negmsg_drv = -1;
        message.sum_negmsg_chol = -1;
        message.sum_negmsg_gluc = -1;
        message.sum_negmsg_trig = -1;
        message.sum_negmsg_fibfood = -1;
        message.sum_negmsg_fatfood = -1;
        message.sum_negmsg_pslist = -1;
        message.sum_negmsg_overhealth = -1;
        message.sum_wellness_score = -1;
        message.sum_key_tobacco = -1;
        message.sum_key_physact = -1;
        message.sum_key_weightrange = -1;
        message.sum_key_bp = -1;
        message.sum_key_stress = -1;
        message.sum_key_alcoholuse = -1;
        message.sum_key_choltotal = -1;
        message.sum_key_drivehabit = -1;
        message.sum_key_illnessdays = -1;
        message.sum_key_nutrition = -1;
        message.sum_physreport = -1;
        message.sum_printreport = -1;
        message.lb_intro_msg = -1;
        message.lb_alcohol_pregnant = -1;
        message.lb_alcohol_msg = -1;
        message.lb_physact_pregnant = -1;
        message.lb_physact_msg = -1;
        message.lb_physact_sitting = -1;
        message.lb_safedriving_msg = -1;
        message.lb_safedriving_pregnant = -1;
        message.lb_tobacco_pregnant = -1;
        message.lb_tobacco_msg = -1;
        message.lb_weight_pregnant = -1;
        message.lb_weight_defaultweight = -1;
        message.lb_weight_msg = -1;
        message.mc_intro_msg = -1;
        message.mc_bp_msg = -1;
        message.mc_chol_msg = -1;
        message.mc_medhistory_disease = -1;
        message.mc_medhistory_condition = -1;
        message.mc_medhistory_bpcholonly = -1;
        message.mc_medhistory_default = -1;
        message.mc_medhistory_none = -1;
        message.mc_prevserv_bp = -1;
        message.mc_prevserv_chol = -1;
        message.mc_prevserv_mammogram = -1;
        message.mc_prevserv_cervicalca = -1;
        message.mc_prevserv_colonca = -1;
        message.mc_prevserv_tetanusshot = -1;
        message.mc_prevserv_flushot = -1;
        message.mc_overallhealth_pregnant = -1;
        message.mc_overallhealth_msg = -1;
        message.eh_intro_msg = -1;
        message.eh_lifesat_msg = -1;
        message.eh_stress_msg = -1;
        message.whatsnext_intro_msg = -1;
        message.whatsnext_summary_choice = -1;
        message.whatsnext_summary_keys = -1;
        message.whatsnext_summary_questions = -1;

        message.sum_focus_top3_alc = -1;
        message.sum_focus_top3_bp = -1;
        message.sum_focus_top3_cc = -1;
        message.sum_focus_top3_chol = -1;
        message.sum_focus_top3_drv = -1;
        message.sum_focus_top3_eat = -1;
        message.sum_focus_top3_gluc = -1;
        message.sum_focus_top3_lsat = -1;
        message.sum_focus_top3_mp = -1;
        message.sum_focus_top3_pa = -1;
        message.sum_focus_top3_sbelt = -1;
        message.sum_focus_top3_stress = -1;
        message.sum_focus_top3_tob = -1;
        message.sum_focus_top3_wgt = -1;
        message.sum_focus_top3_tob_2 = -1;
        message.sum_focus_top3_pa_2 = -1;
        message.sum_focus_top3_wgt_2 = -1;
        message.sum_focus_top3_bp_2 = -1;
        message.sum_focus_top3_stress_2 = -1;
        message.sum_focus_top3_chol_2 = -1;
        message.sum_focus_top3_pa_3 = -1;
        message.sum_focus_top3_wgt_3 = -1;
        message.sum_focus_top3_stress_3 = -1;
        
        message.whatsnext_top3_alc = -1;
        message.whatsnext_top3_bp = -1;
        message.whatsnext_top3_cc = -1;
        message.whatsnext_top3_chol = -1;
        message.whatsnext_top3_drv = -1;
        message.whatsnext_top3_eat = -1;
        message.whatsnext_top3_gluc = -1;
        message.whatsnext_top3_lsat = -1;
        message.whatsnext_top3_mp = -1;
        message.whatsnext_top3_pa = -1;
        message.whatsnext_top3_sbelt = -1;
        message.whatsnext_top3_stress = -1;
        message.whatsnext_top3_tob = -1;
        message.whatsnext_top3_wgt = -1;
        message.whatsnext_top3_tob_2 = -1;
        message.whatsnext_top3_pa_2 = -1;
        message.whatsnext_top3_pa_3 = -1;
        message.whatsnext_top3_wgt_2 = -1;
        message.whatsnext_top3_bp_2 = -1;
        message.whatsnext_top3_stress_2 = -1;
        message.whatsnext_top3_chol_2 = -1;
        message.whatsnext_top3_wgt_3 = -1;
        message.whatsnext_top3_stress_3 = -1;
        
        message.sum_focus_top3_alc_n = -1;
        message.sum_focus_top3_bp_n = -1;
        message.sum_focus_top3_cc_n = -1;
        message.sum_focus_top3_chol_n = -1;
        message.sum_focus_top3_drv_n = -1;
        message.sum_focus_top3_eat_n = -1;
        message.sum_focus_top3_gluc_n = -1;
        message.sum_focus_top3_lsat_n = -1;
        message.sum_focus_top3_mp_n = -1;
        message.sum_focus_top3_pa_n = -1;
        message.sum_focus_top3_sbelt_n = -1;
        message.sum_focus_top3_stress_n = -1;
        message.sum_focus_top3_tob_n = -1;
        message.sum_focus_top3_wgt_n = -1;
        message.sum_focus_top3_tob_2_n = -1;
        message.sum_focus_top3_pa_2_n = -1;
        message.sum_focus_top3_wgt_2_n = -1;
        message.sum_focus_top3_bp_2_n = -1;
        message.sum_focus_top3_stress_2_n = -1;
        message.sum_focus_top3_chol_2_n = -1;
        message.sum_focus_top3_pa_3_n = -1;
        message.sum_focus_top3_wgt_3_n = -1;
        message.sum_focus_top3_stress_3_n = -1;
        
        message.whatsnext_top3_alc_n = -1;
        message.whatsnext_top3_bp_n = -1;
        message.whatsnext_top3_cc_n = -1;
        message.whatsnext_top3_chol_n = -1;
        message.whatsnext_top3_drv_n = -1;
        message.whatsnext_top3_eat_n = -1;
        message.whatsnext_top3_gluc_n = -1;
        message.whatsnext_top3_lsat_n = -1;
        message.whatsnext_top3_mp_n = -1;
        message.whatsnext_top3_pa_n = -1;
        message.whatsnext_top3_sbelt_n = -1;
        message.whatsnext_top3_stress_n = -1;
        message.whatsnext_top3_tob_n = -1;
        message.whatsnext_top3_wgt_n = -1;
        message.whatsnext_top3_tob_2_n = -1;
        message.whatsnext_top3_pa_2_n = -1;
        message.whatsnext_top3_pa_3_n = -1;
        message.whatsnext_top3_wgt_2_n = -1;
        message.whatsnext_top3_bp_2_n = -1;
        message.whatsnext_top3_stress_2_n = -1;
        message.whatsnext_top3_chol_2_n = -1;
        message.whatsnext_top3_wgt_3_n = -1;
        message.whatsnext_top3_stress_3_n = -1;

        # special top3 variables
        message.sum_focus_top3 = 0 ;   # increment as top n are set
        message.whatsnext_top3 = 0  ; # increment as top n are set
        message.sum_focus_top3_list = [];
    
        message.sum_focus_top3_1 = -1;   # first message for sum_focus top3
        message.sum_focus_top3_2 = -1;   # 2nd message for sum_focus top3
        message.sum_focus_top3_3 = -1;   # 3rd message for sum_focus top3

        message.whatsnext_top3_list = [];
        message.whatsnext_top3_1 = -1;
        message.whatsnext_top3_2 = -1;
        message.whatsnext_top3_3 = -1;
        
        # example call setTopN function 
        # n = setTopN('sum_focus_top3',message.sum_focus_top3_alc , 99999)
        # n = setTopN('whatsnext_top3',message.whatsnext_top3_wgt_3, 99999)
        print('completed initialize message variables');
        
        #initialize key variables
        record.key_tobacco = -1;
        record.key_physact = -1;
        record.key_weightrange = -1;
        record.key_bp = -1;
        record.key_stress = -1;
        record.key_alcoholuse = -1;
        record.key_choltotal = -1;
        record.key_drivehabit = -1;
        record.key_illnessdays = -1;
        record.key_nutrition = -1;
        
        #initialize preventative service  variables
      
        record.psgl_bp = -1;
        record.psgl_chol = -1; 
        record.psgl_mammogram = -1;
        record.psgl_cervicalca = -1;
        record.psgl_colonca = -1;
        record.psgl_flushot = -1;
        record.psgl_tetanusshot = -1;

        print('completed record.psgl_ and record.key_ initialize...');


 
    def calcmessages(self):
        record = self.record;
        message = self.messages;
        print('calcmessages start...');

        # these are all the message calculation functions -->
        
        self.calcmess_sum_pos()
        self.calcmess_sum_neg()
        self.calcmess_focus_top_3()

        self.calcmess_wellness_score()
        self.calcmess_key_health_measures()
        self.calcmess_print_options()
        
        self.calcmess_lb_section()
        self.calcmess_mc_section()
        
        self.calcmess_ps_section()
        self.calcmess_mc_overallheath_section()

        self.calcmess_eh_section()
        self.calcmess_whatnext_section()
        
            
    # !! the following functions all called by calcmessages();
    ### if criteria met, message = n 
    def calcmess_sum_pos(self):
        record = self.record;
        message = self.messages;
        print('calcmess_sum_pos start...');

        msgcount = 0  # increment each time criteria met using msgcount += 1
        print('msgcount ',msgcount);
 
        # !!! Positive message section !!!
        # ((cigarette = never || former) && (other forms = none)) => message.sum_posmsg_tob =  102002
        try:
            if ( between(record.tob_cigssmokestatus,2,3) and record.tob_othernone == 1):
                message.sum_posmsg_tob = 102002;
                msgcount += 1 ;
                print(' (cigarette = never || former) && (other forms = none)) => message.sum_posmsg_tob = 102002');
               
        except:
            print('EXCEPTION for message.sum_posmsg_tob =  102002');

        # meets aerobic guideline (vigorous 75+) => message.sum_posmsg_paamount =  102003
        try:
            if record.calc_pa_vig >= 75:
                message.sum_posmsg_paamount = 102003;
                msgcount += 1 ;
        except:
            print('exception for calc_pa_vig...');

        # meets strength guideline (2+) => record.sum_posmsg_pastrength =  102004
        try:
            
            if record.physact_strengthfreq >= 2:
                message.sum_posmsg_pastrength = 102004;
                msgcount += 1 ;
        except:
            print('EXCEPTION for message.sum_posmsg_pastrength');

        # bmi = 18.5-24.9 => message.sum_posmsg_wgt =  102005
        # Meds/Care = Controlled => message.sum_posmsg_bp =  102006
        # hrec.sbp < 120 and hrec.dbp < 80 => message.sum_posmsg_bp =  102007
        # hrec.stress_score<21 and nvl(hrec.feel_stress,0)>1 and nvl(hrec.stress_effect,0)>1 => message.sum_posmsg_stress =  102008
        # hrec.alcohol_weekly = 0 => message.sum_posmsg_alc =  102009
        # hrec.sex=1 and hrec.alcohol_weekly > 0 & < 8 or hrec.sex=2 and hrec.alcohol_weekly > 0 & <4 => message.sum_posmsg_alc =  102010
        # hrec.cholesterol between 21 and 199 => message.sum_posmsg_chol =  102011
        # hrec.high_chol_meds=1 or hrec.high_chol_care=1 => message.sum_posmsg_chol =  102012
        # hrec.life_satis in (1,2) => message.sum_posmsg_outlook =  102013
        # hrec.use_stbt = 1 => message.sum_posmsg_sbelt =  102014
        # hrec.drive_speed = 1 => message.sum_posmsg_speed =  102015
        # fiber = 5+ servings => message.sum_posmsg_fibfood =  102016
        # fat <=2 servings => message.sum_posmsg_fatfood =  102017
        # compliant with all screenings => message.sum_posmsg_ps =  102018
        # overall health = excellent|verygood|good => message.sum_posmsg_overhealth =  102019

        # IF NONE OF THE ABOVE ARE TRUE, USE DEFAULT MESSAGE
        #  => message.sum_posmsg_default =  102020
        if msgcount == 0:
            message.sum_posmsg_default =  102020

        
    def calcmess_sum_neg(self):
        record = self.record;
        message = self.messages;
        print('calcmess_sum_pos start...');
        msgcount = 0  # increment each time criteria met using msgcount += 1

        # !!! Negative message section !!!
        
        # currently smoke cigarettes  => message.sum_negmsg_tob =  102021
        # other = e-cigs => message.sum_negmsg_tob =  102022
        # other = chew => message.sum_negmsg_tob =  102023
        # other = cigar => message.sum_negmsg_tob =  102024
        # other = pipe => message.sum_negmsg_tob =  102025
        # vigorous PA = 25-74 => message.sum_negmsg_paamount =  102026
        # vigorous PA < 25 => message.sum_negmsg_paamount =  102027
        # strength = 1 => message.sum_negmsg_pastrength =  102028
        # strength = 0  => message.sum_negmsg_pastrength =  102029
        # <18.5  => message.sum_negmsg_wgt =  102030
        # >=25 & <30 => message.sum_negmsg_wgt =  102031
        # >=30 => message.sum_negmsg_wgt =  102032
        # >=140/90 & on meds => message.sum_negmsg_bp =  102033
        # >=140/90 & care => message.sum_negmsg_bp =  102034
        # sbp >= 120  or  dbp >= 80 => message.sum_negmsg_bp =  102035
        # (self-report high) => message.sum_negmsg_bp =  102036
        # (hrec.sbp = 0 or hrec.sbp is null) and (hrec.dbp = 0 or hrec.dbp is null) and nvl(hrec.high_bp_when,1) in (1,2) => message.sum_negmsg_bp =  102037
        # stress score > 20 => message.sum_negmsg_stress =  102038
        # feel stress = 1 => message.sum_negmsg_stress =  102039
        # stress effect = 1 => message.sum_negmsg_stress =  102040
        # nvl(hrec.sex,1)=1 and hrec.alcohol_weekly between 15 and 28 => message.sum_negmsg_alc =  102041
        # (male > 65 || female ) and hrec.alcohol_weekly between 8 and 21 => message.sum_negmsg_alc =  102042
        # hrec.alcohol_weekly > 28 or (hrec.alcohol_weekly>21 and (female || male > 65)) => message.sum_negmsg_alc =  102043
        # chol>239 => message.sum_negmsg_chol =  102044
        # chol = 200-239 => message.sum_negmsg_chol =  102045
        # nvl(hrec.cholesterol,0)<21 and hrec.high_chol_when=3 => message.sum_negmsg_chol =  102046
        #  => message.sum_negmsg_chol =  102047
        # hrec.use_stbt > 1  or hrec.use_stbt is null => message.sum_negmsg_drv =  102048
        # hrec.drive_speed >= 3 => message.sum_negmsg_drv =  102049
        # hrec.hdl>hrec.cholesterol and hrec.cholesterol>0 => message.sum_negmsg_chol =  102050
        # glucose = bad => message.sum_negmsg_gluc =  102051
        # triglyceride = bad => message.sum_negmsg_trig =  102052
        # fiber = 3-4 => message.sum_negmsg_fibfood =  102053
        # fiber = 0-2 => message.sum_negmsg_fibfood =  102054
        # fatty = 3-4 => message.sum_negmsg_fatfood =  102055
        # fatty = 5+ => message.sum_negmsg_fatfood =  102056
        #  => message.sum_negmsg_pslist =  102057
        # hrec.physical_health in (4,5) => message.sum_negmsg_overhealth =  102058

        
        

    def calcmess_focus_top_3(self):
        record = self.record;
        message = self.messages;
        print('calcmess_sum_pos start...');

        # !!! Focus_Top_3 Section !!!

        # special top3 variables --->
        # message.sum_focus_top3 = 0 ;   # increment as top n are set
        # message.whatsnext_top3 = 0  ; # increment as top n are set
        # message.sum_focus_top3_1 = -1;   # first message for sum_focus top3
        # message.sum_focus_top3_2 = -1;   # 2nd message for sum_focus top3
        # message.sum_focus_top3_3 = -1;   # 3rd message for sum_focus top3
        
        # message.whatsnext_top3_1 = -1;
        # message.whatsnext_top3_2 = -1;
        # message.whatsnext_top3_3 = -1;
        
        # NOTE for section:
        ## Trigerring risks are outcomes of TMS
        ## Alcohol/Smoking -no further tailoring
        ## Weight- 2nd level message can be controlled outside of TMS. So, you can tailor the message for overweight vs underweight. 
        ## This is NOT  intended to change the framework from existing 2014 engine for top3, allowing beyond TMS maked list within the same level

        # START CODE HERE:
        
        # Risk: MedicalProb, Improve  Notes: any of these 5 (heart, cancer, diabetes, stroke, emphysema) Topic: MP =>
        # topn = setFocusTop3(message.sum_focus_top3_mp, message.sum_focus_top3_mp_n, 102061);

        ### TEST setTopN
        topn = self.setTopN('sum_focus_top3','mp', 102061)  ;
        print ('topn (current rank) ' ,topn)
        print ('sum_focus_top3_mp (message id): ' , message.sum_focus_top3_mp);
        print ('sum_focus_top3_mp_n (rank): ' , message.sum_focus_top3_mp_n);
        print ('sum_focus_top3_list: ' , message.sum_focus_top3_list);
        print ('sum_focus_top3_list[topn-1] ', message.sum_focus_top3_list[topn-1] );

        # these are the equivalent whatsnext variables

        #  =>  topn = setTopN('whatsnext_top3','mp',124434);
        #  =>  topn = setTopN('whatsnext_top3','tob',124435);
        #  =>  topn = setTopN('whatsnext_top3','pa',124436);
        #  =>  topn = setTopN('whatsnext_top3','wgt',124437);
        #  =>  topn = setTopN('whatsnext_top3','bp',124438);
        #  =>  topn = setTopN('whatsnext_top3','stress',124439);
        #  =>  topn = setTopN('whatsnext_top3','alc',124440);
        #  =>  topn = setTopN('whatsnext_top3','chol',124441);
        #  =>  topn = setTopN('whatsnext_top3','lsat',124442);
        #  =>  topn = setTopN('whatsnext_top3','sbelt',124443);
        #  =>  topn = setTopN('whatsnext_top3','gluc',124444);
        #  =>  topn = setTopN('whatsnext_top3','chol',124445);
        #  =>  topn = setTopN('whatsnext_top3','cc',124446);
        #  =>  topn = setTopN('whatsnext_top3','tob_2',124447);
        #  =>  topn = setTopN('whatsnext_top3','pa_2',124448);
        #  =>  topn = setTopN('whatsnext_top3','pa_3',124449);
        #  =>  topn = setTopN('whatsnext_top3','wgt_2',124450);
        #  =>  topn = setTopN('whatsnext_top3','bp_2',124451);
        #  =>  topn = setTopN('whatsnext_top3','stress_2',124452);
        #  =>  topn = setTopN('whatsnext_top3','chol_2',124453);
        #  =>  topn = setTopN('whatsnext_top3','drv',124454);
        #  =>  topn = setTopN('whatsnext_top3','eat',124455);
        #  =>  topn = setTopN('whatsnext_top3','pa_3',124456);
        #  =>  topn = setTopN('whatsnext_top3','wgt_3',124457);
        #  =>  topn = setTopN('whatsnext_top3','stress_3',124458);
        
        # Risk: MedicalProb: Improve  Notes: any of these 5 (heart, cancer, diabetes, stroke, emphysema) Topic: MP =>  topn = setTopN('sum_focus_top3','mp',102061);
        if record.ndiseases > 0:
            topn = setTopN('sum_focus_top3','mp', 102061)  ;
            setTopN('whatsnext_top3','mp', 124434);

        # Risk: Tobacco: Improve  Notes:  Topic: TOB =>  topn = setTopN('sum_focus_top3','tob',102062);
        # Risk: PhysicalAct: Improve  Notes: <25 mins vigorous Topic: PA =>  topn = setTopN('sum_focus_top3','pa',102063);
        # Risk: Weight: Improve  Notes: >=27.5 BMI Topic: WGT =>  topn = setTopN('sum_focus_top3','wgt',102064);
        # Risk: BP: Improve  Notes: SBP>139 || DBP>89 || BPMeds || BPCare || self-report HTN Topic: BP =>  topn = setTopN('sum_focus_top3','bp',102065);
        # Risk: Stress: Improve  Notes: score >20 || TensAnxDep = Often || StressAffectHealth = A lot Topic: STRESS =>  topn = setTopN('sum_focus_top3','stress',102066);
        # Risk: Alcohol: Improve  Notes:  Topic: ALC =>  topn = setTopN('sum_focus_top3','alc',102067);
        # Risk: AlcoholUse >7: Improve  Notes:  Topic: ALC =>  topn = setTopN('sum_focus_top3','alc',102068);
        # Risk: Cholesterol: Improve  Notes: TC >239 Topic: CHOL =>  topn = setTopN('sum_focus_top3','chol',102069);
        # Risk: LifeSat: Improve  Notes: partly sat || not sat Topic: LSAT =>  topn = setTopN('sum_focus_top3','lsat',102070);
        # Risk: SafetyBelt: Improve  Notes: <100% use Topic: SBELT =>  topn = setTopN('sum_focus_top3','sbelt',102071);
        # Risk: BloodGlucose: ImproveIntermediate  Notes: fasting >=110 || non-fasting >=140 Topic: GLUC =>  topn = setTopN('sum_focus_top3','gluc',102072);
        # Risk: Tryglyceride: ImproveIntermediate  Notes: >150 Topic: CHOL =>  topn = setTopN('sum_focus_top3','chol',102073);
        # Risk: ChronicCondition: ImproveSecondary  Notes: any other chronic condition = current (that's not in the 5 above) Topic: CC =>  topn = setTopN('sum_focus_top3','cc',102074);
        # Risk: Tobacco: ImproveSecondary  Notes: e-cig Topic: TOB_2 =>  topn = setTopN('sum_focus_top3','tob_2',102075);
        # Risk: PhysicalAct: ImproveSecondary  Notes: strength <2 || 25-74 vigorous minutes Topic: PA_2 =>  topn = setTopN('sum_focus_top3','pa_2',102076);
        # Risk: Weight: ImproveSecondary  Notes: >=25 Topic: WGT_2 =>  topn = setTopN('sum_focus_top3','wgt_2',102077);
        # Risk: Weight: ImproveSecondary  Notes: <18.5 BMI Topic: WGT_2 =>  topn = setTopN('sum_focus_top3','wgt_2',102078);
        # Risk: BP: ImproveSecondary  Notes: SBP 120-139 ||DBP 80-89 Topic: BP_2 =>  topn = setTopN('sum_focus_top3','bp_2',102079);
        # Risk: Stress: ImproveSecondary  Notes: stress score >15 && feel 2,3,4,missing && effect 2,3, missing Topic: STRESS_2 =>  topn = setTopN('sum_focus_top3','stress_2',102080);
        # Risk: Cholesterol: ImproveSecondary  Notes: TC 200-239 || OnMeds || self-report high Topic: CHOL_2 =>  topn = setTopN('sum_focus_top3','chol_2',102081);
        # Risk: Safe Driving: ImproveSecondary  Notes: Drive or ride drunk > 0; or Speed = 6-10 over || 11+ over Topic: DRV =>  topn = setTopN('sum_focus_top3','drv',102082);
        # Risk: Nutrition: ImproveSecondary  Notes: Fiber = 1-2 servings || Rarely or never; or Fat = 5+ servings Topic: EAT =>  topn = setTopN('sum_focus_top3','eat',102083);
        # Risk: PhysicalAct: Maintain  Notes: default Topic: PA_3 =>  topn = setTopN('sum_focus_top3','pa_3',102084);
        # Risk: Weight: Maintain  Notes: default Topic: WGT_3 =>  topn = setTopN('sum_focus_top3','wgt_3',102085);
        # Risk: Stress: Maintain  Notes: default Topic: STRESS_3 =>  topn = setTopN('sum_focus_top3','stress_3',102086);


    def calcmess_wellness_score(self):
        record = self.record;
        message = self.messages;
        print('calcmess_sum_pos start...');


        try:
            #Wellness score 50-64
            if between(record.calc_wellness_score,50,64):
                message.sum_wellness =  102087;
            #65-74
            if between(record.calc_wellness_score,65,74):
                message.sum_wellness =  102088;

            #75-84
            if between(record.calc_wellness_score,75,84):
                message.sum_wellness =  102089;

            #85-94
            if between(record.calc_wellness_score,85,94):
                message.sum_wellness =  102090;
            
            #95-100
            if between(record.calc_wellness_score,85,94):
                message.sum_wellness =  102091;
        except:
            print('message.sum_wellness exception');

    def calcmess_key_health_measures(self):
        record = self.record;
        message = self.messages;
        print('calcmess_key start...');

      
        # !! key variables
        # coding for risk
        #  1=low 2=moderate 3=high  -9= don't know

        # Label: Not-current User Criteria: Non-smoker || Former Smoker => record.key_tobacco = 1
        # Label: E-cig User Criteria: E-cigarette => record.key_tobacco = 2
        # Label: Current User Criteria: Cigarette || Pipe || Cigar || Smokeless => record.key_tobacco = 3
        # Use "data not available" label or "?" icon if none of other forms of tobacco
        # but didn't answer the cigarette use || all tobacco responses are missing (cigarette & other forms) => record.key_tobacco = -9

        # !! Use total physical activity minutes (converted to vigorous)
        #   Total physical activity minutes = (vigorous frequency per week x minutes per vigorous session)
        #   + ((moderate frequency per week x minutes per moderate session) /2)
        # Label: Actual number Criteria: >74 minutes/week  => record.key_physact = 1
        # Label: Actual number Criteria: 25-74 minutes/week  => record.key_physact = 2
        # Label: Actual number Criteria: <25 minutes/week  => record.key_physact = 3
        # If missing both times per week, then put "data not available" label or "?" icon. => record.key_physact = -9

        # Label: Actual numbers (weight range and BMI) Criteria: >= 18.5 and < 25 => record.key_weightrange = 1
        # Label: Actual numbers (weight range and BMI) Criteria: 25-29.9 => record.key_weightrange = 2
        # Label: Actual numbers (weight range and BMI) Criteria: <18.5 || 30+ => record.key_weightrange = 3
        # Use "data not available" label or "?" icon if BMI cannot be calculated => record.key_weightrange = -9

        # !! This follows a hierarchy -- the label/flag will be placed at the highest risk they qualify for. 
        # !! (Example: SBP = 120 && DBP = 78; then put in Moderate Risk category.)
        # !! If missing 1 number, they can still be placed in Moderate or High Risk categories (but not Low Risk). 
        # !! If missing both numbers, and self-report = high, then put in High Risk category. 
        # !! Self-reported HBP is  considered high risk ONLY if missing both numbers.
        # !! (This is new for v1.5 -- previously, High based only on numbers, medication/care was a separate category.) 

        # Label: Actual number Criteria: SBP <120  && DBP <80 => record.key_bp = 1
        # Label: Actual number= Criteria: (SBP >= 120 and < 140) || (DBP  >= 80 and <90 )  => record.key_bp = 2
        # Label: Actual number Criteria: SBP >= 140 || DBP >= 90 Label: High Criteria: Self-report high => record.key_bp = 3
        # If missing both numbers and did not self-report high, then put  ""data not available"" label or ""?"" icon => record.key_bp = -9

        # !! This follows a hierarchy -- the label/flag will be placed at the highest risk they qualify for. Each row is an || statement to the row above it.
        # !! (Example: StressScore = 17 and also answered StressAffectHealth = A lot; then put in High Risk category.)
        # !! If 1 of the 3 data points is missing, put indicator at the higher of the 2 categories.

        # Label: Low Criteria: Stress score <18 Criteria: StressAffectHealth = Hardly any || None Criteria: TenseAnxiousDepressed = Rarely || Never => record.key_stress = 1
        # Label: Moderate  Criteria: Stress score = 18-20 Criteria: StressAffectHealth - Some Criteria: TenseAnxiousDepressed = Sometimes => record.key_stress = 2
        # Label: High Criteria: Stress score >20 Criteria: StressAffectHealth = A lot  Criteria: TenseAnxiousDepressed = Often => record.key_stress = 3
        # If 2  of the 3 data points are missing, then put ""data not available"" label. => record.key_stress = -9

        # !! AGE 16 to 65 and MALE
        # Label: Actual number Criteria: <15 drinks per week => record.key_alcoholuse = 1
        # N/A => record.key_alcoholuse = 2
        # Label: Actual number  Criteria: More than 14 per week => record.key_alcoholuse = 3
        # If missing, then put "data not available" label or "?" icon. => record.key_alcoholuse = -9

        # !!  AGE > 65 and MALE
        # Label: Actual number Criteria: <8 drinks per week => record.key_alcoholuse = 1
        # N/A => record.key_alcoholuse = 2
        # Label: Actual number Criteria: More than 7 per week => record.key_alcoholuse = 3
        # If missing, then put "data not available" label or "?" icon. => record.key_alcoholuse = -9

        # !! AGE - all and FEMALE
        # Label: Actual number Criteria: <8 drinks per week => record.key_alcoholuse = 1
        # Label: Actual number Criteria: More than 7 per week => record.key_alcoholuse = 3

        # !! Self-reported HighChol is considered high risk ONLY if numbers are missing. (record.mdc_hichol = 3)
        # Label: Actual number Criteria: < 200 mg/dL => record.key_choltotal = 1
        # Label: Actual number Criteria: >= 200  and < 240  => record.key_choltotal = 2
        # Label: Actual number Criteria: >= 240 mg/dL  Label: High  Criteria: Self-report high => record.key_choltotal = 3
        # If missing numbers and did not self-report high, then put ""data not available"" label. => record.key_choltotal = -9

        # !! If you meet 1 of the 3 criteria for high risk, you're high risk.
        # !! To be low risk, you must meet all 3 criteria.
        # Label: Safe Criteria: (seatbelt = 100%)   && (drunk drive = 0) && (speed = within 5 miles) => record.key_drivehabit = 1
        # n/a => record.key_drivehabit = 2
        # Label: Risky Criteria: (seatbelt = <80 || 80-89 || 90-99)  OR (drunk drive = 1+) OR (speed = 6+ miles over) => record.key_drivehabit = 3
        # If you are low risk in 1-2 criteria, but 2-3 are missing, then put ""data not available"" label. => record.key_drivehabit = -9
        # !! This is the general illness days question applicable to everyone, not the work-specific one. 
        # Label: Actual range Criteria: <6 days per year => record.key_illnessdays = 1
        # N/A => record.key_illnessdays = 2
        # Label: Actual range Criteria: 6 days or more per year => record.key_illnessdays = 3
        # If missing, then put ""data not available"" label. => record.key_illnessdays = -9

        # !! This is a combined score that follows a hierarchy -- the label/flag will be placed at the highest risk they qualify for. 
        # !! (Example: if Fat = 6 && Fiber = 6; then put in High Risk category)
        # !! If at least 1 is high, then high.
        # !! If one is missing, put indicator in the category we do know.

        # < 3 servings per day >= 5 servings per day Label: Good ? Criteria: (low & low) || (low & missing) => record.key_nutrition = 1
        # 3-4 servings per day 3-4 servings per day Label: So-So ?
        #     Criteria (exchangeably): (mod & mod) || (mod & low) || (mod & missing) => record.key_nutrition = 2
        #  5 servings per day < 3 servings per day Label: Needs Work ? Criteria (exchangeably):
        #     (high & high) || (high & mod) || (high & low) || (high & missing) => record.key_nutrition = 3
        # If both are missing, then put ""data not available"" label. => record.key_nutrition = -9


    def calcmess_print_options(self):
        record = self.record;
        message = self.messages;
        print('calcmess_print_options start...');


        #  print messages
        #  => message.sum_physreport_msg =  102106
        message.sum_physreport_msg =  102106
        #  => message.sum_printreport_msg =  102107
        message.sum_printreport_msg =  102107

    def calcmess_lb_section(self):
        record = self.record;
        message = self.messages;
        # !! LIFESTYLE BEHAVIORS SECTION lb  (health behaviors)
        print('calcmess_lb_section start...');


        # !! NOTES: Use these variables and coding
        # !!  Planning variable coding from survey
        # 1	Yes
        # 2	No
        # 3	I don't know
        # 4	Not needed
        # !! variable names
        # record.plan_physact
        # record.plan_weight
        # record.plan_alcohol
        # record.plan_tobacco
        # record.plan_nutrfatchol
        # record.plan_bp
        # record.plan_chol
        # record.plan_stress
        # !! Demographic survey variables
        # record.demo_gender   1 = male, 2= female
        # record.demo_pregnant  1 = yes
        # record.demo_age  


        # !! INTRO PAGE
        #  => message.lb_intro_msg =  103108
        message.lb_intro_msg =  103108

        # !! subfunctions for each topic ->
        # calcmess_lb_alcohol();
        # calcmess_lb_physact();
        # calcmess_lb_safedriving();
        # calcmess_lb_tobacco();
        # calcmess_lb_weight()


        def calcmess_lb_alcohol():
            print('SUB FUNCTION calcmess_lb_alchol start...');
            # !! ALCOHOL PAGE
            # Gender: , Age: , Risk: , Planning:  => message.lb_alcohol_pregnant =  103109

            # !! use record.plan_alcohol , record.key_alcoholuse
            # Gender: Male, Age: 16-20, Risk: High, Planning: Yes => message.lb_alcohol_msg =  103110
            # Gender: Male, Age: 16-20, Risk: High, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103111
            # Gender: Female, Age: 16-20, Risk: High, Planning: Yes => message.lb_alcohol_msg =  103112
            # Gender: Female, Age: 16-20, Risk: High, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103113
            # Gender: Male, Age: 21-65, Risk: High, Planning: Yes => message.lb_alcohol_msg =  103114
            # Gender: Male, Age: 21-65, Risk: High, Planning: No => message.lb_alcohol_msg =  103115
            # Gender: Male, Age: 21-65, Risk: High, Planning: DontKnow  Null => message.lb_alcohol_msg =  103116
            # Gender: Male, Age: 21-65, Risk: High, Planning: NotNeeded => message.lb_alcohol_msg =  103117
            # Gender: Female, Age: 21+, Risk: High, Planning: Yes => message.lb_alcohol_msg =  103118
            # Gender: Female, Age: 21+, Risk: High, Planning: No => message.lb_alcohol_msg =  103119
            # Gender: Female, Age: 21+, Risk: High, Planning: DontKnow  Null => message.lb_alcohol_msg =  103120
            # Gender: Female, Age: 21+, Risk: High, Planning: NotNeeded => message.lb_alcohol_msg =  103121
            # Gender: Male, Age: 66+, Risk: High, Planning: Yes => message.lb_alcohol_msg =  103122
            # Gender: Male, Age: 66+, Risk: High, Planning: No => message.lb_alcohol_msg =  103123
            # Gender: Male, Age: 66+, Risk: High, Planning: DontKnow  Null => message.lb_alcohol_msg =  103124
            # Gender: Male, Age: 66+, Risk: High, Planning: NotNeeded => message.lb_alcohol_msg =  103125
            # Gender: Male, Age: 16-20, Risk: Low, Planning: Yes => message.lb_alcohol_msg =  103126
            # Gender: Male, Age: 16-20, Risk: Low, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103127
            # Gender: Female, Age: 16-20, Risk: Low, Planning: Yes => message.lb_alcohol_msg =  103128
            # Gender: Female, Age: 16-20, Risk: Low, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103129
            # Gender: Male, Age: 21-65, Risk: Low, Planning: Yes => message.lb_alcohol_msg =  103130
            # Gender: Male, Age: 21-65, Risk: Low, Planning: No => message.lb_alcohol_msg =  103131
            # Gender: Male, Age: 21-65, Risk: Low, Planning: DontKnow  Null => message.lb_alcohol_msg =  103132
            # Gender: Male, Age: 21-65, Risk: Low, Planning: NotNeeded => message.lb_alcohol_msg =  103133
            # Gender: Female, Age: 21+, Risk: Low, Planning: Yes => message.lb_alcohol_msg =  103134
            # Gender: Female, Age: 21+, Risk: Low, Planning: No => message.lb_alcohol_msg =  103135
            # Gender: Female, Age: 21+, Risk: Low, Planning: DontKnow  Null => message.lb_alcohol_msg =  103136
            # Gender: Female, Age: 21+, Risk: Low, Planning: NotNeeded => message.lb_alcohol_msg =  103137
            # Gender: Male, Age: 66+, Risk: Low, Planning: Yes => message.lb_alcohol_msg =  103138
            # Gender: Male, Age: 66+, Risk: Low, Planning: No => message.lb_alcohol_msg =  103139
            # Gender: Male, Age: 66+, Risk: Low, Planning: DontKnow  Null => message.lb_alcohol_msg =  103140
            # Gender: Male, Age: 66+, Risk: Low, Planning: NotNeeded => message.lb_alcohol_msg =  103141
            # Gender: Male, Age: 16-20, Risk: Abstain, Planning: Yes  No  DontKnow  NotNeeded  Null => message.lb_alcohol_msg =  103142
            # Gender: Female, Age: 16-20, Risk: Abstain, Planning: Yes  No  DontKnow  NotNeeded  Null => message.lb_alcohol_msg =  103143
            # Gender: Male, Age: 21-65, Risk: Abstain, Planning: Yes  No  DontKnow  NotNeeded  Null => message.lb_alcohol_msg =  103144
            # Gender: Female, Age: 21+, Risk: Abstain, Planning: Yes  No  DontKnow  NotNeeded  Null => message.lb_alcohol_msg =  103145
            # Gender: Male, Age: 66+, Risk: Abstain, Planning: Yes  No  DontKnow  NotNeeded  Null => message.lb_alcohol_msg =  103146
            # Gender: Male, Age: 16-20, Risk: Unknown, Planning: Yes => message.lb_alcohol_msg =  103147
            # Gender: Male, Age: 16-20, Risk: Unknown, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103148
            # Gender: Female, Age: 16-20, Risk: Unknown, Planning: Yes => message.lb_alcohol_msg =  103149
            # Gender: Female, Age: 16-20, Risk: Unknown, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103150
            # Gender: Male, Age: 21-65, Risk: Unknown, Planning: Yes => message.lb_alcohol_msg =  103151
            # Gender: Male, Age: 21-65, Risk: Unknown, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103152
            # Gender: Female, Age: 21+, Risk: Unknown, Planning: Yes => message.lb_alcohol_msg =  103153
            # Gender: Female, Age: 21+, Risk: Unknown, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103154
            # Gender: Male, Age: 66+, Risk: Unknown, Planning: Yes => message.lb_alcohol_msg =  103155
            # Gender: Male, Age: 66+, Risk: Unknown, Planning: No   DontKnow   NotNeeded   Null => message.lb_alcohol_msg =  103156

            # Gender: , Age: , Risk: , Planning:  => message.lb_alcohol_msg =  103157
            if message.lb_alcohol_msg <= 0:
                message.lb_alcohol_msg =  103157

        def calcmess_lb_physact():
            print('SUB FUNCTION calcmess_lb_physact start...');
            # !! Physical Activity PAGE
            
            # Gender: , Age: , Risk: , Planning:  => message.lb_physact_pregnant =  103158
            # !! use record.plan_physact , record.key_physact, record.physact_strengthfreq >= 2 (high)

            # Gender: , Age: , Risk: VeryLowAerobic HighStrength, Planning: No   DontKnow   NotNeeded   Null => message.lb_physact_msg =  103159
            # Gender: , Age: , Risk: VeryLowAerobic UnknownStrength, Planning: Yes => message.lb_physact_msg =  103160
            # Gender: , Age: , Risk: VeryLowAerobic UnknownStrength, Planning: No   DontKnow   NotNeeded   Null => message.lb_physact_msg =  103161
            # Gender: , Age: , Risk: LowAerboic LowStrength, Planning: Yes => message.lb_physact_msg =  103162
            # Gender: , Age: , Risk: LowAerboic LowStrength, Planning: No => message.lb_physact_msg =  103163
            # Gender: , Age: , Risk: LowAerboic LowStrength, Planning: DontKnow  Null => message.lb_physact_msg =  103164
            # Gender: , Age: , Risk: LowAerboic LowStrength, Planning: NotNeeded => message.lb_physact_msg =  103165
            # Gender: , Age: , Risk: LowAerobic HighStrength, Planning: Yes => message.lb_physact_msg =  103166
            # Gender: , Age: , Risk: LowAerobic HighStrength, Planning: No => message.lb_physact_msg =  103167
            # Gender: , Age: , Risk: LowAerobic HighStrength, Planning: DontKnow  Null => message.lb_physact_msg =  103168
            # Gender: , Age: , Risk: LowAerobic HighStrength, Planning: NotNeeded => message.lb_physact_msg =  103169
            # Gender: , Age: , Risk: LowAerobic UnknownStrength, Planning: Yes => message.lb_physact_msg =  103170
            # Gender: , Age: , Risk: LowAerobic UnknownStrength, Planning: No => message.lb_physact_msg =  103171
            # Gender: , Age: , Risk: LowAerobic UnknownStrength, Planning: DontKnow  Null => message.lb_physact_msg =  103172
            # Gender: , Age: , Risk: LowAerobic UnknownStrength, Planning: NotNeeded => message.lb_physact_msg =  103173
            # Gender: , Age: , Risk: MeetsAerobic LowStrength, Planning: Yes => message.lb_physact_msg =  103174
            # Gender: , Age: , Risk: MeetsAerobic LowStrength, Planning: No => message.lb_physact_msg =  103175
            # Gender: , Age: , Risk: MeetsAerobic LowStrength, Planning: DontKnow  Null => message.lb_physact_msg =  103176
            # Gender: , Age: , Risk: MeetsAerobic LowStrength, Planning: NotNeeded => message.lb_physact_msg =  103177
            # Gender: , Age: , Risk: MeetsAerobic HighStrength, Planning: Yes => message.lb_physact_msg =  103178
            # Gender: , Age: , Risk: MeetsAerobic HighStrength, Planning: No => message.lb_physact_msg =  103179
            # Gender: , Age: , Risk: MeetsAerobic HighStrength, Planning: DontKnow  Null => message.lb_physact_msg =  103180
            # Gender: , Age: , Risk: MeetsAerobic HighStrength, Planning: NotNeeded => message.lb_physact_msg =  103181
            # Gender: , Age: , Risk: MeetsAerobic UnknownStrength, Planning: Yes => message.lb_physact_msg =  103182
            # Gender: , Age: , Risk: MeetsAerobic UnknownStrength, Planning: No => message.lb_physact_msg =  103183
            # Gender: , Age: , Risk: MeetsAerobic UnknownStrength, Planning: DontKnow  Null => message.lb_physact_msg =  103184
            # Gender: , Age: , Risk: MeetsAerobic UnknownStrength, Planning: NotNeeded => message.lb_physact_msg =  103185
            # Gender: , Age: , Risk: UnknownAerobic LowStrength, Planning: Yes => message.lb_physact_msg =  103186
            # Gender: , Age: , Risk: UnknownAerobic LowStrength, Planning: No  DontKnow  NotNeeded  Null => message.lb_physact_msg =  103187
            # Gender: , Age: , Risk: UnknownAerobic HighStrength, Planning: Yes => message.lb_physact_msg =  103188
            # Gender: , Age: , Risk: UnknownAerobic HighStrength, Planning: No  DontKnow  NotNeeded  Null => message.lb_physact_msg =  103189
            # Gender: , Age: , Risk: UnknownAerobic UnknownStrength, Planning: Yes => message.lb_physact_msg =  103190
            # Gender: , Age: , Risk: UnknownAerobic UnknownStrength, Planning: No  DontKnow  NotNeeded  Null => message.lb_physact_msg =  103191

            # Gender: , Age: , Risk: , Planning:  => message.lb_physact_sitting_msg =  103193


        def calcmess_lb_safedriving():
            print('SUB FUNCTION calcmess_lb_safedriving start...');
            # !! Driving Habits PAGE

            # !! record.drive_speed: 1 = <= 5, 2 = 6-10 over, 3 = more than 10 over
            # !! record.aod_alcoh_drvridedrunkfreq:  number of times

            # Gender: , Age: , Risk: High Speed_5 Drunk_0, Planning:  => message.lb_safedriving_msg =  103194
            # Gender: , Age: , Risk: High Speed_5 Drunk_1+, Planning:  => message.lb_safedriving_msg =  103195
            # Gender: , Age: , Risk: High Speed_5 Drunk_Unknown, Planning:  => message.lb_safedriving_msg =  103196
            # Gender: , Age: , Risk: High Speed_6+ Drunk_0, Planning:  => message.lb_safedriving_msg =  103197
            # Gender: , Age: , Risk: High Speed_6+ Drunk_1+, Planning:  => message.lb_safedriving_msg =  103198
            # Gender: , Age: , Risk: High Speed_6+ Drunk_Unknown, Planning:  => message.lb_safedriving_msg =  103199
            # Gender: , Age: , Risk: High Speed_Unknown Drunk_0, Planning:  => message.lb_safedriving_msg =  103200
            # Gender: , Age: , Risk: High Speed_Unknown Drunk_1+, Planning:  => message.lb_safedriving_msg =  103201
            # Gender: , Age: , Risk: High Speed_Unknown Drunk_Unknown, Planning:  => message.lb_safedriving_msg =  103202
            # Gender: , Age: , Risk: Low Speed_5 Drunk_0, Planning:  => message.lb_safedriving_msg =  103203
            # Gender: , Age: , Risk: Low Speed_5 Drunk_1+, Planning:  => message.lb_safedriving_msg =  103204
            # Gender: , Age: , Risk: Low Speed_5 Drunk_Unknown, Planning:  => message.lb_safedriving_msg =  103205
            # Gender: , Age: , Risk: Low Speed_6+ Drunk_0, Planning:  => message.lb_safedriving_msg =  103206
            # Gender: , Age: , Risk: Low Speed_6+ Drunk_1+, Planning:  => message.lb_safedriving_msg =  103207
            # Gender: , Age: , Risk: Low Speed_6+ Drunk_Unknown, Planning:  => message.lb_safedriving_msg =  103208
            # Gender: , Age: , Risk: Low Speed_Unknown Drunk_0, Planning:  => message.lb_safedriving_msg =  103209
            # Gender: , Age: , Risk: Low Speed_Unknown Drunk_1+, Planning:  => message.lb_safedriving_msg =  103210
            # Gender: , Age: , Risk: Low Speed_Unknown Drunk_Unknown, Planning:  => message.lb_safedriving_msg =  103211
            # Gender: , Age: , Risk: Unknown Speed_5 Drunk_0, Planning:  => message.lb_safedriving_msg =  103212
            # Gender: , Age: , Risk: Unknown Speed_5 Drunk_1+, Planning:  => message.lb_safedriving_msg =  103213
            # Gender: , Age: , Risk: Unknown Speed_5 Drunk_Null, Planning:  => message.lb_safedriving_msg =  103214
            # Gender: , Age: , Risk: Unknown Speed_6+ Drunk_0, Planning:  => message.lb_safedriving_msg =  103215
            # Gender: , Age: , Risk: Unknown Speed_6+ Drunk_1+, Planning:  => message.lb_safedriving_msg =  103216
            # Gender: , Age: , Risk: Unknown Speed_6+ Drunk_Null, Planning:  => message.lb_safedriving_msg =  103217
            # Gender: , Age: , Risk: Unknown Speed_Null Drunk_0, Planning:  => message.lb_safedriving_msg =  103218
            # Gender: , Age: , Risk: Unknown Speed_Null Drunk_1+, Planning:  => message.lb_safedriving_msg =  103219
            # Gender: , Age: , Risk: Unknown Speed_Null Drunk_Null, Planning:  => message.lb_safedriving_msg =  103220
            # Gender: , Age: , Risk: , Planning:  => message.lb_safedriving_pregnant =  103221
            # Gender: , Age: , Risk: , Planning:  => message.lb_tobacco_pregnant =  103222

        def calcmess_lb_tobacco():
            print('SUB FUNCTION calcmess_lb_tobacco start...');
            # !! Tobacco use PAGE

            # !!  record.tob_cigssmokestatus: 1= Still smoke, 2 Used to smoke, 3 Never smoked
            # !! record.tob_othercigars  1 =yes
            # !! record.tob_otherpipes
            # !! record.tob_othersmokeless
            # !! record.tob_otherecigs
            # !!  record.tob_othernone
            # !!  record.plan_tobacco

            # Gender: , Age: , Risk: SmokerCurrent OtherEcig, Planning: Yes => message.lb_tobacco_msg =  103223
            # Gender: , Age: , Risk: SmokerCurrent OtherEcig, Planning: No  NotNeeded => message.lb_tobacco_msg =  103224
            # Gender: , Age: , Risk: SmokerCurrent OtherEcig, Planning: DontKnow  Null => message.lb_tobacco_msg =  103225
            # Gender: , Age: , Risk: SmokerCurrent OtherNotEcig, Planning: Yes => message.lb_tobacco_msg =  103226
            # Gender: , Age: , Risk: SmokerCurrent OtherNotEcig, Planning: No  NotNeeded => message.lb_tobacco_msg =  103227
            # Gender: , Age: , Risk: SmokerCurrent OtherNotEcig, Planning: DontKnow  Null => message.lb_tobacco_msg =  103228
            # Gender: , Age: , Risk: SmokerFormer OtherChew, Planning: Yes => message.lb_tobacco_msg =  103229
            # Gender: , Age: , Risk: SmokerFormer OtherChew, Planning: No  NotNeeded => message.lb_tobacco_msg =  103230
            # Gender: , Age: , Risk: SmokerFormer OtherChew, Planning: DontKnow  Null => message.lb_tobacco_msg =  103231
            # Gender: , Age: , Risk: SmokerFormer OtherCigar, Planning: Yes => message.lb_tobacco_msg =  103232
            # Gender: , Age: , Risk: SmokerFormer OtherCigar, Planning: No  NotNeeded => message.lb_tobacco_msg =  103233
            # Gender: , Age: , Risk: SmokerFormer OtherCigar, Planning: DontKnow  Null => message.lb_tobacco_msg =  103234
            # Gender: , Age: , Risk: SmokerFormer OtherEcig, Planning: Yes => message.lb_tobacco_msg =  103235
            # Gender: , Age: , Risk: SmokerFormer OtherEcig, Planning: No  NotNeeded => message.lb_tobacco_msg =  103236
            # Gender: , Age: , Risk: SmokerFormer OtherEcig, Planning: DontKnow  Null => message.lb_tobacco_msg =  103237
            # Gender: , Age: , Risk: SmokerFormer OtherPipe, Planning: Yes => message.lb_tobacco_msg =  103238
            # Gender: , Age: , Risk: SmokerFormer OtherPipe, Planning: No  NotNeeded => message.lb_tobacco_msg =  103239
            # Gender: , Age: , Risk: SmokerFormer OtherPipe, Planning: DontKnow  Null => message.lb_tobacco_msg =  103240
            # Gender: , Age: , Risk: SmokerFormer MultiUser, Planning: Yes => message.lb_tobacco_msg =  103241
            # Gender: , Age: , Risk: SmokerFormer MultiUser, Planning: No  NotNeeded => message.lb_tobacco_msg =  103242
            # Gender: , Age: , Risk: SmokerFormer MultiUser, Planning: DontKnow  Null => message.lb_tobacco_msg =  103243
            # Gender: , Age: , Risk: SmokerFormer OtherNone, Planning: Yes => message.lb_tobacco_msg =  103244
            # Gender: , Age: , Risk: SmokerFormer OtherUnknown, Planning: Yes => message.lb_tobacco_msg =  103245
            # Gender: , Age: , Risk: SmokerNever OtherChew, Planning: Yes => message.lb_tobacco_msg =  103246
            # Gender: , Age: , Risk: SmokerNever OtherChew, Planning: No  NotNeeded => message.lb_tobacco_msg =  103247
            # Gender: , Age: , Risk: SmokerNever OtherChew, Planning: DontKnow  Null => message.lb_tobacco_msg =  103248
            # Gender: , Age: , Risk: SmokerNever OtherCigar, Planning: Yes => message.lb_tobacco_msg =  103249
            # Gender: , Age: , Risk: SmokerNever OtherCigar, Planning: No  NotNeeded => message.lb_tobacco_msg =  103250
            # Gender: , Age: , Risk: SmokerNever OtherCigar, Planning: DontKnow  Null => message.lb_tobacco_msg =  103251
            # Gender: , Age: , Risk: SmokerNever OtherEcig, Planning: Yes => message.lb_tobacco_msg =  103252
            # Gender: , Age: , Risk: SmokerNever OtherEcig, Planning: No  NotNeeded => message.lb_tobacco_msg =  103253
            # Gender: , Age: , Risk: SmokerNever OtherEcig, Planning: DontKnow  Null => message.lb_tobacco_msg =  103254
            # Gender: , Age: , Risk: SmokerNever OtherPipe, Planning: Yes => message.lb_tobacco_msg =  103255
            # Gender: , Age: , Risk: SmokerNever OtherPipe, Planning: No  NotNeeded => message.lb_tobacco_msg =  103256
            # Gender: , Age: , Risk: SmokerNever OtherPipe, Planning: DontKnow  Null => message.lb_tobacco_msg =  103257
            # Gender: , Age: , Risk: SmokerNever MultiUser, Planning: Yes => message.lb_tobacco_msg =  103258
            # Gender: , Age: , Risk: SmokerNever MultiUser, Planning: No  NotNeeded => message.lb_tobacco_msg =  103259
            # Gender: , Age: , Risk: SmokerNever MultiUser, Planning: DontKnow  Null => message.lb_tobacco_msg =  103260
            # Gender: , Age: , Risk: SmokerNever OtherNone, Planning: Yes => message.lb_tobacco_msg =  103261
            # Gender: , Age: , Risk: SmokerNever OtherNone, Planning: No  NotNeeded => message.lb_tobacco_msg =  103262
            # Gender: , Age: , Risk: SmokerNever OtherUnknown, Planning: Yes => message.lb_tobacco_msg =  103263
            # Gender: , Age: , Risk: SmokerNever OtherUnknown, Planning: No  NotNeeded => message.lb_tobacco_msg =  103264
            # Gender: , Age: , Risk: SmokerNever OtherUnknown, Planning: DontKnow  Null => message.lb_tobacco_msg =  103265
            # Gender: , Age: , Risk: SmokerUnknown OtherChew, Planning: Yes => message.lb_tobacco_msg =  103266
            # Gender: , Age: , Risk: SmokerUnknown OtherChew, Planning: No  NotNeeded => message.lb_tobacco_msg =  103267
            # Gender: , Age: , Risk: SmokerUnknown OtherChew, Planning: DontKnow  Null => message.lb_tobacco_msg =  103268
            # Gender: , Age: , Risk: SmokerUnknown OtherCigar, Planning: Yes => message.lb_tobacco_msg =  103269
            # Gender: , Age: , Risk: SmokerUnknown OtherCigar, Planning: No  NotNeeded => message.lb_tobacco_msg =  103270
            # Gender: , Age: , Risk: SmokerUnknown OtherCigar, Planning: DontKnow  Null => message.lb_tobacco_msg =  103271
            # Gender: , Age: , Risk: SmokerUnknown OtherEcig, Planning: Yes => message.lb_tobacco_msg =  103272
            # Gender: , Age: , Risk: SmokerUnknown OtherEcig, Planning: No  NotNeeded => message.lb_tobacco_msg =  103273
            # Gender: , Age: , Risk: SmokerUnknown OtherEcig, Planning: DontKnow  Null => message.lb_tobacco_msg =  103274
            # Gender: , Age: , Risk: SmokerUnknown OtherPipe, Planning: Yes => message.lb_tobacco_msg =  103275
            # Gender: , Age: , Risk: SmokerUnknown OtherPipe, Planning: No  NotNeeded => message.lb_tobacco_msg =  103276
            # Gender: , Age: , Risk: SmokerUnknown OtherPipe, Planning: DontKnow  Null => message.lb_tobacco_msg =  103277
            # Gender: , Age: , Risk: SmokerUnknown MultiUser, Planning: Yes => message.lb_tobacco_msg =  103278
            # Gender: , Age: , Risk: SmokerUnknown MultiUser, Planning: No  NotNeeded => message.lb_tobacco_msg =  103279
            # Gender: , Age: , Risk: SmokerUnknown MultiUser, Planning: DontKnow  Null => message.lb_tobacco_msg =  103280
            # Gender: , Age: , Risk: SmokerUnknown OtherNone, Planning: Yes => message.lb_tobacco_msg =  103281
            # Gender: , Age: , Risk: SmokerUnknown OtherNone, Planning: No  NotNeeded => message.lb_tobacco_msg =  103282
            # Gender: , Age: , Risk: SmokerUnknown OtherUnknown, Planning: Yes => message.lb_tobacco_msg =  103283
            # Gender: , Age: , Risk: SmokerUnknown OtherUnknown, Planning: No  NotNeeded => message.lb_tobacco_msg =  103284

            # Gender: , Age: , Risk: , Planning:  => message.lb_weight_pregnant =  103285

            # Gender: , Age: , Risk: , Planning:  => message.lb_weight_defaultweight =  103286
            # Gender: , Age: , Risk: , Planning:  => message.lb_weight_defaultweight =  103287

        def calcmess_lb_weight():
            print('SUB FUNCTION calcmess_lb_weight start...');
            # !! Weight Management PAGE

            # !! record.plan_weight
            # !! Underweight: BMI <18.5 ,  Normal (Low risk):BMI = 18.5-24.9,  Overweight (High risk): BMI = 25-29.9 , Obese: BMI >=30

            # Gender: , , Risk: Underweight, Planning: Yes => message.lb_weight_msg =  103288
            # Gender: , Age: , Risk: Underweight, Planning: No  NotNeeded => message.lb_weight_msg =  103289
            # Gender: , Age:  Risk: Underweight, Planning: DontKnow  Null => message.lb_weight_msg =  103290
            # Gender: , Age: , Risk: Low, Planning: Yes => message.lb_weight_msg =  103291
            # Gender: , Age: , Risk: Low, Planning: No  NotNeeded => message.lb_weight_msg =  103292
            # Gender: , Age: , Risk: Low, Planning: DontKnow  Null => message.lb_weight_msg =  103293
            # Gender: , Age: , Risk: High, Planning: Yes => message.lb_weight_msg =  103294
            # Gender: , Age: , Risk: High, Planning: No  NotNeeded => message.lb_weight_msg =  103295
            # Gender: , Age: , Risk: High, Planning: DontKnow  Null => message.lb_weight_msg =  103296
            # Gender: , Age: , Risk: Obese, Planning: Yes => message.lb_weight_msg =  103297
            # Gender: , Age: , Risk: Obese, Planning: No  NotNeeded => message.lb_weight_msg =  103298
            # Gender: , Age: , Risk: Obese, Planning: DontKnow  Null => message.lb_weight_msg =  103299
            # Gender: , Age: , Risk: Unknown, Planning: Yes => message.lb_weight_msg =  103300
            # Gender: , Age: , Risk: Unknown, Planning: No  NotNeeded => message.lb_weight_msg =  103301

        # CALL all subfunctions --->
        calcmess_lb_alcohol();
        calcmess_lb_physact();
        calcmess_lb_safedriving();
        calcmess_lb_tobacco();
        calcmess_lb_weight()
        
    def calcmess_mc_section(self):
        record = self.record;
        message = self.messages;
        
        print('calcmess_mc_section start...');
        
        # !! MEDICAL CONDITIONS Section (health conditions hc)
        # !! hc section
        
        # Gender: , Age: , Risk: , Planning:  => message.mc_intro_msg =  104302
        message.mc_intro_msg =  104302
        
        #  subfunctions -->
        # calcmess_mc_bp();
        # calcmess_chol_bp();
        # calcmess_medhistory_bp();

        def calcmess_mc_bp():
            print('SUB FUNCTION calcmess_mc_bp start...');
            # !! Blood Pressure PAGE

            # !! Add this criteria to BP        
            # on meds & >=140/90
            # on meds & >=140/91
            # on meds & >=140/91
            # on meds & >=140/93
            # on meds & <140/90
            # on meds & <140/91
            # on meds & <140/92
            # on meds & <140/93
            # on meds & >=150/90
            # on meds & >=150/91
            # on meds & >=150/92
            # on meds & >=150/93
            # on meds & <150/90
            # on meds & <150/91
            # on meds & <150/92
            # on meds & <150/93
            # under care  & >=140/90
            # under care  & >=140/91
            # under care  & >=140/92
            # under care  & >=140/93
            # under care  & <140/90
            # under care  & <140/91
            # under care  & <140/92
            # under care  & <140/93
            # under care & >=150/90
            # under care & >=150/91
            # under care & >=150/92
            # under care & >=150/93
            # under care & <150/90
            # under care & <150/91
            # under care & <150/92
            # under care & <150/93
            # SBP > 139 || DBP > 89 || (SBP/DBP missing & CurrentHBP)
            # SBP > 139 || DBP > 89 || (SBP/DBP missing & CurrentHBP)
            # SBP > 139 || DBP > 89 || (SBP/DBP missing & CurrentHBP)
            # SBP > 139 || DBP > 89 || (SBP/DBP missing & CurrentHBP)
            # SBP 120-139 || DBP 80-89
            # SBP 120-139 || DBP 80-89
            # SBP 120-139 || DBP 80-89
            # SBP 120-139 || DBP 80-89
            # SBP <= 119 && DBP <= 79 (not missing numbers and > 0)
            # SBP <= 119 && DBP <= 79 (not missing numbers and > 0)
            # SBP <= 119 && DBP <= 79 (not missing numbers and > 0)
            # SBP <= 119 && DBP <= 79 (not missing numbers and > 0)
            # BP null
            # BP null
            # BP null
            # BP null

            # Gender: , Age: 18-59, Risk: MedUncontrolled, Planning: Yes => message.mc_bp_msg =  104303
            # Gender: , Age: 18-59, Risk: MedUncontrolled, Planning: No => message.mc_bp_msg =  104304
            # Gender: , Age: 18-59, Risk: on meds & >=140/92, Planning: DontKnow  Null => message.mc_bp_msg =  104305
            # Gender: , Age: 18-59, Risk: MedUncontrolled, Planning: NotNeeded => message.mc_bp_msg =  104306

            # Gender: , Age: 18-59, Risk: MedControlled, Planning: Yes => message.mc_bp_msg =  104307
            # Gender: , Age: 18-59, Risk: MedControlled, Planning: No => message.mc_bp_msg =  104308
            # Gender: , Age: 18-59, Risk: MedControlled, Planning: DontKnow  Null => message.mc_bp_msg =  104309
            # Gender: , Age: 18-59, Risk: MedControlled, Planning: NotNeeded => message.mc_bp_msg =  104310

            # Gender: , Age: 60+, Risk: MedUncontrolled, Planning: Yes => message.mc_bp_msg =  104311
            # Gender: , Age: 60+, Risk: MedUncontrolled, Planning: No => message.mc_bp_msg =  104312
            # Gender: , Age: 60+, Risk: MedUncontrolled, Planning: DontKnow  Null => message.mc_bp_msg =  104313
            # Gender: , Age: 60+, Risk: MedUncontrolled, Planning: NotNeeded => message.mc_bp_msg =  104314

            # Gender: , Age: 60+, Risk: MedControlled, Planning: Yes => message.mc_bp_msg =  104315
            # Gender: , Age: 60+, Risk: MedControlled, Planning: No => message.mc_bp_msg =  104316
            # Gender: , Age: 60+, Risk: MedControlled, Planning: DontKnow  Null => message.mc_bp_msg =  104317
            # Gender: , Age: 60+, Risk: MedControlled, Planning: NotNeeded => message.mc_bp_msg =  104318

            # Gender: , Age: 18-59, Risk: CareUncontrolled, Planning: Yes => message.mc_bp_msg =  104319
            # Gender: , Age: 18-59, Risk: CareUncontrolled, Planning: No => message.mc_bp_msg =  104320
            # Gender: , Age: 18-59, Risk: CareUncontrolled, Planning: DontKnow  Null => message.mc_bp_msg =  104321
            # Gender: , Age: 18-59, Risk: CareUncontrolled, Planning: NotNeeded => message.mc_bp_msg =  104322

            # Gender: , Age: 18-59, Risk: CareControlled, Planning: Yes => message.mc_bp_msg =  104323
            # Gender: , Age: 18-59, Risk: CareControlled, Planning: No => message.mc_bp_msg =  104324
            # Gender: , Age: 18-59, Risk: CareControlled, Planning: DontKnow  Null => message.mc_bp_msg =  104325
            # Gender: , Age: 18-59, Risk: CareControlled, Planning: NotNeeded => message.mc_bp_msg =  104326

            # Gender: , Age: 60+, Risk: CareUncontrolled, Planning: Yes => message.mc_bp_msg =  104327
            # Gender: , Age: 60+, Risk: CareUncontrolled, Planning: No => message.mc_bp_msg =  104328
            # Gender: , Age: 60+, Risk: CareUncontrolled, Planning: DontKnow  Null => message.mc_bp_msg =  104329
            # Gender: , Age: 60+, Risk: CareUncontrolled, Planning: NotNeeded => message.mc_bp_msg =  104330

            # Gender: , Age: 60+, Risk: CareControlled, Planning: Yes => message.mc_bp_msg =  104331
            # Gender: , Age: 60+, Risk: CareControlled, Planning: No => message.mc_bp_msg =  104332
            # Gender: , Age: 60+, Risk: CareControlled, Planning: DontKnow  Null => message.mc_bp_msg =  104333
            # Gender: , Age: 60+, Risk: CareControlled, Planning: NotNeeded => message.mc_bp_msg =  104334

            # Gender: , Age: 18+, Risk: High, Planning: Yes => message.mc_bp_msg =  104335
            # Gender: , Age: 18+, Risk: High, Planning: No => message.mc_bp_msg =  104336
            # Gender: , Age: 18+, Risk: High, Planning: DontKnow  Null => message.mc_bp_msg =  104337
            # Gender: , Age: 18+, Risk: High, Planning: NotNeeded => message.mc_bp_msg =  104338

            # Gender: , Age: 18+, Risk: PreH, Planning: Yes => message.mc_bp_msg =  104339
            # Gender: , Age: 18+, Risk: PreH, Planning: No => message.mc_bp_msg =  104340
            # Gender: , Age: 18+, Risk: PreH, Planning: DontKnow  Null => message.mc_bp_msg =  104341
            # Gender: , Age: 18+, Risk: PreH, Planning: NotNeeded => message.mc_bp_msg =  104342

            # Gender: , Age: 18+, Risk: Normal, Planning: Yes => message.mc_bp_msg =  104343
            # Gender: , Age: 18+, Risk: Normal, Planning: No => message.mc_bp_msg =  104344
            # Gender: , Age: 18+, Risk: Normal, Planning: DontKnow  Null => message.mc_bp_msg =  104345
            # Gender: , Age: 18+, Risk: Normal, Planning: NotNeeded => message.mc_bp_msg =  104346

            # Gender: , Age: 18+, Risk: Unknown, Planning: Yes => message.mc_bp_msg =  104347
            # Gender: , Age: 18+, Risk: Unknown, Planning: No => message.mc_bp_msg =  104348
            # Gender: , Age: 18+, Risk: Unknown, Planning: DontKnow  Null => message.mc_bp_msg =  104349
            # Gender: , Age: 18+, Risk: Unknown, Planning: NotNeeded => message.mc_bp_msg =  104350

        def calcmess_mc_chol():
            print('SUB FUNCTION calcmess_mc_chol start...');
            # !! CHOLESTEROL PAGE
            # !! chol-> High: TC > 239 || (TC missing && self-report high chol)
            # !! Borderline:  TC 200-239
            # !!   Desirable/Low risk: TC < 200 && TC > 0
            
            # Gender: , Age: , Risk: High, Planning: Yes => message.mc_chol_msg =  104351
            # Gender: , Age: , Risk: High, Planning: No => message.mc_chol_msg =  104352
            # Gender: , Age: , Risk: High, Planning: DontKnow  Null => message.mc_chol_msg =  104353
            # Gender: , Age: , Risk: High, Planning: NotNeeded => message.mc_chol_msg =  104354
            # Gender: , Age: , Risk: BorderlineHigh, Planning: Yes => message.mc_chol_msg =  104355
            # Gender: , Age: , Risk: BorderlineHigh, Planning: No => message.mc_chol_msg =  104356
            # Gender: , Age: , Risk: BorderlineHigh, Planning: DontKnow  Null => message.mc_chol_msg =  104357
            # Gender: , Age: , Risk: BorderlineHigh, Planning: NotNeeded => message.mc_chol_msg =  104358
            # Gender: , Age: , Risk: Desirable, Planning: Yes => message.mc_chol_msg =  104359
            # Gender: , Age: , Risk: Desirable, Planning: No => message.mc_chol_msg =  104360
            # Gender: , Age: , Risk: Desirable, Planning: DontKnow  Null => message.mc_chol_msg =  104361
            # Gender: , Age: , Risk: Desirable, Planning: NotNeeded => message.mc_chol_msg =  104362
            # Gender: , Age: , Risk: Unknown, Planning: Yes => message.mc_chol_msg =  104363
            # Gender: , Age: , Risk: Unknown, Planning: No => message.mc_chol_msg =  104364
            # Gender: , Age: , Risk: Unknown, Planning: DontKnow  Null => message.mc_chol_msg =  104365
            # Gender: , Age: , Risk: Unknown, Planning: NotNeeded => message.mc_chol_msg =  104366
            # !!  2 message blocks will display on this page of the guide.
            # !! 1 A "condition" message only 1 of the5 "condition" groups messages will display
            # !! 2 An "overall" health message will be displayed after one of the "condition" messages

        def calcmess_mc_medhistory():
            print('SUB FUNCTION calcmess_mc_medhistory start...');
            # !! MEDICAL HISTORY PAGE

            # !! Group 1 - Diseases
            # !!  If user has one disease, that specific message will fire. If the user has 2+ diseases, they will get a more generic multi-disease message.

            # Gender: , Age: , Risk: MultiDiseases, Planning:  => message.mc_medhistory_disease =  104367
            # Gender: , Age: , Risk: Cancer, Planning:  => message.mc_medhistory_disease =  104368
            # Gender: , Age: , Risk: COPD, Planning:  => message.mc_medhistory_disease =  104369
            # Gender: , Age: , Risk: Diabetes, Planning:  => message.mc_medhistory_disease =  104370
            # Gender: , Age: , Risk: HeartDisease, Planning:  => message.mc_medhistory_disease =  104371
            # Gender: , Age: , Risk: Stoke, Planning:  => message.mc_medhistory_disease =  104372

            # !! Risk: Group 2 - conditions
            # !! If a user does not have an above disease, but indicates a condition within this list (NOT including BP/Chol), this group will apply.
            #  (If they have a disease, only that group will fire.)

            # Gender: , Age: , Risk: MultiConditions, Planning:  => message.mc_medhistory_condition =  104374
            # Gender: , Age: , Risk: Allergies, Planning:  => message.mc_medhistory_condition =  104375
            # Gender: , Age: , Risk: Arthritis, Planning:  => message.mc_medhistory_condition =  104376
            # Gender: , Age: , Risk: Asthma, Planning:  => message.mc_medhistory_condition =  104377
            # Gender: , Age: , Risk: BackPain, Planning:  => message.mc_medhistory_condition =  104378
            # Gender: , Age: , Risk: CKD, Planning:  => message.mc_medhistory_condition =  104379
            # Gender: , Age: , Risk: ChronicPain, Planning:  => message.mc_medhistory_condition =  104380
            # Gender: , Age: , Risk: Depression, Planning:  => message.mc_medhistory_condition =  104381
            # Gender: , Age: , Risk: PreDiabetes, Planning:  => message.mc_medhistory_condition =  104382
            # Gender: , Age: , Risk: GERD, Planning:  => message.mc_medhistory_condition =  104383
            # Gender: , Age: , Risk: Migraines, Planning:  => message.mc_medhistory_condition =  104384
            # Gender: , Age: , Risk: Menopause, Planning:  => message.mc_medhistory_condition =  104385
            # Gender: , Age: , Risk: Osteoporosis, Planning:  => message.mc_medhistory_condition =  104386
            # Gender: , Age: , Risk: SleepDisorder, Planning:  => message.mc_medhistory_condition =  104387
            # Gender: , Age: , Risk: Other, Planning:  => message.mc_medhistory_condition =  104388

            # !!  Risk: Group 3
            # !! If a user reponds they currently have HBP and/or HiChol -- NO other conditions, then this group will display

            # Gender: , Age: , Risk: Multi, Planning:  => message.mc_medhistory_bpcholonly =  104390
            # Gender: , Age: , Risk: BloodPressure, Planning:  => message.mc_medhistory_bpcholonly =  104391
            # Gender: , Age: , Risk: Cholesterol, Planning:  => message.mc_medhistory_bpcholonly =  104392

            # !!  Risk: Group 4 
            # Gender: , Age: , Risk: None, Planning:  => message.mc_medhistory_none =  104394

            # !! Risk: Group 5 
            # Gender: , Age: , Risk: Unknown, Planning:  => message.mc_medhistory_default =  104396


        # !! call all subfunctions -->
        try:
            
            calcmess_mc_bp();
            calcmess_mc_chol();
            calcmess_mc_medhistory();
        except:
            print('Exception for calcmess_mc section..');


    def calcmess_ps_section(self):
        record = self.record;
        message = self.messages;
        print('calcmess_ps_section start...');

        # !! PREVENTATIVE SERVICES TABLE (screening)
        # !!  Preventative services (screening)

        # Gender: , Age: 18+, Risk: , Planning:  => message.mc_prevserv_bp =  104397
        # Gender: , Age: 20+, Risk: , Planning:  => message.mc_prevserv_chol =  104398
        # Gender: Female, Age: 50-74, Risk: no mastectomy, Planning:  => message.mc_prevserv_mammogram =  104399
        # Gender: Female, Age: 21-29, Risk: no hysterectomy, Planning:  => message.mc_prevserv_cervicalca =  104400
        # Gender: Female, Age: 30-65, Risk: no hysterectomy, Planning:  => message.mc_prevserv_cervicalca =  104401
        # Gender: , Age: 50-75, Risk: , Planning:  => message.mc_prevserv_colonca =  104402
        # Gender: , Age: , Risk: , Planning:  => message.mc_prevserv_flushot =  104403
        # Gender: , Age: , Risk: , Planning:  => message.mc_prevserv_tetanusshot =  104404


        # !!  Planning variable coding from survey

        # !! PS guideline (PSGL) calculations (uses following data)

        # !! survey data to use:
        # !!   record.ps_bp
        # !!   record.ps_chol
        # !!   record.ps_mammogram

        # !!   record.ps_cervicalca_paponlytime
        # !!   record.ps_cervicalca_paphpvtype
        # !!   record.ps_cervicalca_paphpvtime

        # !!   record.ps_colonca_fobt
        # !!   record.ps_colonca_flexsig
        # !!   record.ps_colonca_colonoscopy	

        # !!   record.ps_flushot
        # !!   record.ps_tetanusshot

        # compliance: <1, 1-2, 2-3 =>record.psgl_bp = 1
        # non-compliance: 3+, Never =>record.psgl_bp = 2
        # unknown compliance: Don't know, Missing =>record.psgl_bp = 3
        # compliance: <1, 1-2, 2-3, 3-4, 4-5, 5-6 =>record.psgl_chol = 1
        # non-compliance: 6+, Never =>record.psgl_chol = 2
        # unknown compliance: Don't know, Missing =>record.psgl_chol = 3
        # compliance: <1, 1-2 =>record.psgl_mammogram = 1
        # non-compliance: 2+, 3+, 4+, 5+, 6+, Never =>record.psgl_mammogram = 2
        # unknown compliance: Don't know, Missing =>record.psgl_mammogram = 3
        # compliance: <1, 1-2, 2-3, 3-4 =>record.psgl_cervicalca = 1
        # non-compliance: 4+, 5+, Never =>record.psgl_cervicalca = 2
        # unknown compliance: Don't know, Missing =>record.psgl_cervicalca = 3
        # compliance: Pap: <1, 1-2, 2-3, 3-4, , Co-test: <1, 1-2, 2-3, 3-4, 4-5 =>record.psgl_cervicalca = 1
        # non-compliance: Pap: 4-5, 5+, Never, , Co-test: 5+, Never =>record.psgl_cervicalca = 2
        # unknown compliance: Don't know, Missing =>record.psgl_cervicalca = 3
        # compliance: Yes (for any) =>record.psgl_colonca = 1
        # non-compliance: No (without any Yes's) =>record.psgl_colonca = 2
        # unknown compliance: Don't know, Missing, (without any Yes's) =>record.psgl_colonca = 3
        # compliance: <1 year, 1-2 =>record.psgl_flushot = 1
        # non-compliance: 2+, 3+, Never =>record.psgl_flushot = 2
        # unknown compliance: Don't know, Missing =>record.psgl_flushot = 3
        # compliance: Yes =>record.psgl_tetanusshot = 1
        # non-compliance: No =>record.psgl_tetanusshot = 2
        # unknown compliance: Don't know, Missing =>record.psgl_tetanusshot = 3

        # !!!!!  NOTE, need to confirm if we use the PS additional here....
        # Gender: , Age: , Risk: , Planning:  => message. =  104406
        # Gender: , Age: , Risk: , Planning:  => message. =  104407
        # Gender: , Age: 16-39, Risk: , Planning:  => message. =  104408
        # Gender: , Age: 40+, Risk: , Planning:  => message. =  104409
        # Gender: Female, Age: , Risk: hysterectomy due to cancer, Planning:  => message. =  104410
        # Gender: , Age: born 1945-65, Risk: , Planning:  => message. =  104411
        # Gender: , Age: 15-65, Risk: , Planning:  => message. =  104412
        # Gender: Female, Age: 65+, Risk: , Planning:  => message. =  104413
        # Gender: , Age: , Risk: , Planning:  => message. =  104414
        # Gender: Female, Age: 18-26, Risk: , Planning:  => message. =  104415
        # Gender: Male, Age: 18-21, Risk: , Planning:  => message. =  104416
        # Gender: , Age: born after 1956, Risk: , Planning:  => message. =  104417
        # Gender: , Age: 65+, Risk: , Planning:  => message. =  104418
        # Gender: , Age: 60+, Risk: , Planning:  => message. =  104419

        
    def calcmess_mc_overallheath_section(self):

        record = self.record;
        message = self.messages;
        print('calcmess_mc_overallheath_section start...');
        
        # Gender: Female, Age: , Risk: pregnant = yes, Planning:  => message.mc_overallhealth_pregnant =  104421
        # Gender: , Age: , Risk: (Perceived Health = Excellent, Very good, Good) && (Illness Days = 0, 1-2, 3-5), Planning:  => message.mc_overallhealth_msg =  104422
        # Gender: , Age: , Risk: (Perceived Health = Fair, Poor) || (Illness Days = 6-10, 11-15, 16+), Planning:  => message.mc_overallhealth_msg =  104423
        # Gender: , Age: , Risk: Unknown/Default, Planning:  => message.mc_overallhealth_msg =  104424

    def calcmess_eh_section(self):
        record = self.record;
        message = self.messages;
        print('calcmess_eh_section start...');

        # !!  EMOTIONAL HEALTH Section
        # !!  eh (emotional health) Section
        # Gender: , Age: , Risk: , Planning:  => message.eh_intro_msg =  106425
        message.eh_intro_msg =  106425 

        # !! Life Satisfaction, Stress/depression ?what are cut-off points???
        
        # Gender: , Age: , Risk: SHDH, Planning:  => message.eh_lifesat_msg =  106426
        # Gender: , Age: , Risk: SHDL, Planning:  => message.eh_lifesat_msg =  106427
        # Gender: , Age: , Risk: SLDH, Planning:  => message.eh_lifesat_msg =  106428
        # Gender: , Age: , Risk: SLDL, Planning:  => message.eh_lifesat_msg =  106429

        # !! STRESS  record.plan_stress , record.key_stress

        # Gender: , Age: , Risk: High, Planning: Yes => message.eh_stress_msg =  106501
        # Gender: , Age: , Risk: High, Planning: No  NotNeeded => message.eh_stress_msg =  106502
        # Gender: , Age: , Risk: High, Planning: DontKnow  Null => message.eh_stress_msg =  106503
        # Gender: , Age: , Risk: Low, Planning: Yes => message.eh_stress_msg =  106504
        # Gender: , Age: , Risk: Low, Planning: No  DontKnow  NotNeeded  Null => message.eh_stress_msg =  106505
        # Gender: , Age: , Risk: Missing, Planning: Yes => message.eh_stress_msg =  106506
        # Gender: , Age: , Risk: Missing, Planning: No  DontKnow  NotNeeded  Null => message.eh_stress_msg =  106507

    def calcmess_whatnext_section(self):
        record = self.record;
        message = self.messages;
        print('calcmess_whatnext_section start...');
        # !!  WHATS NEXT Section
        message.whatsnext_intro_msg =  124432

        # TopN calculated previously with focus_top_3
        
        message.whatsnext_summary_questions =  124460
        message.whatsnext_summary_keys =  124461
        message.whatsnext_summary_choice =  124462
