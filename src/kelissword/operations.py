import string

def evaluate_password(password: str) -> dict:
    """
    Evaluates a password and returns its score and rating.
    
    Score is from 0 to 5 based on:
    - Length >= 8
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character
    
    Returns a dictionary with 'score' (int) and 'rating' (str).
    """
    if not isinstance(password, str) or not password:
        return {"score": 0, "rating": "Very Weak"}

    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
        
    # Check lowercase
    if any(char.islower() for char in password):
        score += 1
        
    # Check uppercase
    if any(char.isupper() for char in password):
        score += 1
        
    # Check digits
    if any(char.isdigit() for char in password):
        score += 1
        
    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
        
    # Determine rating based on score
    ratings = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }
    
    return {
        "score": score,
        "rating": ratings.get(score, "Unknown")
    }
