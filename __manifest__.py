{
    "name": "Central Fitness Membership Gym",
    "version": "1.0",
    "author": "Ali Shidqie Al Faruqi",
    "category": "Fitness",
    "summary": "Comprehensive Gym Membership Management System with features for user onboarding, gym access control, class booking, workout tracking, nutrition tracking, community engagement, personal training, and in-app purchases.",
    "description": """
        Central Fitness Membership Gym is a feature-rich application designed to streamline gym operations and enhance member experiences.
        Key Features:
        - User Onboarding: CRM, Sales, and Website integration for member registration, plan selection, and payment processing.
        - Gym Access: Custom OTP-based access control with real-time occupancy tracking.
        - Class Booking: Manage classes, schedules, and trainer assignments with Project and Calendar modules.
        - Workout Tracking: Log exercises, rest timers, and generate progress reports.
        - Nutrition Tracking: Integrate with third-party Nutrition API for diet logging and calorie tracking.
        - Community Engagement: Forums, challenges, and social features using the Website module.
        - Personal Training: Book sessions, receive training plans, and track progress with Project and CRM modules.
        - In-App Purchases: Manage and sell gym-related products through Inventory and Sales modules.
        - Location Tracker: Google Maps integration for real-time gym location, occupancy, and class schedules.
    """,
    "depends": [
        "base",
        "crm",
        "sales",
        "website",
        "project",
        "calendar",
        "inventory"
    ],
    "data": [
        # Member Management Views
        "views/member/gym_member_views.xml",
        "views/member/gym_membership_plan_views.xml",
        "views/member/gym_progress_report_views.xml",

        # Access Control Views
        "views/access_control/gym_access_control_views.xml",
        "views/access_control/gym_location_views.xml",

        # Class Management Views
        "views/class_management/gym_class_booking_views.xml",
        "views/class_management/gym_class_views.xml",

        # Community Engagement Views
        "views/community/gym_challenge_views.xml",
        "views/community/gym_forum_views.xml",

        # Nutrition Tracking Views
        "views/nutrition_tracking/gym_nutrition_history_views.xml",
        "views/nutrition_tracking/gym_nutrition_meal_views.xml",

        # Personal Training Views
        "views/personal_training/gym_trainer_session_views.xml",
        "views/personal_training/gym_trainer_views.xml",

        # Reporting Views
        "views/reporting/gym_report_views.xml",

        # Workout Tracking Views
        "views/workout_tracking/gym_workout_exercise_views.xml",
        "views/workout_tracking/gym_workout_history_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
