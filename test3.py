
#for /opt/dreamfactory/storage/scripting/python/hra
import json
import sys
import bunch


sys.path.append('/opt/dreamfactory/storage/scripting/python/hra')
from common import *;

#between1 = common.between1;
def test():
    x = HRAData2016({"Account_ID": 476, "Organization_ID": 349,  "Project_ID": 109, "orguserid":"HBI999998" ,"externalsurveyid":"ZHRA12345", "DEMO_GENDER": 1, "DEMO_PREGNANT": 3, "MDC_cancer": 3, "mdc_diabetes": 2, "mdc_other": 1, "mdctx_cancer_meds": 1, "mdctx_other_meds": ""});


class SurveyKeyVars:
# This class processes key variables from an sd_hra POST
   
    def __init__(self, record):
        

        self.errormsg = '';
        self.critical_error = 0;
          
        # fields related to core_person and core_personproject tables
        self.keyvarlist = ['organization_id','project_id','account_id', 'orguserid', 'relationship'];
        self.optionalvarlist = ['person_id'];
        
        self.personlist = ['organization_id','orguserid','firstname', 'lastname', 'middlename','email'];
        self.personlist_ext = ['address1','address2','city','state','zipcode','ssn4','email2','password','username','birth_year','birth_month','birth_day','phone_mobile','phone_main','pin'];
        self.personprojectlist = ['person_id', 'project_id','externalsurveyid','surveycount'];
        self.person_url = '/pgsql-hra15dev/_table/user_person';
        self.personproject_url = '/pgsql-hra15dev/_table/user_personproject';

        self.record = record;
        #set all keys to lowercase
        self.record = setKeysToLower(record);
        self.checkkeyvars();
        self.checkoptvars();
 
    def checkkeyvars(self):
        for item in self.keyvarlist:
            # if item not in data, critical error
            if(item in self.record):
                print('found key: '+item);
            else:
                self.critical_error = 1;
                self.errormsg = 'key variable not found! '+item;
                print(self.errormsg);
        if self.critical_error == 0:        
            for item in self.keyvarlist:
                if isEmpty(self.record[item]):
                    self.critical_error = 1;
                    self.errormsg = 'key variable empty '+item;
                    print(self.errormsg);
    def checkoptvars(self):
        for item in self.optionalvarlist:
            # if item not in data, critical error
            if(item in self.record):
                print('found optional key: '+item);
            else:
                self.record[item] = -9;
 

                
class HRAData_Base:
# This class processes a single HRA survey record from an sd_hra POST

    
    def __init__(self, record, varlist):


        self.varlist = varlist ;
        self.errormsg = '';
        self.critical_error = 0;
          
        # fields related to core_person and core_personproject tables
        self.emptyreclist = [] ;
        self.nullreclist = [];
        #self.records = records ;
        self.record = record;
        #set all keys to lowercase
        self.record = setKeysToLower(record);
        # initialize record
        self.init_rec();

        #self.organization_id = self.record['organization_id'];
        
        print('self.init_rec finished');


        # [todo]  implement self.personproject_insert
        #self.personproject_insert();
        
        # [todo] !!! reset or delete variables that do not exist (-7)


    def init_rec(self):
        print('orig record count: '+str(len(self.record)));
              
        self.varempty();  # set empty variables (variable exists, set to blank string) to -9 and add to self.emptyreclist
        self.varexist();  # set variables that do not exist to -7 (should indicate they are not in questionnaire)
        self.varnull();   # add integer variables that are -7 to self.nullreclist

        print('empty record count: '+str(len(self.emptyreclist)));
        print('null record count: '+str(len(self.nullreclist)));
        self.record_count = len(self.record);
        
   
    def varexist(self):
        for item in self.varlist:
            # if item not in data (null), set to -7
            self.record[item] = self.record[item] if(item in self.record) else -7;

    def varempty(self):
        for item in self.record:
            if isEmpty(self.record[item]):
                # if item is blank (""), set to -9
                #print(item+" is blank");
                self.emptyreclist.append(item);
                self.record[item] = -9;

    def varnull(self):
        for item in self.record:
            if type(self.record[item]) == int:
                if (self.record[item]) == -7:
                    self.nullreclist.append(item);

    def varnulldel(self):
        for item in self.record.keys():
            if type(self.record[item]) == int:
                    if (self.record[item]) == -7:
                        # remove item (will be null in database)
                        #self.record.pop(item, None);
                        del self.record[item];
                        
    def checkkeyvars(self):
        for item in self.keyvarlist:
            # if item not in data, critical error
            if(item in self.record):
                #found ...
                print('found key: '+item);
                #self[item] = self.record[item];
            else:
                self.critical_error = 1;
                self.errormsg = 'key variable not found! '+item;
                print(self.errormsg);


    def person_sp(self):
        print('stored proc person_sp...');

        params =   '{"params": [ { "name": "vorganization_id","value": 349 }, {"name": "vorguserid", "value": "HBI999900" } ]}';
        url = 'pgsql-hra15dev/_func/public.userperson_insert';
        resulta = platform.api.post(url,params);
        print('person_sp after');
        x = resulta.read();
        print('person_sp result.read', x);
        data = bunchify(json.loads(x));
        print('bunchify(json.loads(x)): ', data);
        rec = data[0];
        newv = rec.new;
        person_id = rec.vperson_id;
        print('person_sp person_id', person_id);
        print('person_sp newv', newv);
        
    def person_getid(self):
        # lookup record using orguserid (string variable) and organization_id
        # orguserid is a uniqueid provided by the organization
        # [todo] !!!! need to add spouse field
        orguserid = self.record['orguserid'];
        organization_id = self.record['organization_id'];
        
        filter = "fields=person_id&filter=";
        
        filter += "(orguserid = '"+orguserid+"') AND (organization_id = "+str(organization_id)+")";
        print('person_getid url: '+self.person_url+'?'+filter);

        # !!!!!! this doesn't work ???
        result = platform.api.get(self.person_url+'?'+filter);
        #result = platform['api']['get'](self.person_url+'?'+filter);
        data = bunchify(json.loads(result.read()));

        #print('result.read', result.read);
        print('person data:', data);
    
        if len(data.resource) == 0:
            person_id_exists = 0;
            # INSERT NEW RECORD in user_person
            # [todo]  !!! implement person_insert
            print('person_id NOT found... will insert record');
            #person_insert();
        else:
            # Get the first record 
            r = data.resource[0];
            person_id_exists = 0;
            person_id = r['person_id'];
            record['person_id'] = person_id;
            print('found person_id', person_id);

    def person_insert(self):
        # insert new record into user_person
        postdata = {};  # ? how to format the post data
        
        for item in self.personlist:
            # *item -> keys for person fields
           
            if(item in self.record):
                itemdata = self.record[item];
            # *add itemdata to postdata            
            # result = platform.api.post(self.person_url, postdata);
            # return person_id  (and/or save as self.record["person_id"])

    def personproject_insert(self):
        # insert new record into user_person
        postdata = {};  # ? how to format the post data

        for item in self.personprojectlist:
            if(item in self.record):
                itemdata = self.record[item];
            # * add item to post data
            # result = platform.api.post(self.personproject_url, postdata);
            # return personproject_id  (and/or save as self.record["personproject_id"])
                
                
