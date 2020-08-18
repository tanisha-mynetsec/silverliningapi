from rest_framework import status,generics,mixins
from . import queries,models,serializers,querry  as qr
from .models import Riot
from rest_framework.response import Response
from .serializers import RiotSerializer
from rest_framework import viewsets,filters
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from userapi import permissions
import json
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class CyberViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CyberSerializer
    queryset = models.CyberCrime.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user')

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'response':json.loads(response.data['response'])})

    def update(self, request, *args, **kwargs):
        return Response({'message': "This instance can't be updated"})

    def perform_create(self, serializer):
        r=qr.CyberCrime()
        instance = serializer.validated_data
        respo = []
        if instance['at_work']:
            respo.append(r.work_querry)
        if instance['at_home']:
            respo.append(r.home_querry)
        if not instance['have_secure_connections']:
            respo.append(r.connections_querry)
        if not instance['have_action_plan']:
            respo.append(r.action_plan_querry)
        if instance['how_to_know_risk']:
            respo.append(r.risk_querry)
        if instance['have_shared_card']:
            respo.append(r.shared_card_querry)
        if not instance['identify_phishing']:
            respo.append(r.phishing_querry)
        respo.append(r.third_party_querry)
        if not instance['security_policies']:
            respo.append(r.security_policies_querry)
        if not instance['have_recovery_plan']:
            respo.append(r.recovery_plan_querry)
        if not instance['have_redun']:
            respo.append(r.redun_querry)
        if not instance['perform_bgcheck']:
            respo.append(r.bgcheck_querry)
        if not instance['perform_audit']:
            respo.append(r.audit_query)
        if not instance['have_cyber_insu']:
            respo.append(r.cyber_insu_query)
        if not instance['have_sec_plan']:
            respo.append(r.sec_plan_query)
        if not instance['have_trained']:
            respo.append(r.trained_query)
        if not instance['have_IRP']:
            respo.append(r.IRP_query)
        serializer.save(user_profile=self.request.user,response=json.dumps(respo))


class FloodViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FloodSerializer
    queryset = models.Flood.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user')

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'response':json.loads(response.data['response'])})
        #return Response({'response': 'payment not done '})

    def update(self, request, *args, **kwargs):
        return Response({'message': "This instance can't be updated"})

    def perform_create(self, serializer):
        r=qr.Floods()
        instance = serializer.validated_data
        respo = []
        if instance['near_water_bodies']:
            respo.append(r.water_bodies_querry)
        if instance['house_kind'].lower()=="apartment":
            respo.append(r.apartment_querry)
        if instance['house_kind'].lower()=="independent_home":
            respo.append(r.independent_home_querry)
        respo.append("emergency evacuation: "+instance['emergency_evac'])
        respo.append(r.emergency_evac_querry)
        if not instance['have_higher_ground']:
            respo.append(r.higher_ground_querry)
        if not instance['flood_risk']:
            respo.append(r.flood_risk_querry)
        if not instance['have_signed']:
            respo.append("has not signed up for community’s warning system")
        respo.append("Emergency contact: "+instance['provide_reg_contact'])
        respo.append("Physician contact: " + instance['provide_phy_contact'])
        respo.append("health policies: "+str(instance['have_health']))
        if not instance['have_car_insu_up']:
            respo.append(r.car_insu_up_query)
        if not instance['have_evac_routes']:
            respo.append(r.evac_routes_querry)
        if instance['have_kits']:
            respo.append(r.kits_querry)
        else:
            respo.append(r.nokits_querry)
        if not instance['have_safe_doc']:
            respo.append(r.safe_doc_query)
        if instance['have_health']:
            respo.append("has health or home insurance policies")
        else:
            respo.append("does not have health or home insurance policies")
        if instance['have_flood']:
            respo.append("can purchase flood insurance policy")
        if not instance['have_elv_shelters']:
            respo.append(r.elv_shelters_query)
        if instance['have_specials']:
            respo.append(r.specials_query)
        if instance['to_drive']:
            respo.append(r.to_drive_query)
        if not instance['clean_gutter']:
            respo.append(r.clean_gutter_query)
        if not instance['have_comm_plan']:
            respo.append(r.comm_plan_query)
        if not instance['kids_know']:
            respo.append(r.kids_know_query)
        serializer.save(user_profile=self.request.user,response=json.dumps(respo))



