from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    username = serializers.CharField(source='name', read_only=True)
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'team_id', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_first_name(self, obj):
        # Extract first name from full name (e.g., "Tony Stark (Iron Man)" -> "Tony")
        name_parts = obj.name.split('(')[0].strip().split()
        return name_parts[0] if name_parts else ''
    
    def get_last_name(self, obj):
        # Extract last name from full name (e.g., "Tony Stark (Iron Man)" -> "Stark")
        name_parts = obj.name.split('(')[0].strip().split()
        return ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_members(self, obj):
        # Get all users in this team
        team_id = str(obj._id)
        members = User.objects.filter(team_id=team_id)
        return [{'id': str(m._id), 'name': m.name} for m in members]


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()
    calories_burned = serializers.IntegerField(source='calories', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'activity_type', 'duration', 'distance', 'calories_burned', 'date', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user(self, obj):
        try:
            from bson import ObjectId
            user = User.objects.get(_id=ObjectId(obj.user_id))
            return user.name
        except:
            return obj.user_id
    
    def get_distance(self, obj):
        # Calculate approximate distance based on activity type and duration
        # This is a simplified calculation
        if obj.activity_type in ['Running', 'Cycling']:
            # Assume 10 km/h for running, 20 km/h for cycling
            speed = 20 if obj.activity_type == 'Cycling' else 10
            return round((obj.duration / 60) * speed, 2)
        elif obj.activity_type == 'Swimming':
            # Assume 2 km/h for swimming
            return round((obj.duration / 60) * 2, 2)
        return 0


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    total_points = serializers.IntegerField(source='total_calories', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'team_id', 'total_points', 'total_calories', 'total_activities', 'rank', 'updated_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user(self, obj):
        try:
            from bson import ObjectId
            user = User.objects.get(_id=ObjectId(obj.user_id))
            return user.name
        except:
            return obj.user_id


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'category', 'difficulty', 'duration', 'calories_per_hour', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)
