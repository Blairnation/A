from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company

class CompanySerializer(ModelSerializer):
     employee_count = SerializerMethodField(read_only=True)
     class Meta:
          model = Company
          fields = '__all__'

     def get_employee_count(self, obj):
          count = obj.advocate_set.count()
          return count     

class AdvocateSerializer(ModelSerializer):
      company = CompanySerializer()
      advocates_total = SerializerMethodField(read_only=True)

      class Meta:
          model = Advocate
          fields = ['name','username', 'bio', 'company', 'pic','profile_pic', 'advocates_total']
          # depth = 1

      def get_pic_url(self, obj):
          request = self.context.get('request')
          if obj.pic:
            return request.build_absolute_uri(obj.pic.url)
          return None 
      
      def get_advocates_total(self, obj):
          total = Advocate.objects.count()
          return total
      