class RiotViewSet(viewsets.ModelViewSet):
    """Handle Creating and updating profiles"""
    serializer_class = RiotSerializer
    queryset = Riot.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster,IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user')

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'response':json.loads(response.data['response'])})
        # return Response({'response': 'payment not done '})

    def update(self, request, *args, **kwargs):
        return Response({'message': "This instance can't be updated"})

    def perform_create(self, serializer):
        instance = serializer.validated_data
        respo = []
        if instance['have_infants']:
            respo.append(qr.infant_querry)
        if instance['have_senior_citizens']:
            respo.append(qr.senior_querry)
        if instance['have_existing_medical_conditions']:
            respo.append(qr.medical_querry)
        if not instance['backpack']:
            respo.append(qr.backpack_querry)
        if not instance['sunglasses']:
            respo.append(qr.sunglass_querry)
        if not instance['pepper_spray']:
            respo.append(qr.spray_querry)
        if not instance['flash_light']:
            respo.append(qr.flashlight_querry)
        if not instance['cash']:
            respo.append(qr.cash_querry)
        if not instance['mylar_blanket']:
            respo.append(qr.mylar_querry)
        if not instance['radio_app']:
            respo.append(qr.radio_querry)
        if not instance['survival_manuals']:
            respo.append(qr.manuals_querry)
        if not instance['bandana']:
            respo.append(qr.bandana_querry)
        if instance['have_disability']:
            respo.append(qr.disability_description_query)
        if not instance['have_prescriptions']:
            respo.append(qr.prescription_query)
        if not instance['have_dependable_medium']:
            respo.append(qr.dependable_medium_query)
        if instance['knows_to_drive']:
            respo.append(qr.drive_query)
        if  instance['another_location']:
            respo.append(qr.location_query)
        if not instance['have_emergency_helpline']:
            respo.append(qr.emergency_helpline_query)
        if not instance['children_remember']:
            respo.append(qr.children_remember_query)
        if not instance['medical_supplies']:
            respo.append(qr.medical_supplies_query)
        if not instance['life_insurance']:
            respo.append(qr.life_insurance_query)
        if not instance['mock_drills']:
            respo.append(qr.mock_drills_query)

        serializer.save(user_profile=self.request.user,response=json.dumps(respo))


