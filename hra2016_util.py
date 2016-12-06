## "IHRA_ENGINE"."HRA_UTIL"
from infi.bunch import *;

def init():
   temp_heart_attack = 0;
   temp_stroke = 0;
   Has_simple_mortality = False ;
   mortality_name ='';
   default_mortality ='vmortality';

##  1. (hrarec)
def std_calculate(rec):

   std_hraobj_list = ['demo_gender','demo_age']
   std_hraobj = bunch.bunchify({'std_hraobj':1})
   std_hraobj.demo_gender = rec.demo_gender;

   #std_hraobj_list = ['demo_gender','demo_pregnant','demo_age','sbio_height_feet','sbio_height_inches','sbio_weight','sbio_waist_inches','sbio_bpsystolic','sbio_bpdiastolic','sbio_bp_dk','sbio_choltc','sbio_choltc_dk','sbio_cholhdl','sbio_cholhdl_dk','sbio_cholldl','sbio_cholldl_dk','sbio_trig','sbio_trig_dk','sbio_glucose','sbio_glucose_dk','sbio_glucose_testtype','sbio_hba1c','sbio_hba1c_dk','tob_cigssmokestatus','tob_cigsperday','tob_cigsyearssmoked','tob_cigsyearsquit','tob_cigsavgbeforequit','tob_othercigars','tob_otherpipes','tob_othersmokeless','tob_otherecigs','tob_othernone','aod_drugmedfreq','aod_alcoh_drinksperweek','aod_alcoh_drvridedrunkfreq','drive_cardistance','drive_motorcycledistance','drive_seatbeltuse','drive_speed','drive_usuallytravel','nutr_fiberservings','nutr_fatcholservings','physact_vigorousfreq','physact_vigorousminutes','physact_moderatefreq','physact_moderateminutes','physact_strengthfreq','physact_stretchfreq','physact_limitation','physact_sedentarytime','sc_flossfreq','sc_sunscreenfreq','sc_sleepduration','ql_overallhealth','ql_illnessdaysall','ql_lifesatisfaction','ql_socialtiestrength','ql_personalloss','ql_tenseanxiousdepressed','ql_stresseffecthealth','mdc_cancer','mdc_bronchemph','mdc_diabetes','mdc_heartdz','mdc_hibp','mdc_hichol','mdc_stroke','mdc_allergies','mdc_arthritis','mdc_asthma','mdc_backpain','mdc_chrkidneydz','mdc_chrpain','mdc_depression','mdc_prediabetes','mdc_heartburn','mdc_menopause','mdc_migraine','mdc_osteop','mdc_sleepdisorder','mdc_other','mdctx_allergies_meds','mdctx_allergies_care','mdctx_allergies_none','mdctx_arthritis_meds','mdctx_arthritis_care','mdctx_arthritis_none','mdctx_asthma_meds','mdctx_asthma_care','mdctx_asthma_none','mdctx_backpain_meds','mdctx_backpain_care','mdctx_backpain_none','mdctx_bronchemph_meds','mdctx_bronchemph_care','mdctx_bronchemph_none','mdctx_cancer_meds','mdctx_cancer_care','mdctx_cancer_none','mdctx_chrkidneydz_meds','mdctx_chrkidneydz_care','mdctx_chrkidneydz_none','mdctx_chrpain_meds','mdctx_chrpain_care','mdctx_chrpain_none','mdctx_depression_meds','mdctx_depression_care','mdctx_depression_none','mdctx_prediabetes_meds','mdctx_prediabetes_care','mdctx_prediabetes_none','mdctx_diabetes_meds','mdctx_diabetes_care','mdctx_diabetes_none','mdctx_heartburn_meds','mdctx_heartburn_care','mdctx_heartburn_none','mdctx_heartdz_meds','mdctx_heartdz_care','mdctx_heartdz_none','mdctx_hibp_meds','mdctx_hibp_care','mdctx_hibp_none','mdctx_hichol_meds','mdctx_hichol_care','mdctx_hichol_none','mdctx_menopause_meds','mdctx_menopause_care','mdctx_menopause_none','mdctx_migraine_meds','mdctx_migraine_care','mdctx_migraine_none','mdctx_osteop_meds','mdctx_osteop_care','mdctx_osteop_none','mdctx_sleepdisorder_meds','mdctx_sleepdisorder_care','mdctx_sleepdisorder_none','mdctx_stroke_meds','mdctx_stroke_care','mdctx_stroke_none','mdctx_other_meds','mdctx_other_care','mdctx_other_none','wh_hysterectomy','wh_agefirstperiod','wh_agefirstchildborn','famhx_breastcancer','famhx_cancer_mother','famhx_cancer_father','famhx_cancer_grands','famhx_cancer_sibling','famhx_cancer_dk','famhx_diabetes_mother','famhx_diabetes_father','famhx_diabetes_grands','famhx_diabetes_sibling','famhx_diabetes_dk','famhx_heartprob_mother','famhx_heartprob_father','famhx_heartprob_grands','famhx_heartprob_sibling','famhx_heartprob_dk','famhx_hibp_mother','famhx_hibp_father','famhx_hibp_grands','famhx_hibp_sibling','famhx_hibp_dk','famhx_hichol_mother','famhx_hichol_father','famhx_hichol_grands','famhx_hichol_sibling','famhx_hichol_dk','ps_flushot','ps_tetanusshot','ps_bp','ps_chol','ps_dentalexam','ps_cervicalca_paponlytime','ps_cervicalca_paphpvtype','ps_cervicalca_paphpvtime','ps_mammogram','ps_colonca_fobt','ps_colonca_flexsig','ps_colonca_colonoscopy','sc_pastyrmedvisits_office','sc_pastyrmedvisits_er','sc_pastyrmedvisits_hosp','demo_maritalstatus','demo_race','demo_multiracial','demo_education','demo_employstatus','demo_income','plan_physact','plan_weight','plan_alcohol','plan_tobacco','plan_nutrfatchol','plan_bp','plan_chol','plan_stress','info_enhancehealth','info_followup','job_satisfaction','job_illnessdays','job_healthaffectprod'];

   #std_hraobj = {key:rec[key] for key in std_hraobj_list}

