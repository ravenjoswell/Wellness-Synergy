SELECT 
    id AS "User ID", 
    email AS "Email Address", 
    full_name AS "Full Name", 
    TO_CHAR(last_login, 'YYYY-MM-DD HH24:MI:SS') AS "Last Login", 
    TO_CHAR(date_joined, 'YYYY-MM-DD HH24:MI:SS') AS "Date Joined"
FROM user_app_user;