import sys
import json
#from bunch import *;
from infi.bunch import *;

sys.path.append('/opt/dreamfactory/storage/scripting/python/hra')
from common import *;
#from hra2016_func import *;
import hra2016_func ;
import hra2016_util ;

# make blank string into 0
def mk_int(s):
    s = s.strip()
    return int(s) if s else -99

class HRACalcData :
    version = 'HRA2016'         # class variable shared by all instances
    def __init__(self, record, svl):

        self.record = record ;
        # survey variable list
        self.svl = svl;
        print('Calc engine, svl.biolist',svl.biolist);

        
        self.status = 'Ok';
        self.criticalerror = 0;
        self.fstress_score = 0;

        # 1. set defaults
        self.hra_set_defaults();
        print('calc set defaults completed...');
        print('start calc standcalc ...');

        # 2. standardcalc
        self.standardcalc();

        # 3. hra2016_util  -> IHRA_ENGINE


    def add_data(self, key, value):
        self.record.key = value;


    def standardcalc(self):
        record = self.record;
        # self.fstress_score = stress_score1(1,1,1,1,1,1);
        self.fstress_score =  hra2016_func.stress_score(record.ql_overallhealth
                                           , record.sc_sleepduration
                                           , record.ql_lifesatisfaction
                                           , record.ql_personalloss
                                           , record.demo_maritalstatus
                                           , record.ql_socialtiestrength);
        print('calculating stress score');
        record.stress_score = self.fstress_score;
        print('calc: stress_score ',self.fstress_score);
        
        record.ndiseases = self.ndiseases();
        record.nconditions = self.nconditions();

        # [1]
        #$ !! height_total already calculated in HRAData2016.setbiotype() 
        #$ height:=hrec.height_feet*12+nvl(hrec.height_inches,0);
        
        #$ [old] bmi:=hra_func.bmi(hrec.weight,hrec.height_feet*12+nvl(hrec.height_inches,0));
        print('record.bio_weight',record.bio_weight);
        print('record.bio_height_total:',record.bio_height_total);
        
        print('record.bio_height_feet:',record.bio_height_feet);
        print('record.bio_height_inches:',record.bio_height_inches);
        
        record.calc_bmi = hra2016_func.bmi(record.bio_weight,record.bio_height_total);
        print('calc: calc_bmi ',record.calc_bmi );
        

        #$ hrec.ideal_weight:=/*hra_func.ideal_weight(hrec.sex,height,hrec.frame)*/hra_func.bmi_ideal_weight(height,25);
        record.calc_ideal_weight = hra2016_func.bmi_ideal_weight(record.bio_height_total,25)
        print('calc: calc_ideal_weight ',record.calc_ideal_weight );
        
        #$ output_2k.cur_date:=rtrim(to_char(sysdate,'Month'))||to_char(sysdate,' dd, yyyy');
        #$ output_2k.age:=hrec.age;
        #$ output_2k.sex:=hrec.sex;

        # SMOKEOTHER Variable
        record.smokeother = self.smokeother();
        print('tob_cigssmokestatus: ',record.tob_cigssmokestatus);
        if record.tob_cigssmokestatus not in [1,2,3]:
            smoking_status = self.smoking_status();
            # TODO: check on this recoding  
            if smoking_status > 0:
                record.tob_cigssmokestatus = smoking_status;
 
      

     
        # TODO: no database fields for ndiseases , nconditions (need these?)
        
        #$ [old] output_2k.weight_range:=hra_func.bmi_weight_range(height,19,24.9);
        #$ [old] output_2k.goal_weight_range = goal_weight_range();
        #$ [old] profile()

        
        
    def hra_set_defaults(self):
       #  set default values -->
       default = 0;
       record = self.record;
       print('calc engine set defaults...');

       # TODO: check how birthdate is stored
       
       #$ if hrec.age is null then
       #$    hrec.age:=report_util.age(hrec.birthdate,hrec.scan_date);
       #$    !! age_from_birthdate();
       #$ end if;

       
       #$ orig_height:=hrec.height_feet*12+nvl(hrec.height_inches,0);--prepared for missing string and profile bar
       #$ orig_weight:=hrec.weight;
       #$ orig_age:=hrec.age;

       #$ if hrec.age is null then
       #$ hrec.age:=47;
       #$  elsif hrec.age<19 then
       #$      hrec.age:=19;
       #$  elsif hrec.age>99 then
       #$      hrec.age:=99;
       #$  end if;

       # set_default_height_weight;
       #$ if hrec.job_satis>=5 then hrec.job_satis:=null; end if;
       #$ if hrec.ABSENT_DAYS>=7 then hrec.ABSENT_DAYS:=1; end if;

       return default;

    def ndiseases(self):
    ## 1 = never , 2 = in past, 3 = have currently
        rec = self.record ;
        svl = self.svl;
        ndiseases = 0;
        for item in svl.vlist_mdc_disease:
            if (rec[item] == 3 ):
                ndiseases += 1;
 
        return ndiseases
    
    def nconditions(self):
        rec = self.record;
        svl = self.svl ;
        nconditions = 0;
        for item in svl.vlist_mdc_condition:
            print('calc conditions rec[item]: ',rec[item], item)
            if (rec[item] == 3 ):
                nconditions += 1;
        return nconditions;

    def smokeother(self):
        #$ [old] smoke:=nvl(hrec.cigars,0)=1 or nvl(hrec.pipes,0)=1 or nvl(hrec.smokeless_tob,0)=1;
        rec = self.record;
        smokeother = 0;
        if rec.tob_othercigars == 1:
            smokeother = 1
        elif rec.tob_otherpipes == 1:
            smokeother = 1
        elif rec.tob_othersmokeless == 1:
            smokeother = 1
        elif rec.tob_otherecigs == 1:
            smokeother = 1
            
        return smokeother

    def smoking_status(self):
        rec = self.record ;
        smoking_status = 0;
        if rec.tob_cigssmokestatus in [1,2,3]:
            smoking_status = tob_cigssmokestatus
        elif rec.tob_cigsperday > 0:
            smoking_status = 1
        elif rec.tob_cigsyearsquit > 0:
            smoking_status = 2
        elif rec.tob_cigsavgbeforequit > 0:
            smoking_status = 2

        return smoking_status;

        #$ smoking_status:=case when hrec.smoking_status in (1,2,3) then hrec.smoking_status
        #$ when hrec.cigarettes>0 then 1
        #$ when hrec.years_quit>0 or hrec.AVERAGE_SMOKED>0 then 2 end;

    
    