##IHRA_ENGINE.STD_HRAOBJ		
##		
##	SEX	NUMBER(1)
##	AGE	NUMBER(3)
##	MET_WEIGHT	NUMBER
##	SBP	NUMBER(3)
##	DBP	NUMBER(3)
##	BP_DESCRIPTION	NUMBER(1)
##	CHOLESTEROL	NUMBER(3)
##	CHOL_RANGE	NUMBER(1)
##	HDL	NUMBER(3)
##	SMOKING_STATUS	NUMBER(1)
##	CIGARETTES	NUMBER(2)
##	YEARS_QUIT	NUMBER(2)
##	AVERAGE_SMOKED	NUMBER(2)
##	CIGARS	NUMBER(2)
##	PIPES	NUMBER(2)
##	SMOKELESS_TOB	NUMBER(2)
##	ALCOHOL_WEEKLY	NUMBER(2)
##	WITH_DRUNK_DRIVER	NUMBER(2)
##	CAR_DRIVING	NUMBER(2)
##	MOTOR_RIDING	NUMBER(2)
##	USE_STBT	NUMBER(3)
##	DRIVE_SPEED	NUMBER(1)
##	USUALLY_TRAVEL	NUMBER(1)
##	DIABETES	NUMBER(1)
##	BREAST_X_RAY	NUMBER(1)
##	BREAST_CANCER	NUMBER(2)
##	HYSTERECTOMY	NUMBER(1)
##	LAST_PAP_SMEAR	NUMBER(1)
##	FIRST_MENSTRUAL	NUMBER(2)
##	FIRST_CHILD	NUMBER(2)
##	EXERCISED_MORE	NUMBER(1)
##	member procedure assign_default,	
##	member procedure modify_default,	
##	static function get_nullobj return	std_hraobj   
   
##    appraisal:=
##    hra_util.std_calculate(
##     std_hraobj(
##      hrec.SEX,
##      hrec.AGE,
##      100*bmi/25     /*hra_func.ideal_weight(hrec.sex,hrec.height_feet*12+nvl(hrec.height_inches,0),hrec.frame)*/,
##      hrec.SBP,
##      hrec.DBP,
##      case when hrec.high_bp_when=3 then 1
##      end,
##      hrec.CHOLESTEROL,
##      case when hrec.unsure_chol=1 then 3 end,
##      hrec.HDL,
   
##      SMOKING_STATUS,
##      case when hrec.smoking_status in (2,3) then 0 else hrec.CIGARETTES end,
##      hrec.YEARS_QUIT,
##      case hrec.average_smoked when 1 then 8 when 2 then 10 when 3 then 16 when 4 then 20 end,
##      case hrec.cigars when 1 then 1 when 2 then 0 end,
##      case hrec.pipes when 1 then 1 when 2 then 0 end,
##      case hrec.smokeless_tob when 1 then 1 when 2 then 0 end,
   
