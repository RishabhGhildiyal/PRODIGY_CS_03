import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on specific criteria.

    Parameters:
        password (str): The password to be assessed.

    Returns:
        tuple: A tuple containing the password strength and feedback.
    """
    # Initialize a score to measure password strength
    score = 0
    feedback = []

    # Criteria 1: Length of password (minimum 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Presence of lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include lowercase letters.")

    # Criteria 3: Presence of uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include uppercase letters.")

    # Criteria 4: Presence of numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should include numbers.")

    # Criteria 5: Presence of special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should include special characters.")

    # Provide feedback based on the score
    if score == 5:
        return "Strong password!", feedback
    elif score >= 3:
        return "Moderate password. Improve based on feedback.", feedback
    else:
        return "Weak password. Address the feedback.", feedback

if __name__ == "__main__":
    print("Password Strength Checker")
    while True:
        user_password = input("Enter your password: ")
        strength, feedback = assess_password_strength(user_password)
        print(f"Strength: {strength}")
        if feedback:
            print("Suggestions:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        if strength == "Strong password!":
            print("Your password is strong and has been accepted.")
            input("Press Enter to exit...")
            break
        else:
            print("Please try again to create a stronger password.")