def set_default_height_weight(hrec):

   #  hrec.height_inches:=nvl(hrec.height_inches,0);
   #  hrec.height_feet:=nvl(hrec.height_feet,0);
   
   #  height:=hrec.height_feet*12+hrec.height_inches;
   #  if nvl(hrec.weight,0)=0 and (height<4*12 or height>=8*12) then
   #      if hrec.sex=2 then
   #        hrec.height_feet:=5;
   #        hrec.height_inches:=4;
   #      else
   #        hrec.height_feet:=5;
   #        hrec.height_inches:=9;
   #      end if;
   #  elsif  height>=8*12 then
   #  	   height:=hra_func.bmi_ideal_height(hrec.weight,25);
   #	     	 hrec.height_feet:=least(trunc(height/12),7);
   #  	   hrec.height_inches:=least(11,height-hrec.height_feet*12);
   #  elsif height<4*12 then
   #  	   height:=hra_func.bmi_ideal_height(hrec.weight,25);
   #	     	 hrec.height_feet:=least(7,greatest(trunc(height/12),4));
   #  	   hrec.height_inches:=least(11,greatest(1,height-hrec.height_feet*12));
   #  end if;
   return completed;


   




def age_from_birthdate(birth_date, curr_date):
    # [report_util.age]
    
    #$ if hra_date is null then hra_date:=sysdate; end if;
    #$ calc_age:=to_char(hra_date,'yyyy')-substr(birth_date,5,4);
    #$ if to_char(hra_date,'mm')<substr(birth_date,1,2) or
    #$   (to_char(hra_date,'mm')=substr(birth_date,1,2) and to_char(hra_date,'dd')<substr(birth_date,3,2)) then
    #$   calc_age:=calc_age-1;
    #$ end if;
    #$ if calc_age>1000 or calc_age<10 then return null; end if;
    #$ return calc_age;
    #$   exception
    #$ when others then
    #$    return null;
    return calc_age;
  