##      hrec.ALCOHOL_WEEKLY,
##      hrec.WITH_DRUNK_DRIVER,
##      case hrec.car_driving when 1 then 1 when 2 then 2 when 3 then 7 when 4 then 12 when 5 then 17 when 6 then 22 when 7 then 31 end,
##      case hrec.motor_riding when 1 then 0 when 2 then 1 when 3 then 2 when 4 then 3 when 5 then 4 when 6 then 5 end,
##      case hrec.use_stbt when 1 then 100 when 2 then 90 when 3 then 80 when 4 then 75 end,
##      hrec.drive_speed,
##      case hrec.usually_travel when 1 then 4 when 2 then 5 when 3 then 6 when 4 then 3 end,
##      case when hrec.diabetes_when=3 then 1 end,
##      case hrec.breast_x_ray when 1 then 1 when 2 then 2 when 3 then 3 when 4 then 4 when 5 then 4 when 6 then 4 when 7 then 5 end,
##      case hrec.breast_cancer when 1 then 0 when 2 then 1 when 3 then 2 end,
##      hrec.hysterectomy,
##      case hrec.last_pap_smear when 1 then 1 when 2 then 2 when 3 then 3 when 4 then 4 when 5 then 4 when 6 then 4 when 7 then 5 end,
##      case hrec.first_menstrual when 1 then 11 when 2 then 12 when 3 then 13 when 4 then 14 end,
##      case hrec.first_child when 1 then 18 when 2 then 22 when 3 then 27 when 4 then 35 end,
##      null
##       ));
   
##      HRA_Util_vars.hrarec:=hrarec;
## 1.1 ==>  
##      HRA_Util_vars.default_and_modify;
## 1.2 ==>  
##      HRA_Util_vars.app_rate:=appraised_rate(HRA_Util_vars.hrarec_with_default, 1);
## 1.2 ==>
##      HRA_Util_vars.ach_rate:=appraised_rate(HRA_Util_vars.hrarec_modified, 1);
##
##      HRA_Util_vars.appraised_death:=0;
##      HRA_Util_vars.achievable_death:=0;
##      for i in 1..HRA_Util_vars.app_rate.count loop
##      	 if HRA_Util_vars.app_rate(i)>0 then HRA_Util_vars.appraised_death:=HRA_Util_vars.appraised_death+HRA_Util_vars.app_rate(i); end if;
##      	 if HRA_Util_vars.ach_rate(i)>HRA_Util_vars.app_rate(i) then HRA_Util_vars.ach_rate(i):=HRA_Util_vars.app_rate(i); end if;
##         if HRA_Util_vars.ach_rate(i)>0 then HRA_Util_vars.achievable_death:=HRA_Util_vars.achievable_death+HRA_Util_vars.ach_rate(i); end if;
##      end loop;
   
##      if HRA_Util_vars.appraised_death>=1000 then HRA_Util_vars.appraised_death:=999.99; end if;
##      if HRA_Util_vars.achievable_death>=1000 then HRA_Util_vars.achievable_death:=999.99; end if;
##      HRA_Util_vars.actual_death:=simple_cal(HRA_Util_vars.actual_mortality.total);
##      HRA_Util_vars.actual_hdeath:=simple_cal(HRA_Util_vars.actual_mortality.heart_attack);
##      HRA_Util_vars.appraised_hdeath:=HRA_Util_vars.app_rate(25);
##      HRA_Util_vars.achievable_hdeath:=HRA_Util_vars.ach_rate(25);
##
##      return HRA_Util_vars.appraisal;
##
   return APPRAISALTYPE;


## 1.1
## !! procedure default_and_modify is
def default_and_modify():

##  begin
##       hrarec_with_default:=hrarec;
## 1.1.1 ==>   
##       hrarec_with_default.assign_default();
##       hrarec_modified:=hrarec_with_default;
## 1.1.2 ==>   
##       hrarec_modified.modify_default();
##  end;
   return 0;

## 1.2
#!! function appraised_rate(hra_rec in out nocopy std_hraobj, default_assigned pls_integer:=null) return float_varray;   
def appraised_rate(hra_rec, std_hraobj, default_assigned ):
   return float_varray;

   if default_assigned > 0 :
      # 1.2.1 ==>
      get_mortality(hra_rec.sex, hra_rec.age) ;  ## put in new var names
      death_rate
      

##
##  	if mortality_name is null then init_mortality; end if;
##  	if default_assigned>0 then
##  		 get_mortality(hra_rec.sex, hra_rec.age);

##  here is the complex part -- each of these is a function
      
