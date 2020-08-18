from django.db import models
from django.conf import settings
from userapi.models import UserProfile
# Create your models here.

class Riot(models.Model):

    #Family members
    user_profile= models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )
    no_of_family_members = models.IntegerField(default=5)
    have_infants= models.BooleanField(default=False)
    have_senior_citizens = models.BooleanField(default=False)
    have_existing_medical_conditions = models.BooleanField(default=False)
    backpack = models.BooleanField(default=False)
    sunglasses = models.BooleanField(default=False)
    pepper_spray = models.BooleanField(default=False)
    flash_light = models.BooleanField(default=False)
    cash = models.BooleanField(default=False)
    mylar_blanket = models.BooleanField(default=False)
    radio_app = models.BooleanField(default=False)
    survival_manuals = models.BooleanField(default=False)
    bandana = models.BooleanField(default=False)
    have_disability=models.BooleanField(default=False)
    disability_description=models.TextField(blank=True)
    have_prescriptions=models.BooleanField(default=False)
    have_dependable_medium=models.BooleanField(default=False)
    knows_to_drive=models.BooleanField(default=False)
    another_location=models.BooleanField(default=False)
    have_emergency_helpline=models.BooleanField(default=False)
    children_remember=models.BooleanField(default=False)
    medical_supplies=models.BooleanField(default=False)
    life_insurance=models.BooleanField(default=False)
    mock_drills=models.BooleanField(default=False)
    response = models.TextField(default='')

    def __str__(self):
        return str(self.user_profile)

class Earthquake(models.Model):

    user_profile= models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
    )

    #Types of house
    house = models.CharField(max_length=16,blank=True)

    #How old
    structure = models.CharField(max_length=16,blank=True)

    #Open area
    field = models.CharField(max_length=16,blank=True)

    #heavy furnitures anchored to wall
    furniture = models.CharField(max_length=16,blank=True)

    #Disaster management plan
    disaster_plan = models.CharField(max_length=16,blank=True)

    #Disaster meetup place
    place = models.CharField(max_length=16,blank=True)

    #Cracks in the wall
    cracks = models.CharField(max_length=16,blank=True)

    #Combustable substance stored
    combustible = models.TextField(blank=True)

    #safe place
    safe_places = models.CharField(max_length=16,blank=True)

    #Contact in another region if gets scattered
    contact = models.TextField(blank=True)

    #Disaster kit
    fire_extin = models.BooleanField(default=False)
    first_aid= models.BooleanField(default=False)
    flashlight=models.BooleanField(default=False)
    #Documnets
    documents = models.CharField(max_length=16,blank=True)

    #CASH
    cash = models.CharField(max_length=16,blank=True)

    #Own a Safe
    safe = models.CharField(max_length=16,blank=True)

    #Health plicy
    health_policies = models.CharField(max_length=16,blank=True)

    #Contact info of physician
    physician =  models.TextField(blank=True)

    #disability or special needs
    disability = models.TextField(blank=True)

    #if yes, specify person with disability
    # If_yes_please_specify_Persons_with_Disabilities = models.CharField(max_length=16,blank=True)

    #pregnant women
    # pregnant_women = models.CharField(max_length=16,blank=True)

    #Infants , Senior citizens
    infants_and_senior_citizens = models.CharField(max_length=16,blank=True)

    #switch off gas
    gas = models.CharField(max_length=16,blank=True)

    #Children aware of numbers
    emergency_numbers = models.CharField(max_length=16,blank=True)

    #Where is your vehicle parked
    parked = models.CharField(max_length=16,blank=True)

    #Car Insurance
    car_insurance = models.CharField(max_length=16,blank=True)

    #Pets
    pets = models.CharField(max_length=16,blank=True)

    #No of pets
    # If_yes_how_many_pets = models.CharField(max_length=16,blank=True)

    #Pet's supplies
    # pets_supplies = models.CharField(max_length=16,blank=True)

    #Basement in a house
    basement = models.CharField(max_length=16,blank=True)

    #Ammo
    ammo = models.CharField(max_length=16,blank=True)

    #Repairs in a house
    repairs = models.CharField(max_length=16,blank=True)

    #Blueprint of a house
    blueprint = models.CharField(max_length=16,blank=True)

    response= models.TextField(default='')

    def __str__(self):
        return str(self.user_profile)


class CyberCrime(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )
    at_work = models.BooleanField()
    at_home = models.BooleanField()
    have_secure_connections = models.BooleanField()
    have_action_plan = models.BooleanField()
    how_to_know_risk = models.BooleanField()
    have_shared_card = models.BooleanField()
    identify_phishing = models.BooleanField()
    third_party = models.TextField(blank=True)
    security_policies = models.BooleanField()
    have_recovery_plan = models.BooleanField()
    have_redun = models.BooleanField()
    perform_bgcheck = models.BooleanField()
    perform_audit = models.BooleanField()
    have_cyber_insu = models.BooleanField()
    have_sec_plan = models.BooleanField()
    have_trained = models.BooleanField()
    have_IRP = models.BooleanField()
    response = models.TextField(default='')

    def __str__(self):
        return str(self.user_profile)


