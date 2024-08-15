SELECT 
    id, 
    user_id, 
    date, 
    entry_text, 
    mood, 
    gratitude_1, 
    gratitude_2, 
    gratitude_3, 
    highlights, 
    challenges, 
    goals_for_tomorrow, 
    goals_reflection, 
    mindfulness_practice, 
    self_care_activities, 
    ai_response
FROM 
    journal_app_journalentry
ORDER BY 
    date DESC;