##  		 death_rate:=float_varray(simple_cal(HRA_Util_vars.actual_mortality.hiv_aids),
##					mouth_cncr_cal(HRA_Util_vars.actual_mortality.mouth_cncr, hra_rec.sex, hra_rec.age, hra_rec.cigars,
##					hra_rec.pipes, hra_rec.smokeless_tob, hra_rec.smoking_status, hra_rec.cigarettes, hra_rec.ALCOHOL_WEEKLY),
##					throat_cncr_cal(HRA_Util_vars.actual_mortality.throat_cncr, hra_rec.sex, hra_rec.age, hra_rec.cigars,
##									hra_rec.pipes, hra_rec.smokeless_tob, hra_rec.smoking_status, hra_rec.cigarettes, hra_rec.ALCOHOL_WEEKLY),
##								 	esophageal_cncr_cal (HRA_Util_vars.actual_mortality.esophageal_cncr, hra_rec.sex, hra_rec.age,
##									hra_rec.smoking_status, hra_rec.cigarettes, hra_rec.years_quit),
##								simple_cal(HRA_Util_vars.actual_mortality.stomach_cncr),
##								simple_cal(HRA_Util_vars.actual_mortality.colon_cncr),
##								simple_cal(HRA_Util_vars.actual_mortality.rectal_cncr),
##								pancreatic_cncr_cal(HRA_Util_vars.actual_mortality.pancreatic_cncr,
##									hra_rec.sex, hra_rec.age, hra_rec.smoking_status, hra_rec.cigarettes, hra_rec.years_quit),
##								laryngeal_cncr_cal(HRA_Util_vars.actual_mortality.laryngeal_cncr, hra_rec.sex, hra_rec.age,
##									hra_rec.smoking_status, hra_rec.cigarettes, hra_rec.years_quit, hra_rec.average_smoked, hra_rec.ALCOHOL_WEEKLY),
##								lung_cncr_cal(HRA_Util_vars.actual_mortality.lung_cncr, hra_rec.sex, hra_rec.age, hra_rec.smoking_status,
##									hra_rec.cigarettes, hra_rec.average_smoked, hra_rec.years_quit),
##								simple_cal(HRA_Util_vars.actual_mortality.skin_cncr),
##								breast_cncr_cal(HRA_Util_vars.actual_mortality.breast_cncr, hra_rec.sex, hra_rec.age, hra_rec.first_menstrual,
##									hra_rec.first_child, hra_rec.breast_cancer, hra_rec.breast_x_ray),
##								cervical_cncr_cal(HRA_Util_vars.actual_mortality.cervical_cncr, hra_rec.sex, hra_rec.age, hra_rec.smoking_status,
##									hra_rec.hysterectomy, hra_rec.last_pap_smear),
##								uterine_cncr_cal(HRA_Util_vars.actual_mortality.uterine_cncr, hra_rec.sex, hra_rec.age, hra_rec.hysterectomy),
##								simple_cal(HRA_Util_vars.actual_mortality.ovarian_cncr),
##								simple_cal(HRA_Util_vars.actual_mortality.prostatic_cncr),
##								bladder_cncr_cal(HRA_Util_vars.actual_mortality.bladder_cncr, hra_rec.sex, hra_rec.age, hra_rec.smoking_status,
##									hra_rec.cigarettes, hra_rec.average_smoked, hra_rec.years_quit),
##								simple_cal(HRA_Util_vars.actual_mortality.brain_cncr),
##									simple_cal(HRA_Util_vars.actual_mortality.lymphonia),
##								simple_cal(HRA_Util_vars.actual_mortality.leukemia),
##								diabetes_mellitus_cal(HRA_Util_vars.actual_mortality.diabetes_mellitus, hra_rec.sex, hra_rec.age, hra_rec.diabetes),
##								      simple_cal(HRA_Util_vars.actual_mortality.alchohol_toxicity),
##								simple_cal(HRA_Util_vars.actual_mortality.rheumatic_heart),
##								simple_cal(HRA_Util_vars.actual_mortality.hypertensive_heart),
##								heart_attack_cal(HRA_Util_vars.actual_mortality.heart_attack, hra_rec.sex, hra_rec.age,
##								              hra_rec.diabetes, hra_rec.sbp, hra_rec.bp_description, hra_rec.cholesterol,
##									hra_rec.chol_range, hra_rec.hdl, hra_rec.smoking_status, hra_rec.cigarettes, hra_rec.met_weight),
##								stroke_cal(HRA_Util_vars.actual_mortality.stroke, hra_rec.sex, hra_rec.age, hra_rec.diabetes, hra_rec.sbp, hra_rec.cigarettes),
##								simple_cal(HRA_Util_vars.actual_mortality.arterial_vascular),
##									influenza_pneumonia_cal(HRA_Util_vars.actual_mortality.influenza_pheumonia, hra_rec.sex, hra_rec.age,
##									hra_rec.smoking_status, hra_rec.cigarettes),
##								emphysema_chronic_cal(HRA_Util_vars.actual_mortality.emphysema_chronic, hra_rec.sex, hra_rec.age,
##									hra_rec.smoking_status, hra_rec.cigarettes, hra_rec.cigars, hra_rec.pipes, hra_rec.years_quit),
##								simple_cal(HRA_Util_vars.actual_mortality.pheumoconiosis),
##								peptic_ulcer_cal(HRA_Util_vars.actual_mortality.peptic_ulcer, hra_rec.sex, hra_rec.age, hra_rec.smoking_status,
##									hra_rec.cigars, hra_rec.pipes),
##								liver_cirrhosis_cal(HRA_Util_vars.actual_mortality.liver_cirrrhosis, hra_rec.sex, hra_rec.age, hra_rec.ALCOHOL_WEEKLY),
##								kidney_failure_cal(HRA_Util_vars.actual_mortality.kidney_failure, hra_rec.sex, hra_rec.age, hra_rec.diabetes),
##								motor_vehicle_cal(HRA_Util_vars.actual_mortality.motor_vehicle_injury, hra_rec.sex, hra_rec.age,
##									hra_rec.car_driving, hra_rec.motor_riding, hra_rec.use_stbt, hra_rec.usually_travel,
##									hra_rec.drive_speed, hra_rec.with_drunk_driver),
##								simple_cal(HRA_Util_vars.actual_mortality.pedestrian_injury),
##								simple_cal(HRA_Util_vars.actual_mortality.poisoning),
##								simple_cal(HRA_Util_vars.actual_mortality.falling),
##								simple_cal(HRA_Util_vars.actual_mortality.fire_injury),
##								simple_cal(HRA_Util_vars.actual_mortality.drowning),
##								simple_cal(HRA_Util_vars.actual_mortality.suicide),
##								simple_cal(HRA_Util_vars.actual_mortality.homicide_assault),
##								simple_cal(HRA_Util_vars.actual_mortality.unintentional_injury),
##								simple_cal(HRA_Util_vars.actual_mortality.other_cause));
##						if HRA_Util_vars.simple_mortality is not null then
##							  death_rate.extend(50+HRA_Util_vars.simple_mortality.count-death_rate.count);
##							  for i in 1..HRA_Util_vars.simple_mortality.count loop
##							  	  death_rate(i+50):=simple_cal(HRA_Util_vars.simple_mortality(i));
##							  end loop;
##						end if;
##						return death_rate;
##  	else
##  	    hra_rec.assign_default();
##  	   return appraised_rate(hra_rec,1);
##  	end if;
##  end;