def plan_char():
    
    #$   plan_char:=case when (hrec.plan_physical_activity=1 or hrec.plan_lose_weight=1 or hrec.plan_reduce_alcohol=1 
    #$  or hrec.plan_quit_smoking=1 or hrec.plan_reduce_fat=1 or hrec.plan_lower_bp=1 
    #$ or hrec.plan_lower_chol=1 or hrec.plan_cope_stress=1)
    #$  then 'Y' else 'N' end;
    return plan_char;

def goal_weight_range():

    #$goal_weight_range:=case when bmi<30 then null
    #$  when bmi<35 then hra_func.bmi_weight_range(height,25,29.9)
    #$ when bmi>=35 then hra_func.bmi_weight_range(height,30,34.9) end;
    return bmi_weight_range;


	
def output_2k():
                              
##   passwd varchar2(10);
##   record_count integer;
##   label varchar2(20);  --use serial_number for label
##   biomerged varchar2(1); 
##   sex number(1);
##   cur_date varchar2(20);
##   ref_date varchar2(20);
##   age number(3);
##   wellscore number(3);
##   ref_wellscore number(3);
##   access_msg varchar2(200);  --tab delimited
##   lm_msg varchar2(1000); --text include in {} should be bold
##   pos_msg varchar2(1000); --newline delimited
##   neg_msg varchar2(1000); --newline delimited   
##   sug_msg varchar2(1000); --newline delimited
##   detail_msg varchar2(2000); --'|' delimited
##   profile varchar2(400); --tab delimited
##   ref_profile varchar2(400); --tab delimited 
##   weight_range varchar2(10);
##   goal_weight_range varchar2(10);  --new
##   goal_msg varchar2(500);
##   lm_voucher varchar2(1);
##   pilotcode varchar2(1);
##   risk_topic varchar2(100);
##   risk_topic_ns varchar2(100);
##   weight_catno varchar2(2);
##   hdl_str varchar2(100);
##   preventive_services varchar2(400);  --modified, the first character indicates the update status
##   missingstr varchar2(500);
##   smoking_goal varchar2(30);
##  /* cat1 varchar2(3000);
##   cat2 varchar2(3000);
##   cat3 varchar2(3000);
##   cat4 varchar2(3000);
##   cat5 varchar2(3000);
##   cat6 varchar2(3000);
##   cat7 varchar2(3000);
##   cat8 varchar2(3000);
##   cat9 varchar2(3000);
##   cat10 varchar2(3000);
##   topic1 varchar2(30);
##   topic2 varchar2(30);
##   topic3 varchar2(30);
##   topic4 varchar2(30);
##   topic5 varchar2(30);
##   topic6 varchar2(30);
##   topic7 varchar2(30);
##   topic8 varchar2(30);
##   topic9 varchar2(30);
##   topic10 varchar2(30);
##   where1 varchar2(50);
##   where2 varchar2(50);
##   where3 varchar2(50);
##   where4 varchar2(50);
##   where5 varchar2(50);
##   where6 varchar2(50);
##   where7 varchar2(50);
##   where8 varchar2(50);
##   where9 varchar2(50);
##   where10 varchar2(50);
##   goal1 varchar2(50);
##   goal2 varchar2(50);
##   goal3 varchar2(50);
##   goal4 varchar2(50);
##   goal5 varchar2(50);
##   goal6 varchar2(50);
##   goal7 varchar2(50);
##   goal8 varchar2(50);
##   goal9 varchar2(50);
##   goal10 varchar2(50);*/
##   cat category:=category(null,null,null,null,null,null,null,null,null,null);   
##   TOPICS VARCHAR2(10);
##   phone_msg varchar2(4000);
##   
##   ideal varchar2(20);
##   goal varchar2(20);
##   report_date varchar2(30);   
##   sex_str varchar2(20);
    return variable;