class HRAData2016(HRAData_Base):
# implements HRA2016 specific variables    
# x = HRAData2016([{"demo_gender": 1, "demo_age": 22, "Demo_pregnant":""}]);
     
     def __init__(self, record):
       print('initialize HRAData2016....');  
       self.varlist = ['demo_gender','demo_pregnant','demo_age','sbio_height_feet','sbio_height_inches','sbio_weight','sbio_waist_inches','sbio_bpsystolic','sbio_bpdiastolic','sbio_bp_dk','sbio_choltc','sbio_choltc_dk','sbio_cholhdl','sbio_cholhdl_dk','sbio_cholldl','sbio_cholldl_dk','sbio_trig','sbio_trig_dk','sbio_glucose','sbio_glucose_dk','sbio_glucose_testtype','sbio_hba1c','sbio_hba1c_dk','tob_cigssmokestatus','tob_cigsperday','tob_cigsyearssmoked','tob_cigsyearsquit','tob_cigsavgbeforequit','tob_othercigars','tob_otherpipes','tob_othersmokeless','tob_otherecigs','tob_othernone','aod_drugmedfreq','aod_alcoh_drinksperweek','aod_alcoh_drvridedrunkfreq','drive_cardistance','drive_motorcycledistance','drive_seatbeltuse','drive_speed','drive_usuallytravel','nutr_fiberservings','nutr_fatcholservings','physact_vigorousfreq','physact_vigorousminutes','physact_moderatefreq','physact_moderateminutes','physact_strengthfreq','physact_stretchfreq','physact_limitation','physact_sedentarytime','sc_flossfreq','sc_sunscreenfreq','sc_sleepduration','ql_overallhealth','ql_illnessdaysall','ql_lifesatisfaction','ql_socialtiestrength','ql_personalloss','ql_tenseanxiousdepressed','ql_stresseffecthealth','mdc_cancer','mdc_bronchemph','mdc_diabetes','mdc_heartdz','mdc_hibp','mdc_hichol','mdc_stroke','mdc_allergies','mdc_arthritis','mdc_asthma','mdc_backpain','mdc_chrkidneydz','mdc_chrpain','mdc_depression','mdc_prediabetes','mdc_heartburn','mdc_menopause','mdc_migraine','mdc_osteop','mdc_sleepdisorder','mdc_other','mdctx_allergies_meds','mdctx_allergies_care','mdctx_allergies_none','mdctx_arthritis_meds','mdctx_arthritis_care','mdctx_arthritis_none','mdctx_asthma_meds','mdctx_asthma_care','mdctx_asthma_none','mdctx_backpain_meds','mdctx_backpain_care','mdctx_backpain_none','mdctx_bronchemph_meds','mdctx_bronchemph_care','mdctx_bronchemph_none','mdctx_cancer_meds','mdctx_cancer_care','mdctx_cancer_none','mdctx_chrkidneydz_meds','mdctx_chrkidneydz_care','mdctx_chrkidneydz_none','mdctx_chrpain_meds','mdctx_chrpain_care','mdctx_chrpain_none','mdctx_depression_meds','mdctx_depression_care','mdctx_depression_none','mdctx_prediabetes_meds','mdctx_prediabetes_care','mdctx_prediabetes_none','mdctx_diabetes_meds','mdctx_diabetes_care','mdctx_diabetes_none','mdctx_heartburn_meds','mdctx_heartburn_care','mdctx_heartburn_none','mdctx_heartdz_meds','mdctx_heartdz_care','mdctx_heartdz_none','mdctx_hibp_meds','mdctx_hibp_care','mdctx_hibp_none','mdctx_hichol_meds','mdctx_hichol_care','mdctx_hichol_none','mdctx_menopause_meds','mdctx_menopause_care','mdctx_menopause_none','mdctx_migraine_meds','mdctx_migraine_care','mdctx_migraine_none','mdctx_osteop_meds','mdctx_osteop_care','mdctx_osteop_none','mdctx_sleepdisorder_meds','mdctx_sleepdisorder_care','mdctx_sleepdisorder_none','mdctx_stroke_meds','mdctx_stroke_care','mdctx_stroke_none','mdctx_other_meds','mdctx_other_care','mdctx_other_none','wh_hysterectomy','wh_agefirstperiod','wh_agefirstchildborn','famhx_breastcancer','famhx_cancer_mother','famhx_cancer_father','famhx_cancer_grands','famhx_cancer_sibling','famhx_cancer_dk','famhx_diabetes_mother','famhx_diabetes_father','famhx_diabetes_grands','famhx_diabetes_sibling','famhx_diabetes_dk','famhx_heartprob_mother','famhx_heartprob_father','famhx_heartprob_grands','famhx_heartprob_sibling','famhx_heartprob_dk','famhx_hibp_mother','famhx_hibp_father','famhx_hibp_grands','famhx_hibp_sibling','famhx_hibp_dk','famhx_hichol_mother','famhx_hichol_father','famhx_hichol_grands','famhx_hichol_sibling','famhx_hichol_dk','ps_flushot','ps_tetanusshot','ps_bp','ps_chol','ps_dentalexam','ps_cervicalca_paponlytime','ps_cervicalca_paphpvtype','ps_cervicalca_paphpvtime','ps_mammogram','ps_colonca_fobt','ps_colonca_flexsig','ps_colonca_colonoscopy','sc_pastyrmedvisits_office','sc_pastyrmedvisits_er','sc_pastyrmedvisits_hosp','demo_maritalstatus','demo_race','demo_multiracial','demo_education','demo_employstatus','demo_income','plan_physact','plan_weight','plan_alcohol','plan_tobacco','plan_nutrfatchol','plan_bp','plan_chol','plan_stress','info_enhancehealth','info_followup','job_satisfaction','job_illnessdays','job_healthaffectprod','wlq_workreqhours','wlq_startontime','wlq_repeatmotions','wlq_useequipment','wlq_concentrate','wlq_helpothers','wlq_doreqwork','wlq_capablework','carehrs_sickchild','carehrs_sickadult','carehrs_sickelder','hpq_weekhrs_past','hpq_weekhrs_expect','hpq_missdays_allself','hpq_missdays_allother','hpq_missdays_ptself','hpq_missdays_ptother','hpq_moredays','hpq_monthhrs_past','hpq_perform_most','hpq_perform_selfyear','hpq_perform_selfmonth'];
       # biometric screening data (add date)
       self.biolist = ['bio_choltc','bio_cholhdl','bio_cholldl','bio_choltc_mmol','bio_cholhdl_mmol','bio_cholldl_mmol','bio_trig','bio_trig_mmol','bio_bpsystolic','bio_bpdiastolic','bio_glucose','bio_glucose_testtype','bio_hba1c','bio_height_feet','bio_height_inches','bio_height_cm','bio_height_total','bio_waist_inches','bio_waist_cm','bio_weight','bio_weight_kg','bio_bodyfat','bio_psa','bio_pulse','bio_chol_dt','bio_bp_dt','bio_bodyfat_dt','bio_glucose_dt','bio_pulse_dt','bio_waist_dt','bio_weight_dt','bio_hba1c_dt','bio_psa_dt'];
       self.mdclist = ['cancer','bronchemph','diabetes','heartdz','hibp','hichol','stroke','allergies','arthritis','asthma','backpain','chrkidneydz','chrpain','depression','prediabetes','heartburn','menopause','migraine','osteop','sleepdisorder','other']
       #[only python3] super(HRAData2016, self).__init__(records, self.varlist);
       # initialize parent class
       HRAData_Base.__init__(self,record,self.varlist)

       print('special recodes  start...');
       # special recodes for known potential issues, run first
       self.recodedata();  

       # check data against min/max values, set to -6 if fails
       print('clean data start...');
       self.cleandata();

       print('skip clean data start...');
       # set var to -8 if should be skipped (no answer because item was skipped due to logic)
       self.skipclean();

       print('skip logic for mdc start...');
       # skip logic for mdc variables
       for item in self.mdclist:
           self.skipclean_mdc(item);
           
       # [todo] !!! add other skip logic    

       
     def skipclean_mdc(self, mdc):
         varmdc = 'mdc_'+mdc;
         var1 = 'mdctx_'+mdc+'_meds'
         var2 = 'mdctx_'+mdc+'_care'
         var3 = 'mdctx_'+mdc+'_none'
       
         record = self.record;
         #print('original '+var1, record[var1]);
         if record[var1] >= 0:
             record[var1] = record[var1] if (between(record[varmdc],2,3)) else -8;
         if record[var1] >= 0:
             record[var2] = record[var2] if (between(record[varmdc],2,3)) else -8;
         if record[var1] >= 0:
             record[var3] = record[var3] if (between(record[varmdc],2,3)) else -8;
         #print('recode '+var1, record[var1]);

     def skipclean_wlq(self):
         record = self.record;
         for item in record:
             if item[1:4] == 'wlq_':
                  if record[item] >= 0:
                     record[item]  = record[item] if (record['demo_employstatus'] == 1) else -8;
                 
     def skipclean_hpq(self):
         record = self.record;
         for item in record:
             
             if item[1:4] == 'hpq_':
                 if record[item] >= 0:
                     record[item]  = record[item] if (record['demo_employstatus'] == 1) else -8;
                 
     def cleandata(self):
        # **** Check min / max -> if outside range, set to -6
        record = self.record;
        record['demo_gender'] =  record['demo_gender'] if ( between1(record['demo_gender'],1,2 ) ) else -6;
        record['demo_pregnant'] =  record['demo_pregnant'] if ( between1(record['demo_pregnant'],1,3 ) ) else -6;
        record['demo_age'] =  record['demo_age'] if ( between1(record['demo_age'],16,120 ) ) else -6;

        record['sbio_height_feet'] =  record['sbio_height_feet'] if ( between1(record['sbio_height_feet'],2,8 ) ) else -6;
        record['sbio_height_inches'] =  record['sbio_height_inches'] if ( between1(record['sbio_height_inches'],0,11 ) ) else -6;
        record['sbio_weight'] =  record['sbio_weight'] if ( between1(record['sbio_weight'],40,800 ) ) else -6;
        record['sbio_waist_inches'] =  record['sbio_waist_inches'] if ( between1(record['sbio_waist_inches'],10,99 ) ) else -6;
        record['sbio_bpsystolic'] =  record['sbio_bpsystolic'] if ( between1(record['sbio_bpsystolic'],50,350 ) ) else -6;
        record['sbio_bpdiastolic'] =  record['sbio_bpdiastolic'] if ( between1(record['sbio_bpdiastolic'],30,250 ) ) else -6;
        record['sbio_choltc'] =  record['sbio_choltc'] if ( between1(record['sbio_choltc'],60,800 ) ) else -6;
        record['sbio_cholhdl'] =  record['sbio_cholhdl'] if ( between1(record['sbio_cholhdl'],10,400 ) ) else -6;
        record['sbio_cholldl'] =  record['sbio_cholldl'] if ( between1(record['sbio_cholldl'],5,800 ) ) else -6;
        record['sbio_trig'] =  record['sbio_trig'] if ( between1(record['sbio_trig'],5,4000 ) ) else -6;
        record['sbio_glucose'] =  record['sbio_glucose'] if ( between1(record['sbio_glucose'],30,700 ) ) else -6;
        record['sbio_glucose_testtype'] =  record['sbio_glucose_testtype'] if ( between1(record['sbio_glucose_testtype'],1,3 ) ) else -6;
        record['sbio_hba1c'] =  record['sbio_hba1c'] if ( between1(record['sbio_hba1c'],3,30 ) ) else -6;

        record['tob_cigsperday'] =  record['tob_cigsperday'] if ( between1(record['tob_cigsperday'],1,99 ) ) else -6;
        record['tob_cigsyearssmoked'] =  record['tob_cigsyearssmoked'] if ( between1(record['tob_cigsyearssmoked'],0,99 ) ) else -6;
        record['tob_cigsyearsquit'] =  record['tob_cigsyearsquit'] if ( between1(record['tob_cigsyearsquit'],0,99 ) ) else -6;
        record['tob_cigsavgbeforequit'] =  record['tob_cigsavgbeforequit'] if ( between1(record['tob_cigsavgbeforequit'],1,3 ) ) else -6;
        record['tob_otherecigs'] =  record['tob_otherecigs'] if ( between1(record['tob_otherecigs'],1,2 ) ) else -6;

        record['aod_drugmedfreq'] =  record['aod_drugmedfreq'] if ( between1(record['aod_drugmedfreq'],1,3 ) ) else -6;
        record['aod_alcoh_drinksperweek'] =  record['aod_alcoh_drinksperweek'] if ( between1(record['aod_alcoh_drinksperweek'],0,99 ) ) else -6;
        record['aod_alcoh_drvridedrunkfreq'] =  record['aod_alcoh_drvridedrunkfreq'] if ( between1(record['aod_alcoh_drvridedrunkfreq'],0,99 ) ) else -6;
        record['drive_cardistance'] =  record['drive_cardistance'] if ( between1(record['drive_cardistance'],1,8 ) ) else -6;
        record['drive_motorcycledistance'] =  record['drive_motorcycledistance'] if ( between1(record['drive_motorcycledistance'],1,7 ) ) else -6;
        record['drive_seatbeltuse'] =  record['drive_seatbeltuse'] if ( between1(record['drive_seatbeltuse'],1,4 ) ) else -6;
        record['drive_speed'] =  record['drive_speed'] if ( between1(record['drive_speed'],1,3 ) ) else -6;
        record['drive_usuallytravel'] =  record['drive_usuallytravel'] if ( between1(record['drive_usuallytravel'],1,5 ) ) else -6;
        record['nutr_fiberservings'] =  record['nutr_fiberservings'] if ( between1(record['nutr_fiberservings'],1,4 ) ) else -6;
        record['nutr_fatcholservings'] =  record['nutr_fatcholservings'] if ( between1(record['nutr_fatcholservings'],1,4 ) ) else -6;
        record['physact_vigorousfreq'] =  record['physact_vigorousfreq'] if ( between1(record['physact_vigorousfreq'],0,99 ) ) else -6;
        record['physact_vigorousminutes'] =  record['physact_vigorousminutes'] if ( between1(record['physact_vigorousminutes'],1,999 ) ) else -6;
        record['physact_moderatefreq'] =  record['physact_moderatefreq'] if ( between1(record['physact_moderatefreq'],0,99 ) ) else -6;
        record['physact_moderateminutes'] =  record['physact_moderateminutes'] if ( between1(record['physact_moderateminutes'],1,999 ) ) else -6;
        record['physact_strengthfreq'] =  record['physact_strengthfreq'] if ( between1(record['physact_strengthfreq'],0,99 ) ) else -6;
        record['physact_stretchfreq'] =  record['physact_stretchfreq'] if ( between1(record['physact_stretchfreq'],0,99 ) ) else -6;
        record['physact_limitation'] =  record['physact_limitation'] if ( between1(record['physact_limitation'],1,2 ) ) else -6;
        record['physact_sedentarytime'] =  record['physact_sedentarytime'] if ( between1(record['physact_sedentarytime'],0,24 ) ) else -6;
        record['sc_flossfreq'] =  record['sc_flossfreq'] if ( between1(record['sc_flossfreq'],1,5 ) ) else -6;
        record['sc_sunscreenfreq'] =  record['sc_sunscreenfreq'] if ( between1(record['sc_sunscreenfreq'],1,4 ) ) else -6;
        record['sc_sleepduration'] =  record['sc_sleepduration'] if ( between1(record['sc_sleepduration'],1,5 ) ) else -6;
        record['ql_overallhealth'] =  record['ql_overallhealth'] if ( between1(record['ql_overallhealth'],1,5 ) ) else -6;
        record['ql_illnessdaysall'] =  record['ql_illnessdaysall'] if ( between1(record['ql_illnessdaysall'],1,6 ) ) else -6;
        record['ql_lifesatisfaction'] =  record['ql_lifesatisfaction'] if ( between1(record['ql_lifesatisfaction'],1,4 ) ) else -6;
        record['ql_socialtiestrength'] =  record['ql_socialtiestrength'] if ( between1(record['ql_socialtiestrength'],1,4 ) ) else -6;
        record['ql_personalloss'] =  record['ql_personalloss'] if ( between1(record['ql_personalloss'],1,3 ) ) else -6;
        record['ql_tenseanxiousdepressed'] =  record['ql_tenseanxiousdepressed'] if ( between1(record['ql_tenseanxiousdepressed'],1,4 ) ) else -6;
        record['ql_stresseffecthealth'] =  record['ql_stresseffecthealth'] if ( between1(record['ql_stresseffecthealth'],1,4 ) ) else -6;
        record['mdc_cancer'] =  record['mdc_cancer'] if ( between1(record['mdc_cancer'],1,3 ) ) else -6;
        record['mdc_bronchemph'] =  record['mdc_bronchemph'] if ( between1(record['mdc_bronchemph'],1,3 ) ) else -6;
        record['mdc_diabetes'] =  record['mdc_diabetes'] if ( between1(record['mdc_diabetes'],1,3 ) ) else -6;
        record['mdc_heartdz'] =  record['mdc_heartdz'] if ( between1(record['mdc_heartdz'],1,3 ) ) else -6;
        record['mdc_hibp'] =  record['mdc_hibp'] if ( between1(record['mdc_hibp'],1,3 ) ) else -6;
        record['mdc_hichol'] =  record['mdc_hichol'] if ( between1(record['mdc_hichol'],1,3 ) ) else -6;
        record['mdc_stroke'] =  record['mdc_stroke'] if ( between1(record['mdc_stroke'],1,3 ) ) else -6;
        record['mdc_allergies'] =  record['mdc_allergies'] if ( between1(record['mdc_allergies'],1,3 ) ) else -6;
        record['mdc_arthritis'] =  record['mdc_arthritis'] if ( between1(record['mdc_arthritis'],1,3 ) ) else -6;
        record['mdc_asthma'] =  record['mdc_asthma'] if ( between1(record['mdc_asthma'],1,3 ) ) else -6;
        record['mdc_backpain'] =  record['mdc_backpain'] if ( between1(record['mdc_backpain'],1,3 ) ) else -6;
        record['mdc_chrkidneydz'] =  record['mdc_chrkidneydz'] if ( between1(record['mdc_chrkidneydz'],1,3 ) ) else -6;
        record['mdc_chrpain'] =  record['mdc_chrpain'] if ( between1(record['mdc_chrpain'],1,3 ) ) else -6;
        record['mdc_depression'] =  record['mdc_depression'] if ( between1(record['mdc_depression'],1,3 ) ) else -6;
        record['mdc_prediabetes'] =  record['mdc_prediabetes'] if ( between1(record['mdc_prediabetes'],1,3 ) ) else -6;
        record['mdc_heartburn'] =  record['mdc_heartburn'] if ( between1(record['mdc_heartburn'],1,3 ) ) else -6;
        record['mdc_menopause'] =  record['mdc_menopause'] if ( between1(record['mdc_menopause'],1,3 ) ) else -6;
        record['mdc_migraine'] =  record['mdc_migraine'] if ( between1(record['mdc_migraine'],1,3 ) ) else -6;
        record['mdc_osteop'] =  record['mdc_osteop'] if ( between1(record['mdc_osteop'],1,3 ) ) else -6;
        record['mdc_sleepdisorder'] =  record['mdc_sleepdisorder'] if ( between1(record['mdc_sleepdisorder'],1,3 ) ) else -6;
        record['mdc_other'] =  record['mdc_other'] if ( between1(record['mdc_other'],1,3 ) ) else -6;
        record['wh_hysterectomy'] =  record['wh_hysterectomy'] if ( between1(record['wh_hysterectomy'],1,4 ) ) else -6;
        record['wh_agefirstperiod'] =  record['wh_agefirstperiod'] if ( between1(record['wh_agefirstperiod'],1,4 ) ) else -6;
        record['wh_agefirstchildborn'] =  record['wh_agefirstchildborn'] if ( between1(record['wh_agefirstchildborn'],1,5 ) ) else -6;
        record['famhx_breastcancer'] =  record['famhx_breastcancer'] if ( between1(record['famhx_breastcancer'],1,4 ) ) else -6;
        record['ps_flushot'] =  record['ps_flushot'] if ( between1(record['ps_flushot'],1,4 ) ) else -6;
        record['ps_tetanusshot'] =  record['ps_tetanusshot'] if ( between1(record['ps_tetanusshot'],1,4 ) ) else -6;
        record['ps_bp'] =  record['ps_bp'] if ( between1(record['ps_bp'],1,4 ) ) else -6;
        record['ps_chol'] =  record['ps_chol'] if ( between1(record['ps_chol'],1,4 ) ) else -6;
        record['ps_dentalexam'] =  record['ps_dentalexam'] if ( between1(record['ps_dentalexam'],1,4 ) ) else -6;
        record['ps_cervicalca_paponlytime'] =  record['ps_cervicalca_paponlytime'] if ( between1(record['ps_cervicalca_paponlytime'],1,4 ) ) else -6;
        record['ps_cervicalca_paphpvtype'] =  record['ps_cervicalca_paphpvtype'] if ( between1(record['ps_cervicalca_paphpvtype'],1,4 ) ) else -6;
        record['ps_cervicalca_paphpvtime'] =  record['ps_cervicalca_paphpvtime'] if ( between1(record['ps_cervicalca_paphpvtime'],1,4 ) ) else -6;
        record['ps_mammogram'] =  record['ps_mammogram'] if ( between1(record['ps_mammogram'],1,5 ) ) else -6;
        record['ps_colonca_fobt'] =  record['ps_colonca_fobt'] if ( between1(record['ps_colonca_fobt'],1,3 ) ) else -6;
        record['ps_colonca_flexsig'] =  record['ps_colonca_flexsig'] if ( between1(record['ps_colonca_flexsig'],1,3 ) ) else -6;
        record['ps_colonca_colonoscopy'] =  record['ps_colonca_colonoscopy'] if ( between1(record['ps_colonca_colonoscopy'],1,3 ) ) else -6;
        record['sc_pastyrmedvisits_office'] =  record['sc_pastyrmedvisits_office'] if ( between1(record['sc_pastyrmedvisits_office'],1,4 ) ) else -6;
        record['sc_pastyrmedvisits_er'] =  record['sc_pastyrmedvisits_er'] if ( between1(record['sc_pastyrmedvisits_er'],1,4 ) ) else -6;
        record['sc_pastyrmedvisits_hosp'] =  record['sc_pastyrmedvisits_hosp'] if ( between1(record['sc_pastyrmedvisits_hosp'],1,4 ) ) else -6;
        record['demo_maritalstatus'] =  record['demo_maritalstatus'] if ( between1(record['demo_maritalstatus'],1,6 ) ) else -6;
        record['demo_race'] =  record['demo_race'] if ( between1(record['demo_race'],1,6 ) ) else -6;
        record['demo_multiracial'] =  record['demo_multiracial'] if ( between1(record['demo_multiracial'],1,2 ) ) else -6;
        record['demo_education'] =  record['demo_education'] if ( between1(record['demo_education'],1,6 ) ) else -6;
        record['demo_employstatus'] =  record['demo_employstatus'] if ( between1(record['demo_employstatus'],1,2 ) ) else -6;
        record['demo_income'] =  record['demo_income'] if ( between1(record['demo_income'],1,5 ) ) else -6;
        record['plan_physact'] =  record['plan_physact'] if ( between1(record['plan_physact'],1,4 ) ) else -6;
        record['plan_weight'] =  record['plan_weight'] if ( between1(record['plan_weight'],1,4 ) ) else -6;
        record['plan_alcohol'] =  record['plan_alcohol'] if ( between1(record['plan_alcohol'],1,4 ) ) else -6;
        record['plan_tobacco'] =  record['plan_tobacco'] if ( between1(record['plan_tobacco'],1,4 ) ) else -6;
        record['plan_nutrfatchol'] =  record['plan_nutrfatchol'] if ( between1(record['plan_nutrfatchol'],1,4 ) ) else -6;
        record['plan_bp'] =  record['plan_bp'] if ( between1(record['plan_bp'],1,4 ) ) else -6;
        record['plan_chol'] =  record['plan_chol'] if ( between1(record['plan_chol'],1,4 ) ) else -6;
        record['plan_stress'] =  record['plan_stress'] if ( between1(record['plan_stress'],1,4 ) ) else -6;
        record['info_enhancehealth'] =  record['info_enhancehealth'] if ( between1(record['info_enhancehealth'],1,3 ) ) else -6;
        record['info_followup'] =  record['info_followup'] if ( between1(record['info_followup'],1,2 ) ) else -6;
        record['job_satisfaction'] =  record['job_satisfaction'] if ( between1(record['job_satisfaction'],1,5 ) ) else -6;
        record['job_illnessdays'] =  record['job_illnessdays'] if ( between1(record['job_illnessdays'],1,7 ) ) else -6;
        record['job_healthaffectprod'] =  record['job_healthaffectprod'] if ( between1(record['job_healthaffectprod'],1,6 ) ) else -6;
        record['wlq_workreqhours'] =  record['wlq_workreqhours'] if ( between1(record['wlq_workreqhours'],1,6 ) ) else -6;
        record['wlq_startontime'] =  record['wlq_startontime'] if ( between1(record['wlq_startontime'],1,6 ) ) else -6;
        record['wlq_repeatmotions'] =  record['wlq_repeatmotions'] if ( between1(record['wlq_repeatmotions'],1,6 ) ) else -6;
        record['wlq_useequipment'] =  record['wlq_useequipment'] if ( between1(record['wlq_useequipment'],1,6 ) ) else -6;
        record['wlq_concentrate'] =  record['wlq_concentrate'] if ( between1(record['wlq_concentrate'],1,6 ) ) else -6;
        record['wlq_helpothers'] =  record['wlq_helpothers'] if ( between1(record['wlq_helpothers'],1,6 ) ) else -6;
        record['wlq_doreqwork'] =  record['wlq_doreqwork'] if ( between1(record['wlq_doreqwork'],1,6 ) ) else -6;
        record['wlq_capablework'] =  record['wlq_capablework'] if ( between1(record['wlq_capablework'],1,6 ) ) else -6;
        record['carehrs_sickchild'] =  record['carehrs_sickchild'] if ( between1(record['carehrs_sickchild'],1,5 ) ) else -6;
        record['carehrs_sickadult'] =  record['carehrs_sickadult'] if ( between1(record['carehrs_sickadult'],1,5 ) ) else -6;
        record['carehrs_sickelder'] =  record['carehrs_sickelder'] if ( between1(record['carehrs_sickelder'],1,5 ) ) else -6;
        record['hpq_weekhrs_past'] =  record['hpq_weekhrs_past'] if ( between1(record['hpq_weekhrs_past'],0,97 ) ) else -6;
        record['hpq_weekhrs_expect'] =  record['hpq_weekhrs_expect'] if ( between1(record['hpq_weekhrs_expect'],0,97 ) ) else -6;
        record['hpq_missdays_allself'] =  record['hpq_missdays_allself'] if ( between1(record['hpq_missdays_allself'],0,28 ) ) else -6;
        record['hpq_missdays_allother'] =  record['hpq_missdays_allother'] if ( between1(record['hpq_missdays_allother'],0,28 ) ) else -6;
        record['hpq_missdays_ptself'] =  record['hpq_missdays_ptself'] if ( between1(record['hpq_missdays_ptself'],0,28 ) ) else -6;
        record['hpq_missdays_ptother'] =  record['hpq_missdays_ptother'] if ( between1(record['hpq_missdays_ptother'],0,28 ) ) else -6;
        record['hpq_moredays'] =  record['hpq_moredays'] if ( between1(record['hpq_moredays'],0,28 ) ) else -6;
        record['hpq_monthhrs_past'] =  record['hpq_monthhrs_past'] if ( between1(record['hpq_monthhrs_past'],0,672 ) ) else -6;
        record['hpq_perform_most'] =  record['hpq_perform_most'] if ( between1(record['hpq_perform_most'],1,11 ) ) else -6;
        record['hpq_perform_selfyear'] =  record['hpq_perform_selfyear'] if ( between1(record['hpq_perform_selfyear'],1,11 ) ) else -6;
        record['hpq_perform_selfmonth'] =  record['hpq_perform_selfmonth'] if ( between1(record['hpq_perform_selfmonth'],1,11 ) ) else -6;

        # *** Checkboxes
        # [todo] !!! ? set to 0 if not skipped and no answer 

        record.sbio_bp_dk = record.sbio_bp_dk if (record.sbio_bp_dk <= 1 ) else -6;
        record.sbio_choltc_dk = record.sbio_choltc_dk if (record.sbio_choltc_dk <= 1 ) else -6;
        record.sbio_cholhdl_dk = record.sbio_cholhdl_dk if (record.sbio_cholhdl_dk <= 1 ) else -6;
        record.sbio_cholldl_dk = record.sbio_cholldl_dk if (record.sbio_cholldl_dk <= 1 ) else -6;
        record.sbio_trig_dk = record.sbio_trig_dk if (record.sbio_trig_dk <= 1 ) else -6;
        record.sbio_glucose_dk = record.sbio_glucose_dk if (record.sbio_glucose_dk <= 1 ) else -6;
        record.sbio_hba1c_dk = record.sbio_hba1c_dk if (record.sbio_hba1c_dk <= 1 ) else -6;
        record.tob_othercigars = record.tob_othercigars if (record.tob_othercigars <= 1 ) else -6;
        record.tob_otherpipes = record.tob_otherpipes if (record.tob_otherpipes <= 1 ) else -6;
        record.tob_othersmokeless = record.tob_othersmokeless if (record.tob_othersmokeless <= 1 ) else -6;
        record.tob_otherecigs = record.tob_otherecigs if (record.tob_otherecigs <= 1 ) else -6;
        record.tob_othernone = record.tob_othernone if (record.tob_othernone <= 1 ) else -6;
        record.mdctx_allergies_meds = record.mdctx_allergies_meds if (record.mdctx_allergies_meds <= 1 ) else -6;
        record.mdctx_allergies_care = record.mdctx_allergies_care if (record.mdctx_allergies_care <= 1 ) else -6;
        record.mdctx_allergies_none = record.mdctx_allergies_none if (record.mdctx_allergies_none <= 1 ) else -6;
        record.mdctx_arthritis_meds = record.mdctx_arthritis_meds if (record.mdctx_arthritis_meds <= 1 ) else -6;
        record.mdctx_arthritis_care = record.mdctx_arthritis_care if (record.mdctx_arthritis_care <= 1 ) else -6;
        record.mdctx_arthritis_none = record.mdctx_arthritis_none if (record.mdctx_arthritis_none <= 1 ) else -6;
        record.mdctx_asthma_meds = record.mdctx_asthma_meds if (record.mdctx_asthma_meds <= 1 ) else -6;
        record.mdctx_asthma_care = record.mdctx_asthma_care if (record.mdctx_asthma_care <= 1 ) else -6;
        record.mdctx_asthma_none = record.mdctx_asthma_none if (record.mdctx_asthma_none <= 1 ) else -6;
        record.mdctx_backpain_meds = record.mdctx_backpain_meds if (record.mdctx_backpain_meds <= 1 ) else -6;
        record.mdctx_backpain_care = record.mdctx_backpain_care if (record.mdctx_backpain_care <= 1 ) else -6;
        record.mdctx_backpain_none = record.mdctx_backpain_none if (record.mdctx_backpain_none <= 1 ) else -6;
        record.mdctx_bronchemph_meds = record.mdctx_bronchemph_meds if (record.mdctx_bronchemph_meds <= 1 ) else -6;
        record.mdctx_bronchemph_care = record.mdctx_bronchemph_care if (record.mdctx_bronchemph_care <= 1 ) else -6;
        record.mdctx_bronchemph_none = record.mdctx_bronchemph_none if (record.mdctx_bronchemph_none <= 1 ) else -6;
        record.mdctx_cancer_meds = record.mdctx_cancer_meds if (record.mdctx_cancer_meds <= 1 ) else -6;
        record.mdctx_cancer_care = record.mdctx_cancer_care if (record.mdctx_cancer_care <= 1 ) else -6;
        record.mdctx_cancer_none = record.mdctx_cancer_none if (record.mdctx_cancer_none <= 1 ) else -6;
        record.mdctx_chrkidneydz_meds = record.mdctx_chrkidneydz_meds if (record.mdctx_chrkidneydz_meds <= 1 ) else -6;
        record.mdctx_chrkidneydz_care = record.mdctx_chrkidneydz_care if (record.mdctx_chrkidneydz_care <= 1 ) else -6;
        record.mdctx_chrkidneydz_none = record.mdctx_chrkidneydz_none if (record.mdctx_chrkidneydz_none <= 1 ) else -6;
        record.mdctx_chrpain_meds = record.mdctx_chrpain_meds if (record.mdctx_chrpain_meds <= 1 ) else -6;
        record.mdctx_chrpain_care = record.mdctx_chrpain_care if (record.mdctx_chrpain_care <= 1 ) else -6;
        record.mdctx_chrpain_none = record.mdctx_chrpain_none if (record.mdctx_chrpain_none <= 1 ) else -6;
        record.mdctx_depression_meds = record.mdctx_depression_meds if (record.mdctx_depression_meds <= 1 ) else -6;
        record.mdctx_depression_care = record.mdctx_depression_care if (record.mdctx_depression_care <= 1 ) else -6;
        record.mdctx_depression_none = record.mdctx_depression_none if (record.mdctx_depression_none <= 1 ) else -6;
        record.mdctx_prediabetes_meds = record.mdctx_prediabetes_meds if (record.mdctx_prediabetes_meds <= 1 ) else -6;
        record.mdctx_prediabetes_care = record.mdctx_prediabetes_care if (record.mdctx_prediabetes_care <= 1 ) else -6;
        record.mdctx_prediabetes_none = record.mdctx_prediabetes_none if (record.mdctx_prediabetes_none <= 1 ) else -6;
        record.mdctx_diabetes_meds = record.mdctx_diabetes_meds if (record.mdctx_diabetes_meds <= 1 ) else -6;
        record.mdctx_diabetes_care = record.mdctx_diabetes_care if (record.mdctx_diabetes_care <= 1 ) else -6;
        record.mdctx_diabetes_none = record.mdctx_diabetes_none if (record.mdctx_diabetes_none <= 1 ) else -6;
        record.mdctx_heartburn_meds = record.mdctx_heartburn_meds if (record.mdctx_heartburn_meds <= 1 ) else -6;
        record.mdctx_heartburn_care = record.mdctx_heartburn_care if (record.mdctx_heartburn_care <= 1 ) else -6;
        record.mdctx_heartburn_none = record.mdctx_heartburn_none if (record.mdctx_heartburn_none <= 1 ) else -6;
        record.mdctx_heartdz_meds = record.mdctx_heartdz_meds if (record.mdctx_heartdz_meds <= 1 ) else -6;
        record.mdctx_heartdz_care = record.mdctx_heartdz_care if (record.mdctx_heartdz_care <= 1 ) else -6;
        record.mdctx_heartdz_none = record.mdctx_heartdz_none if (record.mdctx_heartdz_none <= 1 ) else -6;
        record.mdctx_hibp_meds = record.mdctx_hibp_meds if (record.mdctx_hibp_meds <= 1 ) else -6;
        record.mdctx_hibp_care = record.mdctx_hibp_care if (record.mdctx_hibp_care <= 1 ) else -6;
        record.mdctx_hibp_none = record.mdctx_hibp_none if (record.mdctx_hibp_none <= 1 ) else -6;
        record.mdctx_hichol_meds = record.mdctx_hichol_meds if (record.mdctx_hichol_meds <= 1 ) else -6;
        record.mdctx_hichol_care = record.mdctx_hichol_care if (record.mdctx_hichol_care <= 1 ) else -6;
        record.mdctx_hichol_none = record.mdctx_hichol_none if (record.mdctx_hichol_none <= 1 ) else -6;
        record.mdctx_menopause_meds = record.mdctx_menopause_meds if (record.mdctx_menopause_meds <= 1 ) else -6;
        record.mdctx_menopause_care = record.mdctx_menopause_care if (record.mdctx_menopause_care <= 1 ) else -6;
        record.mdctx_menopause_none = record.mdctx_menopause_none if (record.mdctx_menopause_none <= 1 ) else -6;
        record.mdctx_migraine_meds = record.mdctx_migraine_meds if (record.mdctx_migraine_meds <= 1 ) else -6;
        record.mdctx_migraine_care = record.mdctx_migraine_care if (record.mdctx_migraine_care <= 1 ) else -6;
        record.mdctx_migraine_none = record.mdctx_migraine_none if (record.mdctx_migraine_none <= 1 ) else -6;
        record.mdctx_osteop_meds = record.mdctx_osteop_meds if (record.mdctx_osteop_meds <= 1 ) else -6;
        record.mdctx_osteop_care = record.mdctx_osteop_care if (record.mdctx_osteop_care <= 1 ) else -6;
        record.mdctx_osteop_none = record.mdctx_osteop_none if (record.mdctx_osteop_none <= 1 ) else -6;
        record.mdctx_sleepdisorder_meds = record.mdctx_sleepdisorder_meds if (record.mdctx_sleepdisorder_meds <= 1 ) else -6;
        record.mdctx_sleepdisorder_care = record.mdctx_sleepdisorder_care if (record.mdctx_sleepdisorder_care <= 1 ) else -6;
        record.mdctx_sleepdisorder_none = record.mdctx_sleepdisorder_none if (record.mdctx_sleepdisorder_none <= 1 ) else -6;
        record.mdctx_stroke_meds = record.mdctx_stroke_meds if (record.mdctx_stroke_meds <= 1 ) else -6;
        record.mdctx_stroke_care = record.mdctx_stroke_care if (record.mdctx_stroke_care <= 1 ) else -6;
        record.mdctx_stroke_none = record.mdctx_stroke_none if (record.mdctx_stroke_none <= 1 ) else -6;
        record.mdctx_other_meds = record.mdctx_other_meds if (record.mdctx_other_meds <= 1 ) else -6;
        record.mdctx_other_care = record.mdctx_other_care if (record.mdctx_other_care <= 1 ) else -6;
        record.mdctx_other_none = record.mdctx_other_none if (record.mdctx_other_none <= 1 ) else -6;
        record.famhx_cancer_mother = record.famhx_cancer_mother if (record.famhx_cancer_mother <= 1 ) else -6;
        record.famhx_cancer_father = record.famhx_cancer_father if (record.famhx_cancer_father <= 1 ) else -6;
        record.famhx_cancer_grands = record.famhx_cancer_grands if (record.famhx_cancer_grands <= 1 ) else -6;
        record.famhx_cancer_sibling = record.famhx_cancer_sibling if (record.famhx_cancer_sibling <= 1 ) else -6;
        record.famhx_cancer_dk = record.famhx_cancer_dk if (record.famhx_cancer_dk <= 1 ) else -6;
        record.famhx_diabetes_mother = record.famhx_diabetes_mother if (record.famhx_diabetes_mother <= 1 ) else -6;
        record.famhx_diabetes_father = record.famhx_diabetes_father if (record.famhx_diabetes_father <= 1 ) else -6;
        record.famhx_diabetes_grands = record.famhx_diabetes_grands if (record.famhx_diabetes_grands <= 1 ) else -6;
        record.famhx_diabetes_sibling = record.famhx_diabetes_sibling if (record.famhx_diabetes_sibling <= 1 ) else -6;
        record.famhx_diabetes_dk = record.famhx_diabetes_dk if (record.famhx_diabetes_dk <= 1 ) else -6;
        record.famhx_heartprob_mother = record.famhx_heartprob_mother if (record.famhx_heartprob_mother <= 1 ) else -6;
        record.famhx_heartprob_father = record.famhx_heartprob_father if (record.famhx_heartprob_father <= 1 ) else -6;
        record.famhx_heartprob_grands = record.famhx_heartprob_grands if (record.famhx_heartprob_grands <= 1 ) else -6;
        record.famhx_heartprob_sibling = record.famhx_heartprob_sibling if (record.famhx_heartprob_sibling <= 1 ) else -6;
        record.famhx_heartprob_dk = record.famhx_heartprob_dk if (record.famhx_heartprob_dk <= 1 ) else -6;
        record.famhx_hibp_mother = record.famhx_hibp_mother if (record.famhx_hibp_mother <= 1 ) else -6;
        record.famhx_hibp_father = record.famhx_hibp_father if (record.famhx_hibp_father <= 1 ) else -6;
        record.famhx_hibp_grands = record.famhx_hibp_grands if (record.famhx_hibp_grands <= 1 ) else -6;
        record.famhx_hibp_sibling = record.famhx_hibp_sibling if (record.famhx_hibp_sibling <= 1 ) else -6;
        record.famhx_hibp_dk = record.famhx_hibp_dk if (record.famhx_hibp_dk <= 1 ) else -6;
        record.famhx_hichol_mother = record.famhx_hichol_mother if (record.famhx_hichol_mother <= 1 ) else -6;
        record.famhx_hichol_father = record.famhx_hichol_father if (record.famhx_hichol_father <= 1 ) else -6;
        record.famhx_hichol_grands = record.famhx_hichol_grands if (record.famhx_hichol_grands <= 1 ) else -6;
        record.famhx_hichol_sibling = record.famhx_hichol_sibling if (record.famhx_hichol_sibling <= 1 ) else -6;
        record.famhx_hichol_dk = record.famhx_hichol_dk if (record.famhx_hichol_dk <= 1 ) else -6;

        
     def skipclean(self):
         
        record = self.record;

        # recoding ** skip question , if should skip set to -8
        record['demo_pregnant'] = record['demo_pregnant'] if (record['demo_gender'] == 2) else -8;
        # !! NOTE: be careful of spelling for tob_cigssmokestatus 

        record['tob_cigsperday'] = record['tob_cigsperday'] if (record['tob_cigssmokestatus'] == 1) else -8;
        record['tob_cigsyearssmoked'] = record['tob_cigsyearssmoked'] if (record['tob_cigssmokestatus'] == 1) else -8;
        record['tob_cigsyearsquit'] = record['tob_cigsyearsquit'] if (record['tob_cigssmokestatus'] == 2) else -8;
        record['tob_cigsavgbeforequit'] = record['tob_cigsavgbeforequit'] if (record['tob_cigssmokestatus'] == 2) else -8;
        record['physact_vigorousminutes'] = record['physact_vigorousminutes'] if (record['physact_vigorousfreq'] >= 1) else -8;
        record['physact_moderateminutes'] = record['physact_moderateminutes'] if (record['physact_moderatefreq'] >= 1) else -8;

        record['job_satisfaction'] = record['job_satisfaction'] if (record['demo_employstatus'] == 1) else -8;
        record['job_illnessdays'] = record['job_illnessdays'] if (record['demo_employstatus'] == 1) else -8;
        record['job_healthaffectprod'] = record['job_healthaffectprod'] if (record['demo_employstatus'] == 1) else -8;


        record['mdc_menopause']  = record['mdc_menopause'] if (record['demo_gender'] == 2 and record['demo_pregnant'] != 1) else -8;
        
        record['wh_hysterectomy']  = record['wh_hysterectomy'] if (record['demo_gender'] == 2 and record['demo_pregnant'] in [2,3]) else -8;
        # IS BLANK --> make < 0
        record['ps_cervicalca_paponlytime']  = record['ps_cervicalca_paponlytime'] if (record['demo_gender'] == 1 and between(record['demo_age'], 21,29) and ( record['(wh_hysterectomy'] in [3,4] or record['wh_hysterectomy'] < 0) ) else -8;
        record['ps_cervicalca_paphpvtype']  = record['ps_cervicalca_paphpvtype'] if (record['demo_gender'] == 1 and between(record['demo_age'], 30,65) and ( record['wh_hysterectomy'] in [3,4] or record['wh_hysterectomy'] < 0 ) ) else -8;
                                                                        
        record['ps_mammogram']  = record['ps_mammogram'] if ( record['demo_gender'] == 2 and between(record['demo_age'], 40,74)) else -8;
        # finish skipclean()


  
      