## 1.2.1
#!!   procedure get_mortality(sex in number, age in number) is
def get_mortality(sex,age):
   return 0
##  begin
##  	HRA_Util_vars.simple_mortality:=null;
##  	if has_simple_mortality then
##  		 execute immediate 'select mortalities, heart_attack, stroke,simple_mortality from '||mortality_name||' where sex=:sex and age=:age'
##  		    into HRA_Util_vars.actual_mortality, temp_heart_attack, temp_stroke, HRA_Util_vars.simple_mortality using sex,age;
##  	else
##  		 execute immediate 'select mortalities, heart_attack, stroke from '||mortality_name||' where sex=:sex and age=:age'
##  		    into HRA_Util_vars.actual_mortality, temp_heart_attack, temp_stroke using sex,age;
##  	end if;
##  end;
##  -- from get_mortality -> see Mortality type
## -- --IHRA_ENGINE.MORTALITY(0.000177,0.0000044,0.00000333,7.64E-7,0.0000155,0.0000276,0.00000386,0.00000411,4.47E-7,0.0000176,0.0000402,0.0000928,0.0000646,0.00000--559,0.000032,0,0.0000012,0.0000653,0.0000965,0.000104,0.0000832,0.0000185,0.0000257,0.0000172,0.0000589,0.000137,0.0000269,0.0000964,0.00000769,0.000007,0.00-- 000511,0.0000704,0.0000323,0.00126,0.000125,0.00015,0.0000312,0.000072,0.0000462,0.000507,0.000746,0.000236,0.00166,0.006176501)

##! FUNCTION SIMPLE_CAL (mortality NUMBER)
def simple_cal(mortality):
   return float('%.8f' % (mortality*1000))
## (trunc(mortality * 1000,8);

##  RETURN NUMBER IS
##BEGIN
##  RETURN TRUNC(mortality * 1000, 8);
##END;
   
