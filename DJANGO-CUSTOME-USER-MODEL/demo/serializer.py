from  rest_framework import serializers
from .models import Person,AssertModel

class AssertSerializer(serializers.ModelSerializer):
    persons=serializers.SerializerMethodField()
    class Meta:
        model=AssertModel
        fields=['id','name']
#from parent to child the related_name comes in
 
    def get_personS(self,obj):
        individuals=obj.persons.all()
        return PersonSerializer(individuals,many=True).data



class PersonSerializer(serializers.ModelSerializer):
    #asserts=AssertSerializer(many=True,read_only=True)
    asserts_names=serializers.SerializerMethodField()
    class Meta:
        model=Person
        fields=['id','full_name','asserts_names']
# from  child to parent  
    def get_asserts_names(self,obj):
        asserts=obj.asserts.all()
        result=[a.name for a in asserts]
        return result

    


