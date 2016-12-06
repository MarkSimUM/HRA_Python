import math
## IHRA_ENGINE.HRA_FUNC
def stress_score( physical_health, hours_sleep,life_satis, personal_loss,marital_status,social_tie ):
   "function stress score"
    # [old] physical_health, hours_sleep,life_satis, personal_loss,marital_status,social_tie
    # [new] record.ql_overallhealth, record.sc_sleepduration, record.ql_lifesatisfaction,record.ql_personalloss, record.demo_maritalstatus, record.ql_socialtiestrength
   stress_sum = 0;
   addto = 0;

   if physical_health == 1: # excellent
         addto = 1;
   elif physical_health == 2: # very good
         addto = 1;
   elif physical_health == 3:
         addto = 2;
   elif physical_health == 4:
         addto = 3;
   elif physical_health == 5:
         addto = 5;
   elif physical_health == 9: # do not count
         addto = 1;

   else:
         addto = 3;  # others

   stress_sum +=    addto;
   # --- add other items here ---->


   #SC_SLEEPDURATION

   #15 hours or less
   #26 hours
   #37 hours
   #48 hours
   #59 hours or more

   # --- Hours Sleep new coding ---->
   if hours_sleep == 1: # 5 or less
         addto = 4;
   elif hours_sleep == 2: # 6 hrs
         addto = 4;
   elif hours_sleep == 3: #7 hrs 
         addto = 2;
   elif hours_sleep == 4: #8 hrs
         addto = 2;
   elif hours_sleep == 5: # 9 or more
         addto = 4;
   elif hours_sleep == 9: # do not count
         addto = 2;
   else:
         addto = 3;  # others

   stress_sum +=    addto;

   #QL_LIFESATISFACTION
   #1Completely satisfied
   #2Mostly satisfied
   #3Partly satisfied
   #4Not satisfied
   # 1,3, 5, 9, 1, 5
   if life_satis == 1: # 1Completely satisfied
         addto = 1;
   elif life_satis == 2: # 
         addto = 3;
   elif life_satis == 3: #
         addto = 5;
   elif life_satis == 4: # 4 Not satisfied
         addto = 9;
   elif life_satis == 9: # do not count
      addto = 1;

   else:
      addto = 5;  # others
   stress_sum +=    addto;

   # QL_PERSONALLOSS
   #1Yes, two or more serious losses
   #2Yes, one serious loss
   #3No
   # 9,6,3,3,5
   if personal_loss == 1: # 1Yes, two or more serious losses
      addto = 9;
   elif personal_loss == 2: # Yes, one serious loss
      addto = 6;
   elif personal_loss == 3: # No
      addto = 3;
   elif personal_loss == 9: # do not count
      addto = 3;

   else:
      addto = 5;  # others
   stress_sum += addto;


   # DEMO_MARITALSTATUS

   #1Single (never married)
   #2Married
   #3Widowed
   #4Divorced
   #5Separated
   #6Other
   # 2,4,4,1,5,3,1,3
   if marital_status == 1: # Single (never married)
      addto = 2;
   elif marital_status == 2: # Married
      addto = 1;
   elif marital_status == 3: #Widowed
      addto = 5;
   elif marital_status == 4: #Divorced
      addto = 4;
   elif marital_status == 5: #Separated
      addto = 4;
   elif marital_status == 6: # Other
      addto = 3;
   elif marital_status == 9: # do not count
      addto = 1;

   else:
      addto = 3;  # others
   stress_sum +=  addto;

   # social_tie
   #QL_SOCIALTIESTRENGTH

   #1Very strong
   #2About average
   #3Weaker than average
   #4I don't know
   # 2,5,8,5,2,5
   if life_satis == 1: # 1Very strong
      addto = 2;
   elif life_satis == 2: # 2 About average
      addto = 5;
   elif life_satis == 3: # #3Weaker than average
      addto = 8;
   elif life_satis == 4: # 4 I don't know
      addto = 5;
   elif life_satis == 9: # do not count
      addto = 2;

   else:
      addto = 5;  # others
   stress_sum += addto;

   return stress_sum
# stress_score end of function



# !! function ideal_weight(sex varchar2, height_inches pls_integer, frame varchar2) return pls_integer;
#  --default sex: male

def ideal_weight(sex,  height_inches, frame ) :
   return pls_integer;

# !! function bmi(wgt pls_integer, hgt pls_integer) return number;
def bmi(wgt, hgt) :
   if wgt> 0  and hgt > 0:
      #bmi = math.trunc(wgt/2.2046/pow(.0254*hgt,2));
      bmi = float('%.1f'%(wgt/2.2046/pow(.0254*hgt,2)));
     
      if bmi > 99.9:
         bmi = 99.9;
      return bmi;
   else:
      return -1;

# !! function bmi_ideal_weight(hgt_inch pls_integer, bmi number:=24.9) return pls_integer;
def bmi_ideal_weight(hgt, bmi) :
   #return round(bmi*power(hgt_inch*.0254,2)*2.2046);
   return  round(bmi*pow(hgt*.0254,2)*2.2046,1) ;

#!! function bmi_weight_range(hgt number, bmi_low number:=19, bmi_high number:=24.9) return varchar2;
def bmi_weight_range(hgt, bmi_low , bmi_high ) :
   return  varchar2;

# !! function mental_prob (stress_score in number,
#  absent_days in number,
#  use_drug_medication in number,
#  physical_health in number,
#  sex in number,
#  age in number,
#  feel_stress in number,
#  stress_effect in number) return number;

def mental_prob(stress_score, absent_days, use_drug_medication,physical_health, sex, age, feel_stress, stress_effect ) :
   return number;

# !! function bmi_kgcm(wgt pls_integer, hgt pls_integer) return number;
#!! function bmi_ideal_weight_kgcm(hgt_cm pls_integer, bmi number:=24.9) return pls_integer;
#!! function bmi_ideal_height(wt_lb pls_integer, bmi number:=24.9) return pls_integer;
#!! function bmi_ideal_height_kgcm(wt_kg pls_integer, bmi number:=24.9) return pls_integer;
#!!  function bmi_weight_range_kgcm(hgt number, bmi_low number:=19, bmi_high number:=24.9) return varchar2;