##  std_hraobj(hrec.SEX,
##      hrec.AGE,
##      100*bmi/25     /*hra_func.ideal_weight(hrec.sex,hrec.height_feet*12+nvl(hrec.height_inches,0),hrec.frame)*/,
##      hrec.SBP,
##      hrec.DBP,
##      case when hrec.high_bp_when=3 then 1
##      end,
##      hrec.CHOLESTEROL,
##      case when hrec.unsure_chol=1 then 3 end,
##      hrec.HDL,
##      SMOKING_STATUS,
##      case when hrec.smoking_status in (2,3) then 0 else hrec.CIGARETTES end,
##      hrec.YEARS_QUIT,
##      case hrec.average_smoked when 1 then 8 when 2 then 10 when 3 then 16 when 4 then 20 end,
##      case hrec.cigars when 1 then 1 when 2 then 0 end,
##      case hrec.pipes when 1 then 1 when 2 then 0 end,
##      case hrec.smokeless_tob when 1 then 1 when 2 then 0 end,
##      hrec.ALCOHOL_WEEKLY,
##      hrec.WITH_DRUNK_DRIVER,
##      case hrec.car_driving when 1 then 1 when 2 then 2 when 3 then 7 when 4 then 12 when 5 then 17 when 6 then 22 when 7 then 31 end,
##      case hrec.motor_riding when 1 then 0 when 2 then 1 when 3 then 2 when 4 then 3 when 5 then 4 when 6 then 5 end,
##      case hrec.use_stbt when 1 then 100 when 2 then 90 when 3 then 80 when 4 then 75 end,
##      hrec.drive_speed,
##      case hrec.usually_travel when 1 then 4 when 2 then 5 when 3 then 6 when 4 then 3 end,
##      case when hrec.diabetes_when=3 then 1 end,
##      case hrec.breast_x_ray when 1 then 1 when 2 then 2 when 3 then 3 when 4 then 4 when 5 then 4 when 6 then 4 when 7 then 5 end,
##      case hrec.breast_cancer when 1 then 0 when 2 then 1 when 3 then 2 end,
##      hrec.hysterectomy,
##      case hrec.last_pap_smear when 1 then 1 when 2 then 2 when 3 then 3 when 4 then 4 when 5 then 4 when 6 then 4 when 7 then 5 end,
##      case hrec.first_menstrual when 1 then 11 when 2 then 12 when 3 then 13 when 4 then 14 end,
##      case hrec.first_child when 1 then 18 when 2 then 22 when 3 then 27 when 4 then 35 end,
##      null));

##  CREATE OR REPLACE TYPE "IHRA_ENGINE"."APPRAISALTYPE" as object
##(HEALTH_AGE                                         NUMBER(5,2),
##ACHIEVABLE_AGE                                     NUMBER(5,2),
##ACTUAL_DEATH                                       NUMBER(5,2),
##APPRAISED_DEATH                                    NUMBER(5,2),
##ACHIEVABLE_DEATH                                   NUMBER(5,2),
##ACTUAL_HDEATH                                      NUMBER(5,2),
##APPRAISED_HDEATH                                   NUMBER(5,2),
##ACHIEVABLE_HDEATH                                  NUMBER(5,2));
##


##"HRA_UTIL_VARS" IS
##  function appraisal return appraisaltype is
##  begin
##    	return appraisaltype(health_age,
##            achievable_age,
##            ACTUAL_DEATH,
##            APPRAISED_DEATH,
##            ACHIEVABLE_DEATH,
##            ACTUAL_HDEATH,
##            APPRAISED_HDEATH,
##            ACHIEVABLE_HDEATH);
##  end;
   
##  function appraisal_death_rate return float_varray is
##  begin
##  	 return app_rate;
##  end;
   
##  function achievable_death_rate return float_varray is
##  begin
##  	 return ach_rate;
##  end;
   
##  function actual_death_rate return float_varray is
##     ret_list float_varray;
##  begin
##  	 ret_list:=float_varray(actual_mortality.HIV_AIDS,
##                         actual_mortality.MOUTH_CNCR,
##                         actual_mortality.THROAT_CNCR,
##                         actual_mortality.ESOPHAGEAL_CNCR,
##                         actual_mortality.STOMACH_CNCR,
##                         actual_mortality.COLON_CNCR,
##                         actual_mortality.RECTAL_CNCR,
##                         actual_mortality.PANCREATIC_CNCR,
##                         actual_mortality.LARYNGEAL_CNCR,
##                         actual_mortality.LUNG_CNCR,
##                         actual_mortality.SKIN_CNCR,
##                         actual_mortality.BREAST_CNCR,
##                         actual_mortality.CERVICAL_CNCR,
##                         actual_mortality.UTERINE_CNCR,
##                         actual_mortality.OVARIAN_CNCR,
##                         actual_mortality.PROSTATIC_CNCR,
##                         actual_mortality.BLADDER_CNCR,
##                         actual_mortality.BRAIN_CNCR,
##                         actual_mortality.LYMPHONIA,
##                         actual_mortality.LEUKEMIA,
##                         actual_mortality.DIABETES_MELLITUS,
##                         actual_mortality.ALCHOHOL_TOXICITY,
##                         actual_mortality.RHEUMATIC_HEART,
##                         actual_mortality.HYPERTENSIVE_HEART,
##                         actual_mortality.HEART_ATTACK,
##                         actual_mortality.STROKE,
##                         actual_mortality.ARTERIAL_VASCULAR,
##                         actual_mortality.INFLUENZA_PHEUMONIA,
##                         actual_mortality.EMPHYSEMA_CHRONIC,
##                         actual_mortality.PHEUMOCONIOSIS,
##                         actual_mortality.PEPTIC_ULCER,
##                         actual_mortality.LIVER_CIRRRHOSIS,
##                         actual_mortality.KIDNEY_FAILURE,
##                         actual_mortality.MOTOR_VEHICLE_INJURY,
##                         actual_mortality.PEDESTRIAN_INJURY,
##                         actual_mortality.POISONING,
##                         actual_mortality.FALLING,
##                         actual_mortality.FIRE_INJURY,
##                         actual_mortality.DROWNING,
##                         actual_mortality.SUICIDE,
##                         actual_mortality.HOMICIDE_ASSAULT,
##                         actual_mortality.UNINTENTIONAL_INJURY,
##                         actual_mortality.OTHER_CAUSE);
##  	 if simple_mortality is not null then
##  	 	  ret_list.extend(50+simple_mortality.count-ret_list.count);
##  	 	  for i in 1..simple_mortality.count loop
##  	 	  	 ret_list(50+i):=simple_mortality(i);
##  	 	  end loop;
##  	 else
##  	 	  ret_list.extend(43);
##  	 end if;
##  	 return ret_list;
##  end;
##
   