# class EarthQuakeViewset(viewsets.ModelViewSet):
#
#     serializer_class = serializers.EarthquakeSerializer
#     queryset = models.Earthquake.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (permissions.UpdateOwnDisaster, IsAuthenticated)
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('user_profile', 'response')
#
#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         # print(repr(self.get_serializer))
#         return Response({'response': json.loads(response.data['response'])})
#
#     def update(self, request, *args, **kwargs):
#         return Response({'message': "This instance can't be updated"})
#
#     def perform_create(self, serializer):
#         query = serializer.validated_data
#         response = []
#         if query['house'].lower() == 'apartment':
#             response += queries.apartment
#         else:
#             response += queries.independent_home
#         response += queries.donts
#         if query['structure'] == '0-15':
#             response += ["House falls under yellow zone", "Evacuation is an option"]
#         elif query['structure'] == '15-30':
#             response += ["House falls under orange zone",
#                          "Evacuation is recommended"
#                          ]
#         else:
#             response += [
#                 "House falls under red zone",
#                 "Evacuation is highly recommended and should be a priority if possible"
#             ]
#         if query['field'].lower() == 'yes':
#             response += queries.field_query
#         if query['furniture'].lower() == 'yes':
#             response += queries.furniture_query
#         if query['disaster_plan'].lower() == 'no':
#             response += queries.plan_query
#         response += query['place']
#         if query['cracks'].lower() == 'yes':
#             response += queries.cracks_query
#         response += query['combustible']
#         response += queries.combustible_query
#         if query['house'].lower() == 'apartment':
#             response += queries.safe_apartment_query
#         else:
#             response += queries.safe_home_query
#         # response+='Please contact the following person in case everyone gets scattered and can’t get home or in case of an emergency evacuation:\n'  + query['contact'] +'\n'
#         if not query['fire_extin']:
#             response += [
#                 'Get a fire extinguisher for your home. Your local fire department can train you and your family to use it properly.']
#         if not query['first_aid']:
#             response += [
#                 'Purchase a first aid kit and one can take a cardiopulmonary resuscitation (CPR) training course. Learn who else in your neighborhood is trained in first aid and CPR.']
#         if not query['flashlight']:
#             response += [
#                 'Purchase Flashlights with extra bulbs and batteries and a portable radio with extra batteries.']
#         response += queries.documents_query
#         if query['cash'].lower() == 'yes':
#             response += queries.cash_query
#         if query['safe'].lower() == 'no':
#             response += queries.safe_query
#         response.append(query['physician'])
#         if query['disability'].lower() != 'no':
#             response += queries.disability_query
#         if query['infants_and_senior_citizens'].lower() == 'yes':
#             response += queries.infant_query
#         if query['gas'].lower() == 'no':
#             response += queries.gas_query
#         if query['emergency_numbers'].lower() == 'no':
#             response += queries.emergency_query
#         if query['car_insurance'].lower() == 'no':
#             response += queries.insurance_query
#         response += queries.parked_query
#         if query['pets'].lower() != 'no':
#             response += queries.pets_query
#         if query['basement'].lower() == 'yes':
#             response += queries.basement_query
#         if query['ammo'].lower() == 'yes':
#             response += queries.ammo_query
#         if query['repairs'].lower() == 'yes':
#             response += queries.repair_query
#         if query['blueprint'].lower() == 'no':
#             response += queries.blueprint_query
#
#         serializer.save(user_profile=self.request.user, response=json.dumps(response))

class TsunamiViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.TsunamiSerializer
    queryset=models.Tsunami.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster,IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_profile','response')

    def create(self,request,*args,**kwargs):
        response=super().create(request,*args,**kwargs)
        # print(repr(self.get_serializer))
        return Response({'response':json.loads(response.data['response'])})

    def update(self,request,*args,**kwargs):
        return Response({'message':"This instance can't be updated"})

    def perform_create(self,serializer):
        q=serializer.validated_data
        tsu=qr.TsunamiQuery()
        response=[]
        if q['have_water_bodies']:
            response.append(tsu.water_bodies_query)
        if q['house_kind'].lower()=='building':
            response.append(tsu.building_query)
        else:
            response.append(tsu.wooden_house_query)
        if not q['have_alarm_system']:
            response.append(tsu.alarm_system_query)
        response.append(tsu.to_do_query)
        if not q['have_elevated_area']:
            response.append(tsu.elevated_area_query)
        response.append(tsu.maps_query)
        if not q['have_learnt_signs']:
            response.append(tsu.learnt_signs_query)
        response.append(tsu.shelters_query)
        if not q['have_contact']:
            response.append(tsu.contact_query)
        if q['have_health']:
            response.append(tsu.health_query)
        if q['have_specials']:
            response.append(tsu.specials_query)
        if not q['have_latest_prescriptions']:
            response.append(tsu.prescriptions_query)
        response.append([q['near_home']])
        response.append(tsu.near_home_query)
        response.append([q['have_higher_ground']])
        response.append(tsu.higher_ground_query)
        response.append([q['provide_reg_contact']])
        response.append([q['provide_phy_contact']])
        if not q['have_car_insu_up']:
            response.append(tsu.car_insu_up_query)

        serializer.save(user_profile=self.request.user,response=json.dumps(response))


class EarthQuakeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.EarthquakeSerializer
    queryset = models.Earthquake.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_profile', 'response')

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # print(repr(self.get_serializer))
        return Response({'response': json.loads(response.data['response'])})

    def update(self, request, *args, **kwargs):
        return Response({'message': "This instance can't be updated"})

    def perform_create(self, serializer):
        query = serializer.validated_data
        response = []
        if query['house'].lower() == 'apartment':
            response.append(queries.apartment)
        else:
            response.append(queries.independent_home)
        response.append(queries.donts)
        if query['structure'] == '0-15':
            response.append(["House falls under yellow zone", "Evacuation is an option"])
        elif query['structure'] == '15-30':
            response.append(["House falls under orange zone",
                             "Evacuation is recommended"
                             ])
        else:
            response.append([
                "House falls under red zone",
                "Evacuation is highly recommended and should be a priority if possible"
            ])
        if query['field'].lower() == 'yes':
            response.append(queries.field_query)
        if query['furniture'].lower() == 'yes':
            response.append(queries.furniture_query)
        if query['disaster_plan'].lower() == 'no':
            response.append(queries.plan_query)
        response.append([query['place']])
        if query['cracks'].lower() == 'yes':
            response.append(queries.cracks_query)
        response.append([query['combustible']])
        response.append(queries.combustible_query)
        if query['house'].lower() == 'apartment':
            response.append(queries.safe_apartment_query)
        else:
            response.append(queries.safe_home_query)
        # response+='Please contact the following person in case everyone gets scattered and can’t get home or in case of an emergency evacuation:\n'  + query['contact'] +'\n'
        response.append([query['contact']])
        if not query['fire_extin']:
            response.append([
                                'Get a fire extinguisher for your home. Your local fire department can train you and your family to use it properly.'])
        if not query['first_aid']:
            response.append([
                                'Purchase a first aid kit and one can take a cardiopulmonary resuscitation (CPR) training course. Learn who else in your neighborhood is trained in first aid and CPR.'])
        if not query['flashlight']:
            response.append(
                ['Purchase Flashlights with extra bulbs and batteries and a portable radio with extra batteries.'])
        response.append(queries.documents_query)
        if query['cash'].lower() == 'yes':
            response.append(queries.cash_query)
        if query['safe'].lower() == 'no':
            response.append(queries.safe_query)
        response.append([query['physician']])
        if query['disability'].lower() != 'no':
            response.append(queries.disability_query)
        if query['infants_and_senior_citizens'].lower() == 'yes':
            response.append(queries.infant_query)
        if query['gas'].lower() == 'no':
            response.append(queries.gas_query)
        if query['emergency_numbers'].lower() == 'no':
            response.append(queries.emergency_query)
        if query['car_insurance'].lower() == 'no':
            response.append(queries.insurance_query)
        response.append(queries.parked_query)
        if query['pets'].lower() != 'no':
            response.append(queries.pets_query)
        if query['basement'].lower() == 'yes':
            response.append(queries.basement_query)
        if query['ammo'].lower() == 'yes':
            response.append(queries.ammo_query)
        if query['repairs'].lower() == 'yes':
            response.append(queries.repair_query)
        if query['blueprint'].lower() == 'no':
            response.append(queries.blueprint_query)

        serializer.save(user_profile=self.request.user, response=json.dumps(response))

class TerrorViewSet(viewsets.ModelViewSet):
    """Handle Creating and updating profiles"""
    serializer_class =serializers.TerrorSerializer
    queryset = models.Terrorism.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user')

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'response': json.loads(response.data['response'])})

    def update(self, request, *args, **kwargs):
        return Response({'message': "This instance can't be updated"})

    def perform_create(self, serializer):
        instance = serializer.validated_data
        q=queries.TerrorQuerry
        respo = []
        respo.append(instance['state'])
        respo.append(instance['dist'])
        respo.append(instance['loc'])
        respo.append(instance['count_people'])
        if instance['have_infant']:
            respo.append(q.infant_querry)
        if instance['have_school_kids']:
            respo.append(q.school_kids_querry)
        if instance['have_specials']:
            respo.append(instance['specify_specials'])
        if instance['have_emerg']:
            respo.append(q.emerg_querry)
        respo.append(instance['three_emg_name_num'])
        respo.append(q.shelter_querry)
        if not instance['have_inventory']:
            respo.append(q.inventory_querry)
        if not instance['have_emg_kits']:
            respo.append(q.emg_kits_querry)
        respo.append(instance['have_add_kits'])
        respo.append(instance['docs'])
        if not instance['have_plan_school']:
            respo.append(q.plan_school_querry)
        if not instance['have_evac_plans']:
            respo.append(q.evac_plans_querry)
        serializer.save(user_profile=self.request.user, response=json.dumps(respo))