def profile():
    
##    output_2k.profile:=case when smoking_status=1 then 1
##when smoking_status=3 then 5
##when nvl(smoking_status,0)=0 then 5
##else case when nvl(hrec.years_quit,0)<=5 then 2
##         when hrec.years_quit<=10 then 3
##         when hrec.years_quit<=20 then 4 else 5 end
##end
##||case smoking_status when 1 then 'Current smoker' when 2 then  'Ex-smoker'
##when 3 then 'Non-smoker'
##else 'Non-smoker' end
##||chr(9)||case when hrec.sbp>0 and hrec.dbp>0 then 
##case when hrec.sbp>=140 and hrec.dbp>=90 then 1
##when hrec.sbp>=140 or hrec.dbp>=90 then 2
##when hrec.sbp between 120 and 139 and hrec.dbp between 80 and 89 then 3
##when hrec.sbp between 120 and 139 or hrec.dbp between 80 and 89 then 4
##when hrec.sbp<120 and hrec.dbp<80 then 5 end
##when hrec.high_bp_when=3 and nvl(hrec.high_bp_meds,0)!=1 and nvl(hrec.high_bp_care,0)!=1 then 1
##else 0 end
##||case when hrec.sbp>0 and hrec.dbp>0 then ltrim(to_char(hrec.sbp))||'/'||ltrim(to_char(hrec.dbp))
##when hrec.high_bp_when=3 and nvl(hrec.high_bp_meds,0)!=1 and nvl(hrec.high_bp_care,0)!=1 then 'High'
##else 'Unknown' end
##||chr(9)||case when hrec.hdl>=hrec.cholesterol and hrec.cholesterol>0 then 0
##when hrec.cholesterol between 0 and 199 then 5
##when hrec.cholesterol<=210 then 3
##when hrec.cholesterol<=220 then 3
##when hrec.cholesterol<=240 then 2
##when hrec.cholesterol>240 then 1
##when hrec.high_chol_when=3 then 1
##when hrec.high_chol_meds=1 then 2
##when hrec.high_chol_care=1 then 2
##/*when hrec.high_chol_when=1 then 5*/
##else 0 end
##||case when hrec.hdl>=hrec.cholesterol and hrec.cholesterol>0
##         then ltrim(to_char(hrec.cholesterol))||' recheck value'
##when hrec.cholesterol>0 then ltrim(to_char(hrec.cholesterol))
##when hrec.high_chol_when=3 then 'High'
##when hrec.high_chol_meds=1 then 'Cholesterol medication'
##when hrec.high_chol_care=1 then 'Under medical care'
##/*when hrec.high_chol_when=1 then 'Normal'*/
##when hrec.unsure_chol=1 then 'Unsure' else 'Unknown'
##end
##||chr(9)||case when bmi<18.5 then 3 when bmi<25 then 5 when bmi<27.5 then 4 when bmi<30 then 3 when bmi>=30 then 1 else 0 end
##||case when nvl(orig_weight,0)=0 and nvl(orig_height,0)=0 then
##        'Weight and height are missing'
##when nvl(orig_weight,0)=0 then
##        'Weight is missing'
##when nvl(orig_height,0)=0 then
##        'Height is missing'
##else
##       ltrim(to_char(hrec.weight))||' lbs'
##end
##||chr(9)||case hrec.physical_activity
##when 1 then 1 when 2 then 3 when 3 then 5 when 4 then 5 else 0 end
##||case hrec.physical_activity
##when 1 then '0-1x'
##when 2 then '1-2x'
##when 3 then '3x'
##when 4 then '4+x'
##else 'Unknown' end;
    return profile;
	


