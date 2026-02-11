from django.core.management.base import BaseCommand
from django.utils import timezone
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
from bson import ObjectId


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')
        
        # Delete existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes fitness team',
            created_at=timezone.now()
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League fitness warriors',
            created_at=timezone.now()
        )
        
        marvel_id = str(team_marvel._id)
        dc_id = str(team_dc._id)
        
        # Create Users - Marvel Heroes
        self.stdout.write('Creating Marvel heroes...')
        iron_man = User.objects.create(
            name='Tony Stark (Iron Man)',
            email='tony.stark@marvel.com',
            team_id=marvel_id,
            created_at=timezone.now()
        )
        captain_america = User.objects.create(
            name='Steve Rogers (Captain America)',
            email='steve.rogers@marvel.com',
            team_id=marvel_id,
            created_at=timezone.now()
        )
        black_widow = User.objects.create(
            name='Natasha Romanoff (Black Widow)',
            email='natasha.romanoff@marvel.com',
            team_id=marvel_id,
            created_at=timezone.now()
        )
        hulk = User.objects.create(
            name='Bruce Banner (Hulk)',
            email='bruce.banner@marvel.com',
            team_id=marvel_id,
            created_at=timezone.now()
        )
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@marvel.com',
            team_id=marvel_id,
            created_at=timezone.now()
        )
        
        # Create Users - DC Heroes
        self.stdout.write('Creating DC heroes...')
        batman = User.objects.create(
            name='Bruce Wayne (Batman)',
            email='bruce.wayne@dc.com',
            team_id=dc_id,
            created_at=timezone.now()
        )
        superman = User.objects.create(
            name='Clark Kent (Superman)',
            email='clark.kent@dc.com',
            team_id=dc_id,
            created_at=timezone.now()
        )
        wonder_woman = User.objects.create(
            name='Diana Prince (Wonder Woman)',
            email='diana.prince@dc.com',
            team_id=dc_id,
            created_at=timezone.now()
        )
        flash = User.objects.create(
            name='Barry Allen (The Flash)',
            email='barry.allen@dc.com',
            team_id=dc_id,
            created_at=timezone.now()
        )
        aquaman = User.objects.create(
            name='Arthur Curry (Aquaman)',
            email='arthur.curry@dc.com',
            team_id=dc_id,
            created_at=timezone.now()
        )
        
        # Create Activities
        self.stdout.write('Creating activities...')
        users = [
            (iron_man, 'Iron Man'), (captain_america, 'Captain America'), 
            (black_widow, 'Black Widow'), (hulk, 'Hulk'), (thor, 'Thor'),
            (batman, 'Batman'), (superman, 'Superman'), 
            (wonder_woman, 'Wonder Woman'), (flash, 'Flash'), (aquaman, 'Aquaman')
        ]
        
        activities_data = [
            {'type': 'Running', 'duration': 45, 'calories': 450},
            {'type': 'Weight Training', 'duration': 60, 'calories': 500},
            {'type': 'Yoga', 'duration': 30, 'calories': 200},
            {'type': 'Swimming', 'duration': 40, 'calories': 400},
            {'type': 'Cycling', 'duration': 50, 'calories': 480},
            {'type': 'Boxing', 'duration': 35, 'calories': 420},
            {'type': 'HIIT', 'duration': 25, 'calories': 350},
        ]
        
        for user, name in users:
            for i in range(5):  # 5 activities per user
                activity_data = activities_data[i % len(activities_data)]
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_data['type'],
                    duration=activity_data['duration'],
                    calories=activity_data['calories'],
                    date=timezone.now() - timedelta(days=i),
                    created_at=timezone.now()
                )
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard...')
        leaderboard_data = [
            (superman, dc_id, 2500, 5, 1),
            (captain_america, marvel_id, 2400, 5, 2),
            (wonder_woman, dc_id, 2300, 5, 3),
            (thor, marvel_id, 2250, 5, 4),
            (flash, dc_id, 2200, 5, 5),
            (black_widow, marvel_id, 2150, 5, 6),
            (batman, dc_id, 2100, 5, 7),
            (iron_man, marvel_id, 2050, 5, 8),
            (hulk, marvel_id, 2000, 5, 9),
            (aquaman, dc_id, 1950, 5, 10),
        ]
        
        for user, team, calories, activities_count, rank in leaderboard_data:
            Leaderboard.objects.create(
                user_id=str(user._id),
                team_id=team,
                total_calories=calories,
                total_activities=activities_count,
                rank=rank,
                updated_at=timezone.now()
            )
        
        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Superhero Strength Training',
                'description': 'Build strength like your favorite heroes with compound exercises',
                'category': 'Strength',
                'difficulty': 'intermediate',
                'duration': 60,
                'calories_per_hour': 500
            },
            {
                'name': 'Speed & Agility Workout',
                'description': 'Train like Flash with high-intensity sprints and agility drills',
                'category': 'Cardio',
                'difficulty': 'advanced',
                'duration': 45,
                'calories_per_hour': 700
            },
            {
                'name': 'Warrior Yoga Flow',
                'description': 'Balance and flexibility training inspired by Wonder Woman',
                'category': 'Flexibility',
                'difficulty': 'beginner',
                'duration': 30,
                'calories_per_hour': 250
            },
            {
                'name': 'Aquatic Power Session',
                'description': 'Swimming workout for full-body conditioning',
                'category': 'Swimming',
                'difficulty': 'intermediate',
                'duration': 40,
                'calories_per_hour': 600
            },
            {
                'name': 'Combat Training Circuit',
                'description': 'Mixed martial arts inspired circuit training',
                'category': 'Martial Arts',
                'difficulty': 'advanced',
                'duration': 50,
                'calories_per_hour': 650
            },
            {
                'name': 'Endurance Run',
                'description': 'Long-distance running for stamina building',
                'category': 'Cardio',
                'difficulty': 'beginner',
                'duration': 45,
                'calories_per_hour': 550
            },
            {
                'name': 'Power Lifting Session',
                'description': 'Heavy compound lifts for maximum strength',
                'category': 'Strength',
                'difficulty': 'advanced',
                'duration': 75,
                'calories_per_hour': 450
            },
            {
                'name': 'HIIT Hero Workout',
                'description': 'High-intensity interval training for fat burning',
                'category': 'HIIT',
                'difficulty': 'intermediate',
                'duration': 30,
                'calories_per_hour': 750
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(
                name=workout_data['name'],
                description=workout_data['description'],
                category=workout_data['category'],
                difficulty=workout_data['difficulty'],
                duration=workout_data['duration'],
                calories_per_hour=workout_data['calories_per_hour'],
                created_at=timezone.now()
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with superhero test data!'))
        self.stdout.write(f'Created:')
        self.stdout.write(f'  - {Team.objects.count()} teams')
        self.stdout.write(f'  - {User.objects.count()} users')
        self.stdout.write(f'  - {Activity.objects.count()} activities')
        self.stdout.write(f'  - {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'  - {Workout.objects.count()} workouts')