class PollutionViewSet(viewsets.ModelViewSet):
    """Handle Creating and updating profiles"""
    serializer_class =serializers.PollutionSerializer
    queryset = models.Severe_Pollution.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user')

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'response': json.loads(response.data['response'])})

    def update(self, request, *args, **kwargs):
        return Response({'message': "This instance can't be updated"})

    def perform_create(self, serializer):
        instance = serializer.validated_data
        q=qr.Severe_Pollution()
        respo = []
        respo.append(instance['state'])
        respo.append(instance['dist'])
        respo.append(instance['loc'])
        respo.append(instance['count_people'])
        if instance['have_seniors']:
            respo.append(q.seniors_querry)
        if instance['have_specials']:
            respo.append(q.specials_querry)
        if not instance['have_masks']:
            respo.append(q.masks_querry)
        if instance['have_cardiac']:
            respo.append(q.cardiac_querry)
        if instance['have_medicines']:
            respo.append(q.medicines_YES_querry)
        else:
            respo.append(q.medicines_NO_querry)
        if instance['have_CO_detector']:
            respo.append(q.CO_detector_YES_querry)
        else:
            respo.append(q.medicines_NO_querry)
        if instance['CO_off']:
            respo.append(q.CO_off_query)
        serializer.save(user_profile=self.request.user, response=json.dumps(respo))

class NuclearWarViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.NuclearWarSerializer
    queryset=models.NuclearWar.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster,IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_profile','response')

    def create(self,request,*args,**kwargs):
        response=super().create(request,*args,**kwargs)
        # print(repr(self.get_serializer))
        return Response({'response':json.loads(response.data['response'])})

    def update(self,request,*args,**kwargs):
        return Response({'message':"This instance can't be updated"})

    def perform_create(self,serializer):
        nu=queries.NuclearWarQuery()
        q=serializer.validated_data
        response=[]
        response.append([q['state']])
        response.append([q['dist']])
        response.append([q['loc']])
        response.append([q['count_people']])
        if q['have_infant']:
            response.append(nu.infant_query)
        if q['have_specials'].lower()!='no':
            response.append(nu.specials_query)
        response.append(nu.base_query)
        response.append(nu.media_query)
        if not q['have_add_kits']:
            response.append(nu.add_kits_query)
        if not q['have_switch_board']:
            response.append(nu.switch_board_query)
        response.append(nu.school_base_query)
        response.append(nu.conduct_drill_query)
        if not q['have_shelter_plan']:
            response.append(nu.shelter_plan_query)
        if not q['have_nuclear_kit']:
            response.append(nu.nuclear_kit_query)
        response.append(nu.addn_query)

        serializer.save(user_profile=self.request.user,response=json.dumps(response))

class FireViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.FireSerializer
    queryset=models.Fire.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster,IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_profile','response')

    def create(self,request,*args,**kwargs):
        response=super().create(request,*args,**kwargs)
        # print(repr(self.get_serializer))
        return Response({'response':json.loads(response.data['response'])})

    def update(self,request,*args,**kwargs):
        return Response({'message':"This instance can't be updated"})

    def perform_create(self,serializer):
        fi=queries.FireQuery()
        q=serializer.validated_data
        response=[]
        response.append(fi.esc_plan_query)
        response.append(fi.special_needs_query)
        if q['have_seniors']:
            response.append(fi.seniors_query)
        response.append(fi.smoke_in_out_query)
        response.append(fi.discuss_out_query)
        response.append(fi.exits_query)
        response.append(fi.fire_extin_query)
        response.append(fi.maint_check_query)
        if q['have_pets']:
            response.append(fi.pets_query)
        if not q['have_policy']:
            response.append(fi.policy_query)
        response.append(fi.doc_query)
        response.append(fi.keep_doc_query)
        response.append(fi.kit_query)

        serializer.save(user_profile=self.request.user,response=json.dumps(response))