##function health_age return number is
##begin
##   return TRUNC(AGE_CALCULATION(appraised_death/1000, actual_mortality.total, hrarec_modified.age), 1);
##end;
##
   
##function achievable_age return number is
##begin
##   return TRUNC(AGE_CALCULATION(achievable_death/1000, actual_mortality.total, hrarec_modified.age), 1);
##end;
##
   
##--age_calculation-----------------------------------------------------------------------------
##Function AGE_CALCULATION (risk_score NUMBER, total_risk NUMBER, age NUMBER) RETURN NUMBER IS
##BEGIN
##  return LN(risk_score / total_risk)/ LN(1.08) + age;
##END;
##
##END;


## 1.2.1
##CREATE OR REPLACE TYPE BODY "IHRA_ENGINE"."STD_HRAOBJ" as
##--assign_default-------------------------------------------------------------------------------
##member PROCEDURE ASSIGN_DEFAULT IS
##  total_inches NUMBER;
##  car NUMBER;
##  motor NUMBER;
##BEGIN
##  if hdl>100 or hdl<10 then
##      if sex=2 then
##          hdl:=55;
##      else
##          hdl:=45;
##      end if;
##  end if;
## -- Defaule age
##  IF age<10 THEN
##  	 age:=10;
##  elsIF age>75 THEN
##  	 age:=75;
##  elsif age IS NULL THEN
##  	 age:=35;
##  END IF;
##  if sex is null then	 sex:=1; end if;
##  --rule added by common sense 6/29/02
##  if met_weight between 10 and 900 then null; else met_weight:=100; end if;
##  -- Default BP and cholesterol values
##  IF sbp IS NULL THEN
##    IF bp_description=1 THEN
##      sbp:=160;
##    ELSE
##      sbp:=138;
##    END IF;
##  END IF;
##  IF dbp IS NULL THEN
##    IF bp_description=1 THEN
##      dbp:=90;
##    ELSE
##      dbp:=88;
##    END IF;
##  END IF;
##  -- Default cholesterol range
##  IF chol_range IS NULL and cholesterol IS NULL THEN
##    chol_range := 3;
##  END IF;
##  -- Default smoke related data
##  IF cigarettes IS NULL THEN cigarettes:=0; END IF;
##  IF average_smoked IS NULL THEN average_smoked:=0; END IF;
##  IF cigars IS NULL THEN cigars:=0; END IF;
##  IF smokeless_tob IS NULL THEN smokeless_tob:=0; END IF;
##  IF pipes IS NULL THEN pipes:=0; END IF;
##  IF years_quit IS NULL THEN years_quit:=0; END IF;
##  IF smoking_status IS NULL and cigarettes=0 and average_smoked=0
##     and cigars =0 and pipes =0 and smokeless_tob=0 THEN
##    smoking_status:=3;
##  ELSIF cigarettes > 0 THEN
##    smoking_status:=1;
##  ELSIF average_smoked >0 OR years_quit > 0 THEN
##    smoking_status:=2;
##  ELSE
##    smoking_status:=3;
##  END IF;
##  -- Adjust the default values
##  IF smoking_status=1 THEN
##    IF cigarettes=0 THEN
##      cigarettes:=20;
##      years_quit:=0;
##    END IF;
##  ELSIF smoking_status=2 THEN
##    IF average_smoked=0 THEN
##      average_smoked:=20;
##      cigarettes:=0;
##    END IF;
##    IF years_quit=0 THEN
##      years_quit:=3;
##    END IF;
##  ELSE
##    cigarettes:=0;
##    average_smoked:=0;
##    years_quit:=0;
##  END IF;
##  -- Default motor driving values
##  IF car_driving IS NULL or car_driving>99 or
##     motor_riding IS NULL or motor_riding>99 THEN
##    IF usually_travel=4 or usually_travel=5 or usually_travel=6 THEN
##       car := 10; motor:=0;
##    ELSIF usually_travel=3 THEN
##       car := 2;  motor:=10;
##    ELSE
##       car := 2; motor:=0;
##    END IF;
##  END IF;
##  if alcohol_weekly is null then alcohol_weekly:=0; end if;
##  IF car_driving IS NULL THEN car_driving:=car; END IF;
##  IF motor_riding IS NULL THEN motor_riding:=motor; END IF;
##  IF diabetes IS NULL THEN diabetes:=0; END IF;
##  IF cigarettes IS NULL THEN cigarettes:=0; END IF;
##  IF use_stbt IS NULL THEN use_stbt:=0; END IF;
##  IF drive_speed IS NULL THEN drive_speed:=1; END IF;
##  IF with_drunk_driver IS NULL THEN with_drunk_driver:=0; END IF;
##  IF first_menstrual IS NULL THEN first_menstrual:=13; END IF;
##  IF first_child IS NULL THEN first_child:=99; END IF;
##  IF breast_x_ray IS NULL or breast_x_ray=0 THEN breast_x_ray:=5; END IF;
##  IF hysterectomy IS NULL or hysterectomy=0 THEN hysterectomy:=2; END IF;
##  IF last_pap_smear IS NULL or last_pap_smear=0 THEN last_pap_smear:=4; END IF;
##  IF use_stbt > 100 THEN use_stbt:=100; END IF;
##  IF with_drunk_driver > 20 THEN with_drunk_driver:=20; END IF;
##  IF breast_cancer IS NULL THEN
##    breast_cancer:=0;
##  ELSIF breast_cancer > 2 THEN
##    breast_cancer:=2;
##  END IF;
##END;