class Tsunami(models.Model):
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    have_water_bodies = models.BooleanField()
    house_kind = models.CharField(max_length=16,blank=True)
    # building = models.BooleanField()
    # wooden_house = models.BooleanField()
    have_alarm_system = models.BooleanField()
    # to_do = models.TextField(default="NA")
    have_elevated_area = models.BooleanField()
    have_maps = models.BooleanField()
    have_learnt_signs = models.BooleanField()
    have_shelters = models.BooleanField()
    have_contact = models.BooleanField()
    have_health = models.BooleanField()
    have_specials = models.BooleanField()
    have_latest_prescriptions = models.BooleanField()
    near_home = models.TextField(default="NA",blank=True)
    have_higher_ground = models.TextField(default="NA",blank=True)
    provide_reg_contact = models.TextField(default="NA",blank=True)
    provide_phy_contact = models.TextField(default="NA",blank=True)
    have_car_insu_up = models.BooleanField()
    response=models.TextField(default='')

    def __str__(self):
        return str(self.user_profile)


class Flood(models.Model):
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    near_water_bodies = models.BooleanField()
    house_kind = models.CharField(max_length=30)
    emergency_evac = models.TextField(blank=True)
    have_higher_ground = models.BooleanField()
    flood_risk = models.BooleanField()
    have_signed = models.BooleanField()
    provide_reg_contact = models.TextField(blank=True)
    provide_phy_contact = models.TextField(blank=True)
    have_health = models.BooleanField()
    have_car_insu_up = models.BooleanField()
    have_evac_routes = models.BooleanField()
    have_kits = models.BooleanField()
    have_safe_doc = models.BooleanField()
    have_flood = models.BooleanField()
    have_elv_shelters = models.BooleanField()
    have_specials = models.BooleanField()
    to_drive = models.BooleanField()
    clean_gutter = models.BooleanField()
    have_comm_plan = models.BooleanField()
    kids_know = models.BooleanField()
    response=models.TextField()

    def __str__(self):
        return str(self.user_profile)

class Terrorism(models.Model):
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    state = models.TextField(blank=True)
    dist = models.TextField(blank=True)
    loc = models.TextField(blank=True)
    count_people = models.IntegerField()
    have_infant = models.BooleanField()
    have_school_kids = models.BooleanField()
    have_specials = models.BooleanField()
    specify_specials = models.TextField(blank=True)
    have_emerg = models.BooleanField()
    three_emg_name_num = models.TextField(blank=True)
    have_shelter = models.BooleanField()
    have_inventory = models.BooleanField()
    have_emg_kits = models.BooleanField()
    have_add_kits = models.TextField(blank=True)
    docs = models.TextField(blank=True)
    have_plan_school = models.BooleanField()
    have_evac_plans = models.BooleanField()
    response = models.TextField()

    def __str__(self):
        return str(self.user_profile)

class Severe_Pollution(models.Model):
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    state = models.TextField(blank=True)
    dist = models.TextField(blank=True)
    loc = models.TextField(blank=True)
    count_people = models.IntegerField()
    have_seniors = models.BooleanField()
    have_specials = models.BooleanField()
    specify_specials = models.TextField(blank=True)
    have_policies = models.BooleanField()
    have_hard_cpy = models.BooleanField()
    have_masks = models.BooleanField()
    have_air_purifier = models.BooleanField()
    have_check_quality = models.BooleanField()
    have_cardiac = models.BooleanField()
    have_medicines = models.BooleanField()
    have_CO_detector = models.BooleanField()
    CO_off = models.BooleanField()
    response=models.TextField()

    def __str__(self):
        return str(self.user_profile)

class NuclearWar(models.Model):
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    state = models.TextField(default="NA",blank=True)
    dist = models.TextField(default="NA",blank=True)
    loc = models.TextField(default="NA",blank=True)
    count_people = models.CharField(max_length=16,blank=True)
    have_infant = models.BooleanField()
    # have_school_kids = models.BooleanField()
    # have_specials = models.BooleanField()
    have_specials = models.TextField(default="NA",blank=True)
    have_policies = models.BooleanField()
    have_hard_cpy = models.BooleanField()
    have_base = models.BooleanField()
    have_brick_shelter = models.BooleanField()
    have_media = models.BooleanField()
    # have_basic_kits = models.BooleanField()
    Water = models.BooleanField()
    Food = models.BooleanField()
    radio = models.BooleanField()
    Flashlight = models.BooleanField()
    First_aid_kit = models.BooleanField()
    Extra_batteries = models.BooleanField()
    Whistle = models.BooleanField()
    Dust_mask = models.BooleanField()
    Plastic_sheeting = models.BooleanField()
    Moist_towelettes = models.BooleanField()
    Wrench = models.BooleanField()
    Manual_can_opener = models.BooleanField()
    Local_maps = models.BooleanField()
    Cell_phone = models.BooleanField()
    have_add_kits = models.BooleanField()
    have_switch_board = models.BooleanField()
    have_school_base = models.BooleanField()
    have_schl_brick = models.BooleanField()
    have_conduct_drill = models.BooleanField()
    have_shelter_plan = models.BooleanField()
    have_nuclear_kit = models.BooleanField()
    response=models.TextField(default='')

    def __str__(self):
        return str(self.user_profile)

class Fire(models.Model):

    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    have_esc_plan = models.BooleanField()
##    special_needs = models.TextField(default="NA")
    have_seniors = models.BooleanField()
    have_smoke_det = models.BooleanField()
    have_smoke_det_out_bed = models.BooleanField()
    have_discuss_out = models.BooleanField()
    count_exits = models.CharField(max_length=16,blank=True)
    have_fire_extin = models.BooleanField()
    have_maint_check = models.BooleanField()
    have_pets = models.BooleanField()
    have_policy = models.BooleanField()
##    utmost_doc = models.TextField(default="NA")
##    keep_doc = models.TextField(default="NA")
    have_kit = models.BooleanField()
    response=models.TextField(default='')

    def __str__(self):
        return str(self.user_profile)
