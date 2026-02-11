from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team_id', 'created_at')
    list_filter = ('team_id', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'user_id', 'duration', 'calories', 'date', 'created_at')
    list_filter = ('activity_type', 'date', 'created_at')
    search_fields = ('user_id', 'activity_type')
    readonly_fields = ('created_at',)
    ordering = ('-date', '-created_at')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('rank', 'user_id', 'team_id', 'total_calories', 'total_activities', 'updated_at')
    list_filter = ('team_id', 'rank', 'updated_at')
    search_fields = ('user_id', 'team_id')
    readonly_fields = ('updated_at',)
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'duration', 'calories_per_hour', 'created_at')
    list_filter = ('category', 'difficulty', 'created_at')
    search_fields = ('name', 'description', 'category')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