## 1.2.2
   
##--Modify_default-------------------------------------------------------------------------------
##member PROCEDURE MODIFY_DEFAULT IS
##  se pls_integer;
##  de pls_integer;
##BEGIN
##  -- Modify questionaire answers in achievable risk calculation
##  -- Calculation total drinks
##  IF alcohol_weekly > 40 THEN
##    alcohol_weekly:=0;
##  ELSE
##    IF 8 <= alcohol_weekly and alcohol_weekly <= 40 THEN
##      alcohol_weekly :=7;
##    END IF;
##  END IF;
##  with_drunk_driver := 0;
##  -- Modify pap_smear and mamo
##  IF sex = 2 THEN
##    IF age >= 50 and breast_x_ray > 2 THEN
##      breast_x_ray := 1;
##    END IF;
##    IF last_pap_smear > 3 THEN
##      last_pap_smear := 1;
##    END IF;
##  END IF;
##  -- Modify smoking-related data
##  IF smoking_status = 1 THEN
##    smoking_status:=2;
##    average_smoked:=cigarettes;
##    cigarettes:=0;
##    years_quit:=1;
##  END IF;
##  cigars:=0;
##  pipes:=0;
##  smokeless_tob:=0;
##  -- Modify blood pressure
##  IF sbp>0 OR dbp>0 OR bp_description=2 THEN
##    se := sbp-138;
##    de := dbp-88;
##    IF sbp>140 OR dbp>88 THEN
##      IF se>=de THEN
##        sbp:=138;
##      ELSE
##        sbp:=sbp-de;
##      END IF;
##    END IF;
##  END IF;
## -- Modify cholesterol, hdl and related data
##  IF cholesterol > 200 THEN
##    cholesterol:=200;
##  END IF;
##  IF hdl > 0 THEN
##    IF cholesterol<150 THEN hdl:=hdl;
##    ELSIF exercised_more=3 and smoking_status=3 and met_weight<120 THEN
##	hdl:=hdl;
##    ELSIF sex=2 and age<40 and hdl<65 THEN
##	hdl:=hdl+5;
##        IF hdl>65 THEN hdl:=65; END IF;
##    ELSIF sex=2 and age>=40 and hdl<60 THEN
##	hdl:=hdl+5;
##        IF hdl>60 THEN hdl:=60; END IF;
##    ELSIF sex=2 and age>=65 and hdl<55 THEN
##	hdl:=hdl+5;
##        IF hdl>55 THEN hdl:=55; END IF;
##    ELSIF sex=1 and age<55 and hdl<55 THEN
##	hdl:=hdl+5;
##        IF hdl>55 THEN hdl:=55; END IF;
##    END IF;
##  END IF;
##
##  use_stbt:=100;
##
##  if met_weight>100 then
##  	met_weight:=100;
##  end if;
##
## drive_speed:=1;
##
##  if nvl(first_child,99)=99 then
##      if age<59 then
##         first_child:=age+1;
##      else
##         first_child:=99;
##      end if;
##  end if;
##END;



##static function get_nullobj return std_hraobj is
##begin
##   return std_hraobj(null,null,null,null,null,null,null,null,null,
##          null,null,null,null,null,null,null,null,null,null,null,
##          null,null,null,null,null,null,null,null,null,null,null);
##end;


